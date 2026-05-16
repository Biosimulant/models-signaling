# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sneyd2002_IP3_Receptor."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sneyd2002Ip3ReceptorModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000057'
    _TITLE = 'Sneyd2002_IP3_Receptor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'receptor': ('R',
                  'native SBML value',
                  'Receptor. Maps to SBML symbol `R` and is emitted in native SBML units.'),
     'open_state': ('O',
                    'native SBML value',
                    'open State. Maps to SBML symbol `O` and is emitted in native SBML units.'),
     'inactivated_state_1': ('I1',
                             'native SBML value',
                             'Inactivated State 1. Maps to SBML symbol `I1` and is emitted in native '
                             'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_receptor': ('R',
                          0.0,
                          'native SBML value',
                          'Initial level of Receptor. Maps to SBML symbol `R`; exposed as a traceable '
                          'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'R': 'Receptor',
     'O': 'open State',
     'I1': 'Inactivated State 1',
     'S': 'Shut State',
     'A': 'Activated State',
     'I2': 'Inactivated State 2'}
    _STATE_OUTPUT_ALIASES = {'R': 'receptor',
     'O': 'open_state',
     'I1': 'inactivated_state_1',
     'S': 'shut_state',
     'A': 'activated_state',
     'I2': 'inactivated_state_2'}

    def __init__(self, model_path: str = 'data/BIOMD0000000057.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sneyd2002Ip3ReceptorBiomd0000000057Model = Sneyd2002Ip3ReceptorModel
