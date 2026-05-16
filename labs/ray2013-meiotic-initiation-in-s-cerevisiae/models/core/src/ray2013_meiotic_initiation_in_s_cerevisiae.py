# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ray2013 - Meiotic initiation in S. cerevisiae."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ray2013MeioticInitiationInSCerevisiaeModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000626'
    _TITLE = 'Ray2013 - Meiotic initiation in S. cerevisiae'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'rim11': ('Rim11',
               'native SBML value',
               'Rim11. Maps to SBML symbol `Rim11` and is emitted in native SBML units.'),
     'source_defined_pume6_state': ('pUme6',
                                    'native SBML value',
                                    'source-defined PUME6 state. Maps to SBML symbol `pUme6` and is '
                                    'emitted in native SBML units.'),
     'source_defined_psok2_state': ('pSok2',
                                    'native SBML value',
                                    'source-defined PSOK2 state. Maps to SBML symbol `pSok2` and is '
                                    'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_rim11': ('Rim11',
                       0.0,
                       'native SBML value',
                       'Initial level of Rim11. Maps to SBML symbol `Rim11`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Rim11': 'Rim11',
     'pUme6': 'source-defined PUME6 state',
     'pSok2': 'source-defined PSOK2 state',
     'Ime1': 'source-defined IME1 state',
     'pIme1': 'source-defined PIME1 state',
     'Ime2': 'source-defined IME2 state'}
    _STATE_OUTPUT_ALIASES = {'Rim11': 'rim11',
     'pUme6': 'source_defined_pume6_state',
     'pSok2': 'source_defined_psok2_state',
     'Ime1': 'source_defined_ime1_state',
     'pIme1': 'source_defined_pime1_state',
     'Ime2': 'source_defined_ime2_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000626.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Ray2013MeioticInitiationInSCerevisiaeBiomd0000000626Model = Ray2013MeioticInitiationInSCerevisiaeModel
