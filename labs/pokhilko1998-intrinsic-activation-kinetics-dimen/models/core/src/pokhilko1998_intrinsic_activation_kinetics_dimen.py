# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Pokhilko1998 - Intrinsic Activation Kinetics (Dimensional Model)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pokhilko1998IntrinsicActivationKineticsDimenModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1808210003'
    _TITLE = 'Pokhilko1998 - Intrinsic Activation Kinetics (Dimensional Model)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'response_node_x': ('X',
                         'native SBML value',
                         'response node X. Maps to SBML symbol `X` and is emitted in native SBML '
                         'units.'),
     'source_defined_y_state': ('Y',
                                'native SBML value',
                                'source-defined Y state. Maps to SBML symbol `Y` and is emitted in '
                                'native SBML units.'),
     'source_defined_z_state': ('Z',
                                'native SBML value',
                                'source-defined Z state. Maps to SBML symbol `Z` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_response_node_x': ('X',
                                 0.5,
                                 'native SBML value',
                                 'Initial level of response node X. Maps to SBML symbol `X`; exposed '
                                 'as a traceable initial-condition perturbation.'),
     'initial_source_defined_y_state': ('Y',
                                        0.5,
                                        'native SBML value',
                                        'Initial level of source-defined Y state. Maps to SBML symbol '
                                        '`Y`; exposed as a traceable initial-condition perturbation.'),
     'initial_source_defined_z_state': ('Z',
                                        2.0,
                                        'native SBML value',
                                        'Initial level of source-defined Z state. Maps to SBML symbol '
                                        '`Z`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'X': 'response node X',
     'Y': 'source-defined Y state',
     'Z': 'source-defined Z state',
     'S': 'source-defined S state'}
    _STATE_OUTPUT_ALIASES = {'X': 'response_node_x',
     'Y': 'source_defined_y_state',
     'Z': 'source_defined_z_state',
     'S': 'source_defined_s_state'}

    def __init__(self, model_path: str = 'data/MODEL1808210003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Pokhilko1998IntrinsicActivationKineticsDimenModel1808210003Model = Pokhilko1998IntrinsicActivationKineticsDimenModel
