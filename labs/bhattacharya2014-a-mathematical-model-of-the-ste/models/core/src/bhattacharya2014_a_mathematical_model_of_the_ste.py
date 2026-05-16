# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bhattacharya2014 - A mathematical model of the sterol regulatory element binding protein 2 cholesterol biosynthesis pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhattacharya2014AMathematicalModelOfTheSteModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000890'
    _TITLE = 'Bhattacharya2014 - A mathematical model of the sterol regulatory element binding protein 2 cholesterol biosynthesis pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_m_state': ('m',
                                'native SBML value',
                                'source-defined M state. Maps to SBML symbol `m` and is emitted in '
                                'native SBML units.'),
     'source_defined_h_state': ('h',
                                'native SBML value',
                                'source-defined H state. Maps to SBML symbol `h` and is emitted in '
                                'native SBML units.'),
     'source_defined_c_state': ('c',
                                'native SBML value',
                                'source-defined C state. Maps to SBML symbol `c` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_m_state': ('m',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined M state. Maps to SBML symbol '
                                        '`m`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'m': 'source-defined M state', 'h': 'source-defined H state', 'c': 'source-defined C state'}
    _STATE_OUTPUT_ALIASES = {'m': 'source_defined_m_state', 'h': 'source_defined_h_state', 'c': 'source_defined_c_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000890.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bhattacharya2014AMathematicalModelOfTheSteBiomd0000000890Model = Bhattacharya2014AMathematicalModelOfTheSteModel
