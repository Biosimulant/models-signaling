# COMBO_0043 - Signaling General

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
- `signaling-sbml-li2019-neurogranin-stimulates-ca-calmodulin-depe-model1903010001-model`: Signaling: Li2019NeurograninStimulatesCaCalmodulinDepeModel1903010001Model
- `signaling-sbml-machado2014-curcumin-production-pathway-in-esche-biomd0000000565-model`: Signaling: Machado2014CurcuminProductionPathwayInEscheBiomd0000000565Model
- `signaling-sbml-maeda2006-myosinphosphorylation-biomd0000000088-model`: Signaling: Maeda2006MyosinphosphorylationBiomd0000000088Model

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
- signaling-sbml-li2019-neurogranin-stimulates-ca-calmodulin-depe-model1903010001-model :: biomodels_ebi:MODEL1903010001 :: https://www.ebi.ac.uk/biomodels/MODEL1903010001
- signaling-sbml-machado2014-curcumin-production-pathway-in-esche-biomd0000000565-model :: biomodels_ebi:BIOMD0000000565 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000565
- signaling-sbml-maeda2006-myosinphosphorylation-biomd0000000088-model :: biomodels_ebi:BIOMD0000000088 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000088

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
