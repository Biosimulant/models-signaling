# Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1

This Biosimulant lab wraps `Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for developmental and growth-control signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1 shift hormone-linked signaling readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on source-defined DSH_I state, source-defined DSH_A state, APC Axin GSK3, source-defined GSK3 state, APC Axin, and source-defined APC state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **FWD1** moved from 0 to 26.928 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1 - run interpretation](assets/01-visualisation-table.png)

*Summary table for Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1, reporting the scientific question, observed answer, dominant module, and caveat.*

![Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1 - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of FWD1, B Catenin*, B Catenin, TCF, B Catenin TCF, and B Catenin* APC* Axin* GSK3 FWD1 across the 1.0 simulation. In this run **FWD1** climbed from 0 to 26.928 and **B Catenin*** fell from 1.000 to 0.9908 — the largest movements among the focused observables.*

![Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1 - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Dsh I** = 100.0, **APC** = 98.000, **GSK3** = 50.000, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1908050003`
- License: `CC0`
- Visual scope: metabolic and hormone signaling response
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial source-defined WNT state | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.initial_source_defined_wnt_state` |  | Initial level of source-defined WNT state. Maps to SBML symbol `Wnt`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `b_catenin_apc_axin_gsk3` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.b_catenin_apc_axin_gsk3` | B Catenin APC Axin GSK3. |
| `b_catenin_apc_axin_gsk3_2` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.b_catenin_apc_axin_gsk3_2` | B Catenin APC Axin GSK3. |
| `b_catenin` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.b_catenin` | B Catenin. |
| `state` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_benary2015_feedback_regulation_of_beta_catenin_p_model1908050003_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
