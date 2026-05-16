# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Reiterer2013 - pseudophosphatase STYX role in ERK signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reiterer2013PseudophosphataseStyxRoleInErkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000557'
    _TITLE = 'Reiterer2013 - pseudophosphatase STYX role in ERK signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytosolic_phosphorylated_erk': ('ERKc',
                                      'native SBML value',
                                      'cytosolic phosphorylated ERK. Maps to SBML symbol `ERKc` and is '
                                      'emitted in native SBML units.'),
     'p_erkc': ('pERKc',
                'native SBML value',
                'P Erkc. Maps to SBML symbol `pERKc` and is emitted in native SBML units.'),
     'pp_erkc': ('ppERKc',
                 'native SBML value',
                 'Pp Erkc. Maps to SBML symbol `ppERKc` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_phosphorylated_erk': ('ERKc',
                                              0.0,
                                              'native SBML value',
                                              'Initial level of cytosolic phosphorylated ERK. Maps to '
                                              'SBML symbol `ERKc`; exposed as a traceable '
                                              'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'ERKc': 'cytosolic phosphorylated ERK',
     'pERKc': 'P Erkc',
     'ppERKc': 'Pp Erkc',
     'ERK_ppMEKc': 'ERK Pp Mekc',
     'pERK_ppMEKc': 'P ERK Pp Mekc',
     'DUSPc': 'Duspc',
     'pERK_DUSPc': 'P ERK Duspc',
     'ppERK_DUSPc': 'Pp ERK Duspc',
     'ERKn': 'nuclear phosphorylated ERK',
     'pERKn': 'P Erkn',
     'ppERKn': 'Pp Erkn',
     'pERK_DUSPn': 'P ERK Duspn',
     'ppERK_DUSPn': 'Pp ERK Duspn',
     'STYXn': 'Styxn',
     'ERK_STYXn': 'ERK Styxn',
     'pERK_STYXn': 'P ERK Styxn',
     'ppERK_STYXn': 'Pp ERK Styxn',
     'duspn': 'Duspn',
     'DUSPn': 'Duspn',
     'u_ppMEKc_tot': 'U Pp Mekc Tot',
     'ppMEKc_tot': 'Pp Mekc Tot',
     'ERKc_obs': 'Erkc Obs',
     'pERKc_obs': 'P Erkc Obs',
     'ppERKc_obs': 'Pp Erkc Obs',
     'ERK_ppMEKc_obs': 'ERK Pp Mekc Obs'}
    _STATE_OUTPUT_ALIASES = {'ERKc': 'cytosolic_phosphorylated_erk',
     'pERKc': 'p_erkc',
     'ppERKc': 'pp_erkc',
     'ERK_ppMEKc': 'erk_pp_mekc',
     'pERK_ppMEKc': 'p_erk_pp_mekc',
     'DUSPc': 'duspc',
     'pERK_DUSPc': 'p_erk_duspc',
     'ppERK_DUSPc': 'pp_erk_duspc',
     'ERKn': 'nuclear_phosphorylated_erk',
     'pERKn': 'p_erkn',
     'ppERKn': 'pp_erkn',
     'pERK_DUSPn': 'p_erk_duspn',
     'ppERK_DUSPn': 'pp_erk_duspn',
     'STYXn': 'styxn',
     'ERK_STYXn': 'erk_styxn',
     'pERK_STYXn': 'p_erk_styxn',
     'ppERK_STYXn': 'pp_erk_styxn',
     'duspn': 'duspn',
     'DUSPn': 'duspn_2',
     'u_ppMEKc_tot': 'u_pp_mekc_tot',
     'ppMEKc_tot': 'pp_mekc_tot',
     'ERKc_obs': 'erkc_obs',
     'pERKc_obs': 'p_erkc_obs',
     'ppERKc_obs': 'pp_erkc_obs',
     'ERK_ppMEKc_obs': 'erk_pp_mekc_obs'}

    def __init__(self, model_path: str = 'data/BIOMD0000000557.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Reiterer2013PseudophosphataseStyxRoleInErkBiomd0000000557Model = Reiterer2013PseudophosphataseStyxRoleInErkModel
