# Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ)

This Biosimulant lab wraps `Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ)` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for MAPK/ERK receptor signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Sarma2012 - Interaction topologies of MAPK cascade (M4 K2 USEQ) propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on MAP kinase, MAPK kinase PP, MAP kinase MAPK kinase PP, source-defined MK-P state, MAP kinase P MAPK kinase PP, and source-defined MK-PP state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **MAPK kinase kinase** moved from 300.0 to 286.8 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ) - run interpretation](assets/01-visualisation-table.png)

*Summary table for Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ), reporting the scientific question, observed answer, dominant module, and caveat.*

![Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ) - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of MAPK kinase kinase, source-defined SIG state, MAPK kinase kinase Sig, MAPK kinase, MAPK kinase MAPK kinase kinase P, and MAPK kinase kinase P across the 1.0 simulation. In this run **MAPK kinase kinase Sig** climbed from 0 to 7.415 and **MAPK kinase kinase** fell from 300.0 to 286.8 — the largest movements among the focused observables.*

![Sarma2012 - Interaction topologies of MAPK cascade (M4_K2_USEQ) - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **MAP kinase** = 1200.0, **MAPK kinase** = 1195.1, **MAPK kinase kinase** = 286.8, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000430`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial MAP kinase | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.initial_map_kinase` |  | Initial level of MAP kinase. Maps to SBML symbol `species_1`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `mapk_kinase_pp` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.mapk_kinase_pp` | MAPK kinase PP. |
| `map_kinase_mapk_kinase_pp` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.map_kinase_mapk_kinase_pp` | MAP kinase MAPK kinase PP. |
| `source_defined_mk_p_state` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.source_defined_mk_p_state` | source-defined MK-P state. |
| `state` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_sarma2012_interaction_topologies_of_mapk_cascade_biomd0000000430_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
