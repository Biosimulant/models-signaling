# COMBO_0046 - Signaling Calcium Signaling

## Scientific Question
How do calcium signaling mechanisms compare across these models?

## Biological Context
Intracellular signaling cascades and cross-pathway modulation.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `signaling-sbml-cui2008-cardiacmyocytes-model1172425728-model`: Signaling: Cui2008CardiacmyocytesModel1172425728Model
- `signaling-sbml-iribe2006-camkiikineticsmodel-model1006230085-model`: Signaling: Iribe2006CamkiikineticsmodelModel1006230085Model
- `signaling-sbml-jafri1998-ventricularmyocyte-model0847869198-model`: Signaling: Jafri1998VentricularmyocyteModel0847869198Model

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
- signaling-sbml-cui2008-cardiacmyocytes-model1172425728-model :: biomodels_ebi:MODEL1172425728 :: https://www.ebi.ac.uk/biomodels/MODEL1172425728
- signaling-sbml-iribe2006-camkiikineticsmodel-model1006230085-model :: biomodels_ebi:MODEL1006230085 :: https://www.ebi.ac.uk/biomodels/MODEL1006230085
- signaling-sbml-jafri1998-ventricularmyocyte-model0847869198-model :: biomodels_ebi:MODEL0847869198 :: https://www.ebi.ac.uk/biomodels/MODEL0847869198

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
