# Space Plan - signaling-general-combo-0022

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-dupeux2011-abareceptor-dimer-model1202030000-model, signaling-sbml-dupeux2011-abareceptor-monomer-model1202030001-model

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
