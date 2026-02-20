# COMBO_0064 - Signaling Mapk Pi3K

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
- `signaling-sbml-padala2017-erk-pi3k-akt-and-wnt-signalling-netwo-biomd0000000656-model`: Signaling: Padala2017ErkPi3kAktAndWntSignallingNetwoBiomd0000000656Model
- `signaling-sbml-pathak2013-mapk-activation-in-response-to-variou-biomd0000000491-model`: Signaling: Pathak2013MapkActivationInResponseToVariouBiomd0000000491Model
- `signaling-sbml-pathak2013-mapk-activation-in-response-to-variou-biomd0000000492-model`: Signaling: Pathak2013MapkActivationInResponseToVariouBiomd0000000492Model
- `signaling-sbml-perrett2014-gnrh-pulse-erk-activity-model1509050002-model`: Signaling: Perrett2014GnrhPulseErkActivityModel1509050002Model

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
- signaling-sbml-padala2017-erk-pi3k-akt-and-wnt-signalling-netwo-biomd0000000656-model :: biomodels_ebi:BIOMD0000000656 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000656
- signaling-sbml-pathak2013-mapk-activation-in-response-to-variou-biomd0000000491-model :: biomodels_ebi:BIOMD0000000491 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000491
- signaling-sbml-pathak2013-mapk-activation-in-response-to-variou-biomd0000000492-model :: biomodels_ebi:BIOMD0000000492 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000492
- signaling-sbml-perrett2014-gnrh-pulse-erk-activity-model1509050002-model :: biomodels_ebi:MODEL1509050002 :: https://www.ebi.ac.uk/biomodels/MODEL1509050002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
