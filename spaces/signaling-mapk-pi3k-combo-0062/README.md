# COMBO_0062 - Signaling Mapk Pi3K

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
- `signaling-sbml-muller2008-simplified-mapk-activation-dynamics-m-biomd0000000664-model`: Signaling: Muller2008SimplifiedMapkActivationDynamicsMBiomd0000000664Model
- `signaling-sbml-nakakuki2010-cellfatedecision-core-biomd0000000251-model`: Signaling: Nakakuki2010CellfatedecisionCoreBiomd0000000251Model
- `signaling-sbml-nakakuki2010-cellfatedecision-mechanistic-biomd0000000250-model`: Signaling: Nakakuki2010CellfatedecisionMechanisticBiomd0000000250Model
- `signaling-sbml-padala2017-erk-pi3k-akt-and-wnt-signalling-netwo-biomd0000000648-model`: Signaling: Padala2017ErkPi3kAktAndWntSignallingNetwoBiomd0000000648Model

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
- signaling-sbml-muller2008-simplified-mapk-activation-dynamics-m-biomd0000000664-model :: biomodels_ebi:BIOMD0000000664 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000664
- signaling-sbml-nakakuki2010-cellfatedecision-core-biomd0000000251-model :: biomodels_ebi:BIOMD0000000251 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000251
- signaling-sbml-nakakuki2010-cellfatedecision-mechanistic-biomd0000000250-model :: biomodels_ebi:BIOMD0000000250 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000250
- signaling-sbml-padala2017-erk-pi3k-akt-and-wnt-signalling-netwo-biomd0000000648-model :: biomodels_ebi:BIOMD0000000648 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000648

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
