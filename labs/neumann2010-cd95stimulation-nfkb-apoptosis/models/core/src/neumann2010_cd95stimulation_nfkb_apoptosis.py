# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Neumann2010_CD95Stimulation_NFkB_Apoptosis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Neumann2010Cd95stimulationNfkbApoptosisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000243'
    _TITLE = 'Neumann2010_CD95Stimulation_NFkB_Apoptosis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nf_k_b_ik_b': ('NF_kB_IkB',
                     'native SBML value',
                     'NF K B Ik B. Maps to SBML symbol `NF_kB_IkB` and is emitted in native SBML '
                     'units.'),
     'nf_k_b_ik_b_p': ('NF_kB_IkB_P',
                       'native SBML value',
                       'NF K B Ik B P. Maps to SBML symbol `NF_kB_IkB_P` and is emitted in native SBML '
                       'units.'),
     'nfkb': ('NF_kB_star',
              'native SBML value',
              'NF-kB. Maps to SBML symbol `NF_kB_star` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_l_state': ('L',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined L state. Maps to SBML symbol '
                                        '`L`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'L': 'source-defined L state',
     'L_RF': 'source-defined L_RF state',
     'L_RF_C8': 'source-defined L_RF_C8 state',
     'L_RF_FL': 'L RF FL',
     'L_RF_FS': 'L RF FS',
     'p43_p41': 'P43 P41',
     'C3': 'complement C3',
     'C8': 'source-defined C8 state',
     'C8_star': 'source-defined C8* state',
     'C3_star': 'complement C3',
     'p43_FLIP': 'P43 FLIP',
     'NF_kB_IkB': 'NF K B Ik B',
     'NF_kB_IkB_P': 'NF K B Ik B P',
     'p43_FLIP_IKK_star': 'P43 FLIP IKK',
     'NF_kB_star': 'NF-kB',
     'RF': 'source-defined RF state',
     'FL': 'source-defined FL state',
     'FS': 'source-defined FS state',
     'IKK': 'source-defined IKK state',
     'L_RF_C8_FS': 'L RF C8 FS',
     'L_RF_FL_FL': 'L RF FL FL',
     'L_RF_FL_FS': 'L RF FL FS',
     'L_RF_FS_FS': 'L RF FS FS'}
    _STATE_OUTPUT_ALIASES = {'L': 'source_defined_l_state',
     'L_RF': 'source_defined_l_rf_state',
     'L_RF_C8': 'source_defined_l_rf_c8_state',
     'L_RF_FL': 'l_rf_fl',
     'L_RF_FS': 'l_rf_fs',
     'p43_p41': 'p43_p41',
     'C3': 'complement_c3',
     'C8': 'source_defined_c8_state',
     'C8_star': 'source_defined_c8_state_2',
     'C3_star': 'complement_c3_2',
     'p43_FLIP': 'p43_flip',
     'NF_kB_IkB': 'nf_k_b_ik_b',
     'NF_kB_IkB_P': 'nf_k_b_ik_b_p',
     'p43_FLIP_IKK_star': 'p43_flip_ikk',
     'NF_kB_star': 'nfkb',
     'RF': 'source_defined_rf_state',
     'FL': 'source_defined_fl_state',
     'FS': 'source_defined_fs_state',
     'IKK': 'source_defined_ikk_state',
     'L_RF_C8_FS': 'l_rf_c8_fs',
     'L_RF_FL_FL': 'l_rf_fl_fl',
     'L_RF_FL_FS': 'l_rf_fl_fs',
     'L_RF_FS_FS': 'l_rf_fs_fs'}

    def __init__(self, model_path: str = 'data/BIOMD0000000243.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Neumann2010Cd95stimulationNfkbApoptosisBiomd0000000243Model = Neumann2010Cd95stimulationNfkbApoptosisModel
