# Space Plan - signaling-calcium-signaling-combo-0047

## Scientific Scope
- Domain: signaling
- Theme: calcium_signaling
- Base models: signaling-sbml-kummer2000-oscillations-in-calcium-signalling-biomd0000000329-model, signaling-sbml-lemon2003-ca2dynamics-model1006230039-model, signaling-sbml-pepke2010-full-ca2-cam-mcamkii-model1001150000-model

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
