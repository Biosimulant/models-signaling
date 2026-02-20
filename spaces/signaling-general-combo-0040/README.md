# COMBO_0040 - Signaling General

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
- `signaling-sbml-kholodenko1999-egfr-signaling-biomd0000000048-model`: Signaling: Kholodenko1999EgfrSignalingBiomd0000000048Model
- `signaling-sbml-koch2005-sucrose-breakdown-pathway-petri-net-model1308080002-model`: Signaling: Koch2005SucroseBreakdownPathwayPetriNetModel1308080002Model
- `signaling-sbml-kofahl2004-pheromonepathway-biomd0000000032-model`: Signaling: Kofahl2004PheromonepathwayBiomd0000000032Model

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
- signaling-sbml-kholodenko1999-egfr-signaling-biomd0000000048-model :: biomodels_ebi:BIOMD0000000048 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000048
- signaling-sbml-koch2005-sucrose-breakdown-pathway-petri-net-model1308080002-model :: biomodels_ebi:MODEL1308080002 :: https://www.ebi.ac.uk/biomodels/MODEL1308080002
- signaling-sbml-kofahl2004-pheromonepathway-biomd0000000032-model :: biomodels_ebi:BIOMD0000000032 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000032

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
