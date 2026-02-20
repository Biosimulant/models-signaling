# Space Plan - signaling-immune-signaling-combo-0076

## Scientific Scope
- Domain: signaling
- Theme: immune_signaling
- Base models: signaling-sbml-lipniacki2004-mathematical-model-of-nfkb-regulat-biomd0000000786-model, signaling-sbml-sobotta2017-il-6-induced-jak1-stat3-signaling-model2307050001-model, signaling-sbml-tiwari2019-mathematical-model-of-nfkb-regulatory-model1911140002-model, signaling-sbml-yao2016-calcium-signaling-model1611150001-model

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
