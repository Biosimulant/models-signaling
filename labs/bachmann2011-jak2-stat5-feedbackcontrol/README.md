# Bachmann2011_JAK2-STAT5_FeedbackControl

This Biosimulant lab wraps `Bachmann2011_JAK2-STAT5_FeedbackControl` as a runnable signaling model with a companion visualization module.
Clean Biosimulant lab for JAK/STAT cytokine signaling. It can be used to explore second-messenger and pathway-signaling dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does Bachmann2011 JAK2-STAT5 FeedbackControl transmit cytokine receptor activity into STAT pathway states? It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on EPO receptor-JAK2 complex, phosphorylated EPO receptor-JAK2 complex, site 1 phosphorylated EPO receptor-JAK2 complex, site 2 phosphorylated EPO receptor-JAK2 complex, dual-site phosphorylated EPO receptor-JAK2 complex, and CIS-bound EPO receptor-JAK2 complex, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **EPORJAK2** moved from 1.590 to 1.481 across 1.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Bachmann2011_JAK2-STAT5_FeedbackControl - run interpretation](assets/01-visualisation-table.png)

*Summary table for Bachmann2011_JAK2-STAT5_FeedbackControl, reporting the scientific question, observed answer, dominant module, and caveat.*

![Bachmann2011_JAK2-STAT5_FeedbackControl - timeseries visualization](assets/02-visualisation-timeseries.png)

*Trajectories of EPORJAK2, STAT5, PSTAT5, EPORPJAK2, P2EpoRpJAK2, and P1EpoRpJAK2 across the 1.0 simulation. In this run **PSTAT5** climbed from 0 to 0.0910 and **EPORJAK2** fell from 1.590 to 1.481 — the largest movements among the focused observables.*

![Bachmann2011_JAK2-STAT5_FeedbackControl - excursions bar](assets/03-visualisation-bar.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **STAT5** = 31.810, **SHP1** = 10.690, **EPORJAK2** = 1.481, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000347`
- License: `CC0`
- Visual scope: JAK/STAT receptor-to-transcription signaling
- Caveat: Values are native SBML quantities; equations, parameters, units, and initial values remain in the bundled source file.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial EPO receptor-JAK2 complex | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.initial_epo_receptor_jak2_complex` |  | Initial level of EPO receptor-JAK2 complex. Maps to SBML symbol `EpoRJAK2`; exposed as a traceable initial-condition perturbation. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `stat5` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.stat5` | STAT5. |
| `phosphorylated_stat5` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.phosphorylated_stat5` | phosphorylated STAT5. |
| `nuclear_phosphorylated_stat5` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.nuclear_phosphorylated_stat5` | nuclear phosphorylated STAT5. |
| `state` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `signaling_sbml_bachmann2011_jak2_stat5_feedbackcontrol_biomd0000000347_model.species_labels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve .
```
