# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ajay_Bhalla_2007_Bistable."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AjayBhalla2007BistableModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9147091146'
    _TITLE = 'Ajay_Bhalla_2007_Bistable'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca',
                           'native SBML value',
                           'Calcium bound PKC. Maps to SBML symbol `PKC_slash_PKC_minus_Ca` and is '
                           'emitted in native SBML units.'),
     'arachidonic_acid_active_calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_AA_star_',
                                                   'native SBML value',
                                                   'Arachidonic Acid active Calcium bound PKC. Maps to '
                                                   'SBML symbol '
                                                   '`PKC_slash_PKC_minus_Ca_minus_AA_star_` and is '
                                                   'emitted in native SBML units.'),
     'membrane_active_calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_memb_star_',
                                           'native SBML value',
                                           'Membrane active Calcium bound PKC. Maps to SBML symbol '
                                           '`PKC_slash_PKC_minus_Ca_minus_memb_star_` and is emitted '
                                           'in native SBML units.')}
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
     'initial_ip3': ('IP3',
                     0.730005303632989,
                     'native SBML value',
                     'Initial level of IP3. Maps to SBML symbol `IP3`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'PKC_slash_PKC_minus_Ca': 'Calcium bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_AA_star_': 'DAG And Arachidonic Acid active PKC',
     'PKC_slash_PKC_minus_Ca_minus_AA_star_': 'Arachidonic Acid active Calcium bound PKC',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'Membrane active Calcium bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'Membrane active DAG bound PKC',
     'PKC_slash_PKC_minus_basal_star_': 'Basal active PKC',
     'PKC_slash_PKC_minus_AA_star_': 'Arachidonic Acid active PKC',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'Calcium And DAG bound PKC',
     'PKC_slash_PKC_minus_DAG': 'DAG bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_AA': 'DAG And Arachidonic Acid bound PKC',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic PKC',
     'AA': 'Source Defined AA State',
     'PLA2_slash_PLA2_minus_cytosolic': 'cytosolic PLA2',
     'PLA2_slash_PLA2_minus_Ca_star_': 'Calcium Activated PLA2',
     'PLA2_slash_PLA2_minus_Ca_star__slash_kenz_slash_kenz_cplx': 'PLA2 PLA2 Calcium active Kenz Kenz '
                                                                  'Cplx',
     'PLA2_slash_PIP2_minus_PLA2_star_': 'PIP2 bound active PLA2',
     'PLA2_slash_PIP2_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'PLA2 PIP2 PLA2 active Kenz Kenz '
                                                                    'Cplx',
     'PLA2_slash_PIP2_minus_Ca_minus_PLA2_star_': 'PIP2 And Calcium bound active PLA2',
     'PLA2_slash_PIP2_minus_Ca_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'PLA2 PIP2 Calcium PLA2 '
                                                                             'active Kenz Kenz Cplx',
     'PLA2_slash_DAG_minus_Ca_minus_PLA2_star_': 'DAG And Calcium bound active PLA2',
     'PLA2_slash_DAG_minus_Ca_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'PLA2 DAG Calcium PLA2 '
                                                                            'active Kenz Kenz Cplx',
     'PLA2_slash_PLA2_star__minus_Ca': 'Calcium bound active PLA2',
     'PLA2_slash_PLA2_star__minus_Ca_slash_kenz_slash_kenz_cplx': 'PLA2 PLA2 active Calcium Kenz Kenz '
                                                                  'Cplx',
     'PLA2_slash_PLA2_star_': 'active PLA2',
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
     'Ca': 'Calcium',
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
     'PKC_minus_active_slash_phosph_minus_AC2_slash_phosph_minus_AC2_cplx': 'PKC active Phosph AC2 '
                                                                            'Phosph AC2 Cplx',
     'MAPK_star_': 'MAPK active',
     'MAPK_star__slash_MAPK_star__slash_MAPK_star__cplx': 'MAPK active MAPK active MAPK active Cplx',
     'MAPK_star__slash_MAPK_star__minus_feedback_slash_MAPK_star__minus_feedback_cplx': 'MAPK active '
                                                                                        'MAPK active '
                                                                                        'Feedback MAPK '
                                                                                        'active '
                                                                                        'Feedback Cplx',
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
     'CaM_slash_CaM': 'Calcium M Calcium M',
     'CaM_slash_CaM_minus_Ca3': 'Calcium M Calcium M CA3',
     'CaM_slash_CaM_minus_TR2_minus_Ca2': 'Calcium M Calcium M TR2 CA2',
     'CaM_slash_CaM_minus_Ca4': 'Calcium M Calcium M CA4',
     'PLA2_slash_APC': 'PLA2 APC',
     'temp_minus_PIP2': 'Temp PIP2',
     'DAG': 'DAG',
     'IP3': 'IP3',
     'Ca_input': 'Calcium Input',
     'PKC_minus_active': 'active PKC'}
    _STATE_OUTPUT_ALIASES = {'PKC_slash_PKC_minus_Ca': 'calcium_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_AA_star_': 'dag_and_arachidonic_acid_active_pkc',
     'PKC_slash_PKC_minus_Ca_minus_AA_star_': 'arachidonic_acid_active_calcium_bound_pkc',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'membrane_active_calcium_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'membrane_active_dag_bound_pkc',
     'PKC_slash_PKC_minus_basal_star_': 'basal_active_pkc',
     'PKC_slash_PKC_minus_AA_star_': 'arachidonic_acid_active_pkc',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'calcium_and_dag_bound_pkc',
     'PKC_slash_PKC_minus_DAG': 'dag_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_AA': 'dag_and_arachidonic_acid_bound_pkc',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic_pkc',
     'AA': 'source_defined_aa_state',
     'PLA2_slash_PLA2_minus_cytosolic': 'cytosolic_pla2',
     'PLA2_slash_PLA2_minus_Ca_star_': 'calcium_activated_pla2',
     'PLA2_slash_PLA2_minus_Ca_star__slash_kenz_slash_kenz_cplx': 'pla2_pla2_calcium_active_kenz_kenz_cplx',
     'PLA2_slash_PIP2_minus_PLA2_star_': 'pip2_bound_active_pla2',
     'PLA2_slash_PIP2_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'pla2_pip2_pla2_active_kenz_kenz_cplx',
     'PLA2_slash_PIP2_minus_Ca_minus_PLA2_star_': 'pip2_and_calcium_bound_active_pla2',
     'PLA2_slash_PIP2_minus_Ca_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'pla2_pip2_calcium_pla2_active_kenz_kenz_cplx',
     'PLA2_slash_DAG_minus_Ca_minus_PLA2_star_': 'dag_and_calcium_bound_active_pla2',
     'PLA2_slash_DAG_minus_Ca_minus_PLA2_star__slash_kenz_slash_kenz_cplx': 'pla2_dag_calcium_pla2_active_kenz_kenz_cplx',
     'PLA2_slash_PLA2_star__minus_Ca': 'calcium_bound_active_pla2',
     'PLA2_slash_PLA2_star__minus_Ca_slash_kenz_slash_kenz_cplx': 'pla2_pla2_active_calcium_kenz_kenz_cplx',
     'PLA2_slash_PLA2_star_': 'active_pla2',
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
     'Ca': 'calcium',
     'PKC_minus_active_slash_PKC_minus_act_minus_raf_slash_PKC_minus_act_minus_raf_cplx': 'pkc_active_pkc_act_raf_pkc_act_raf_cplx',
     'PKC_minus_active_slash_PKC_minus_inact_minus_GAP_slash_PKC_minus_inact_minus_GAP_cplx': 'pkc_active_pkc_inact_gap_pkc_inact_gap_cplx',
     'PKC_minus_active_slash_PKC_minus_act_minus_GEF_slash_PKC_minus_act_minus_GEF_cplx': 'pkc_active_pkc_act_gef_pkc_act_gef_cplx',
     'PKC_minus_active_slash_phosph_minus_AC2_slash_phosph_minus_AC2_cplx': 'pkc_active_phosph_ac2_phosph_ac2_cplx',
     'MAPK_star_': 'mapk_active',
     'MAPK_star__slash_MAPK_star__slash_MAPK_star__cplx': 'mapk_active_mapk_active_mapk_active_cplx',
     'MAPK_star__slash_MAPK_star__minus_feedback_slash_MAPK_star__minus_feedback_cplx': 'mapk_active_mapk_active_feedback_mapk_active_feedback_cplx',
     'MKP_minus_1': 'source_defined_mkp_1_state',
     'MKP_minus_1_slash_MKP1_minus_tyr_minus_deph_slash_MKP1_minus_tyr_minus_deph_cplx': 'mkp_1_mkp1_tyrosine_site_deph_mkp1_tyrosine_site_deph_cplx',
     'MKP_minus_1_slash_MKP1_minus_thr_minus_deph_slash_MKP1_minus_thr_minus_deph_cplx': 'mkp_1_mkp1_thr_deph_mkp1_thr_deph_cplx',
     'PPhosphatase2A': 'pphosphatase2a',
     'PPhosphatase2A_slash_craf_minus_deph_slash_craf_minus_deph_cplx': 'pphosphatase2a_craf_deph_craf_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_slash_MAPKK_minus_deph_cplx': 'pphosphatase2a_mapkk_deph_mapkk_deph_cplx',
     'PPhosphatase2A_slash_MAPKK_minus_deph_minus_ser_slash_MAPKK_minus_deph_minus_ser_cplx': 'pphosphatase2a_mapkk_deph_ser_mapkk_deph_ser_cplx',
     'PPhosphatase2A_slash_craf_star__star__minus_deph_slash_craf_star__star__minus_deph_cplx': 'pphosphatase2a_craf_active_active_deph_craf_active_active_deph_cplx',
     'CaM_slash_CaM': 'calcium_m_calcium_m',
     'CaM_slash_CaM_minus_Ca3': 'calcium_m_calcium_m_ca3',
     'CaM_slash_CaM_minus_TR2_minus_Ca2': 'calcium_m_calcium_m_tr2_ca2',
     'CaM_slash_CaM_minus_Ca4': 'calcium_m_calcium_m_ca4',
     'PLA2_slash_APC': 'pla2_apc',
     'temp_minus_PIP2': 'temp_pip2',
     'DAG': 'dag',
     'IP3': 'ip3',
     'Ca_input': 'calcium_input',
     'PKC_minus_active': 'active_pkc'}

    def __init__(self, model_path: str = 'data/MODEL9147091146.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


AjayBhalla2007BistableModel9147091146Model = AjayBhalla2007BistableModel
