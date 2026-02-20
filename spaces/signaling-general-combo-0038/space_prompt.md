# Space Prompt - signaling-general-combo-0038

Create a scientifically coherent **signaling / general** comparative space using:
- Base models: signaling-sbml-jung2019-regulating-glioblastoma-signaling-pathw-biomd0000000828-model, signaling-sbml-kawka2014-revealing-the-role-of-sgk1-in-the-dyna-model1912090002-model, signaling-sbml-keizer1996-ryanodine-receptor-adaptation-biomd0000000060-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
