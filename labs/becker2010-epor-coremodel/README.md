# Becker2010_EpoR_CoreModel

This Biosimulant lab wraps `Becker2010_EpoR_CoreModel` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Becker2010_EpoR_CoreModel. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Becker2010 EpoR CoreModel route receptor activity into cAMP/PKA-linked readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on EPO receptor, erythropoietin, erythropoietin erythropoietin R, and erythropoietin erythropoietin Ri, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Epo** moved from 2030.2 to 1942.6 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Becker2010_EpoR_CoreModel - run interpretation](assets/01-visualisation-table.png)

*Summary table for Becker2010_EpoR_CoreModel, reporting the scientific question, observed answer, dominant module, and caveat.*

![Becker2010_EpoR_CoreModel - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of Epo, EpoR, Epo EpoR, and Epo EpoRi across the 1.0 simulation. In this run **Epo EpoR** climbed from 0 to 84.640 and **Epo** fell from 2030.2 to 1942.6 — the largest movements among the focused observables.*

![Becker2010_EpoR_CoreModel - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Epo** = 1942.6, **EpoR** = 429.7, **Epo EpoR** = 84.640, with 1 more observable below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000271`
- License: `CC0`
- Visual scope: GPCR and cAMP/PKA signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial EPO receptor | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.initial_epo_receptor` |  | Initial level of EPO receptor. Maps to SBML symbol `EpoR`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `epo_receptor` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.epo_receptor` | EPO receptor. |
| `erythropoietin` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.erythropoietin` | erythropoietin. |
| `erythropoietin_erythropoietin_r` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.erythropoietin_erythropoietin_r` | erythropoietin erythropoietin R. |
| `state` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_becker2010_epor_coremodel_biomd0000000271_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
