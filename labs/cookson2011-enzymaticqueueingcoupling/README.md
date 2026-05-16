# Cookson2011_EnzymaticQueueingCoupling

This Biosimulant lab wraps `Cookson2011_EnzymaticQueueingCoupling` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Cookson2011_EnzymaticQueueingCoupling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Cookson2011 EnzymaticQueueingCoupling express its source-modeled signaling motif over the baseline run? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on source-defined X1 state, source-defined X2 state, source-defined E1 state, source-defined E2 state, source-defined E state, and source-defined E+X1 state, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **E** moved from 100.0 to 0.3838 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Cookson2011_EnzymaticQueueingCoupling - run interpretation](assets/01-visualisation-table.png)

*Summary table for Cookson2011_EnzymaticQueueingCoupling, reporting the scientific question, observed answer, dominant module, and caveat.*

![Cookson2011_EnzymaticQueueingCoupling - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of E, E1, E2, X1, X2, and EX1 across the 1.0 simulation. In this run **E1** climbed from 0 to 49.808 and **E** fell from 100.0 to 0.3838 — the largest movements among the focused observables.*

![Cookson2011_EnzymaticQueueingCoupling - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **E1** = 49.808, **E2** = 49.808, **X1** = 1.298, with 3 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000405`
- License: `CC0`
- Visual scope: phosphorylation and regulatory motif dynamics
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial source-defined X1 state | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.initial_source_defined_x1_state` |  | Initial level of source-defined X1 state. Maps to SBML symbol `species_1`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `source_defined_e_x1_state` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.source_defined_e_x1_state` | source-defined E+X1 state. |
| `source_defined_x1_state` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.source_defined_x1_state` | source-defined X1 state. |
| `source_defined_x2_state` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.source_defined_x2_state` | source-defined X2 state. |
| `state` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_cookson2011_enzymaticqueueingcoupling_biomd0000000405_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
