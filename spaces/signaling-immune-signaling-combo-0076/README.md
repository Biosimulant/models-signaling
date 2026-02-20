# COMBO_0076 - Signaling Immune Signaling

## Scientific Question
How do immune signaling mechanisms compare across these models?

## Biological Context
Intracellular signaling cascades and cross-pathway modulation.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `signaling-sbml-lipniacki2004-mathematical-model-of-nfkb-regulat-biomd0000000786-model`: Signaling: Lipniacki2004MathematicalModelOfNfkbRegulatBiomd0000000786Model
- `signaling-sbml-sobotta2017-il-6-induced-jak1-stat3-signaling-model2307050001-model`: Signaling: Sobotta2017Il6InducedJak1Stat3SignalingModel2307050001Model
- `signaling-sbml-tiwari2019-mathematical-model-of-nfkb-regulatory-model1911140002-model`: Signaling: Tiwari2019MathematicalModelOfNfkbRegulatoryModel1911140002Model
- `signaling-sbml-yao2016-calcium-signaling-model1611150001-model`: Signaling: Yao2016CalciumSignalingModel1611150001Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- signaling-sbml-lipniacki2004-mathematical-model-of-nfkb-regulat-biomd0000000786-model :: biomodels_ebi:BIOMD0000000786 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000786
- signaling-sbml-sobotta2017-il-6-induced-jak1-stat3-signaling-model2307050001-model :: biomodels_ebi:MODEL2307050001 :: https://www.ebi.ac.uk/biomodels/MODEL2307050001
- signaling-sbml-tiwari2019-mathematical-model-of-nfkb-regulatory-model1911140002-model :: biomodels_ebi:MODEL1911140002 :: https://www.ebi.ac.uk/biomodels/MODEL1911140002
- signaling-sbml-yao2016-calcium-signaling-model1611150001-model :: biomodels_ebi:MODEL1611150001 :: https://www.ebi.ac.uk/biomodels/MODEL1611150001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
