# Space Plan - signaling-calcium-signaling-combo-0045

## Scientific Scope
- Domain: signaling
- Theme: calcium_signaling
- Base models: signaling-sbml-abell2011-calciumsignaling-withadaptation-biomd0000000355-model, signaling-sbml-abell2011-calciumsignaling-withoutadaptation-biomd0000000354-model, signaling-sbml-bertram2006-endothelin-biomd0000000128-model

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
