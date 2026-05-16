# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Palini2011_Minimal_2_Feedback_Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Palini2011Minimal2FeedbackModelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000325'
    _TITLE = 'Palini2011_Minimal_2_Feedback_Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_l_state': ('L',
                                'native SBML value',
                                'Source Defined L State. Maps to SBML symbol `L` and is emitted in '
                                'native SBML units.'),
     'source_defined_r_state': ('R',
                                'native SBML value',
                                'Source Defined R State. Maps to SBML symbol `R` and is emitted in '
                                'native SBML units.'),
     'source_defined_c_state': ('C',
                                'native SBML value',
                                'Source Defined C State. Maps to SBML symbol `C` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_l_state': ('L',
                                        0.1,
                                        'native SBML value',
                                        'Initial level of source-defined L state. Maps to SBML symbol '
                                        '`L`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'L': 'Source Defined L State',
     'R': 'Source Defined R State',
     'C': 'Source Defined C State',
     'I': 'Source Defined I State',
     'X': 'Response Node X',
     'A': 'Source Defined A State'}
    _STATE_OUTPUT_ALIASES = {'L': 'source_defined_l_state',
     'R': 'source_defined_r_state',
     'C': 'source_defined_c_state',
     'I': 'source_defined_i_state',
     'X': 'response_node_x',
     'A': 'source_defined_a_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000325.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Palini2011Minimal2FeedbackModelBiomd0000000325Model = Palini2011Minimal2FeedbackModelModel
