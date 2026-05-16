# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ajay_Bhalla_2007_PKM."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AjayBhalla2007PkmModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9147232940'
    _TITLE = 'Ajay_Bhalla_2007_PKM'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca',
                           'native SBML value',
                           'Calcium bound PKC. Maps to SBML symbol `PKC_slash_PKC_minus_Ca` and is '
                           'emitted in native SBML units.'),
     'membrane_active_calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_memb_star_',
                                           'native SBML value',
                                           'Membrane active Calcium bound PKC. Maps to SBML symbol '
                                           '`PKC_slash_PKC_minus_Ca_minus_memb_star_` and is emitted '
                                           'in native SBML units.'),
     'calcium_and_dag_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_DAG',
                                   'native SBML value',
                                   'Calcium And DAG bound PKC. Maps to SBML symbol '
                                   '`PKC_slash_PKC_minus_Ca_minus_DAG` and is emitted in native SBML '
                                   'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_input': ('Ca_input',
                               0.08,
                               'native SBML value',
                               'Initial level of calcium Input. Maps to SBML symbol `Ca_input`; '
                               'exposed as a traceable initial-condition perturbation.'),
     'initial_dag': ('DAG',
                     12.1999469636701,
                     'native SBML value',
                     'Initial level of DAG. Maps to SBML symbol `DAG`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_active_pkc': ('PKC_minus_active',
                            0.0,
                            'native SBML value',
                            'Initial level of active PKC. Maps to SBML symbol `PKC_minus_active`; '
                            'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'PKC_slash_PKC_minus_Ca': 'Calcium bound PKC',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'Membrane active Calcium bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'Membrane active DAG bound PKC',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'Calcium And DAG bound PKC',
     'PKC_slash_PKC_minus_DAG': 'DAG bound PKC',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic PKC',
     'PKC_slash_PKM_minus_zeta': 'PKM Zeta',
     'PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx': 'PKC active '
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
     'MAPK_slash_Raf_minus_GTP_minus_Ras': 'MAPK RAF GTP RAS',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_slash_Raf_minus_GTP_minus_Ras_dot_1_slash_Raf_minus_GTP_minus_Ras_dot_1_cplx': 'MAPK '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'Dot '
                                                                                                                        '1 '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'Dot '
                                                                                                                        '1 '
                                                                                                                        'Cplx',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_slash_Raf_minus_GTP_minus_Ras_dot_2_slash_Raf_minus_GTP_minus_Ras_dot_2_cplx': 'MAPK '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'Dot '
                                                                                                                        '2 '
                                                                                                                        'RAF '
                                                                                                                        'GTP '
                                                                                                                        'RAS '
                                                                                                                        'Dot '
                                                                                                                        '2 '
                                                                                                                        'Cplx',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras': 'MAPK RAF active GTP RAS',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras_slash_Raf_star__minus_GTP_minus_Ras_dot_1_slash_Raf_star__minus_GTP_minus_Ras_dot_1_cplx': 'MAPK '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'Dot '
                                                                                                                                          '1 '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'Dot '
                                                                                                                                          '1 '
                                                                                                                                          'Cplx',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras_slash_Raf_star__minus_GTP_minus_Ras_dot_2_slash_Raf_star__minus_GTP_minus_Ras_dot_2_cplx': 'MAPK '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
                                                                                                                                          'Dot '
                                                                                                                                          '2 '
                                                                                                                                          'RAF '
                                                                                                                                          'active '
                                                                                                                                          'GTP '
                                                                                                                                          'RAS '
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
     'Ras_slash_inact_minus_GEF': 'RAS Inact GEF',
     'Ras_slash_inact_minus_GEF_slash_basal_GEF_activity_slash_basal_GEF_activity_cplx': 'RAS Inact '
                                                                                         'GEF Basal '
                                                                                         'GEF Activity '
                                                                                         'Basal GEF '
                                                                                         'Activity '
                                                                                         'Cplx',
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
     'CaM_slash_CaM': 'Calcium M Calcium M',
     'CaM_slash_CaM_minus_Ca3': 'Calcium M Calcium M CA3',
     'CaM_slash_CaM_minus_Ca4': 'Calcium M Calcium M CA4',
     'CaM_slash_CaM_minus_Ca2': 'Calcium M Calcium M CA2',
     'CaM_slash_CaM_minus_Ca': 'Calcium M Calcium M Calcium',
     'Ca': 'Calcium',
     'PKM_slash_Ca_detector': 'PKM Calcium Detector',
     'PKM_slash_PKM_synthesis': 'PKM PKM Synthesis',
     'PKM_slash_PKM_synthesis_slash_kenz_slash_kenz_cplx': 'PKM PKM Synthesis Kenz Kenz Cplx',
     'PKM_slash_Ca_dot_detector_complex': 'PKM Calcium Dot Detector Complex',
     'PKM_slash_Ca_dot_detector_complex_slash_kenz_slash_kenz_cplx': 'PKM Calcium Dot Detector Complex '
                                                                     'Kenz Kenz Cplx',
     'PKM_slash_PKM_activator': 'PKM PKM Activator',
     'DAG': 'DAG',
     'PKM_slash_AA_pool': 'PKM AA Pool',
     'PKM_slash_degraded_PKM': 'PKM Degraded PKM',
     'Ca_input': 'Calcium Input',
     'PKC_minus_active': 'active PKC'}
    _STATE_OUTPUT_ALIASES = {'PKC_slash_PKC_minus_Ca': 'calcium_bound_pkc',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'membrane_active_calcium_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'membrane_active_dag_bound_pkc',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'calcium_and_dag_bound_pkc',
     'PKC_slash_PKC_minus_DAG': 'dag_bound_pkc',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic_pkc',
     'PKC_slash_PKM_minus_zeta': 'pkm_zeta',
     'PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx': 'pkc_active_pkc_act_raf_pkc_act_raf_cplx',
     'PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx': 'pkc_active_pkc_inact_gap_pkc_inact_gap_cplx',
     'PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx': 'pkc_active_pkc_act_gef_pkc_act_gef_cplx',
     'MAPK_star_': 'mapk_active',
     'MAPK_star__slash_MAPK_star__minus_feedback_slash_MAPK_star__minus_feedback_cplx': 'mapk_active_mapk_active_feedback_mapk_active_feedback_cplx',
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
     'MAPK_slash_Raf_minus_GTP_minus_Ras': 'mapk_raf_gtp_ras',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_slash_Raf_minus_GTP_minus_Ras_dot_1_slash_Raf_minus_GTP_minus_Ras_dot_1_cplx': 'mapk_raf_gtp_ras_raf_gtp_ras_dot_1_raf_gtp_ras_dot_1_cplx',
     'MAPK_slash_Raf_minus_GTP_minus_Ras_slash_Raf_minus_GTP_minus_Ras_dot_2_slash_Raf_minus_GTP_minus_Ras_dot_2_cplx': 'mapk_raf_gtp_ras_raf_gtp_ras_dot_2_raf_gtp_ras_dot_2_cplx',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras': 'mapk_raf_active_gtp_ras',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras_slash_Raf_star__minus_GTP_minus_Ras_dot_1_slash_Raf_star__minus_GTP_minus_Ras_dot_1_cplx': 'mapk_raf_active_gtp_ras_raf_active_gtp_ras_dot_1_raf_active_gtp_ras_dot_1_cplx',
     'MAPK_slash_Raf_star__minus_GTP_minus_Ras_slash_Raf_star__minus_GTP_minus_Ras_dot_2_slash_Raf_star__minus_GTP_minus_Ras_dot_2_cplx': 'mapk_raf_active_gtp_ras_raf_active_gtp_ras_dot_2_raf_active_gtp_ras_dot_2_cplx',
     'MKP_minus_1': 'source_defined_mkp_1_state',
     'MKP_minus_1_slash_MKP1_minus_tyr_minus_deph_slash_MKP1_minus_tyr_minus_deph_cplx': 'mkp_1_mkp1_tyrosine_site_deph_mkp1_tyrosine_site_deph_cplx',
     'MKP_minus_1_slash_MKP1_minus_thr_minus_deph_slash_MKP1_minus_thr_minus_deph_cplx': 'mkp_1_mkp1_thr_deph_mkp1_thr_deph_cplx',
     'PPhosphatase2A': 'pphosphatase2a',
     'PPhosphatase2A_slash_craf_minus_deph_slash_craf_minus_deph_cplx': 'pphosphatase2a_craf_deph_craf_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_slash_MAPKK_minus_deph_cplx': 'pphosphatase2a_mapkk_deph_mapkk_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_minus_ser_slash_MAPKK_minus_deph_minus_ser_cplx': 'pphosphatase2a_mapkk_deph_ser_mapkk_deph_ser_cplx',
     'PPhosphatase2A_slash_craf_star__star__minus_deph_slash_craf_star__star__minus_deph_cplx': 'pphosphatase2a_craf_active_active_deph_craf_active_active_deph_cplx',
     'Ras_slash_inact_minus_GEF': 'ras_inact_gef',
     'Ras_slash_inact_minus_GEF_slash_basal_GEF_activity_slash_basal_GEF_activity_cplx': 'ras_inact_gef_basal_gef_activity_basal_gef_activity_cplx',
     'Ras_slash_GEF_star_': 'active_ras_gef',
     'Ras_slash_GEF_star__slash_GEF_star__minus_act_minus_ras_slash_GEF_star__minus_act_minus_ras_cplx': 'ras_gef_active_gef_active_act_ras_gef_active_act_ras_cplx',
     'Ras_slash_GTP_minus_Ras': 'gtp_bound_ras',
     'Ras_slash_GDP_minus_Ras': 'gdp_bound_ras',
     'Ras_slash_GAP_star_': 'active_ras_gap',
     'Ras_slash_GAP': 'ras_gap',
     'Ras_slash_GAP_slash_GAP_minus_inact_minus_ras_slash_GAP_minus_inact_minus_ras_cplx': 'ras_gap_gap_inact_ras_gap_inact_ras_cplx',
     'Ras_slash_CaM_minus_GEF': 'ras_calcium_m_gef',
     'Ras_slash_CaM_minus_GEF_slash_CaM_minus_GEF_minus_act_minus_ras_slash_CaM_minus_GEF_minus_act_minus_ras_cplx': 'ras_calcium_m_gef_calcium_m_gef_act_ras_calcium_m_gef_act_ras_cplx',
     'CaM_slash_CaM': 'calcium_m_calcium_m',
     'CaM_slash_CaM_minus_Ca3': 'calcium_m_calcium_m_ca3',
     'CaM_slash_CaM_minus_Ca4': 'calcium_m_calcium_m_ca4',
     'CaM_slash_CaM_minus_Ca2': 'calcium_m_calcium_m_ca2',
     'CaM_slash_CaM_minus_Ca': 'calcium_m_calcium_m_calcium',
     'Ca': 'calcium',
     'PKM_slash_Ca_detector': 'pkm_calcium_detector',
     'PKM_slash_PKM_synthesis': 'pkm_pkm_synthesis',
     'PKM_slash_PKM_synthesis_slash_kenz_slash_kenz_cplx': 'pkm_pkm_synthesis_kenz_kenz_cplx',
     'PKM_slash_Ca_dot_detector_complex': 'pkm_calcium_dot_detector_complex',
     'PKM_slash_Ca_dot_detector_complex_slash_kenz_slash_kenz_cplx': 'pkm_calcium_dot_detector_complex_kenz_kenz_cplx',
     'PKM_slash_PKM_activator': 'pkm_pkm_activator',
     'DAG': 'dag',
     'PKM_slash_AA_pool': 'pkm_aa_pool',
     'PKM_slash_degraded_PKM': 'pkm_degraded_pkm',
     'Ca_input': 'calcium_input',
     'PKC_minus_active': 'active_pkc'}

    def __init__(self, model_path: str = 'data/MODEL9147232940.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


AjayBhalla2007PkmModel9147232940Model = AjayBhalla2007PkmModel
