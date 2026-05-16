# Strasen2018 - TGFb SMAD Signalling Class 4

This Biosimulant lab wraps `Strasen2018 - TGFb SMAD Signalling Class 4` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for developmental and growth-control signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Strasen2018 - TGFb SMAD Signalling Class 4 propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on TGF-beta TGFR1 Surface, TGF-beta TGFR2 Surface, TGF-beta TGFR1 Endo, TGF-beta TGFR2 Endo, TGF-beta, and TGF-beta In, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **SMAD2 C** moved from 1967.8 to 1949.5 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Strasen2018 - TGFb SMAD Signalling Class 4 - run interpretation](assets/01-visualisation-table.png)

*Summary table for Strasen2018 - TGFb SMAD Signalling Class 4, reporting the scientific question, observed answer, dominant module, and caveat.*

![Strasen2018 - TGFb SMAD Signalling Class 4 - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of SMAD2 C, SMAD4 C, P S2 P S2 S4 C, TGF-beta TGFR1 Surface, TGF-beta TGFR2 Surface, and Inactive TGF-beta TGFR1 TGFR2 across the 1.0 simulation. In this run **P S2 P S2 S4 C** climbed from 0 to 9.418 and **SMAD2 C** fell from 1967.8 to 1949.5 — the largest movements among the focused observables.*

![Strasen2018 - TGFb SMAD Signalling Class 4 - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **SMAD2 C** = 1949.5, **SMAD4 C** = 633.7, **SMAD2 N** = 329.5, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001001`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Index Induced Ligand Deg | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.initial_index_induced_ligand_deg_level` |  | Index Induced Ligand Deg source parameter. Maps to SBML symbol `index_induced_ligand_deg` and preserves the bundled default. |
| Kin Deg Ligand | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.initial_kin_deg_ligand_level` |  | Kin Deg Ligand source parameter. Maps to SBML symbol `kin_deg_Ligand` and preserves the bundled default. |
| Kout Deg Ligand 100p M | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.initial_kout_deg_ligand_100p_m_level` |  | Kout Deg Ligand 100p M source parameter. Maps to SBML symbol `kout_deg_Ligand_100pM` and preserves the bundled default. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `active_tgfr2` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.active_tgfr2` | active TGFR2. |
| `active_tgf_beta_tgfr1_tgfr2` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.active_tgf_beta_tgfr1_tgfr2` | active TGF-beta TGFR1 TGFR2. |
| `active_tgf_beta_tgfr1_tgfr2_endo` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.active_tgf_beta_tgfr1_tgfr2_endo` | active TGF-beta TGFR1 TGFR2 Endo. |
| `state` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_strasen2018_tgfb_smad_signalling_class_4_biomd0000001001_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
