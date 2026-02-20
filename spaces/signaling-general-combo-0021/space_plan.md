# Space Plan - signaling-general-combo-0021

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-dicamillo2016-insulin-signalling-pathway-rule-ba-biomd0000000833-model, signaling-sbml-dual-g-protein-model-model2306210001-model

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
