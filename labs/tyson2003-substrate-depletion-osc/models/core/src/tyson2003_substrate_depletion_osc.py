# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Tyson2003_Substrate_Depletion_Osc."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tyson2003SubstrateDepletionOscModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000307'
    _TITLE = 'Tyson2003_Substrate_Depletion_Osc'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_r_state': ('R',
                                'native SBML value',
                                'Source Defined R State. Maps to SBML symbol `R` and is emitted in '
                                'native SBML units.'),
     'response_node_x': ('X',
                         'native SBML value',
                         'Response Node X. Maps to SBML symbol `X` and is emitted in native SBML '
                         'units.'),
     'source_defined_s_state': ('S',
                                'native SBML value',
                                'Source Defined S State. Maps to SBML symbol `S` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_e_state': ('E',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined E state. Maps to SBML symbol '
                                        '`E`; exposed as a traceable initial-condition perturbation.'),
     'initial_source_defined_ep_state': ('Ep',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined EP state. Maps to SBML '
                                         'symbol `Ep`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_source_defined_s_state': ('S',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined S state. Maps to SBML symbol '
                                        '`S`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'R': 'Source Defined R State',
     'X': 'Response Node X',
     'S': 'Source Defined S State',
     'Ep': 'Source Defined EP State',
     'E': 'Source Defined E State'}
    _STATE_OUTPUT_ALIASES = {'R': 'source_defined_r_state',
     'X': 'response_node_x',
     'S': 'source_defined_s_state',
     'Ep': 'source_defined_ep_state',
     'E': 'source_defined_e_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000307.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Tyson2003SubstrateDepletionOscBiomd0000000307Model = Tyson2003SubstrateDepletionOscModel
