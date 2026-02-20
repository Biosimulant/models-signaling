# COMBO_0032 - Signaling General

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
- `signaling-sbml-heitzler2012-gpcr-signalling-biomd0000000842-model`: Signaling: Heitzler2012GpcrSignallingBiomd0000000842Model
- `signaling-sbml-hermansen2015-denovo-biosynthesis-of-pyrimidines-biomd0000000590-model`: Signaling: Hermansen2015DenovoBiosynthesisOfPyrimidinesBiomd0000000590Model
- `signaling-sbml-hetmanski2019-mechanochemical-signaling-controll-model1908290001-model`: Signaling: Hetmanski2019MechanochemicalSignalingControllModel1908290001Model

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
- signaling-sbml-heitzler2012-gpcr-signalling-biomd0000000842-model :: biomodels_ebi:BIOMD0000000842 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000842
- signaling-sbml-hermansen2015-denovo-biosynthesis-of-pyrimidines-biomd0000000590-model :: biomodels_ebi:BIOMD0000000590 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000590
- signaling-sbml-hetmanski2019-mechanochemical-signaling-controll-model1908290001-model :: biomodels_ebi:MODEL1908290001 :: https://www.ebi.ac.uk/biomodels/MODEL1908290001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
