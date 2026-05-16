# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for GonzalezMiranda2013 - The effect of circadian oscillations on biochemical cell signaling by NF-κB."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gonzalezmiranda2013TheEffectOfCircadianOsciModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000893'
    _TITLE = 'GonzalezMiranda2013 - The effect of circadian oscillations on biochemical cell signaling by NF-κB'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'response_node_x': ('x',
                         'native SBML value',
                         'response node X. Maps to SBML symbol `x` and is emitted in native SBML '
                         'units.'),
     'source_defined_y_state': ('y',
                                'native SBML value',
                                'source-defined Y state. Maps to SBML symbol `y` and is emitted in '
                                'native SBML units.'),
     'source_defined_z_state': ('z',
                                'native SBML value',
                                'source-defined Z state. Maps to SBML symbol `z` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_response_node_x': ('x',
                                 0.0,
                                 'native SBML value',
                                 'Initial level of response node X. Maps to SBML symbol `x`; exposed '
                                 'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x': 'response node X', 'y': 'source-defined Y state', 'z': 'source-defined Z state'}
    _STATE_OUTPUT_ALIASES = {'x': 'response_node_x', 'y': 'source_defined_y_state', 'z': 'source_defined_z_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000893.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gonzalezmiranda2013TheEffectOfCircadianOsciBiomd0000000893Model = Gonzalezmiranda2013TheEffectOfCircadianOsciModel
