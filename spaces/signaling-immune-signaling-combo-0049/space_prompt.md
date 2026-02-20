# Space Prompt - signaling-immune-signaling-combo-0049

Create a scientifically coherent **signaling / immune_signaling** comparative space using:
- Base models: signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000448-model, signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000449-model, signaling-sbml-brown2004-ngf-and-egf-signaling-biomd0000000033-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
