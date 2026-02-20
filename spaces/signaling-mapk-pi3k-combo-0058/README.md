# COMBO_0058 - Signaling Mapk Pi3K

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
- `signaling-sbml-heberlerazquinnavas2019-the-pi3k-and-mapk-p38-pa-biomd0000000907-model`: Signaling: Heberlerazquinnavas2019ThePi3kAndMapkP38PaBiomd0000000907Model
- `signaling-sbml-heberlerazquinnavas2019-the-pi3k-and-mapk-p38-pa-model2001030002-model`: Signaling: Heberlerazquinnavas2019ThePi3kAndMapkP38PaModel2001030002Model
- `signaling-sbml-hornberg2005-mapksignalling-biomd0000000667-model`: Signaling: Hornberg2005MapksignallingBiomd0000000667Model
- `signaling-sbml-huang1996-ultrasensitivity-in-mapk-cascade-biomd0000000009-model`: Signaling: Huang1996UltrasensitivityInMapkCascadeBiomd0000000009Model

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
- signaling-sbml-heberlerazquinnavas2019-the-pi3k-and-mapk-p38-pa-biomd0000000907-model :: biomodels_ebi:BIOMD0000000907 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000907
- signaling-sbml-heberlerazquinnavas2019-the-pi3k-and-mapk-p38-pa-model2001030002-model :: biomodels_ebi:MODEL2001030002 :: https://www.ebi.ac.uk/biomodels/MODEL2001030002
- signaling-sbml-hornberg2005-mapksignalling-biomd0000000667-model :: biomodels_ebi:BIOMD0000000667 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000667
- signaling-sbml-huang1996-ultrasensitivity-in-mapk-cascade-biomd0000000009-model :: biomodels_ebi:BIOMD0000000009 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000009

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
