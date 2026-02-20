# COMBO_0061 - Signaling Mapk Pi3K

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
- `signaling-sbml-markevich2004-mapk-orderedelementary-biomd0000000026-model`: Signaling: Markevich2004MapkOrderedelementaryBiomd0000000026Model
- `signaling-sbml-markevich2004-mapk-orderedmm2kinases-biomd0000000031-model`: Signaling: Markevich2004MapkOrderedmm2kinasesBiomd0000000031Model
- `signaling-sbml-markevich2004-mapk-phosphorandomelementary-biomd0000000028-model`: Signaling: Markevich2004MapkPhosphorandomelementaryBiomd0000000028Model
- `signaling-sbml-markevich2004-mapk-phosphorandommm-biomd0000000029-model`: Signaling: Markevich2004MapkPhosphorandommmBiomd0000000029Model

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
- signaling-sbml-markevich2004-mapk-orderedelementary-biomd0000000026-model :: biomodels_ebi:BIOMD0000000026 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000026
- signaling-sbml-markevich2004-mapk-orderedmm2kinases-biomd0000000031-model :: biomodels_ebi:BIOMD0000000031 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000031
- signaling-sbml-markevich2004-mapk-phosphorandomelementary-biomd0000000028-model :: biomodels_ebi:BIOMD0000000028 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000028
- signaling-sbml-markevich2004-mapk-phosphorandommm-biomd0000000029-model :: biomodels_ebi:BIOMD0000000029 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000029

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
