# Space Prompt - signaling-immune-signaling-combo-0048

Create a scientifically coherent **signaling / immune_signaling** comparative space using:
- Base models: signaling-sbml-adlung2021-cell-to-cell-variability-in-jak2-stat-biomd0000001077-model, signaling-sbml-amstein2017-tnfr1-mediated-nf-b-signaling-petri-model2312010001-model, signaling-sbml-bachmann2011-jak2-stat5-feedbackcontrol-biomd0000000347-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
