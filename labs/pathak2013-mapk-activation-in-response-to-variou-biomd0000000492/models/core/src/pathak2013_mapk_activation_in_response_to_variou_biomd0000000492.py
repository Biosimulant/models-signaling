# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Pathak2013 - MAPK activation in response to various biotic stresses."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pathak2013MapkActivationInResponseToVariouBiomd0000000492Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000492'
    _TITLE = 'Pathak2013 - MAPK activation in response to various biotic stresses'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapkkk': ('s7',
                'substance',
                'MAPKKK. Maps to SBML symbol `s7` and is emitted in native SBML units.'),
     'mapkkk_2': ('s8',
                  'substance',
                  'MAPKKK. Maps to SBML symbol `s8` and is emitted in native SBML units.'),
     'mapkkk1': ('s9',
                 'substance',
                 'MAPKKK1. Maps to SBML symbol `s9` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_fungal_pathogen': ('s1',
                                 0.0,
                                 'native SBML value',
                                 'Initial level of Fungal Pathogen. Maps to SBML symbol `s1`; exposed '
                                 'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s1': 'Fungal Pathogen',
     's2': 'Bacterial Pathogen',
     's3': 'source-defined LYSM state',
     's4': 'source-defined PRRS state',
     's5': 'source-defined FLS2 state',
     's6': 'source-defined LRR state',
     's7': 'MAPKKK',
     's8': 'MAPKKK',
     's9': 'MAPKKK1',
     's10': 'MAPKKK18',
     's11': 'MAPKKK19',
     's12': 'MAPKKK20',
     's13': 'source-defined EDR1 state',
     's14': 'MAPKK',
     's15': 'MAPKK',
     's16': 'MAPKK2',
     's17': 'MAPKK4',
     's18': 'MAPKK5',
     's19': 'MAPKK9',
     's20': 'MAPK',
     's21': 'MAPK',
     's22': 'source-defined MAPK2 state',
     's23': 'source-defined MAPK3 state',
     's24': 'source-defined MAPK4 state',
     's25': 'source-defined MAPK6 state',
     's28': 'source-defined WRKY1 state',
     's29': 'source-defined WRKY1 state',
     's30': 'source-defined MYB2 state',
     's31': 'source-defined MYB2 state',
     's32': 'WRKY33',
     's33': 'WRKY33',
     's34': 'source-defined WRKY6 state',
     's35': 'source-defined WRKY6 state',
     's36': 'source-defined MYB4 state',
     's37': 'source-defined MYB4 state',
     's38': 'WRKY25',
     's39': 'WRKY25',
     's40': 'WRKY12',
     's41': 'WRKY12',
     's42': 'WRKY22',
     's43': 'WRKY22',
     's44': 'WRKY28',
     's45': 'WRKY28',
     's46': 'WRKY29',
     's47': 'WRKY29',
     's48': 'MYB44',
     's49': 'source-defined NAC state',
     's50': 'source-defined BZIP state',
     's51': 'source-defined AP2 state',
     's52': 'Response',
     's26': 'source-defined SIMK state',
     's27': 'source-defined SAMK state'}
    _STATE_OUTPUT_ALIASES = {'s1': 'fungal_pathogen',
     's2': 'bacterial_pathogen',
     's3': 'source_defined_lysm_state',
     's4': 'source_defined_prrs_state',
     's5': 'source_defined_fls2_state',
     's6': 'source_defined_lrr_state',
     's7': 'mapkkk',
     's8': 'mapkkk_2',
     's9': 'mapkkk1',
     's10': 'mapkkk18',
     's11': 'mapkkk19',
     's12': 'mapkkk20',
     's13': 'source_defined_edr1_state',
     's14': 'mapkk',
     's15': 'mapkk_2',
     's16': 'mapkk2',
     's17': 'mapkk4',
     's18': 'mapkk5',
     's19': 'mapkk9',
     's20': 'mapk',
     's21': 'mapk_2',
     's22': 'source_defined_mapk2_state',
     's23': 'source_defined_mapk3_state',
     's24': 'source_defined_mapk4_state',
     's25': 'source_defined_mapk6_state',
     's28': 'source_defined_wrky1_state',
     's29': 'source_defined_wrky1_state_2',
     's30': 'source_defined_myb2_state',
     's31': 'source_defined_myb2_state_2',
     's32': 'wrky33',
     's33': 'wrky33_2',
     's34': 'source_defined_wrky6_state',
     's35': 'source_defined_wrky6_state_2',
     's36': 'source_defined_myb4_state',
     's37': 'source_defined_myb4_state_2',
     's38': 'wrky25',
     's39': 'wrky25_2',
     's40': 'wrky12',
     's41': 'wrky12_2',
     's42': 'wrky22',
     's43': 'wrky22_2',
     's44': 'wrky28',
     's45': 'wrky28_2',
     's46': 'wrky29',
     's47': 'wrky29_2',
     's48': 'myb44',
     's49': 'source_defined_nac_state',
     's50': 'source_defined_bzip_state',
     's51': 'source_defined_ap2_state',
     's52': 'response',
     's26': 'source_defined_simk_state',
     's27': 'source_defined_samk_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000492.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Pathak2013MapkActivationInResponseToVariouBiomd0000000492Model = Pathak2013MapkActivationInResponseToVariouBiomd0000000492Model
