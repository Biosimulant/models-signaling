# Space Plan - signaling-calcium-signaling-combo-0046

## Scientific Scope
- Domain: signaling
- Theme: calcium_signaling
- Base models: signaling-sbml-cui2008-cardiacmyocytes-model1172425728-model, signaling-sbml-iribe2006-camkiikineticsmodel-model1006230085-model, signaling-sbml-jafri1998-ventricularmyocyte-model0847869198-model

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
