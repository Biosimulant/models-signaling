# Space Plan - signaling-general-combo-0008

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-benary2019-controlling-nfkb-dynamics-by-b-trcp-biomd0000000794-model, signaling-sbml-benson2017-systems-pharmacology-multidrug-choles-model1506220000-model

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
