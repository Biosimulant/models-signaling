# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wegner2012_TGFbetaSignalling_FeedbackLoops."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wegner2012TgfbetasignallingFeedbackloopsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000410'
    _TITLE = 'Wegner2012_TGFbetaSignalling_FeedbackLoops'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'rec_active': ('_96',
                    'native SBML value',
                    'Rec active. Maps to SBML symbol `_96` and is emitted in native SBML units.'),
     'smad2_c': ('_99',
                 'native SBML value',
                 'Smad2 C. Maps to SBML symbol `_99` and is emitted in native SBML units.'),
     'smad2_sara': ('_105',
                    'native SBML value',
                    'Smad2 SARA. Maps to SBML symbol `_105` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tgf_ri': ('_84',
                        0.0,
                        'native SBML value',
                        'Initial level of TGF RI. Maps to SBML symbol `_84`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_tgf_rii': ('_75',
                         0.0,
                         'native SBML value',
                         'Initial level of TGF RII. Maps to SBML symbol `_75`; exposed as a traceable '
                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_tgfbeta_level': ('parameter_1',
                               0.01,
                               'native SBML value',
                               'Tgfbeta source parameter. Maps to SBML symbol `parameter_1` and '
                               'preserves the bundled default.')}
    _SPECIES_LABELS = {'_75': 'TGF RII',
     '_79': 'Tgfbeta TGF RII',
     '_84': 'TGF RI',
     '_96': 'Rec active',
     '_99': 'Smad2 C',
     '_101': 'source-defined SARA state',
     '_105': 'Smad2 SARA',
     '_129': 'P Smad2 C',
     '_147': 'Smad4 C',
     '_153': 'P Smad2 Smad4 C',
     '_174': 'SMAD7 C',
     '_181': 'SMAD7 Smurf2 C',
     '_198': 'Rec SMAD7',
     'species_1': 'Smurf2 C',
     'species_2': 'Sno N C',
     'species_3': 'Smad3 C',
     'species_4': 'P Smad3 C',
     'species_5': 'Smad3 SARA',
     'species_6': 'P Smad3 Smad4 C',
     'species_7': 'source-defined SKI_C state',
     'species_8': 'Smad3 Ski C',
     'species_9': 'Smurf1 C',
     'species_10': 'SMAD7 Smurf1 C',
     'species_11': 'P Smad2 Smad4 Ski N',
     'species_12': 'Smad2 Ski C',
     'species_13': 'P Smad2 Sno N N',
     'species_14': 'P Smad3 Sno N N',
     'species_15': 'Arkadia C',
     '_5': 'Smad4 N',
     '_9': 'P Smad2 Smad4 N',
     '_11': 'Sno N N',
     '_13': 'P Smad2 Smad4 Sno N N',
     '_15': 'Smurf2 N',
     '_19': 'P Smad2 N',
     '_21': 'Smad2 N',
     '_25': 'SMAD7 N',
     '_27': 'SMAD7 Smurf2 N',
     'species_16': 'Smad4 Sno N N',
     'species_17': 'Smad3 N',
     'species_18': 'P Smad3 Smad4 N',
     'species_19': 'Smad4 Smad2 N',
     'species_20': 'P Smad3 N',
     'species_21': 'P Smad3 Smad4 Sno N N',
     'species_22': 'source-defined SKI_N state',
     'species_23': 'Smad4 Ski N',
     'species_24': 'Smurf1 N',
     'species_25': 'SMAD7 Smurf1 N',
     'species_26': 'P Smad3 Smad4 Ski N',
     'species_27': 'Smad4 Smad3 N',
     'species_28': 'free Promoters',
     'species_29': 'Inactive Promoters',
     'species_30': 'Gene Product',
     'species_31': 'Arkadia N'}
    _STATE_OUTPUT_ALIASES = {'_75': 'tgf_rii',
     '_79': 'tgfbeta_tgf_rii',
     '_84': 'tgf_ri',
     '_96': 'rec_active',
     '_99': 'smad2_c',
     '_101': 'source_defined_sara_state',
     '_105': 'smad2_sara',
     '_129': 'p_smad2_c',
     '_147': 'smad4_c',
     '_153': 'p_smad2_smad4_c',
     '_174': 'smad7_c',
     '_181': 'smad7_smurf2_c',
     '_198': 'rec_smad7',
     'species_1': 'smurf2_c',
     'species_2': 'sno_n_c',
     'species_3': 'smad3_c',
     'species_4': 'p_smad3_c',
     'species_5': 'smad3_sara',
     'species_6': 'p_smad3_smad4_c',
     'species_7': 'source_defined_ski_c_state',
     'species_8': 'smad3_ski_c',
     'species_9': 'smurf1_c',
     'species_10': 'smad7_smurf1_c',
     'species_11': 'p_smad2_smad4_ski_n',
     'species_12': 'smad2_ski_c',
     'species_13': 'p_smad2_sno_n_n',
     'species_14': 'p_smad3_sno_n_n',
     'species_15': 'arkadia_c',
     '_5': 'smad4_n',
     '_9': 'p_smad2_smad4_n',
     '_11': 'sno_n_n',
     '_13': 'p_smad2_smad4_sno_n_n',
     '_15': 'smurf2_n',
     '_19': 'p_smad2_n',
     '_21': 'smad2_n',
     '_25': 'smad7_n',
     '_27': 'smad7_smurf2_n',
     'species_16': 'smad4_sno_n_n',
     'species_17': 'smad3_n',
     'species_18': 'p_smad3_smad4_n',
     'species_19': 'smad4_smad2_n',
     'species_20': 'p_smad3_n',
     'species_21': 'p_smad3_smad4_sno_n_n',
     'species_22': 'source_defined_ski_n_state',
     'species_23': 'smad4_ski_n',
     'species_24': 'smurf1_n',
     'species_25': 'smad7_smurf1_n',
     'species_26': 'p_smad3_smad4_ski_n',
     'species_27': 'smad4_smad3_n',
     'species_28': 'free_promoters',
     'species_29': 'inactive_promoters',
     'species_30': 'gene_product',
     'species_31': 'arkadia_n'}

    def __init__(self, model_path: str = 'data/BIOMD0000000410.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Wegner2012TgfbetasignallingFeedbackloopsBiomd0000000410Model = Wegner2012TgfbetasignallingFeedbackloopsModel
