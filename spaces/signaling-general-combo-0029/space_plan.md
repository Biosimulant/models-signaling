# Space Plan - signaling-general-combo-0029

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-grigolon2018-responses-to-auxin-signals-model2003060002-model, signaling-sbml-gupta2007-hypothalamicpituitaryadrenal-modela-model1006230111-model

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
