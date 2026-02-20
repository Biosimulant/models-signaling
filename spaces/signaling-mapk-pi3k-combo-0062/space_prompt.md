# Space Prompt - signaling-mapk-pi3k-combo-0062

Create a scientifically coherent **signaling / mapk_pi3k** comparative space using:
- Base models: signaling-sbml-muller2008-simplified-mapk-activation-dynamics-m-biomd0000000664-model, signaling-sbml-nakakuki2010-cellfatedecision-core-biomd0000000251-model, signaling-sbml-nakakuki2010-cellfatedecision-mechanistic-biomd0000000250-model, signaling-sbml-padala2017-erk-pi3k-akt-and-wnt-signalling-netwo-biomd0000000648-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
