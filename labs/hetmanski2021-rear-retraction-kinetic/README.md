# Hetmanski2021 rear retraction kinetic

This Biosimulant lab wraps `Hetmanski2021 rear retraction kinetic` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Hetmanski2021 rear retraction kinetic. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Hetmanski2021 rear retraction kinetic route receptor activity into cAMP/PKA-linked readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Rho Agdp, Rho Agtp, Rock1i, Rock1a, Rho A Rock1, and source-defined DRFI state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **RhoAgdp** moved from 100.0 to 28.581 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Hetmanski2021 rear retraction kinetic - run interpretation](assets/01-visualisation-table.png)

*Summary table for Hetmanski2021 rear retraction kinetic, reporting the scientific question, observed answer, dominant module, and caveat.*

![Hetmanski2021 rear retraction kinetic - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of RhoAgdp, Gefa, P190GAPi, Rho Gef, Srca, and Cav1i across the 1.0 simulation. In this run **Rho Gef** climbed from 0 to 40.875 and **RhoAgdp** fell from 100.0 to 28.581 — the largest movements among the focused observables.*

![Hetmanski2021 rear retraction kinetic - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Polcont.Low** = 100.0, **Polystiff.High** = 100.0, **Tension.I** = 100.0, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2103010001`
- License: `CC0`
- Visual scope: GPCR and cAMP/PKA signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Rho Agdp | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.initial_rho_agdp` |  | Initial level of Rho Agdp. Maps to SBML symbol `RhoAgdp`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `actinf` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.actinf` | Actinf. |
| `p_mlca` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.p_mlca` | P Mlca. |
| `cavi_src` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.cavi_src` | Cavi Src. |
| `state` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_hetmanski2021_rear_retraction_kinetic_model2103010001_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
