# Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net

This Biosimulant lab wraps `Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for NF-kB pathway signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net move NF-kB and inhibitor-linked signaling states? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on CD40, C IAP1 2 Ub, CD40L, source-defined TRAF3 state, CD40 CD40L, and P100 Phos Rel B, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **CD40** moved from 0 to 0 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net - run interpretation](assets/01-visualisation-table.png)

*Summary table for Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net, reporting the scientific question, observed answer, dominant module, and caveat.*

![Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of CD40, C IAP1 2 Ub, CD40L, source-defined TRAF3 state, CD40 CD40L, and P100 Phos Rel B across the 1.0 simulation. In this run CD40, C IAP1 2 Ub, CD40L, source-defined TRAF3 state stayed near their initial values — no observable moved appreciably.*

![Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **CD40** = 0, **C IAP1 2 Ub** = 0, **CD40L** = 0, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2207210003`
- License: `CC0`
- Visual scope: NF-kB activation and feedback signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial CD40 | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.initial_cd40` |  | Initial level of CD40. Maps to SBML symbol `P0`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `ikk_complex_c` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.ikk_complex_c` | IKK Complex C. |
| `ikk_complex` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.ikk_complex` | IKK Complex. |
| `ikk_complex_activated` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.ikk_complex_activated` | IKK Complex Activated. |
| `state` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_trares2022_crosstalk_between_the_canonical_and_n_model2207210003_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
