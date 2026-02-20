# COMBO_0077 - Signaling General

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
- `signaling-sbml-a-model-of-yeast-cell-cycle-regulation-based-on-model1812060001-model`: Signaling: AModelOfYeastCellCycleRegulationBasedOnModel1812060001Model
- `signaling-sbml-ahmedmobeen2021-nf-kb-activation-model-model2001290001-model`: Signaling: Ahmedmobeen2021NfKbActivationModelModel2001290001Model
- `signaling-sbml-almeida2019-transcription-based-circadian-mechan-biomd0000000839-model`: Signaling: Almeida2019TranscriptionBasedCircadianMechanBiomd0000000839Model
- `signaling-sbml-amara2013-pcna-ubiquitylation-in-the-activation-biomd0000000475-model`: Signaling: Amara2013PcnaUbiquitylationInTheActivationBiomd0000000475Model

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
- signaling-sbml-a-model-of-yeast-cell-cycle-regulation-based-on-model1812060001-model :: biomodels_ebi:MODEL1812060001 :: https://www.ebi.ac.uk/biomodels/MODEL1812060001
- signaling-sbml-ahmedmobeen2021-nf-kb-activation-model-model2001290001-model :: biomodels_ebi:MODEL2001290001 :: https://www.ebi.ac.uk/biomodels/MODEL2001290001
- signaling-sbml-almeida2019-transcription-based-circadian-mechan-biomd0000000839-model :: biomodels_ebi:BIOMD0000000839 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000839
- signaling-sbml-amara2013-pcna-ubiquitylation-in-the-activation-biomd0000000475-model :: biomodels_ebi:BIOMD0000000475 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000475

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
