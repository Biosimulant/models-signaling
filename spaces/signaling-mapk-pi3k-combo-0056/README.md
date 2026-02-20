# COMBO_0056 - Signaling Mapk Pi3K

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
- `signaling-sbml-cursons2015-regulation-of-erk-mapk-signaling-in-biomd0000000659-model`: Signaling: Cursons2015RegulationOfErkMapkSignalingInBiomd0000000659Model
- `signaling-sbml-froehlich2022-model-of-adaptive-resistance-in-me-model2207130001-model`: Signaling: Froehlich2022ModelOfAdaptiveResistanceInMeModel2207130001Model
- `signaling-sbml-fujita2010-akt-signalling-egf-biomd0000000262-model`: Signaling: Fujita2010AktSignallingEgfBiomd0000000262Model
- `signaling-sbml-fujita2010-akt-signalling-egfrinhib-biomd0000000264-model`: Signaling: Fujita2010AktSignallingEgfrinhibBiomd0000000264Model

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
- signaling-sbml-cursons2015-regulation-of-erk-mapk-signaling-in-biomd0000000659-model :: biomodels_ebi:BIOMD0000000659 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000659
- signaling-sbml-froehlich2022-model-of-adaptive-resistance-in-me-model2207130001-model :: biomodels_ebi:MODEL2207130001 :: https://www.ebi.ac.uk/biomodels/MODEL2207130001
- signaling-sbml-fujita2010-akt-signalling-egf-biomd0000000262-model :: biomodels_ebi:BIOMD0000000262 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000262
- signaling-sbml-fujita2010-akt-signalling-egfrinhib-biomd0000000264-model :: biomodels_ebi:BIOMD0000000264 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000264

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
