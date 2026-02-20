# COMBO_0060 - Signaling Mapk Pi3K

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
- `signaling-sbml-lee2008-erk-and-pi3k-signal-integration-by-myc-biomd0000000818-model`: Signaling: Lee2008ErkAndPi3kSignalIntegrationByMycBiomd0000000818Model
- `signaling-sbml-levchenko2000-mapk-noscaffold-biomd0000000011-model`: Signaling: Levchenko2000MapkNoscaffoldBiomd0000000011Model
- `signaling-sbml-levchenko2000-mapk-scaffold-biomd0000000014-model`: Signaling: Levchenko2000MapkScaffoldBiomd0000000014Model
- `signaling-sbml-markevich2004-mapk-double-phosphorylation-ordere-biomd0000000027-model`: Signaling: Markevich2004MapkDoublePhosphorylationOrdereBiomd0000000027Model

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
- signaling-sbml-lee2008-erk-and-pi3k-signal-integration-by-myc-biomd0000000818-model :: biomodels_ebi:BIOMD0000000818 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000818
- signaling-sbml-levchenko2000-mapk-noscaffold-biomd0000000011-model :: biomodels_ebi:BIOMD0000000011 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000011
- signaling-sbml-levchenko2000-mapk-scaffold-biomd0000000014-model :: biomodels_ebi:BIOMD0000000014 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000014
- signaling-sbml-markevich2004-mapk-double-phosphorylation-ordere-biomd0000000027-model :: biomodels_ebi:BIOMD0000000027 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000027

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
