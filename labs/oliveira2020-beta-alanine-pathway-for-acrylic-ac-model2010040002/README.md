# Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol

This Biosimulant lab wraps `Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for systems signaling model: Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol shift hormone-linked signaling readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on ACCOA, source-defined ACO state, source-defined ACP state, source-defined AKG state, source-defined BPG state, and source-defined CIT state, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **source-defined GLYX state** moved from 2.17e+04 to 2.17e+04 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol - run interpretation](assets/01-visualisation-table.png)

*Summary table for Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol, reporting the scientific question, observed answer, dominant module, and caveat.*

![Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of source-defined GLYX state, source-defined GLY state, source-defined GLYP state, source-defined DHA state, aspartate ligand, and source-defined P state across the 1.0 simulation. In this run **source-defined GLY state** climbed from 1.000 to 35.159 and **source-defined GLYX state** fell from 2.17e+04 to 2.17e+04 — the largest movements among the focused observables.*

![Oliveira2020 - Beta-Alanine pathway for Acrylic Acid production from glycerol - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **source-defined GLYX state** = 2.17e+04, **source-defined PX state** = 1000.0, **source-defined GLY state** = 35.159, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2010040002`
- License: `CC0`
- Visual scope: metabolic and hormone signaling response
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial coenzyme A | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.initial_coenzyme_a` |  | Initial level of coenzyme A. Maps to SBML symbol `COA`; exposed as a traceable initial-condition perturbation. |
| Initial cysteine | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.initial_cysteine` |  | Initial level of cysteine. Maps to SBML symbol `CYS`; exposed as a traceable initial-condition perturbation. |
| Initial H2O | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.initial_h2o` |  | Initial level of H2O. Maps to SBML symbol `H2O`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `camp` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.camp` | cAMP. |
| `accoa` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.accoa` | ACCOA. |
| `source_defined_aco_state` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.source_defined_aco_state` | source-defined ACO state. |
| `state` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_oliveira2020_beta_alanine_pathway_for_acrylic_ac_model2010040002_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
