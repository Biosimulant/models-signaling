# COMBO_0038 - Signaling General

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
- `signaling-sbml-jung2019-regulating-glioblastoma-signaling-pathw-biomd0000000828-model`: Signaling: Jung2019RegulatingGlioblastomaSignalingPathwBiomd0000000828Model
- `signaling-sbml-kawka2014-revealing-the-role-of-sgk1-in-the-dyna-model1912090002-model`: Signaling: Kawka2014RevealingTheRoleOfSgk1InTheDynaModel1912090002Model
- `signaling-sbml-keizer1996-ryanodine-receptor-adaptation-biomd0000000060-model`: Signaling: Keizer1996RyanodineReceptorAdaptationBiomd0000000060Model

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
- signaling-sbml-jung2019-regulating-glioblastoma-signaling-pathw-biomd0000000828-model :: biomodels_ebi:BIOMD0000000828 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000828
- signaling-sbml-kawka2014-revealing-the-role-of-sgk1-in-the-dyna-model1912090002-model :: biomodels_ebi:MODEL1912090002 :: https://www.ebi.ac.uk/biomodels/MODEL1912090002
- signaling-sbml-keizer1996-ryanodine-receptor-adaptation-biomd0000000060-model :: biomodels_ebi:BIOMD0000000060 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000060

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
