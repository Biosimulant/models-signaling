# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Dedicated visualisation model for cleaned signaling SBML labs."""

from __future__ import annotations

from typing import Any, Mapping

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec, unwrap_payload


SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


class SignalingVisualisationModel(BioModule):
    """Render compact, desktop-compatible signaling visuals."""

    def __init__(
        self,
        source_alias: str,
        title: str,
        context: str,
        question: str,
        visual_scope: str,
        caveat: str,
        state_schema: Mapping[str, str],
        species_labels: Mapping[str, str] | None = None,
    ) -> None:
        self.source_alias = source_alias
        self.title = title
        self.context = context
        self.question = question
        self.visual_scope = visual_scope
        self.caveat = caveat
        self.state_schema = dict(state_schema)
        self.species_labels = dict(species_labels or {})
        self._state: dict[str, float] = {}
        self._summary: dict[str, Any] = {}
        self._labels: dict[str, str] = dict(self.species_labels)
        self._history: list[tuple[float, dict[str, float]]] = []
        self._time = 0.0

    def inputs(self) -> dict[str, SignalSpec]:
        return {
            f"{self.source_alias}_state": SignalSpec.record(
                schema=self.state_schema or {"payload": "json"},
                description="Latest public observable state from the core SBML model.",
            ),
            f"{self.source_alias}_summary": SignalSpec.record(
                schema=SUMMARY_SCHEMA,
                description="Simulation summary from the core SBML model.",
            ),
            f"{self.source_alias}_species_labels": SignalSpec.record(
                schema={key: "str" for key in (self.state_schema or self.species_labels or {"payload": "json"})},
                description="Human-readable labels for public observables.",
            ),
        }

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def set_inputs(self, signals: dict[str, BioSignal]) -> None:
        state = unwrap_payload(signals.get(f"{self.source_alias}_state"))
        summary = unwrap_payload(signals.get(f"{self.source_alias}_summary"))
        labels = unwrap_payload(signals.get(f"{self.source_alias}_species_labels"))
        if isinstance(state, Mapping):
            self._state = {str(k): _finite_float(v) for k, v in state.items() if _finite_float(v) is not None}
        if isinstance(summary, Mapping):
            self._summary = dict(summary)
        if isinstance(labels, Mapping):
            self._labels.update({str(k): str(v) for k, v in labels.items()})

    def advance_window(self, start: float, end: float) -> None:
        self._time = float(end)
        if self._state:
            self._history.append((self._time, dict(self._state)))
            if len(self._history) > 200:
                del self._history[:-200]

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> list[dict[str, Any]]:
        visuals: list[dict[str, Any]] = []
        if self._summary or self._state:
            visuals.append(self._qa_visual())
        ts = self._timeseries_visual()
        if ts is not None:
            visuals.append(ts)
        bar = self._bar_visual()
        if bar is not None:
            visuals.append(bar)
        return visuals

    def _qa_visual(self) -> dict[str, Any]:
        largest = str(self._summary.get("largest_change_observable") or "")
        magnitude = _finite_float(self._summary.get("largest_change_magnitude")) or 0.0
        peak = str(self._summary.get("peak_observable") or largest or "")
        peak_value = _finite_float(self._summary.get("peak_value")) or 0.0
        if largest and magnitude > 0:
            answer = f"{self._label(largest)} changed most over the simulated window."
            evidence = f"Largest absolute change: {magnitude:.6g}; peak readout: {self._label(peak)} = {peak_value:.6g}."
        elif self._state:
            answer = "The model remained near its initialized state over this short baseline run."
            evidence = f"{len(self._state)} observables were finite; the summary reported no dominant excursion."
        else:
            answer = "No finite pathway state was available for interpretation."
            evidence = "Core simulation did not provide renderable state values."
        return {
            "render": "table",
            "title": "Scientific answer",
            "data": {
                "columns": ["Item", "Value"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", answer],
                    ["Evidence", evidence],
                    ["Dominant module", self.visual_scope],
                    ["Caveat", self.caveat],
                ],
            },
        }

    def _timeseries_visual(self) -> dict[str, Any] | None:
        if not self._history:
            return None
        keys = self._ranked_keys()[: min(8, len(self._state))]
        series = []
        for key in keys:
            points = [[t, values[key]] for t, values in self._history if key in values]
            if points:
                series.append({"name": self._label(key), "points": points})
        if not series:
            return None
        return {
            "render": "timeseries",
            "title": self.visual_scope,
            "data": {"series": series},
        }

    def _bar_visual(self) -> dict[str, Any] | None:
        if not self._state:
            return None
        items = [
            {"label": self._label(key), "value": value}
            for key, value in sorted(self._state.items(), key=lambda item: abs(item[1]), reverse=True)[:10]
            if value is not None and not isinstance(value, bool)
        ]
        if not items:
            return None
        return {
            "render": "bar",
            "title": "Latest dominant observables",
            "data": {"items": items},
        }

    def _ranked_keys(self) -> list[str]:
        if len(self._history) >= 2:
            first = self._history[0][1]
            last = self._history[-1][1]
            return sorted(last, key=lambda key: abs(last.get(key, 0.0) - first.get(key, 0.0)), reverse=True)
        return sorted(self._state, key=lambda key: abs(self._state.get(key, 0.0)), reverse=True)

    def _label(self, key: str) -> str:
        return self._labels.get(key, key.replace("_", " ").title())


def _finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number or number in {float("inf"), float("-inf")}:
        return None
    return number
