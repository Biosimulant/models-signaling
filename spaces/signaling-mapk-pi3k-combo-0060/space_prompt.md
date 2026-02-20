# Space Prompt - signaling-mapk-pi3k-combo-0060

Create a scientifically coherent **signaling / mapk_pi3k** comparative space using:
- Base models: signaling-sbml-lee2008-erk-and-pi3k-signal-integration-by-myc-biomd0000000818-model, signaling-sbml-levchenko2000-mapk-noscaffold-biomd0000000011-model, signaling-sbml-levchenko2000-mapk-scaffold-biomd0000000014-model, signaling-sbml-markevich2004-mapk-double-phosphorylation-ordere-biomd0000000027-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
