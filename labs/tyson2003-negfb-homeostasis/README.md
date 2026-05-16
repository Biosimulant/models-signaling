# Tyson2003_NegFB_Homeostasis

This Biosimulant lab wraps `Tyson2003_NegFB_Homeostasis` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Tyson2003_NegFB_Homeostasis. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Tyson2003 NegFB Homeostasis propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Source Defined R State, Source Defined S State, Source Defined EP State, and Source Defined E State, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Source Defined E State** moved from 1.0000 to 0.0815 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Tyson2003_NegFB_Homeostasis - run interpretation](assets/01-visualisation-table.png)

*Summary table for Tyson2003_NegFB_Homeostasis, reporting the scientific question, observed answer, dominant module, and caveat.*

![Tyson2003_NegFB_Homeostasis - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of Source Defined EP State, Source Defined E State, Source Defined R State, and Source Defined S State across the 1.0 simulation. In this run **Source Defined EP State** climbed from 8.88e-16 to 0.9185 and **Source Defined E State** fell from 1.0000 to 0.0815 — the largest movements among the focused observables.*

![Tyson2003_NegFB_Homeostasis - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Source Defined EP State** = 0.9185, **Source Defined R State** = 0.5553, **Source Defined E State** = 0.0815, with 1 more observable below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000309`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial source-defined E state | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.initial_source_defined_e_state` |  | Initial level of source-defined E state. Maps to SBML symbol `E`; exposed as a traceable initial-condition perturbation. |
| Initial source-defined EP state | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.initial_source_defined_ep_state` |  | Initial level of source-defined EP state. Maps to SBML symbol `Ep`; exposed as a traceable initial-condition perturbation. |
| Initial source-defined S state | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.initial_source_defined_s_state` |  | Initial level of source-defined S state. Maps to SBML symbol `S`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `source_defined_r_state` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.source_defined_r_state` | Source Defined R State. |
| `source_defined_s_state` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.source_defined_s_state` | Source Defined S State. |
| `source_defined_ep_state` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.source_defined_ep_state` | Source Defined EP State. |
| `state` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_tyson2003_negfb_homeostasis_biomd0000000309_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
