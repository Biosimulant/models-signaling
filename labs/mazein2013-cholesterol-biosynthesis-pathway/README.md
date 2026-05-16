# Mazein2013 - Cholesterol biosynthesis pathway

This Biosimulant lab wraps `Mazein2013 - Cholesterol biosynthesis pathway` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for metabolic and hormone-linked signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Mazein2013 - Cholesterol biosynthesis pathway shift hormone-linked signaling readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Acety Co A, Acetoacetyl Co A, 3 Hydroxy 3 Methylglutaryl Co A, Mevalonate, Acetoacetate, and HMGCR, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Acety Co A** moved from 0 to 0 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Mazein2013 - Cholesterol biosynthesis pathway - run interpretation](assets/01-visualisation-table.png)

*Summary table for Mazein2013 - Cholesterol biosynthesis pathway, reporting the scientific question, observed answer, dominant module, and caveat.*

![Mazein2013 - Cholesterol biosynthesis pathway - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of Acety Co A, Acetoacetyl Co A, 3 Hydroxy 3 Methylglutaryl Co A, Mevalonate, Acetoacetate, and HMGCR across the 1.0 simulation. In this run Acety Co A, Acetoacetyl Co A, 3 Hydroxy 3 Methylglutaryl Co A, Mevalonate stayed near their initial values — no observable moved appreciably.*

![Mazein2013 - Cholesterol biosynthesis pathway - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Acety Co A** = 0, **Acetoacetyl Co A** = 0, **3 Hydroxy 3 Methylglutaryl Co A** = 0, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1409170000`
- License: `CC0`
- Visual scope: metabolic and hormone signaling response
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Acety Co A | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.initial_acety_co_a` |  | Initial level of Acety Co A. Maps to SBML symbol `s1`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `source_defined_acat2_state` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.source_defined_acat2_state` | source-defined ACAT2 state. |
| `acety_co_a` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.acety_co_a` | Acety Co A. |
| `acetoacetyl_co_a` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.acetoacetyl_co_a` | Acetoacetyl Co A. |
| `state` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_mazein2013_cholesterol_biosynthesis_pathway_model1409170000_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
