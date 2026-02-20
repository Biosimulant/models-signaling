# COMBO_0039 - Signaling General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Intracellular signaling cascades and cross-pathway modulation.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `signaling-sbml-kervizic2008-cholesterol-srebp-model0568648427-model`: Signaling: Kervizic2008CholesterolSrebpModel0568648427Model
- `signaling-sbml-kessler2025-il-6-and-il-22-pathway-in-human-hepa-model2509100001-model`: Signaling: Kessler2025Il6AndIl22PathwayInHumanHepaModel2509100001Model
- `signaling-sbml-khan2018-origins-of-robustness-in-translational-model1911120001-model`: Signaling: Khan2018OriginsOfRobustnessInTranslationalModel1911120001Model

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
- signaling-sbml-kervizic2008-cholesterol-srebp-model0568648427-model :: biomodels_ebi:MODEL0568648427 :: https://www.ebi.ac.uk/biomodels/MODEL0568648427
- signaling-sbml-kessler2025-il-6-and-il-22-pathway-in-human-hepa-model2509100001-model :: biomodels_ebi:MODEL2509100001 :: https://www.ebi.ac.uk/biomodels/MODEL2509100001
- signaling-sbml-khan2018-origins-of-robustness-in-translational-model1911120001-model :: biomodels_ebi:MODEL1911120001 :: https://www.ebi.ac.uk/biomodels/MODEL1911120001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
