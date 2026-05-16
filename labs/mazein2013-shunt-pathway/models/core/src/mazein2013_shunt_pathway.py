# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mazein2013 - Shunt pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mazein2013ShuntPathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1409170003'
    _TITLE = 'Mazein2013 - Shunt pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_4_alpha_carboxyzymosterol': ('s60',
                                          'native SBML value',
                                          '4 Alpha Carboxyzymosterol. Maps to SBML symbol `s60` and is '
                                          'emitted in native SBML units.'),
     'source_4_alpha_carboxy_4_beta_response_parameter_methylzymosterol': ('s55',
                                                                           'native SBML value',
                                                                           '4 Alpha Carboxy 4 beta '
                                                                           'response parameter '
                                                                           'Methylzymosterol. Maps to '
                                                                           'SBML symbol `s55` and is '
                                                                           'emitted in native SBML '
                                                                           'units.'),
     'source_4_alpha_carboxy_4_beta_response_parameter_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol': ('s71',
                                                                                                                   'native '
                                                                                                                   'SBML '
                                                                                                                   'value',
                                                                                                                   '4 '
                                                                                                                   'Alpha '
                                                                                                                   'Carboxy '
                                                                                                                   '4 '
                                                                                                                   'beta '
                                                                                                                   'response '
                                                                                                                   'parameter '
                                                                                                                   'Methyl '
                                                                                                                   '5 '
                                                                                                                   'Alpha '
                                                                                                                   'Cholest '
                                                                                                                   '8 '
                                                                                                                   'En '
                                                                                                                   '3 '
                                                                                                                   'beta '
                                                                                                                   'response '
                                                                                                                   'parameter '
                                                                                                                   'Ol. '
                                                                                                                   'Maps '
                                                                                                                   'to '
                                                                                                                   'SBML '
                                                                                                                   'symbol '
                                                                                                                   '`s71` '
                                                                                                                   'and '
                                                                                                                   'is '
                                                                                                                   'emitted '
                                                                                                                   'in '
                                                                                                                   'native '
                                                                                                                   'SBML '
                                                                                                                   'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tm7sf2': ('s54',
                        0.0,
                        'native SBML value',
                        'Initial level of TM7SF2. Maps to SBML symbol `s54`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s54': 'TM7SF2',
     's52': 'CYP51A1',
     's44': 'source-defined LSS state',
     's48': 'source-defined SQLE state',
     's24': 'source-defined EBP state',
     's28': 'SC5D',
     's30': 'source-defined DHCR7 state',
     's18': 'Desmosterol',
     's15': '7 Dehydrodesmosterol',
     's14': '5 Alpha Cholesta 7 24 Dien 3 beta response parameter Ol',
     's13': 'Zymosterol',
     's12': 'Zymosterone',
     's60': '4 Alpha Carboxyzymosterol',
     's81': '4 Alpha Formyl 5 Alpha Cholesta 8 24 Dien 3 beta response parameter Ol',
     's82': '4 Alpha Hydroxymethyl 5 Alpha Cholesta 8 24 Dien 3 beta response parameter Ol',
     's59': '4 Alpha Methylzymosterol',
     's56': '3 Keto 4 Alpha Methylzymosterol',
     's55': '4 Alpha Carboxy 4 beta response parameter Methylzymosterol',
     's42': 'Lanosterol',
     's41': 'Squalene 2 3 Epoxide',
     's27': 'Squalene',
     's90': '4 Alpha Formyl 4 beta response parameter Methyl 5 Alpha Cholesta 8 24 Dien 3 beta '
            'response parameter Ol',
     's91': '4 Alpha Hydroxymethyl 4 beta response parameter Methyl 5 Alpha Cholesta 8 24 Dien 3 beta '
            'response parameter Ol',
     's53': '14 Dimethyllanosterol',
     's43': '4 4 Dimethyl 5 Alpha Cholesta 8 14 24 Trien 3 beta response parameter Ol',
     's92': '32 Hydroxylanosterol',
     's93': '32 Oxolanosterol',
     's49': '24 25 Dihydrolanosterole',
     's94': '4 4 Dimethyl 14 Alpha Formyl 5 Alpha Cholest 8 En 3 beta response parameter Ol',
     's95': '4 4 Dimethyl 14 Alpha Hydroxymethyl 5 Alpha Cholest 8 En 3 beta response parameter Ol',
     's51': '4 4 Dimethyl 5 Alpha Cholest 8 En 3 beta response parameter Ol',
     's33': '4 4 Dimethyl 5 Alpha Cholest 8 En 2 beta response parameter Ol',
     's71': '4 Alpha Carboxy 4 beta response parameter Methyl 5 Alpha Cholest 8 En 3 beta response '
            'parameter Ol',
     's96': '4 Alpha Formyl 4 beta response parameter Methyl 5 Alpha Cholest 8 En 3 beta response '
            'parameter Ol',
     's97': '4 Alpha Hydroxymethyl 4 beta response parameter Methyl 5 Alpha Cholest 8 En 3 beta '
            'response parameter Ol',
     's70': '4 Alpha Methyl 5 Alpha Cholest 8 En 3 beta response parameter One',
     's98': '4 Alpha Methyl 5 Alpha Cholest 8 En 3 beta response parameter Ol',
     's99': '4 Alpha Carboxymethyl 5 Alpha Cholesta 8 En 3 beta response parameter Ol',
     's100': '4 Alpha Formyl 5 Alpha Cholesta 8 En 3 beta response parameter Ol',
     's86': '4 Alpha Carboxy 5 Alpha Cholesta 8 En 3 beta response parameter Ol',
     's68': '5 Alpha Cholest 8 En 3 One',
     's66': '5 Alpha Cholest 8 En 3 beta response parameter Ol',
     's65': 'Lathosterol',
     's64': '7 Dehydroxycholesterol',
     's103': 'CYP27A1',
     's104': 'CYP3A4',
     's105': 'CH25H',
     's106': 'CYP7A1',
     's107': 'CYP46A1',
     's32': 'Cholesterol',
     's108': '24 Hydroxycholesterol',
     's109': '7 Alpha Hydroxycholesterol',
     's110': '4 beta response parameter Hydroxycholesterol',
     's111': '25 Xydroxycholesterol',
     's112': '25 Hydroxycholesterol',
     's113': '27 Hydroxycholesterol',
     's114': 'Cholesterol',
     's37': '24 S 25 Epoxycholesterol',
     's62': '24 S 25 Epoxylathosterol',
     's61': '24 S 25 Epoxy 7 Dehydrocholesterol',
     's35': '24 S 25 Epoxyzymosterol',
     's46': '24 S 25 Epoxylanosterol',
     's45': '2 3 22 23 Dioxidosqualene',
     's47': '4 4 Dimethyl 3 beta response parameter Hydroxy 5 Alpha Cholesta 8 14 Dien 24 S 25 Epoxide',
     's34': '4 4 Dimethyl 3 beta response parameter Hydroxy 5 Alpha Cholest 8 En 24 S 25 Epoxide',
     's115': 'NSDHL',
     's116': 'source-defined MSMO1 state',
     's117': 'DHCR24',
     's118': 'HSD17B7'}
    _STATE_OUTPUT_ALIASES = {'s54': 'tm7sf2',
     's52': 'cyp51a1',
     's44': 'source_defined_lss_state',
     's48': 'source_defined_sqle_state',
     's24': 'source_defined_ebp_state',
     's28': 'sc5d',
     's30': 'source_defined_dhcr7_state',
     's18': 'desmosterol',
     's15': 'source_7_dehydrodesmosterol',
     's14': 'source_5_alpha_cholesta_7_24_dien_3_beta_response_parameter_ol',
     's13': 'zymosterol',
     's12': 'zymosterone',
     's60': 'source_4_alpha_carboxyzymosterol',
     's81': 'source_4_alpha_formyl_5_alpha_cholesta_8_24_dien_3_beta_response_parameter_ol',
     's82': 'source_4_alpha_hydroxymethyl_5_alpha_cholesta_8_24_dien_3_beta_response_parameter_ol',
     's59': 'source_4_alpha_methylzymosterol',
     's56': 'source_3_keto_4_alpha_methylzymosterol',
     's55': 'source_4_alpha_carboxy_4_beta_response_parameter_methylzymosterol',
     's42': 'lanosterol',
     's41': 'squalene_2_3_epoxide',
     's27': 'squalene',
     's90': 'source_4_alpha_formyl_4_beta_response_parameter_methyl_5_alpha_cholesta_8_24_dien_3_beta_response_parameter_ol',
     's91': 'source_4_alpha_hydroxymethyl_4_beta_response_parameter_methyl_5_alpha_cholesta_8_24_dien_3_beta_response_parameter_ol',
     's53': 'source_14_dimethyllanosterol',
     's43': 'source_4_4_dimethyl_5_alpha_cholesta_8_14_24_trien_3_beta_response_parameter_ol',
     's92': 'source_32_hydroxylanosterol',
     's93': 'source_32_oxolanosterol',
     's49': 'source_24_25_dihydrolanosterole',
     's94': 'source_4_4_dimethyl_14_alpha_formyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's95': 'source_4_4_dimethyl_14_alpha_hydroxymethyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's51': 'source_4_4_dimethyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's33': 'source_4_4_dimethyl_5_alpha_cholest_8_en_2_beta_response_parameter_ol',
     's71': 'source_4_alpha_carboxy_4_beta_response_parameter_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's96': 'source_4_alpha_formyl_4_beta_response_parameter_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's97': 'source_4_alpha_hydroxymethyl_4_beta_response_parameter_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's70': 'source_4_alpha_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_one',
     's98': 'source_4_alpha_methyl_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's99': 'source_4_alpha_carboxymethyl_5_alpha_cholesta_8_en_3_beta_response_parameter_ol',
     's100': 'source_4_alpha_formyl_5_alpha_cholesta_8_en_3_beta_response_parameter_ol',
     's86': 'source_4_alpha_carboxy_5_alpha_cholesta_8_en_3_beta_response_parameter_ol',
     's68': 'source_5_alpha_cholest_8_en_3_one',
     's66': 'source_5_alpha_cholest_8_en_3_beta_response_parameter_ol',
     's65': 'lathosterol',
     's64': 'source_7_dehydroxycholesterol',
     's103': 'cyp27a1',
     's104': 'cyp3a4',
     's105': 'ch25h',
     's106': 'cyp7a1',
     's107': 'cyp46a1',
     's32': 'cholesterol',
     's108': 'source_24_hydroxycholesterol',
     's109': 'source_7_alpha_hydroxycholesterol',
     's110': 'source_4_beta_response_parameter_hydroxycholesterol',
     's111': 'source_25_xydroxycholesterol',
     's112': 'source_25_hydroxycholesterol',
     's113': 'source_27_hydroxycholesterol',
     's114': 'cholesterol_2',
     's37': 'source_24_s_25_epoxycholesterol',
     's62': 'source_24_s_25_epoxylathosterol',
     's61': 'source_24_s_25_epoxy_7_dehydrocholesterol',
     's35': 'source_24_s_25_epoxyzymosterol',
     's46': 'source_24_s_25_epoxylanosterol',
     's45': 'source_2_3_22_23_dioxidosqualene',
     's47': 'source_4_4_dimethyl_3_beta_response_parameter_hydroxy_5_alpha_cholesta_8_14_dien_24_s_25_epoxide',
     's34': 'source_4_4_dimethyl_3_beta_response_parameter_hydroxy_5_alpha_cholest_8_en_24_s_25_epoxide',
     's115': 'nsdhl',
     's116': 'source_defined_msmo1_state',
     's117': 'dhcr24',
     's118': 'hsd17b7'}

    def __init__(self, model_path: str = 'data/MODEL1409170003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Mazein2013ShuntPathwayModel1409170003Model = Mazein2013ShuntPathwayModel
