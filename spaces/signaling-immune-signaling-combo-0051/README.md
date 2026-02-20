# COMBO_0051 - Signaling Immune Signaling

## Scientific Question
How do immune signaling mechanisms compare across these models?

## Biological Context
Intracellular signaling cascades and cross-pathway modulation.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `signaling-sbml-gex-fabry1984-model-of-receptor-mediated-endocyt-biomd0000000985-model`: Signaling: GexFabry1984ModelOfReceptorMediatedEndocytBiomd0000000985Model
- `signaling-sbml-hofmeyer1986-seqfb-proc-aa-synthesis-biomd0000000284-model`: Signaling: Hofmeyer1986SeqfbProcAaSynthesisBiomd0000000284Model
- `signaling-sbml-koch2021-phospholamban-network-model2011110001-model`: Signaling: Koch2021PhospholambanNetworkModel2011110001Model

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
- signaling-sbml-gex-fabry1984-model-of-receptor-mediated-endocyt-biomd0000000985-model :: biomodels_ebi:BIOMD0000000985 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000985
- signaling-sbml-hofmeyer1986-seqfb-proc-aa-synthesis-biomd0000000284-model :: biomodels_ebi:BIOMD0000000284 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000284
- signaling-sbml-koch2021-phospholamban-network-model2011110001-model :: biomodels_ebi:MODEL2011110001 :: https://www.ebi.ac.uk/biomodels/MODEL2011110001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
