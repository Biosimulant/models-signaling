# Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal)

This Biosimulant lab wraps `Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal)` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for MAPK/ERK receptor signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Sarma2012 - Interaction topologies of MAPK cascade (M1 K2 PSEQ short duration signal) propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on MAP kinase, MAPK kinase PP, MAP kinase MAPK kinase PP, source-defined MK-P state, MAP kinase P MAPK kinase PP, and source-defined MK-PP state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **MAP kinase** moved from 1200.0 to 1005.0 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal) - run interpretation](assets/01-visualisation-table.png)

*Summary table for Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal), reporting the scientific question, observed answer, dominant module, and caveat.*

![Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal) - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of MAP kinase, source-defined P3 state, source-defined MK_P3 state, MAPK kinase, source-defined P2 state, and source-defined MKK_P2 state across the 1.0 simulation. In this run **source-defined MK_P3 state** climbed from 0 to 195.0 and **MAP kinase** fell from 1200.0 to 1005.0 — the largest movements among the focused observables.*

![Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_PSEQ_short_duration_signal) - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **MAPK kinase** = 1097.3, **MAP kinase** = 1005.0, **MAPK kinase kinase** = 222.2, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1204280029`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial MAP kinase | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.initial_map_kinase` |  | Initial level of MAP kinase. Maps to SBML symbol `species_1`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `mapk_kinase_pp` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.mapk_kinase_pp` | MAPK kinase PP. |
| `map_kinase_mapk_kinase_pp` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.map_kinase_mapk_kinase_pp` | MAP kinase MAPK kinase PP. |
| `source_defined_mk_p_state` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.source_defined_mk_p_state` | source-defined MK-P state. |
| `state` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_model1204280029_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
