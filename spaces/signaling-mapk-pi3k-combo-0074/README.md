# COMBO_0074 - Signaling Mapk Pi3K

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
- `signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280032-model`: Signaling: Sarma2012InteractionTopologiesOfMapkCascadeModel1204280032Model
- `signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280033-model`: Signaling: Sarma2012InteractionTopologiesOfMapkCascadeModel1204280033Model
- `signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280034-model`: Signaling: Sarma2012InteractionTopologiesOfMapkCascadeModel1204280034Model
- `signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280035-model`: Signaling: Sarma2012InteractionTopologiesOfMapkCascadeModel1204280035Model

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
- signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280032-model :: biomodels_ebi:MODEL1204280032 :: https://www.ebi.ac.uk/biomodels/MODEL1204280032
- signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280033-model :: biomodels_ebi:MODEL1204280033 :: https://www.ebi.ac.uk/biomodels/MODEL1204280033
- signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280034-model :: biomodels_ebi:MODEL1204280034 :: https://www.ebi.ac.uk/biomodels/MODEL1204280034
- signaling-sbml-sarma2012-interaction-topologies-of-mapk-cascade-model1204280035-model :: biomodels_ebi:MODEL1204280035 :: https://www.ebi.ac.uk/biomodels/MODEL1204280035

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
