# Hornberg2005 - MAPKsignalling

This Biosimulant lab wraps `Hornberg2005 - MAPKsignalling` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for MAPK/ERK receptor signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Hornberg2005 - MAPKsignalling propagate receptor or RAS/ERK pathway activity? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on EGF, EGFR, EGF EGFR, EGF EGFR 2, Egfri, and EGF EGFR 2 GAP Grb2 adapter protein Prot, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **EGFR** moved from 5e+04 to 1.3e+04 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Hornberg2005 - MAPKsignalling - run interpretation](assets/01-visualisation-table.png)

*Summary table for Hornberg2005 - MAPKsignalling, reporting the scientific question, observed answer, dominant module, and caveat.*

![Hornberg2005 - MAPKsignalling - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of EGFR, EGF EGFR, EGF EGFR2, GRB2, Sos, and GRB2 Sos across the 1.0 simulation. In this run **EGF EGFR** climbed from 0 to 2.54e+04 and **EGFR** fell from 5e+04 to 1.3e+04 — the largest movements among the focused observables.*

![Hornberg2005 - MAPKsignalling - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **ERK** = 2.21e+07, **MEK** = 2.1e+07, **PHOSPHATASE3** = 1e+07, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000667`
- License: `CC0`
- Visual scope: receptor-to-MAPK cascade signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial EGF | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.initial_egf` |  | Initial level of EGF. Maps to SBML symbol `EGF`; exposed as a traceable initial-condition perturbation. |
| Initial EGF EGFR | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.initial_egf_egfr` |  | Initial level of EGF EGFR. Maps to SBML symbol `EGF_EGFR`; exposed as a traceable initial-condition perturbation. |
| Initial EGF EGFR 2 | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.initial_egf_egfr_2` |  | Initial level of EGF EGFR 2. Maps to SBML symbol `_EGF_EGFR_2`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp` | EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GDP. |
| `egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp` | EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GTP. |
| `ras_gdp` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.ras_gdp` | RAS GDP. |
| `state` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_hornberg2005_mapksignalling_biomd0000000667_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
