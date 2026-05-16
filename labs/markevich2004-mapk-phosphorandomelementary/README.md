# Markevich2004_MAPK_phosphoRandomElementary

This Biosimulant lab wraps `Markevich2004_MAPK_phosphoRandomElementary` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for MAPK/ERK receptor signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Markevich2004 MAPK phosphoRandomElementary propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on ERK, ERK PY, ERK PT, ERK PP, MEK, and source-defined MKP3 state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **ERK** moved from 800.0 to 540.6 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Markevich2004_MAPK_phosphoRandomElementary - run interpretation](assets/01-visualisation-table.png)

*Summary table for Markevich2004_MAPK_phosphoRandomElementary, reporting the scientific question, observed answer, dominant module, and caveat.*

![Markevich2004_MAPK_phosphoRandomElementary - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of ERK, MEK, ERK MEK T, source-defined MKP3 state, ERK MKP3 Y, and ERK MKP3 T across the 1.0 simulation. In this run **ERK MEK T** climbed from 0 to 163.9 and **ERK** fell from 800.0 to 540.6 — the largest movements among the focused observables.*

![Markevich2004_MAPK_phosphoRandomElementary - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **ERK** = 540.6, **ERK MEK T** = 163.9, **ERK MKP3 Y** = 45.581, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000028`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial ERK | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.initial_erk` |  | Initial level of ERK. Maps to SBML symbol `M`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `erk` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.erk` | ERK. |
| `erk_py` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.erk_py` | ERK PY. |
| `erk_pt` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.erk_pt` | ERK PT. |
| `state` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_markevich2004_mapk_phosphorandomelementary_biomd0000000028_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
