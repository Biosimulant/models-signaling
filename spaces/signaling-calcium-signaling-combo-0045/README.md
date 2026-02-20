# COMBO_0045 - Signaling Calcium Signaling

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
- `signaling-sbml-abell2011-calciumsignaling-withadaptation-biomd0000000355-model`: Signaling: Abell2011CalciumsignalingWithadaptationBiomd0000000355Model
- `signaling-sbml-abell2011-calciumsignaling-withoutadaptation-biomd0000000354-model`: Signaling: Abell2011CalciumsignalingWithoutadaptationBiomd0000000354Model
- `signaling-sbml-bertram2006-endothelin-biomd0000000128-model`: Signaling: Bertram2006EndothelinBiomd0000000128Model

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
- signaling-sbml-abell2011-calciumsignaling-withadaptation-biomd0000000355-model :: biomodels_ebi:BIOMD0000000355 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000355
- signaling-sbml-abell2011-calciumsignaling-withoutadaptation-biomd0000000354-model :: biomodels_ebi:BIOMD0000000354 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000354
- signaling-sbml-bertram2006-endothelin-biomd0000000128-model :: biomodels_ebi:BIOMD0000000128 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000128

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
