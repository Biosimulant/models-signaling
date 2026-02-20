# COMBO_0059 - Signaling Mapk Pi3K

## Scientific Question
How do mapk pi3k mechanisms compare across these models?

## Biological Context
Intracellular signaling cascades and cross-pathway modulation.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `signaling-sbml-kholodenko2000-ultrasensitivity-and-negative-fee-biomd0000000010-model`: Signaling: Kholodenko2000UltrasensitivityAndNegativeFeeBiomd0000000010Model
- `signaling-sbml-koo2013-shear-stress-induced-akt-and-enos-phosph-biomd0000000465-model`: Signaling: Koo2013ShearStressInducedAktAndEnosPhosphBiomd0000000465Model
- `signaling-sbml-kubota2012-insulinaction-aktpathway-model1204060000-model`: Signaling: Kubota2012InsulinactionAktpathwayModel1204060000Model
- `signaling-sbml-kwang2003-the-influence-of-rkip-on-the-erk-signa-biomd0000000647-model`: Signaling: Kwang2003TheInfluenceOfRkipOnTheErkSignaBiomd0000000647Model

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
- signaling-sbml-kholodenko2000-ultrasensitivity-and-negative-fee-biomd0000000010-model :: biomodels_ebi:BIOMD0000000010 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000010
- signaling-sbml-koo2013-shear-stress-induced-akt-and-enos-phosph-biomd0000000465-model :: biomodels_ebi:BIOMD0000000465 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000465
- signaling-sbml-kubota2012-insulinaction-aktpathway-model1204060000-model :: biomodels_ebi:MODEL1204060000 :: https://www.ebi.ac.uk/biomodels/MODEL1204060000
- signaling-sbml-kwang2003-the-influence-of-rkip-on-the-erk-signa-biomd0000000647-model :: biomodels_ebi:BIOMD0000000647 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000647

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
