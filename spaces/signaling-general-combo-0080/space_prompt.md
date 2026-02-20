# Space Prompt - signaling-general-combo-0080

Create a scientifically coherent **signaling / general** comparative space using:
- Base models: signaling-sbml-amara2013-pcna-ubiquitylation-in-the-activation-biomd0000000475-model, signaling-sbml-anand2003-reactions-of-the-intrinsic-pathway-of-model1806130003-model, signaling-sbml-araujo2016-positive-feedback-in-cdk1-signalling-biomd0000000657-model, signaling-sbml-bakshi2020-minimal-model-of-alternative-pathway-biomd0000001017-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
