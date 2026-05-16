# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hofmeyer1986_SeqFb_Proc_AA_Synthesis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hofmeyer1986SeqfbProcAaSynthesisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000284'
    _TITLE = 'Hofmeyer1986_SeqFb_Proc_AA_Synthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_a_state': ('A',
                                'native SBML value',
                                'source-defined A state. Maps to SBML symbol `A` and is emitted in '
                                'native SBML units.'),
     'source_defined_b_state': ('B',
                                'native SBML value',
                                'source-defined B state. Maps to SBML symbol `B` and is emitted in '
                                'native SBML units.'),
     'source_defined_c_state': ('C',
                                'native SBML value',
                                'source-defined C state. Maps to SBML symbol `C` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_response_node_x': ('X',
                                 10.0,
                                 'native SBML value',
                                 'Initial level of response node X. Maps to SBML symbol `X`; exposed '
                                 'as a traceable initial-condition perturbation.'),
     'initial_source_defined_y_state': ('Y',
                                        2.0,
                                        'native SBML value',
                                        'Initial level of source-defined Y state. Maps to SBML symbol '
                                        '`Y`; exposed as a traceable initial-condition perturbation.'),
     'initial_source_defined_z_state': ('Z',
                                        1.0,
                                        'native SBML value',
                                        'Initial level of source-defined Z state. Maps to SBML symbol '
                                        '`Z`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'A': 'source-defined A state',
     'B': 'source-defined B state',
     'C': 'source-defined C state',
     'D': 'source-defined D state',
     'E': 'source-defined E state',
     'F': 'source-defined F state',
     'X': 'response node X',
     'Y': 'source-defined Y state',
     'Z': 'source-defined Z state'}
    _STATE_OUTPUT_ALIASES = {'A': 'source_defined_a_state',
     'B': 'source_defined_b_state',
     'C': 'source_defined_c_state',
     'D': 'source_defined_d_state',
     'E': 'source_defined_e_state',
     'F': 'source_defined_f_state',
     'X': 'response_node_x',
     'Y': 'source_defined_y_state',
     'Z': 'source_defined_z_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000284.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hofmeyer1986SeqfbProcAaSynthesisBiomd0000000284Model = Hofmeyer1986SeqfbProcAaSynthesisModel
