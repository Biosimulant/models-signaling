# Space Plan - signaling-immune-signaling-combo-0049

## Scientific Scope
- Domain: signaling
- Theme: immune_signaling
- Base models: signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000448-model, signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000449-model, signaling-sbml-brown2004-ngf-and-egf-signaling-biomd0000000033-model

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
