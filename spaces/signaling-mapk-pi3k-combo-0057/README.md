# COMBO_0057 - Signaling Mapk Pi3K

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
- `signaling-sbml-fujita2010-akt-signalling-ngf-biomd0000000263-model`: Signaling: Fujita2010AktSignallingNgfBiomd0000000263Model
- `signaling-sbml-gray2016-the-akt-switch-model-biomd0000000854-model`: Signaling: Gray2016TheAktSwitchModelBiomd0000000854Model
- `signaling-sbml-harish2009-nuclear-cytoplasmic-erk-oscillation-m-model2306170002-model`: Signaling: Harish2009NuclearCytoplasmicErkOscillationMModel2306170002Model
- `signaling-sbml-heberle-razquin-navas-2019-pi3k-mapk-p38-mtor-mo-model1902140002-model`: Signaling: HeberleRazquinNavas2019Pi3kMapkP38MtorMoModel1902140002Model

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
- signaling-sbml-fujita2010-akt-signalling-ngf-biomd0000000263-model :: biomodels_ebi:BIOMD0000000263 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000263
- signaling-sbml-gray2016-the-akt-switch-model-biomd0000000854-model :: biomodels_ebi:BIOMD0000000854 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000854
- signaling-sbml-harish2009-nuclear-cytoplasmic-erk-oscillation-m-model2306170002-model :: biomodels_ebi:MODEL2306170002 :: https://www.ebi.ac.uk/biomodels/MODEL2306170002
- signaling-sbml-heberle-razquin-navas-2019-pi3k-mapk-p38-mtor-mo-model1902140002-model :: biomodels_ebi:MODEL1902140002 :: https://www.ebi.ac.uk/biomodels/MODEL1902140002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
