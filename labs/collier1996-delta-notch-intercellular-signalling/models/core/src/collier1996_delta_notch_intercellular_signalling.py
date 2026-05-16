# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Collier1996 - Delta Notch intercellular signalling and lateral inhibition."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Collier1996DeltaNotchIntercellularSignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001047'
    _TITLE = 'Collier1996 - Delta Notch intercellular signalling and lateral inhibition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'delta1': ('delta1',
                'native SBML value',
                'Delta1. Maps to SBML symbol `delta1` and is emitted in native SBML units.'),
     'delta2': ('delta2',
                'native SBML value',
                'Delta2. Maps to SBML symbol `delta2` and is emitted in native SBML units.'),
     'notch1': ('notch1',
                'native SBML value',
                'Notch1. Maps to SBML symbol `notch1` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_notch1': ('notch1',
                        0.999999999999987,
                        'native SBML value',
                        'Initial level of Notch1. Maps to SBML symbol `notch1`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_notch2': ('notch2',
                        0.99,
                        'native SBML value',
                        'Initial level of Notch2. Maps to SBML symbol `notch2`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'delta1': 'Delta1', 'delta2': 'Delta2', 'notch1': 'Notch1', 'notch2': 'Notch2'}
    _STATE_OUTPUT_ALIASES = {'delta1': 'delta1', 'delta2': 'delta2', 'notch1': 'notch1', 'notch2': 'notch2'}

    def __init__(self, model_path: str = 'data/BIOMD0000001047.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Collier1996DeltaNotchIntercellularSignallingBiomd0000001047Model = Collier1996DeltaNotchIntercellularSignallingModel
