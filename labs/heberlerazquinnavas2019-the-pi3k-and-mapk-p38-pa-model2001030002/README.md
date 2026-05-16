# HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2

This Biosimulant lab wraps `HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for MAPK/ERK receptor signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2 propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on X1 0, X1 1, X2 0, X2 1, X2 2, and X4 0, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **P70 S6K PT229 Obs** moved from 0.1941 to 0.1445 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2 - run interpretation](assets/01-visualisation-table.png)

*Summary table for HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2 - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of P70 S6K PT229 Obs, P70 S6K PT389 Obs, TSC1 TSC2 PT1462 Obs, PRAS40 PS183 Obs, IRS1 PS636 639 Obs, and X10 2 across the 1.0 simulation. In this run **TSC1 TSC2 PT1462 Obs** climbed from 0.1453 to 0.1782 and **P70 S6K PT229 Obs** fell from 0.1941 to 0.1445 — the largest movements among the focused observables.*

![HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 2 - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **X5 0** = 9.995, **X10 0** = 6.512, **X8 0** = 6.406, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2001030002`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial AKT P S473 Obs | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.initial_akt_p_s473_obs` |  | Initial level of AKT P S473 Obs. Maps to SBML symbol `Akt_pS473_obs`; exposed as a traceable initial-condition perturbation. |
| Initial AKT P T308 Obs | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.initial_akt_p_t308_obs` |  | Initial level of AKT P T308 Obs. Maps to SBML symbol `Akt_pT308_obs`; exposed as a traceable initial-condition perturbation. |
| Initial Four EBP1 P T37 46 Obs | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.initial_four_ebp1_p_t37_46_obs` |  | Initial level of Four EBP1 P T37 46 Obs. Maps to SBML symbol `fourEBP1_pT37_46_obs`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `akt_p_t308_obs` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.akt_p_t308_obs` | AKT P T308 Obs. |
| `akt_p_s473_obs` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.akt_p_s473_obs` | AKT P S473 Obs. |
| `pras40_p_t246_obs` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.pras40_p_t246_obs` | PRAS40 P T246 Obs. |
| `state` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_heberlerazquinnavas2019_the_pi3k_and_mapk_p38_pa_model2001030002_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
