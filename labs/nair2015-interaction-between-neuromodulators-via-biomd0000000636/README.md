# Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron)

This Biosimulant lab wraps `Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron)` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron). It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron) route receptor activity into cAMP/PKA-linked readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Gai GTP, Gaolf GDP, Gbgolf, Gaolf GTP, Golf G protein, and A2argolf, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **D2rdagi** moved from 3.04e-13 to 3.04e-13 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron) - run interpretation](assets/01-visualisation-table.png)

*Summary table for Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron), reporting the scientific question, observed answer, dominant module, and caveat.*

![Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron) - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of D2rdagi, D2R, source-defined GI state, PDE4 C AMP, source-defined PDE4 state, and cAMP across the 1.0 simulation. In this run **D2rdagi** climbed from 3.04e-13 to 3.04e-13 and **D2R** fell from 1.18e-12 to 1.18e-12 — the largest movements among the focused observables.*

![Nair2015 - Interaction between neuromodulators via GPCRs - Effect on cAMP/PKA signaling (D2 Neuron) - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **ATP** = 5e-09, **DARPP32** = 3.68e-11, **D32p75** = 9.81e-12, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000636`
- License: `CC0`
- Visual scope: GPCR and cAMP/PKA signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial adenosine | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.initial_adenosine` |  | Initial level of adenosine. Maps to SBML symbol `mwbe974953_e869_4622_b4a8_745555c8d7fd`; exposed as a traceable initial-condition perturbation. |
| Initial AMP | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.initial_amp` |  | Initial level of AMP. Maps to SBML symbol `mw9710c658_a2a1_4f49_b494_af109853f251`; exposed as a traceable initial-condition perturbation. |
| Initial ATP | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.initial_atp` |  | Initial level of ATP. Maps to SBML symbol `mw46dccec6_6f0f_40f6_a10c_2f34ae7a005a`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `golf_g_protein` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.golf_g_protein` | Golf G protein. |
| `camp` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.camp` | cAMP. |
| `source_defined_ac5_state` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.source_defined_ac5_state` | source-defined AC5 state. |
| `state` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_nair2015_interaction_between_neuromodulators_via_biomd0000000636_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
