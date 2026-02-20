# COMBO_0050 - Signaling Immune Signaling

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
- `signaling-sbml-chaouiya2013-egf-and-tnfalpha-mediated-signallin-biomd0000000562-model`: Signaling: Chaouiya2013EgfAndTnfalphaMediatedSignallinBiomd0000000562Model
- `signaling-sbml-collier1996-delta-notch-intercellular-signalling-biomd0000001047-model`: Signaling: Collier1996DeltaNotchIntercellularSignallingBiomd0000001047Model
- `signaling-sbml-dutta-roy2015-opening-of-the-multiple-ampa-recep-biomd0000000569-model`: Signaling: DuttaRoy2015OpeningOfTheMultipleAmpaRecepBiomd0000000569Model

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
- signaling-sbml-chaouiya2013-egf-and-tnfalpha-mediated-signallin-biomd0000000562-model :: biomodels_ebi:BIOMD0000000562 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000562
- signaling-sbml-collier1996-delta-notch-intercellular-signalling-biomd0000001047-model :: biomodels_ebi:BIOMD0000001047 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001047
- signaling-sbml-dutta-roy2015-opening-of-the-multiple-ampa-recep-biomd0000000569-model :: biomodels_ebi:BIOMD0000000569 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000569

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
