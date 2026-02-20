# COMBO_0075 - Signaling Calcium Signaling

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
- `signaling-sbml-kummer2000-oscillations-in-calcium-signalling-biomd0000000329-model`: Signaling: Kummer2000OscillationsInCalciumSignallingBiomd0000000329Model
- `signaling-sbml-lemon2003-ca2dynamics-model1006230039-model`: Signaling: Lemon2003Ca2dynamicsModel1006230039Model
- `signaling-sbml-pepke2010-full-ca2-cam-mcamkii-model1001150000-model`: Signaling: Pepke2010FullCa2CamMcamkiiModel1001150000Model
- `signaling-sbml-sneyd2002-ip3-receptor-biomd0000000057-model`: Signaling: Sneyd2002Ip3ReceptorBiomd0000000057Model

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
- signaling-sbml-kummer2000-oscillations-in-calcium-signalling-biomd0000000329-model :: biomodels_ebi:BIOMD0000000329 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000329
- signaling-sbml-lemon2003-ca2dynamics-model1006230039-model :: biomodels_ebi:MODEL1006230039 :: https://www.ebi.ac.uk/biomodels/MODEL1006230039
- signaling-sbml-pepke2010-full-ca2-cam-mcamkii-model1001150000-model :: biomodels_ebi:MODEL1001150000 :: https://www.ebi.ac.uk/biomodels/MODEL1001150000
- signaling-sbml-sneyd2002-ip3-receptor-biomd0000000057-model :: biomodels_ebi:BIOMD0000000057 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000057

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
