# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for DiCamillo2016 - Insulin signalling pathway - Rule-based model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dicamillo2016InsulinSignallingPathwayRuleBaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000833'
    _TITLE = 'DiCamillo2016 - Insulin signalling pathway - Rule-based model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt_s474_u_t309_u': ('S15',
                           'native SBML value',
                           'AKT S474 U T309 U. Maps to SBML symbol `S15` and is emitted in native SBML '
                           'units.'),
     'gs_sh2_state_a': ('S20',
                        'native SBML value',
                        'GS SH2 State A. Maps to SBML symbol `S20` and is emitted in native SBML '
                        'units.'),
     'ras_gap_bs': ('S21',
                    'native SBML value',
                    'RAS GAP Bs. Maps to SBML symbol `S21` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_amino_acids_input': ('Amino_Acids_input',
                                   0.0,
                                   'native SBML value',
                                   'Amino Acids Input source parameter. Maps to SBML symbol '
                                   '`Amino_Acids_input` and preserves the bundled default.')}
    _SPECIES_LABELS = {'S1': 'source-defined I(BS) state',
     'S2': 'insulin receptor NPXY Y999 U Alpha beta response parameter Loc M',
     'S3': 'insulin receptor NPXY Y999 U Alpha beta response parameter Loc C',
     'S4': 'IRS1 S636 U Y U Y896 YXXM',
     'S5': 'PI3K SH2',
     'S6': 'PI3K Variant Y U',
     'S7': 'PI45',
     'S8': 'PI345',
     'S9': 'PI34',
     'S10': 'PKC T410 U',
     'S11': 'GLUT4 Loc C',
     'S12': 'GLUT4 Loc M',
     'S13': 'Amino Acids',
     'S14': 'AMPK T172 U',
     'S15': 'AKT S474 U T309 U',
     'S16': 'M TORC1 S2448 U',
     'S17': 'M TORC2 S2481 U',
     'S18': 'P70s6k T389 U',
     'S19': 'TSC1 TSC2 S1387 U T1462 P',
     'S20': 'GS SH2 State A',
     'S21': 'RAS GAP Bs',
     'S22': 'SHP2 SH2',
     'S23': 'Src State I',
     'S24': 'RAS State GDP',
     'S25': 'RAF State I',
     'S26': 'MEK S218 S222 U',
     'S27': 'ERK T202 T185 U Y204 Y187 U',
     'S28': 'Synth G4',
     'S29': 'Synth insulin receptor',
     'S30': 'I Bs 1 insulin receptor NPXY Y999 U Alpha 1 beta response parameter Loc M',
     'S31': 'source-defined DEGR() state',
     'S32': 'IRS1 S636 U Y P Y896 YXXM',
     'S33': 'IRS1 S636 P Y U Y896 YXXM',
     'S34': 'AKT S474 U T309 P',
     'S35': 'PKC T410 P',
     'S36': 'PI3K Variant Y P',
     'S37': 'AMPK T172 P',
     'S38': 'AKT S474 P T309 U',
     'S39': 'TSC1 TSC2 S1387 P T1462 U',
     'S40': 'M TORC1 S2448 P',
     'S41': 'M TORC2 S2481 P',
     'S42': 'P70s6k T389 P',
     'S43': 'Src State A',
     'S44': 'RAS State GTP',
     'S45': 'RAF State A',
     'S46': 'MEK S218 S222 P',
     'S47': 'ERK T202 T185 P Y204 Y187 U',
     'S48': 'GS SH2 State I',
     'S49': 'I Bs 1 insulin receptor NPXY Y999 P Alpha 1 beta response parameter Loc M',
     'S50': 'IRS1 S636 U Y P Y896 YXXM 1 PI3K SH2 1',
     'S51': 'AKT S474 P T309 P',
     'S52': 'GS SH2 1 State A IRS1 S636 U Y P Y896 1 YXXM',
     'S53': 'IRS1 S636 U Y P Y896 1 YXXM SHP2 SH2 1',
     'S54': 'RAF State Aa',
     'S55': 'ERK T202 T185 P Y204 Y187 P',
     'S56': 'I Bs 1 I Bs 2 insulin receptor NPXY Y999 P Alpha 1 beta response parameter 2 Loc M',
     'S57': 'I Bs 1 insulin receptor NPXY Y999 P Alpha 1 beta response parameter Loc C',
     'S58': 'I Bs 1 insulin receptor NPXY 2 Y999 P Alpha 1 beta response parameter Loc M RAS GAP Bs 2',
     'S59': 'GS SH2 1 State A IRS1 S636 U Y P Y896 1 YXXM 2 PI3K SH2 2',
     'S60': 'I Bs 1 I Bs 2 insulin receptor NPXY Y999 P Alpha 1 beta response parameter 2 Loc C',
     'S61': 'I Bs 1 I Bs 2 insulin receptor NPXY 3 Y999 P Alpha 1 beta response parameter 2 Loc M RAS '
            'GAP Bs 3'}
    _STATE_OUTPUT_ALIASES = {'S1': 'source_defined_i_bs_state',
     'S2': 'insulin_receptor_npxy_y999_u_alpha_beta_response_parameter_loc_m',
     'S3': 'insulin_receptor_npxy_y999_u_alpha_beta_response_parameter_loc_c',
     'S4': 'irs1_s636_u_y_u_y896_yxxm',
     'S5': 'pi3k_sh2',
     'S6': 'pi3k_variant_y_u',
     'S7': 'pi45',
     'S8': 'pi345',
     'S9': 'pi34',
     'S10': 'pkc_t410_u',
     'S11': 'glut4_loc_c',
     'S12': 'glut4_loc_m',
     'S13': 'amino_acids',
     'S14': 'ampk_t172_u',
     'S15': 'akt_s474_u_t309_u',
     'S16': 'm_torc1_s2448_u',
     'S17': 'm_torc2_s2481_u',
     'S18': 'p70s6k_t389_u',
     'S19': 'tsc1_tsc2_s1387_u_t1462_p',
     'S20': 'gs_sh2_state_a',
     'S21': 'ras_gap_bs',
     'S22': 'shp2_sh2',
     'S23': 'src_state_i',
     'S24': 'ras_state_gdp',
     'S25': 'raf_state_i',
     'S26': 'mek_s218_s222_u',
     'S27': 'erk_t202_t185_u_y204_y187_u',
     'S28': 'synth_g4',
     'S29': 'synth_insulin_receptor',
     'S30': 'i_bs_1_insulin_receptor_npxy_y999_u_alpha_1_beta_response_parameter_loc_m',
     'S31': 'source_defined_degr_state',
     'S32': 'irs1_s636_u_y_p_y896_yxxm',
     'S33': 'irs1_s636_p_y_u_y896_yxxm',
     'S34': 'akt_s474_u_t309_p',
     'S35': 'pkc_t410_p',
     'S36': 'pi3k_variant_y_p',
     'S37': 'ampk_t172_p',
     'S38': 'akt_s474_p_t309_u',
     'S39': 'tsc1_tsc2_s1387_p_t1462_u',
     'S40': 'm_torc1_s2448_p',
     'S41': 'm_torc2_s2481_p',
     'S42': 'p70s6k_t389_p',
     'S43': 'src_state_a',
     'S44': 'ras_state_gtp',
     'S45': 'raf_state_a',
     'S46': 'mek_s218_s222_p',
     'S47': 'erk_t202_t185_p_y204_y187_u',
     'S48': 'gs_sh2_state_i',
     'S49': 'i_bs_1_insulin_receptor_npxy_y999_p_alpha_1_beta_response_parameter_loc_m',
     'S50': 'irs1_s636_u_y_p_y896_yxxm_1_pi3k_sh2_1',
     'S51': 'akt_s474_p_t309_p',
     'S52': 'gs_sh2_1_state_a_irs1_s636_u_y_p_y896_1_yxxm',
     'S53': 'irs1_s636_u_y_p_y896_1_yxxm_shp2_sh2_1',
     'S54': 'raf_state_aa',
     'S55': 'erk_t202_t185_p_y204_y187_p',
     'S56': 'i_bs_1_i_bs_2_insulin_receptor_npxy_y999_p_alpha_1_beta_response_parameter_2_loc_m',
     'S57': 'i_bs_1_insulin_receptor_npxy_y999_p_alpha_1_beta_response_parameter_loc_c',
     'S58': 'i_bs_1_insulin_receptor_npxy_2_y999_p_alpha_1_beta_response_parameter_loc_m_ras_gap_bs_2',
     'S59': 'gs_sh2_1_state_a_irs1_s636_u_y_p_y896_1_yxxm_2_pi3k_sh2_2',
     'S60': 'i_bs_1_i_bs_2_insulin_receptor_npxy_y999_p_alpha_1_beta_response_parameter_2_loc_c',
     'S61': 'i_bs_1_i_bs_2_insulin_receptor_npxy_3_y999_p_alpha_1_beta_response_parameter_2_loc_m_ras_gap_bs_3'}

    def __init__(self, model_path: str = 'data/BIOMD0000000833.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dicamillo2016InsulinSignallingPathwayRuleBaBiomd0000000833Model = Dicamillo2016InsulinSignallingPathwayRuleBaModel
