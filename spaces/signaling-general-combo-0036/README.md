# COMBO_0036 - Signaling General

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
- `signaling-sbml-ihekwaba2004-nfkb-sensitivity-biomd0000000230-model`: Signaling: Ihekwaba2004NfkbSensitivityBiomd0000000230Model
- `signaling-sbml-integrated-model-of-dna-damage-response-and-p53-model2503190002-model`: Signaling: IntegratedModelOfDnaDamageResponseAndP53Model2503190002Model
- `signaling-sbml-ito2019-gefitnib-resistance-of-lung-adenocarcino-biomd0000000827-model`: Signaling: Ito2019GefitnibResistanceOfLungAdenocarcinoBiomd0000000827Model

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
- signaling-sbml-ihekwaba2004-nfkb-sensitivity-biomd0000000230-model :: biomodels_ebi:BIOMD0000000230 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000230
- signaling-sbml-integrated-model-of-dna-damage-response-and-p53-model2503190002-model :: biomodels_ebi:MODEL2503190002 :: https://www.ebi.ac.uk/biomodels/MODEL2503190002
- signaling-sbml-ito2019-gefitnib-resistance-of-lung-adenocarcino-biomd0000000827-model :: biomodels_ebi:BIOMD0000000827 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000827

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
