# Space Prompt - signaling-general-combo-0040

Create a scientifically coherent **signaling / general** comparative space using:
- Base models: signaling-sbml-kholodenko1999-egfr-signaling-biomd0000000048-model, signaling-sbml-koch2005-sucrose-breakdown-pathway-petri-net-model1308080002-model, signaling-sbml-kofahl2004-pheromonepathway-biomd0000000032-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
