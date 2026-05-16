# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Goldbeter1996 - Cyclin Cdc2 kinase Oscillations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter1996CyclinCdc2KinaseOscillationsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000729'
    _TITLE = 'Goldbeter1996 - Cyclin Cdc2 kinase Oscillations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_c_state': ('C',
                                'native SBML value',
                                'source-defined C state. Maps to SBML symbol `C` and is emitted in '
                                'native SBML units.'),
     'source_defined_m_state': ('M',
                                'native SBML value',
                                'source-defined M state. Maps to SBML symbol `M` and is emitted in '
                                'native SBML units.'),
     'response_node_x': ('X',
                         'native SBML value',
                         'response node X. Maps to SBML symbol `X` and is emitted in native SBML '
                         'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_c_state': ('C',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined C state. Maps to SBML symbol '
                                        '`C`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C': 'source-defined C state', 'M': 'source-defined M state', 'X': 'response node X'}
    _STATE_OUTPUT_ALIASES = {'C': 'source_defined_c_state', 'M': 'source_defined_m_state', 'X': 'response_node_x'}

    def __init__(self, model_path: str = 'data/BIOMD0000000729.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Goldbeter1996CyclinCdc2KinaseOscillationsBiomd0000000729Model = Goldbeter1996CyclinCdc2KinaseOscillationsModel
