# Space Plan - signaling-general-combo-0016

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-caruso2020-activation-of-the-alternative-complem-model2109110001-model, signaling-sbml-caruso2020-alternative-complement-pathway-model-model2206230002-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
