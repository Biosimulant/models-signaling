# COMBO_0020 - Signaling General

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
- `signaling-sbml-dasgupta2020-reduced-model-of-receptor-clusturin-biomd0000000973-model`: Signaling: Dasgupta2020ReducedModelOfReceptorClusturinBiomd0000000973Model
- `signaling-sbml-deback2013-pancreas-differentiation-patterning-i-model2011260001-model`: Signaling: Deback2013PancreasDifferentiationPatterningIModel2011260001Model

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
- signaling-sbml-dasgupta2020-reduced-model-of-receptor-clusturin-biomd0000000973-model :: biomodels_ebi:BIOMD0000000973 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000973
- signaling-sbml-deback2013-pancreas-differentiation-patterning-i-model2011260001-model :: biomodels_ebi:MODEL2011260001 :: https://www.ebi.ac.uk/biomodels/MODEL2011260001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
