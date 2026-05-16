# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Huang1996 - Ultrasensitivity in MAPK cascade."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Huang1996UltrasensitivityInMapkCascadeModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000009'
    _TITLE = 'Huang1996 - Ultrasensitivity in MAPK cascade'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapkkk_activator_ras': ('E1',
                              'native SBML value',
                              'MAPKKK Activator RAS. Maps to SBML symbol `E1` and is emitted in native '
                              'SBML units.'),
     'mapkkk_inactivator': ('E2',
                            'native SBML value',
                            'MAPKKK Inactivator. Maps to SBML symbol `E2` and is emitted in native '
                            'SBML units.'),
     'source_defined_erk2_state': ('K',
                                   'native SBML value',
                                   'source-defined ERK2 state. Maps to SBML symbol `K` and is emitted '
                                   'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_mapkkk_activator_ras': ('E1',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of MAPKKK Activator RAS. Maps to SBML symbol '
                                      '`E1`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'E1': 'MAPKKK Activator RAS',
     'E2': 'MAPKKK Inactivator',
     'KKK': 'Mos kinase',
     'P_KKK': 'source-defined MOS-P state',
     'KK': 'source-defined MEK1 state',
     'P_KK': 'Mek1 P',
     'PP_KK': 'Mek1 PP',
     'K': 'source-defined ERK2 state',
     'P_K': 'Erk2 P',
     'PP_K': 'Erk2 PP',
     'KPase': 'MAPK Pase',
     'KKPase': 'MAPKK Pase',
     'E1_KKK': 'E1 Mos kinase',
     'E2_P_KKK': 'E2 Mos kinase P',
     'P_KKK_KK': 'P Mos kinase Mek1',
     'P_KKK_P_KK': 'P Mos kinase P Mek1',
     'PP_KK_K': 'PP Mek1 Erk2',
     'PP_KK_P_K': 'PP Mek1 P Erk2',
     'KKPase_PP_KK': 'MAPKK Pase PP Mek1',
     'KKPase_P_KK': 'MAPKK Pase P Mek1',
     'KPase_PP_K': 'MAPK Pase PP Erk2',
     'KPase_P_K': 'MAPK Pase P Erk2',
     'K_PP_norm': 'K PP Norm',
     'KK_PP_norm': 'KK PP Norm',
     'KKK_P_norm': 'KKK P Norm',
     'rel_K_PP_max': 'Relative Maximal K PP'}
    _STATE_OUTPUT_ALIASES = {'E1': 'mapkkk_activator_ras',
     'E2': 'mapkkk_inactivator',
     'KKK': 'mos_kinase',
     'P_KKK': 'source_defined_mos_p_state',
     'KK': 'source_defined_mek1_state',
     'P_KK': 'mek1_p',
     'PP_KK': 'mek1_pp',
     'K': 'source_defined_erk2_state',
     'P_K': 'erk2_p',
     'PP_K': 'erk2_pp',
     'KPase': 'mapk_pase',
     'KKPase': 'mapkk_pase',
     'E1_KKK': 'e1_mos_kinase',
     'E2_P_KKK': 'e2_mos_kinase_p',
     'P_KKK_KK': 'p_mos_kinase_mek1',
     'P_KKK_P_KK': 'p_mos_kinase_p_mek1',
     'PP_KK_K': 'pp_mek1_erk2',
     'PP_KK_P_K': 'pp_mek1_p_erk2',
     'KKPase_PP_KK': 'mapkk_pase_pp_mek1',
     'KKPase_P_KK': 'mapkk_pase_p_mek1',
     'KPase_PP_K': 'mapk_pase_pp_erk2',
     'KPase_P_K': 'mapk_pase_p_erk2',
     'K_PP_norm': 'k_pp_norm',
     'KK_PP_norm': 'kk_pp_norm',
     'KKK_P_norm': 'kkk_p_norm',
     'rel_K_PP_max': 'relative_maximal_k_pp'}

    def __init__(self, model_path: str = 'data/BIOMD0000000009.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Huang1996UltrasensitivityInMapkCascadeBiomd0000000009Model = Huang1996UltrasensitivityInMapkCascadeModel
