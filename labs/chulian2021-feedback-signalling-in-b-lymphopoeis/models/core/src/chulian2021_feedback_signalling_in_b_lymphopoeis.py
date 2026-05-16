# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chulian2021 - feedback signalling in B lymphopoeisis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chulian2021FeedbackSignallingInBLymphopoeisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001056'
    _TITLE = 'Chulian2021 - feedback signalling in B lymphopoeisis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_c1_state': ('C1',
                                 'native SBML value',
                                 'source-defined C1 state. Maps to SBML symbol `C1` and is emitted in '
                                 'native SBML units.'),
     'source_defined_c2_state': ('C2',
                                 'native SBML value',
                                 'source-defined C2 state. Maps to SBML symbol `C2` and is emitted in '
                                 'native SBML units.'),
     'complement_c3': ('C3',
                       'native SBML value',
                       'complement C3. Maps to SBML symbol `C3` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_c1_state': ('C1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined C1 state. Maps to SBML '
                                         'symbol `C1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C1': 'source-defined C1 state', 'C2': 'source-defined C2 state', 'C3': 'complement C3'}
    _STATE_OUTPUT_ALIASES = {'C1': 'source_defined_c1_state', 'C2': 'source_defined_c2_state', 'C3': 'complement_c3'}

    def __init__(self, model_path: str = 'data/BIOMD0000001056.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Chulian2021FeedbackSignallingInBLymphopoeisBiomd0000001056Model = Chulian2021FeedbackSignallingInBLymphopoeisModel
