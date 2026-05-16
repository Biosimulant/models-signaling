# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bhalla2004_EGFR_MAPK."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhalla2004EgfrMapkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9085850385'
    _TITLE = 'Bhalla2004_EGFR_MAPK'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pkc_active_pkc_act_raf_pkc_act_raf_cplx': ('PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx',
                                                 'native SBML value',
                                                 'PKC active PKC Act RAF PKC Act RAF Cplx. Maps to '
                                                 'SBML symbol '
                                                 '`PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx` '
                                                 'and is emitted in native SBML units.'),
     'pkc_active_pkc_inact_gap_pkc_inact_gap_cplx': ('PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx',
                                                     'native SBML value',
                                                     'PKC active PKC Inact GAP PKC Inact GAP Cplx. '
                                                     'Maps to SBML symbol '
                                                     '`PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx` '
                                                     'and is emitted in native SBML units.'),
     'pkc_active_pkc_act_gef_pkc_act_gef_cplx': ('PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx',
                                                 'native SBML value',
                                                 'PKC active PKC Act GEF PKC Act GEF Cplx. Maps to '
                                                 'SBML symbol '
                                                 '`PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx` '
                                                 'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_beta_response_parameter_gamma': ('BetaGamma',
                                               0.0094,
                                               'native SBML value',
                                               'Initial level of beta response parameter Gamma. Maps '
                                               'to SBML symbol `BetaGamma`; exposed as a traceable '
                                               'initial-condition perturbation.'),
     'initial_calcium_m_ca4': ('CaM_minus_Ca4',
                               0.0,
                               'native SBML value',
                               'Initial level of calcium M Ca4. Maps to SBML symbol `CaM_minus_Ca4`; '
                               'exposed as a traceable initial-condition perturbation.'),
     'initial_egfr_egf': ('EGFR_slash_EGF',
                          0.0,
                          'native SBML value',
                          'Initial level of EGFR EGF. Maps to SBML symbol `EGFR_slash_EGF`; exposed as '
                          'a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx': 'PKC active '
                                                                                          'PKC Act RAF '
                                                                                          'PKC Act RAF '
                                                                                          'Cplx',
     'PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx': 'PKC '
                                                                                              'active '
                                                                                              'PKC '
                                                                                              'Inact '
                                                                                              'GAP PKC '
                                                                                              'Inact '
                                                                                              'GAP '
                                                                                              'Cplx',
     'PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx': 'PKC active '
                                                                                          'PKC Act GEF '
                                                                                          'PKC Act GEF '
                                                                                          'Cplx',
     'MAPK_star_': 'MAPK active',
     'MAPK_star__slash_MAPK_star__minus_feedback_slash_MAPK_star__minus_feedback_cplx': 'MAPK active '
                                                                                        'MAPK active '
                                                                                        'Feedback MAPK '
                                                                                        'active '
                                                                                        'Feedback Cplx',
     'MAPK_star__slash_phosph_Sos_slash_phosph_Sos_cplx': 'MAPK active Phosph SOS guanine-nucleotide '
                                                          'exchange factor Guanine Nucleotide Exchange '
                                                          'Factor Guanine Nucleotide Exchange Factor '
                                                          'Guanine Nucleotide Exchange Factor Guanine '
                                                          'Nucleotide Exchange Factor Phosph SOS '
                                                          'guanine-nucleotide exchange factor Guanine '
                                                          'Nucleotide Exchange Factor Guanine '
                                                          'Nucleotide Exchange Factor Guanine '
                                                          'Nucleotide Exchange Factor Guanine '
                                                          'Nucleotide Exchange Factor Cplx',
     'MAPK_slash_craf_minus_1': 'MAPK Craf 1',
     'MAPK_slash_craf_minus_1_star_': 'MAPK Craf 1 active',
     'MAPK_slash_MAPKK': 'MAPK Kinase',
     'MAPK_slash_MAPK': 'MAPK',
     'MAPK_slash_craf_minus_1_star__star_': 'MAPK Craf 1 active active',
     'MAPK_slash_MAPK_minus_tyr': 'MAPK MAPK Tyrosine Site',
     'MAPK_slash_MAPKK_star_': 'active MAPK Kinase',
     'MAPK_slash_MAPKK_star__slash_MAPKKtyr_slash_MAPKKtyr_cplx': 'MAPK MAPKK active Mapkktyr Mapkktyr '
                                                                  'Cplx',
     'MAPK_slash_MAPKK_star__slash_MAPKKthr_slash_MAPKKthr_cplx': 'MAPK MAPKK active Mapkkthr Mapkkthr '
                                                                  'Cplx',
     'MAPK_slash_MAPKK_minus_ser': 'MAPK Kinase Serine Phosphorylation State',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star_': 'MAPK RAF GTP RAS active',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star__slash_Raf_minus_GTP_minus_Ras_star__dot_1_slash_Raf_minus_GTP_minus_Ras_star__dot_1_cplx': 'MAPK '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'Dot '
                                                                                                                                          '1 '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'Dot '
                                                                                                                                          '1 '
                                                                                                                                          'Cplx',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star__slash_Raf_minus_GTP_minus_Ras_star__dot_2_slash_Raf_minus_GTP_minus_Ras_star__dot_2_cplx': 'MAPK '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'Dot '
                                                                                                                                          '2 '
                                                                                                                                          'RAF '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'active '
                                                                                                                                          'Dot '
                                                                                                                                          '2 '
                                                                                                                                          'Cplx',
     'MKP_minus_1': 'Source Defined MKP 1 State',
     'MKP_minus_1_slash_MKP1_minus_tyr_minus_deph_slash_MKP1_minus_tyr_minus_deph_cplx': 'MKP 1 MKP1 '
                                                                                         'Tyrosine '
                                                                                         'Site Deph '
                                                                                         'MKP1 '
                                                                                         'Tyrosine '
                                                                                         'Site Deph '
                                                                                         'Cplx',
     'MKP_minus_1_slash_MKP1_minus_thr_minus_deph_slash_MKP1_minus_thr_minus_deph_cplx': 'MKP 1 MKP1 '
                                                                                         'Thr Deph '
                                                                                         'MKP1 Thr '
                                                                                         'Deph Cplx',
     'PPhosphatase2A': 'Pphosphatase2a',
     'PPhosphatase2A_slash_craf_minus_deph_slash_craf_minus_deph_cplx': 'Pphosphatase2a Craf Deph Craf '
                                                                        'Deph Cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_slash_MAPKK_minus_deph_cplx': 'Pphosphatase2a MAPKK Deph '
                                                                          'MAPKK Deph Cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_minus_ser_slash_MAPKK_minus_deph_minus_ser_cplx': 'Pphosphatase2a '
                                                                                              'MAPKK '
                                                                                              'Deph '
                                                                                              'Ser '
                                                                                              'MAPKK '
                                                                                              'Deph '
                                                                                              'Ser '
                                                                                              'Cplx',
     'PPhosphatase2A_slash_craf_star__star__minus_deph_slash_craf_star__star__minus_deph_cplx': 'Pphosphatase2a '
                                                                                                'Craf '
                                                                                                'active '
                                                                                                'active '
                                                                                                'Deph '
                                                                                                'Craf '
                                                                                                'active '
                                                                                                'active '
                                                                                                'Deph '
                                                                                                'Cplx',
     'Ras_slash_GEF_minus_Gprot_minus_bg': 'RAS GEF Gprot Bg',
     'Ras_slash_GEF_minus_Gprot_minus_bg_slash_GEF_minus_bg_act_minus_ras_slash_GEF_minus_bg_act_minus_ras_cplx': 'RAS '
                                                                                                                  'GEF '
                                                                                                                  'Gprot '
                                                                                                                  'Bg '
                                                                                                                  'GEF '
                                                                                                                  'Bg '
                                                                                                                  'Act '
                                                                                                                  'RAS '
                                                                                                                  'GEF '
                                                                                                                  'Bg '
                                                                                                                  'Act '
                                                                                                                  'RAS '
                                                                                                                  'Cplx',
     'Ras_slash_inact_minus_GEF': 'RAS Inact GEF',
     'Ras_slash_GEF_star_': 'active RAS GEF',
     'Ras_slash_GEF_star__slash_GEF_star__minus_act_minus_ras_slash_GEF_star__minus_act_minus_ras_cplx': 'RAS '
                                                                                                         'GEF '
                                                                                                         'active '
                                                                                                         'GEF '
                                                                                                         'active '
                                                                                                         'Act '
                                                                                                         'RAS '
                                                                                                         'GEF '
                                                                                                         'active '
                                                                                                         'Act '
                                                                                                         'RAS '
                                                                                                         'Cplx',
     'Ras_slash_GTP_minus_Ras': 'GTP bound RAS',
     'Ras_slash_GDP_minus_Ras': 'GDP bound RAS',
     'Ras_slash_GAP_star_': 'active RAS GAP',
     'Ras_slash_GAP': 'RAS GAP',
     'Ras_slash_GAP_slash_GAP_minus_inact_minus_ras_slash_GAP_minus_inact_minus_ras_cplx': 'RAS GAP '
                                                                                           'GAP Inact '
                                                                                           'RAS GAP '
                                                                                           'Inact RAS '
                                                                                           'Cplx',
     'Ras_slash_inact_minus_GEF_star_': 'RAS Inact GEF active',
     'Ras_slash_CaM_minus_GEF': 'RAS Calcium M GEF',
     'Ras_slash_CaM_minus_GEF_slash_CaM_minus_GEF_minus_act_minus_ras_slash_CaM_minus_GEF_minus_act_minus_ras_cplx': 'RAS '
                                                                                                                     'Calcium '
                                                                                                                     'M '
                                                                                                                     'GEF '
                                                                                                                     'Calcium '
                                                                                                                     'M '
                                                                                                                     'GEF '
                                                                                                                     'Act '
                                                                                                                     'RAS '
                                                                                                                     'Calcium '
                                                                                                                     'M '
                                                                                                                     'GEF '
                                                                                                                     'Act '
                                                                                                                     'RAS '
                                                                                                                     'Cplx',
     'PKA_minus_active_slash_PKA_minus_phosph_minus_GEF_slash_PKA_minus_phosph_minus_GEF_cplx': 'PKA '
                                                                                                'active '
                                                                                                'PKA '
                                                                                                'Phosph '
                                                                                                'GEF '
                                                                                                'PKA '
                                                                                                'Phosph '
                                                                                                'GEF '
                                                                                                'Cplx',
     'Shc_star__dot_Sos_dot_Grb2': 'Shc adapter protein Adapter Protein Adapter Protein Adapter '
                                   'Protein Adapter Protein Adapter Protein active Dot SOS '
                                   'guanine-nucleotide exchange factor Guanine Nucleotide Exchange '
                                   'Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                                   'Exchange Factor Guanine Nucleotide Exchange Factor Dot Grb2 '
                                   'adapter protein Adapter Protein Adapter Protein Adapter Protein '
                                   'Adapter Protein Adapter Protein',
     'Shc_star__dot_Sos_dot_Grb2_slash_Sos_dot_Ras_GEF_slash_Sos_dot_Ras_GEF_cplx': 'Shc adapter '
                                                                                    'protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein active '
                                                                                    'Dot SOS '
                                                                                    'guanine-nucleotide '
                                                                                    'exchange factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Dot Grb2 adapter '
                                                                                    'protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein Adapter '
                                                                                    'Protein SOS '
                                                                                    'guanine-nucleotide '
                                                                                    'exchange factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Dot RAS GEF SOS '
                                                                                    'guanine-nucleotide '
                                                                                    'exchange factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Guanine '
                                                                                    'Nucleotide '
                                                                                    'Exchange Factor '
                                                                                    'Dot RAS GEF Cplx',
     'EGFR_slash_EGFR': 'EGFR EGFR',
     'EGFR_slash_L_dot_EGFR': 'EGFR L Dot EGFR',
     'EGFR_slash_L_dot_EGFR_slash_phosph_Shc_slash_phosph_Shc_cplx': 'EGFR L Dot EGFR Phosph Shc '
                                                                     'adapter protein Adapter Protein '
                                                                     'Adapter Protein Adapter Protein '
                                                                     'Adapter Protein Adapter Protein '
                                                                     'Phosph Shc adapter protein '
                                                                     'Adapter Protein Adapter Protein '
                                                                     'Adapter Protein Adapter Protein '
                                                                     'Adapter Protein Cplx',
     'EGFR_slash_SHC': 'EGFR Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                       'Adapter Protein Adapter Protein',
     'EGFR_slash_SHC_star_': 'EGFR Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                             'Adapter Protein Adapter Protein active',
     'EGFR_slash_Internal_L_dot_EGFR': 'EGFR Internal L Dot EGFR',
     'Sos_slash_Sos_star__dot_Grb2': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide '
                                     'Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                                     'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                                     'SOS guanine-nucleotide exchange factor Guanine Nucleotide '
                                     'Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                                     'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                                     'active Dot Grb2 adapter protein Adapter Protein Adapter Protein '
                                     'Adapter Protein Adapter Protein Adapter Protein',
     'Sos_slash_Grb2': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
                       'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                       'Nucleotide Exchange Factor Grb2 adapter protein Adapter Protein Adapter '
                       'Protein Adapter Protein Adapter Protein Adapter Protein',
     'Sos_slash_Sos_dot_Grb2': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange '
                               'Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange '
                               'Factor Guanine Nucleotide Exchange Factor SOS guanine-nucleotide '
                               'exchange factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                               'Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                               'Exchange Factor Dot Grb2 adapter protein Adapter Protein Adapter '
                               'Protein Adapter Protein Adapter Protein Adapter Protein',
     'Sos_slash_Sos_star_': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
                            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                            'Guanine Nucleotide Exchange Factor SOS guanine-nucleotide exchange factor '
                            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                            'active',
     'Sos_slash_Sos': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
                      'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                      'Nucleotide Exchange Factor SOS guanine-nucleotide exchange factor Guanine '
                      'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                      'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor',
     'PKC_minus_active': 'active PKC',
     'BetaGamma': 'beta response parameter Response Parameter Response Parameter Response Parameter '
                  'Response Parameter Response Parameter Gamma',
     'PKA_minus_active': 'PKA active',
     'CaM_minus_Ca4': 'Calcium M CA4',
     'EGFR_slash_EGF': 'EGFR EGF'}
    _STATE_OUTPUT_ALIASES = {'PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx': 'pkc_active_pkc_act_raf_pkc_act_raf_cplx',
     'PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx': 'pkc_active_pkc_inact_gap_pkc_inact_gap_cplx',
     'PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx': 'pkc_active_pkc_act_gef_pkc_act_gef_cplx',
     'MAPK_star_': 'mapk_active',
     'MAPK_star__slash_MAPK_star__minus_feedback_slash_MAPK_star__minus_feedback_cplx': 'mapk_active_mapk_active_feedback_mapk_active_feedback_cplx',
     'MAPK_star__slash_phosph_Sos_slash_phosph_Sos_cplx': 'mapk_active_phosph_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phosph_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_cplx',
     'MAPK_slash_craf_minus_1': 'mapk_craf_1',
     'MAPK_slash_craf_minus_1_star_': 'mapk_craf_1_active',
     'MAPK_slash_MAPKK': 'mapk_kinase',
     'MAPK_slash_MAPK': 'mapk',
     'MAPK_slash_craf_minus_1_star__star_': 'mapk_craf_1_active_active',
     'MAPK_slash_MAPK_minus_tyr': 'mapk_mapk_tyrosine_site',
     'MAPK_slash_MAPKK_star_': 'active_mapk_kinase',
     'MAPK_slash_MAPKK_star__slash_MAPKKtyr_slash_MAPKKtyr_cplx': 'mapk_mapkk_active_mapkktyr_mapkktyr_cplx',
     'MAPK_slash_MAPKK_star__slash_MAPKKthr_slash_MAPKKthr_cplx': 'mapk_mapkk_active_mapkkthr_mapkkthr_cplx',
     'MAPK_slash_MAPKK_minus_ser': 'mapk_kinase_serine_phosphorylation_state',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star_': 'mapk_raf_gtp_ras_active',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star__slash_Raf_minus_GTP_minus_Ras_star__dot_1_slash_Raf_minus_GTP_minus_Ras_star__dot_1_cplx': 'mapk_raf_gtp_ras_active_raf_gtp_ras_active_dot_1_raf_gtp_ras_active_dot_1_cplx',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_star__slash_Raf_minus_GTP_minus_Ras_star__dot_2_slash_Raf_minus_GTP_minus_Ras_star__dot_2_cplx': 'mapk_raf_gtp_ras_active_raf_gtp_ras_active_dot_2_raf_gtp_ras_active_dot_2_cplx',
     'MKP_minus_1': 'source_defined_mkp_1_state',
     'MKP_minus_1_slash_MKP1_minus_tyr_minus_deph_slash_MKP1_minus_tyr_minus_deph_cplx': 'mkp_1_mkp1_tyrosine_site_deph_mkp1_tyrosine_site_deph_cplx',
     'MKP_minus_1_slash_MKP1_minus_thr_minus_deph_slash_MKP1_minus_thr_minus_deph_cplx': 'mkp_1_mkp1_thr_deph_mkp1_thr_deph_cplx',
     'PPhosphatase2A': 'pphosphatase2a',
     'PPhosphatase2A_slash_craf_minus_deph_slash_craf_minus_deph_cplx': 'pphosphatase2a_craf_deph_craf_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_slash_MAPKK_minus_deph_cplx': 'pphosphatase2a_mapkk_deph_mapkk_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_minus_ser_slash_MAPKK_minus_deph_minus_ser_cplx': 'pphosphatase2a_mapkk_deph_ser_mapkk_deph_ser_cplx',
     'PPhosphatase2A_slash_craf_star__star__minus_deph_slash_craf_star__star__minus_deph_cplx': 'pphosphatase2a_craf_active_active_deph_craf_active_active_deph_cplx',
     'Ras_slash_GEF_minus_Gprot_minus_bg': 'ras_gef_gprot_bg',
     'Ras_slash_GEF_minus_Gprot_minus_bg_slash_GEF_minus_bg_act_minus_ras_slash_GEF_minus_bg_act_minus_ras_cplx': 'ras_gef_gprot_bg_gef_bg_act_ras_gef_bg_act_ras_cplx',
     'Ras_slash_inact_minus_GEF': 'ras_inact_gef',
     'Ras_slash_GEF_star_': 'active_ras_gef',
     'Ras_slash_GEF_star__slash_GEF_star__minus_act_minus_ras_slash_GEF_star__minus_act_minus_ras_cplx': 'ras_gef_active_gef_active_act_ras_gef_active_act_ras_cplx',
     'Ras_slash_GTP_minus_Ras': 'gtp_bound_ras',
     'Ras_slash_GDP_minus_Ras': 'gdp_bound_ras',
     'Ras_slash_GAP_star_': 'active_ras_gap',
     'Ras_slash_GAP': 'ras_gap',
     'Ras_slash_GAP_slash_GAP_minus_inact_minus_ras_slash_GAP_minus_inact_minus_ras_cplx': 'ras_gap_gap_inact_ras_gap_inact_ras_cplx',
     'Ras_slash_inact_minus_GEF_star_': 'ras_inact_gef_active',
     'Ras_slash_CaM_minus_GEF': 'ras_calcium_m_gef',
     'Ras_slash_CaM_minus_GEF_slash_CaM_minus_GEF_minus_act_minus_ras_slash_CaM_minus_GEF_minus_act_minus_ras_cplx': 'ras_calcium_m_gef_calcium_m_gef_act_ras_calcium_m_gef_act_ras_cplx',
     'PKA_minus_active_slash_PKA_minus_phosph_minus_GEF_slash_PKA_minus_phosph_minus_GEF_cplx': 'pka_active_pka_phosph_gef_pka_phosph_gef_cplx',
     'Shc_star__dot_Sos_dot_Grb2': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_active_dot_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_dot_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Shc_star__dot_Sos_dot_Grb2_slash_Sos_dot_Ras_GEF_slash_Sos_dot_Ras_GEF_cplx': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_active_dot_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_dot_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_dot_ras_gef_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_dot_ras_gef_cplx',
     'EGFR_slash_EGFR': 'egfr_egfr',
     'EGFR_slash_L_dot_EGFR': 'egfr_l_dot_egfr',
     'EGFR_slash_L_dot_EGFR_slash_phosph_Shc_slash_phosph_Shc_cplx': 'egfr_l_dot_egfr_phosph_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phosph_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_cplx',
     'EGFR_slash_SHC': 'egfr_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'EGFR_slash_SHC_star_': 'egfr_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_active',
     'EGFR_slash_Internal_L_dot_EGFR': 'egfr_internal_l_dot_egfr',
     'Sos_slash_Sos_star__dot_Grb2': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_active_dot_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Sos_slash_Grb2': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Sos_slash_Sos_dot_Grb2': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_dot_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Sos_slash_Sos_star_': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_active',
     'Sos_slash_Sos': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor',
     'PKC_minus_active': 'active_pkc',
     'BetaGamma': 'beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_gamma',
     'PKA_minus_active': 'pka_active',
     'CaM_minus_Ca4': 'calcium_m_ca4',
     'EGFR_slash_EGF': 'egfr_egf'}

    def __init__(self, model_path: str = 'data/MODEL9085850385.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bhalla2004EgfrMapkModel9085850385Model = Bhalla2004EgfrMapkModel
