# Space Prompt - signaling-calcium-signaling-combo-0045

Create a scientifically coherent **signaling / calcium_signaling** comparative space using:
- Base models: signaling-sbml-abell2011-calciumsignaling-withadaptation-biomd0000000355-model, signaling-sbml-abell2011-calciumsignaling-withoutadaptation-biomd0000000354-model, signaling-sbml-bertram2006-endothelin-biomd0000000128-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
