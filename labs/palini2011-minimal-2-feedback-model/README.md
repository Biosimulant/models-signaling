# Palini2011_Minimal_2_Feedback_Model

This Biosimulant lab wraps `Palini2011_Minimal_2_Feedback_Model` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Palini2011_Minimal_2_Feedback_Model. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Palini2011 Minimal 2 Feedback Model route receptor activity into cAMP/PKA-linked readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Source Defined L State, Source Defined R State, Source Defined C State, Source Defined I State, Response Node X, and Source Defined A State, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **source-defined R state** moved from 1.000 to 0.9999 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Palini2011_Minimal_2_Feedback_Model - run interpretation](assets/01-visualisation-table.png)

*Summary table for Palini2011_Minimal_2_Feedback_Model, reporting the scientific question, observed answer, dominant module, and caveat.*

![Palini2011_Minimal_2_Feedback_Model - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of source-defined R state, source-defined C state, source-defined I state, source-defined A state, response node X, and source-defined L state across the 1.0 simulation. In this run **source-defined C state** climbed from 0 to 8.6e-05 and **source-defined R state** fell from 1.000 to 0.9999 — the largest movements among the focused observables.*

![Palini2011_Minimal_2_Feedback_Model - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **source-defined I state** = 1.0000, **source-defined R state** = 0.9999, **source-defined L state** = 0.1000, with 3 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000325`
- License: `CC0`
- Visual scope: GPCR and cAMP/PKA signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial source-defined L state | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.initial_source_defined_l_state` |  | Initial level of source-defined L state. Maps to SBML symbol `L`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `source_defined_l_state` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.source_defined_l_state` | Source Defined L State. |
| `source_defined_r_state` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.source_defined_r_state` | Source Defined R State. |
| `source_defined_c_state` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.source_defined_c_state` | Source Defined C State. |
| `state` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_palini2011_minimal_2_feedback_model_biomd0000000325_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
