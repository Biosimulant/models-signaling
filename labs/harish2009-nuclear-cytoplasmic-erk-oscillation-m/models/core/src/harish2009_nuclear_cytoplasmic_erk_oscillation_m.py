# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Harish2009 - nuclear–cytoplasmic ERK oscillation model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Harish2009NuclearCytoplasmicErkOscillationMModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2306170002'
    _TITLE = 'Harish2009 - nuclear–cytoplasmic ERK oscillation model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytosolic_phosphorylated_erk': ('ERK_c',
                                      'native SBML value',
                                      'cytosolic Phosphorylated ERK. Maps to SBML symbol `ERK_c` and '
                                      'is emitted in native SBML units.'),
     'pp_mapk_kinase_erk_c': ('PP_MKK_ERK_c',
                              'native SBML value',
                              'PP MAPK Kinase ERK C. Maps to SBML symbol `PP_MKK_ERK_c` and is emitted '
                              'in native SBML units.'),
     'p_erk_c': ('P_ERK_c',
                 'native SBML value',
                 'P ERK C. Maps to SBML symbol `P_ERK_c` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_e1_mos_kinase': ('E1_MKKK',
                               0.0,
                               'native SBML value',
                               'Initial level of E1 Mos kinase. Maps to SBML symbol `E1_MKKK`; exposed '
                               'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'E1_MKKK': 'E1 Mos kinase',
     'P_MKKK': 'source-defined MOS-P state',
     'E2_P_MKKK': 'E2 Mos kinase P',
     'MKK_c': 'Source Defined MAPK Kinase C State',
     'P_MKKK_MKK': 'P Mos kinase Mek1',
     'P_MKK_c': 'P MAPK Kinase C',
     'P1_P_MKK_c': 'P1 P MAPK Kinase C',
     'P_MKKK_P_MKK': 'P Mos kinase P Mek1',
     'PP_MKK_c': 'PP MAPK Kinase C',
     'P1_PP_MKK_c': 'P1 PP MAPK Kinase C',
     'P1_c': 'P1 C',
     'ERK_c': 'cytosolic Phosphorylated ERK',
     'PP_MKK_ERK_c': 'PP MAPK Kinase ERK C',
     'P_ERK_c': 'P ERK C',
     'P2_P_ERK_c': 'P2 P ERK C',
     'PP_MKK_P_ERK_c': 'PP MAPK Kinase P ERK C',
     'PP_ERK_c': 'PP ERK C',
     'P2_PP_ERK_c': 'P2 PP ERK C',
     'P2_c': 'P2 C',
     'P_MKK_n': 'P MAPK Kinase N',
     'P1_P_MKK_n': 'P1 P MAPK Kinase N',
     'PP_MKK_n': 'PP MAPK Kinase N',
     'P1_PP_MKK_n': 'P1 PP MAPK Kinase N',
     'PP_MKK_ERK_n': 'PP MAPK Kinase ERK N',
     'P_ERK_n': 'P ERK N',
     'P2_P_ERK_n': 'P2 P ERK N',
     'PP_MKK_P_ERK_n': 'PP MAPK Kinase P ERK N',
     'PP_ERK_n': 'PP ERK N',
     'P2_PP_ERK_n': 'P2 PP ERK N',
     'MKK_ERK_c': 'MAPK Kinase ERK C',
     'MKK_ERK_n': 'MAPK Kinase ERK N',
     'E1': 'MAPKKK Activator RAS',
     'E2': 'MAPKKK Inactivator',
     'MKKK': 'Mos kinase',
     'MKK_n': 'Source Defined MAPK Kinase N State',
     'ERK_n': 'nuclear Phosphorylated ERK',
     'P2_n': 'P2 N',
     'P1_n': 'P1 N'}
    _STATE_OUTPUT_ALIASES = {'E1_MKKK': 'e1_mos_kinase',
     'P_MKKK': 'source_defined_mos_p_state',
     'E2_P_MKKK': 'e2_mos_kinase_p',
     'MKK_c': 'source_defined_mapk_kinase_c_state',
     'P_MKKK_MKK': 'p_mos_kinase_mek1',
     'P_MKK_c': 'p_mapk_kinase_c',
     'P1_P_MKK_c': 'p1_p_mapk_kinase_c',
     'P_MKKK_P_MKK': 'p_mos_kinase_p_mek1',
     'PP_MKK_c': 'pp_mapk_kinase_c',
     'P1_PP_MKK_c': 'p1_pp_mapk_kinase_c',
     'P1_c': 'p1_c',
     'ERK_c': 'cytosolic_phosphorylated_erk',
     'PP_MKK_ERK_c': 'pp_mapk_kinase_erk_c',
     'P_ERK_c': 'p_erk_c',
     'P2_P_ERK_c': 'p2_p_erk_c',
     'PP_MKK_P_ERK_c': 'pp_mapk_kinase_p_erk_c',
     'PP_ERK_c': 'pp_erk_c',
     'P2_PP_ERK_c': 'p2_pp_erk_c',
     'P2_c': 'p2_c',
     'P_MKK_n': 'p_mapk_kinase_n',
     'P1_P_MKK_n': 'p1_p_mapk_kinase_n',
     'PP_MKK_n': 'pp_mapk_kinase_n',
     'P1_PP_MKK_n': 'p1_pp_mapk_kinase_n',
     'PP_MKK_ERK_n': 'pp_mapk_kinase_erk_n',
     'P_ERK_n': 'p_erk_n',
     'P2_P_ERK_n': 'p2_p_erk_n',
     'PP_MKK_P_ERK_n': 'pp_mapk_kinase_p_erk_n',
     'PP_ERK_n': 'pp_erk_n',
     'P2_PP_ERK_n': 'p2_pp_erk_n',
     'MKK_ERK_c': 'mapk_kinase_erk_c',
     'MKK_ERK_n': 'mapk_kinase_erk_n',
     'E1': 'mapkkk_activator_ras',
     'E2': 'mapkkk_inactivator',
     'MKKK': 'mos_kinase',
     'MKK_n': 'source_defined_mapk_kinase_n_state',
     'ERK_n': 'nuclear_phosphorylated_erk',
     'P2_n': 'p2_n',
     'P1_n': 'p1_n'}

    def __init__(self, model_path: str = 'data/MODEL2306170002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Harish2009NuclearCytoplasmicErkOscillationMModel2306170002Model = Harish2009NuclearCytoplasmicErkOscillationMModel
