# Bakshi2020 - Properdin model of alternative pathway of complement system

This Biosimulant lab wraps `Bakshi2020 - Properdin model of alternative pathway of complement system` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for immune signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Bakshi2020 - Properdin model of alternative pathway of complement system shift hormone-linked signaling readouts? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on complement C3, complement C3b, closed complement C3bB complex, open complement C3bB complex, complement C3b complement factor Bb, and complement C3b complement factor Bb H, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **IC3b** moved from 0 to 0.000535 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Bakshi2020 - Properdin model of alternative pathway of complement system - run interpretation](assets/01-visualisation-table.png)

*Summary table for Bakshi2020 - Properdin model of alternative pathway of complement system, reporting the scientific question, observed answer, dominant module, and caveat.*

![Bakshi2020 - Properdin model of alternative pathway of complement system - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of IC3b, C3, Factor B, Properdin, C3bH, and Factor H across the 1.0 simulation. In this run **IC3b** climbed from 0 to 0.000535 — the largest movements among the focused observables.*

![Bakshi2020 - Properdin model of alternative pathway of complement system - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **C3** = 6.000, **Factor H** = 3.000, **Factor B** = 2.000, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001018`
- License: `CC0`
- Visual scope: metabolic and hormone signaling response
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial complement C3b Total | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.initial_complement_c3b_total` |  | Initial level of complement C3b Total. Maps to SBML symbol `C3b_total`; exposed as a traceable initial-condition perturbation. |
| Initial complement C3b B closed Total | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.initial_complement_c3b_b_closed_total` |  | Initial level of complement C3b B closed Total. Maps to SBML symbol `C3bB_closed_total`; exposed as a traceable initial-condition perturbation. |
| Initial complement C3b B open Total | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.initial_complement_c3b_b_open_total` |  | Initial level of complement C3b B open Total. Maps to SBML symbol `C3bB_open_total`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `complement_c3b` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.complement_c3b` | complement C3b. |
| `closed_complement_c3bb_complex` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.closed_complement_c3bb_complex` | closed complement C3bB complex. |
| `open_complement_c3bb_complex` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.open_complement_c3bb_complex` | open complement C3bB complex. |
| `state` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_bakshi2020_properdin_model_of_alternative_pathwa_biomd0000001018_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
