# COMBO_0049 - Signaling Immune Signaling

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
- `signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000448-model`: Signaling: BrNnmark2013InsulinSignallingInHumanAdipocBiomd0000000448Model
- `signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000449-model`: Signaling: BrNnmark2013InsulinSignallingInHumanAdipocBiomd0000000449Model
- `signaling-sbml-brown2004-ngf-and-egf-signaling-biomd0000000033-model`: Signaling: Brown2004NgfAndEgfSignalingBiomd0000000033Model

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
- signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000448-model :: biomodels_ebi:BIOMD0000000448 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000448
- signaling-sbml-br-nnmark2013-insulin-signalling-in-human-adipoc-biomd0000000449-model :: biomodels_ebi:BIOMD0000000449 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000449
- signaling-sbml-brown2004-ngf-and-egf-signaling-biomd0000000033-model :: biomodels_ebi:BIOMD0000000033 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000033

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
