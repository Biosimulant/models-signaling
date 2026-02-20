# Space Plan - signaling-general-combo-0017

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-celli-re2011-plasticity-of-tgf-signalling-biomd0000000600-model, signaling-sbml-chan2004-tcell-receptor-activation-biomd0000000120-model

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
