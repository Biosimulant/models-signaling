# COMBO_0035 - Signaling General

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
- `signaling-sbml-huarat2016-starvation-induced-ser-thr-protein-ki-model1607210000-model`: Signaling: Huarat2016StarvationInducedSerThrProteinKiModel1607210000Model
- `signaling-sbml-hui2016-age-related-changes-in-articular-cartila-biomd0000000560-model`: Signaling: Hui2016AgeRelatedChangesInArticularCartilaBiomd0000000560Model
- `signaling-sbml-iancu2007-cardiacmyoscytes-campsignaling-model1006230117-model`: Signaling: Iancu2007CardiacmyoscytesCampsignalingModel1006230117Model

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
- signaling-sbml-huarat2016-starvation-induced-ser-thr-protein-ki-model1607210000-model :: biomodels_ebi:MODEL1607210000 :: https://www.ebi.ac.uk/biomodels/MODEL1607210000
- signaling-sbml-hui2016-age-related-changes-in-articular-cartila-biomd0000000560-model :: biomodels_ebi:BIOMD0000000560 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000560
- signaling-sbml-iancu2007-cardiacmyoscytes-campsignaling-model1006230117-model :: biomodels_ebi:MODEL1006230117 :: https://www.ebi.ac.uk/biomodels/MODEL1006230117

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
