# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kummer2000 - Oscillations in Calcium Signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kummer2000OscillationsInCalciumSignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000329'
    _TITLE = 'Kummer2000 - Oscillations in Calcium Signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'active_plc': ('b',
                    'native SBML value',
                    'active PLC. Maps to SBML symbol `b` and is emitted in native SBML units.'),
     'calcium': ('c',
                 'native SBML value',
                 'Calcium. Maps to SBML symbol `c` and is emitted in native SBML units.'),
     'g_alpha': ('a',
                 'native SBML value',
                 'G Alpha. Maps to SBML symbol `a` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium': ('c',
                         0.01,
                         'native SBML value',
                         'Initial level of Calcium. Maps to SBML symbol `c`; exposed as a traceable '
                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'a': 'G Alpha', 'b': 'active PLC', 'c': 'Calcium'}
    _STATE_OUTPUT_ALIASES = {'a': 'g_alpha', 'b': 'active_plc', 'c': 'calcium'}

    def __init__(self, model_path: str = 'data/BIOMD0000000329.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kummer2000OscillationsInCalciumSignallingBiomd0000000329Model = Kummer2000OscillationsInCalciumSignallingModel
