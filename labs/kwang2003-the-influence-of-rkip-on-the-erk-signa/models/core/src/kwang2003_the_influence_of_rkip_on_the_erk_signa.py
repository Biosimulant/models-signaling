# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kwang2003 - The influence of RKIP on the ERK signaling pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kwang2003TheInfluenceOfRkipOnTheErkSignaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000647'
    _TITLE = 'Kwang2003 - The influence of RKIP on the ERK signaling pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'raf1_rkip_erkpp': ('Raf1_RKIP_ERKPP',
                         'native SBML value',
                         'RAF1 RKIP ERKPP. Maps to SBML symbol `Raf1_RKIP_ERKPP` and is emitted in '
                         'native SBML units.'),
     'erk': ('ERK',
             'native SBML value',
             'ERK. Maps to SBML symbol `ERK` and is emitted in native SBML units.'),
     'mekpp_erk': ('MEKPP_ERK',
                   'native SBML value',
                   'MEKPP ERK. Maps to SBML symbol `MEKPP_ERK` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_raf1': ('Raf1',
                      0.0,
                      'native SBML value',
                      'Initial level of RAF1. Maps to SBML symbol `Raf1`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Raf1': 'RAF1',
     'RKIP': 'source-defined RKIP state',
     'Raf1_RKIP': 'RAF1 RKIP',
     'Raf1_RKIP_ERKPP': 'RAF1 RKIP ERKPP',
     'ERK': 'ERK',
     'RKIPP': 'RKIPP',
     'MEKPP': 'MEKPP',
     'MEKPP_ERK': 'MEKPP ERK',
     'ERKPP': 'ERKPP',
     'RP': 'source-defined RP state',
     'RKIPP_RP': 'RKIPP RP'}
    _STATE_OUTPUT_ALIASES = {'Raf1': 'raf1',
     'RKIP': 'source_defined_rkip_state',
     'Raf1_RKIP': 'raf1_rkip',
     'Raf1_RKIP_ERKPP': 'raf1_rkip_erkpp',
     'ERK': 'erk',
     'RKIPP': 'rkipp',
     'MEKPP': 'mekpp',
     'MEKPP_ERK': 'mekpp_erk',
     'ERKPP': 'erkpp',
     'RP': 'source_defined_rp_state',
     'RKIPP_RP': 'rkipp_rp'}

    def __init__(self, model_path: str = 'data/BIOMD0000000647.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kwang2003TheInfluenceOfRkipOnTheErkSignaBiomd0000000647Model = Kwang2003TheInfluenceOfRkipOnTheErkSignaModel
