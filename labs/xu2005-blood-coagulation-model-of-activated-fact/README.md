# Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI

This Biosimulant lab wraps `Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI shift hormone-linked signaling readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on source-defined X1 state, source-defined X2 state, source-defined X3 state, source-defined X4 state, source-defined X5 state, and source-defined X6 state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **source-defined X2 state** moved from 0 to 13.235 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI - run interpretation](assets/01-visualisation-table.png)

*Summary table for Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI, reporting the scientific question, observed answer, dominant module, and caveat.*

![Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of source-defined X2 state, source-defined X1 state, source-defined X3 state, source-defined X4 state, source-defined X5 state, and source-defined X6 state across the 1.0 simulation. In this run **source-defined X2 state** climbed from 0 to 13.235 — the largest movements among the focused observables.*

![Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **source-defined X2 state** = 13.235, **source-defined X1 state** = 6.300, **source-defined X3 state** = 2.082, with 4 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1806130002`
- License: `CC0`
- Visual scope: metabolic and hormone signaling response
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial source-defined X1 state | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.initial_source_defined_x1_state` |  | Initial level of source-defined X1 state. Maps to SBML symbol `x1`; exposed as a traceable initial-condition perturbation. |
| Initial source-defined X2 state | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.initial_source_defined_x2_state` |  | Initial level of source-defined X2 state. Maps to SBML symbol `x2`; exposed as a traceable initial-condition perturbation. |
| Initial source-defined X3 state | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.initial_source_defined_x3_state` |  | Initial level of source-defined X3 state. Maps to SBML symbol `x3`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `source_defined_x1_state` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.source_defined_x1_state` | source-defined X1 state. |
| `source_defined_x2_state` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.source_defined_x2_state` | source-defined X2 state. |
| `source_defined_x3_state` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.source_defined_x3_state` | source-defined X3 state. |
| `state` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_xu2005_blood_coagulation_model_of_activated_fact_model1806130002_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
