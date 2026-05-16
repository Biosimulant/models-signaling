# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Almeida2019 - Transcription-based circadian mechanism controls the duration of molecular clock states in response to signaling inputs."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Almeida2019TranscriptionBasedCircadianMechanModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000839'
    _TITLE = 'Almeida2019 - Transcription-based circadian mechanism controls the duration of molecular clock states in response to signaling inputs'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_bmal1_state': ('BMAL1',
                                    'native SBML value',
                                    'source-defined BMAL1 state. Maps to SBML symbol `BMAL1` and is '
                                    'emitted in native SBML units.'),
     'source_defined_ror_state': ('ROR',
                                  'native SBML value',
                                  'source-defined ROR state. Maps to SBML symbol `ROR` and is emitted '
                                  'in native SBML units.'),
     'source_defined_rev_state': ('REV',
                                  'native SBML value',
                                  'source-defined REV state. Maps to SBML symbol `REV` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_bmal1_state': ('BMAL1',
                                            0.0,
                                            'native SBML value',
                                            'Initial level of source-defined BMAL1 state. Maps to SBML '
                                            'symbol `BMAL1`; exposed as a traceable initial-condition '
                                            'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'BMAL1': 'source-defined BMAL1 state',
     'ROR': 'source-defined ROR state',
     'REV': 'source-defined REV state',
     'DBP': 'source-defined DBP state',
     'E4BP4': 'E4BP4',
     'CRY': 'source-defined CRY state',
     'PER': 'source-defined PER state',
     'PERCRY': 'PERCRY'}
    _STATE_OUTPUT_ALIASES = {'BMAL1': 'source_defined_bmal1_state',
     'ROR': 'source_defined_ror_state',
     'REV': 'source_defined_rev_state',
     'DBP': 'source_defined_dbp_state',
     'E4BP4': 'e4bp4',
     'CRY': 'source_defined_cry_state',
     'PER': 'source_defined_per_state',
     'PERCRY': 'percry'}

    def __init__(self, model_path: str = 'data/BIOMD0000000839.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Almeida2019TranscriptionBasedCircadianMechanBiomd0000000839Model = Almeida2019TranscriptionBasedCircadianMechanModel
