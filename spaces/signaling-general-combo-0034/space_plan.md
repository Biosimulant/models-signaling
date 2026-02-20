# Space Plan - signaling-general-combo-0034

## Scientific Scope
- Domain: signaling
- Theme: general
- Base models: signaling-sbml-hodgson2018-tgfbeta-signalling-and-inflammatory-model1805080001-model, signaling-sbml-hoffmann2002-wt-ikbnfkb-signaling-biomd0000000140-model, signaling-sbml-huang2014-systematic-modeling-for-the-insulin-si-model1912090001-model

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
