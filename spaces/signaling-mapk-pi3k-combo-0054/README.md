# COMBO_0054 - Signaling Mapk Pi3K

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
- `signaling-sbml-bhalla2002-mkp1-feedback-effects-model9070467164-model`: Signaling: Bhalla2002Mkp1FeedbackEffectsModel9070467164Model
- `signaling-sbml-bhalla2004-egfr-mapk-model9085850385-model`: Signaling: Bhalla2004EgfrMapkModel9085850385Model
- `signaling-sbml-bidkhori2012-egfr-signalling-in-nsclc-biomd0000000453-model`: Signaling: Bidkhori2012EgfrSignallingInNsclcBiomd0000000453Model

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
- signaling-sbml-bhalla2002-mkp1-feedback-effects-model9070467164-model :: biomodels_ebi:MODEL9070467164 :: https://www.ebi.ac.uk/biomodels/MODEL9070467164
- signaling-sbml-bhalla2004-egfr-mapk-model9085850385-model :: biomodels_ebi:MODEL9085850385 :: https://www.ebi.ac.uk/biomodels/MODEL9085850385
- signaling-sbml-bidkhori2012-egfr-signalling-in-nsclc-biomd0000000453-model :: biomodels_ebi:BIOMD0000000453 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000453

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
