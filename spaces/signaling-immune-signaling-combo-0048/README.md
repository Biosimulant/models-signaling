# COMBO_0048 - Signaling Immune Signaling

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
- `signaling-sbml-adlung2021-cell-to-cell-variability-in-jak2-stat-biomd0000001077-model`: Signaling: Adlung2021CellToCellVariabilityInJak2StatBiomd0000001077Model
- `signaling-sbml-amstein2017-tnfr1-mediated-nf-b-signaling-petri-model2312010001-model`: Signaling: Amstein2017Tnfr1MediatedNfBSignalingPetriModel2312010001Model
- `signaling-sbml-bachmann2011-jak2-stat5-feedbackcontrol-biomd0000000347-model`: Signaling: Bachmann2011Jak2Stat5FeedbackcontrolBiomd0000000347Model

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
- signaling-sbml-adlung2021-cell-to-cell-variability-in-jak2-stat-biomd0000001077-model :: biomodels_ebi:BIOMD0000001077 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001077
- signaling-sbml-amstein2017-tnfr1-mediated-nf-b-signaling-petri-model2312010001-model :: biomodels_ebi:MODEL2312010001 :: https://www.ebi.ac.uk/biomodels/MODEL2312010001
- signaling-sbml-bachmann2011-jak2-stat5-feedbackcontrol-biomd0000000347-model :: biomodels_ebi:BIOMD0000000347 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000347

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
