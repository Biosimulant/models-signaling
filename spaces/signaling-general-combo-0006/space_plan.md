# Space Plan - signaling-general-combo-0006

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-beard2005-mitochondrial-respiration-model4151491057-model, signaling-sbml-becker2010-epor-auxiliarymodel-biomd0000000272-model

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
