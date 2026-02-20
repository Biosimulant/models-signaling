# Space Prompt - signaling-immune-signaling-combo-0076

Create a scientifically coherent **signaling / immune_signaling** comparative space using:
- Base models: signaling-sbml-lipniacki2004-mathematical-model-of-nfkb-regulat-biomd0000000786-model, signaling-sbml-sobotta2017-il-6-induced-jak1-stat3-signaling-model2307050001-model, signaling-sbml-tiwari2019-mathematical-model-of-nfkb-regulatory-model1911140002-model, signaling-sbml-yao2016-calcium-signaling-model1611150001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
