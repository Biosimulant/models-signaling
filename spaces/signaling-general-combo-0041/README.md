# COMBO_0041 - Signaling General

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
- `signaling-sbml-kok2020-ifnalpha-induced-signaling-in-huh7-5-cel-biomd0000000959-model`: Signaling: Kok2020IfnalphaInducedSignalingInHuh75CelBiomd0000000959Model
- `signaling-sbml-kolodkin2013-nuclear-receptor-mediated-cortisol-biomd0000000576-model`: Signaling: Kolodkin2013NuclearReceptorMediatedCortisolBiomd0000000576Model
- `signaling-sbml-komarova2005-theoreticalframework-basicarchitect-biomd0000000125-model`: Signaling: Komarova2005TheoreticalframeworkBasicarchitectBiomd0000000125Model

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
- signaling-sbml-kok2020-ifnalpha-induced-signaling-in-huh7-5-cel-biomd0000000959-model :: biomodels_ebi:BIOMD0000000959 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000959
- signaling-sbml-kolodkin2013-nuclear-receptor-mediated-cortisol-biomd0000000576-model :: biomodels_ebi:BIOMD0000000576 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000576
- signaling-sbml-komarova2005-theoreticalframework-basicarchitect-biomd0000000125-model :: biomodels_ebi:BIOMD0000000125 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000125

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
