# COMBO_0053 - Signaling Mapk Pi3K

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
- `signaling-sbml-ajay-bhalla-2007-bistable-model9147091146-model`: Signaling: AjayBhalla2007BistableModel9147091146Model
- `signaling-sbml-ajay-bhalla-2007-pkm-model9147232940-model`: Signaling: AjayBhalla2007PkmModel9147232940Model
- `signaling-sbml-asthagiri2001-mapk-asthagiri-adapt-fb-model9147975215-model`: Signaling: Asthagiri2001MapkAsthagiriAdaptFbModel9147975215Model

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
- signaling-sbml-ajay-bhalla-2007-bistable-model9147091146-model :: biomodels_ebi:MODEL9147091146 :: https://www.ebi.ac.uk/biomodels/MODEL9147091146
- signaling-sbml-ajay-bhalla-2007-pkm-model9147232940-model :: biomodels_ebi:MODEL9147232940 :: https://www.ebi.ac.uk/biomodels/MODEL9147232940
- signaling-sbml-asthagiri2001-mapk-asthagiri-adapt-fb-model9147975215-model :: biomodels_ebi:MODEL9147975215 :: https://www.ebi.ac.uk/biomodels/MODEL9147975215

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
