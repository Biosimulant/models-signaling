# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sharp2013 - Lipopolysaccharide induced NFkB activation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sharp2013LipopolysaccharideInducedNfkbActivaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000489'
    _TITLE = 'Sharp2013 - Lipopolysaccharide induced NFkB activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_tnfa_state': ('species_24',
                                   'native SBML value',
                                   'source-defined TNFA state. Maps to SBML symbol `species_24` and is '
                                   'emitted in native SBML units.'),
     'tnf_receptor_1': ('species_25',
                        'native SBML value',
                        'TNF receptor 1. Maps to SBML symbol `species_25` and is emitted in native '
                        'SBML units.'),
     'tnfa_tnf_receptor_1_traf2_tradd_rip1': ('species_28',
                                              'native SBML value',
                                              'Tnfa TNF receptor 1 TRAF2 TRADD RIP1. Maps to SBML '
                                              'symbol `species_28` and is emitted in native SBML '
                                              'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cd14': ('species_1',
                      1.0,
                      'native SBML value',
                      'Initial level of CD14. Maps to SBML symbol `species_1`; exposed as a traceable '
                      'initial-condition perturbation.'),
     'initial_source_defined_irak4_state': ('species_2',
                                            1.0,
                                            'native SBML value',
                                            'Initial level of source-defined IRAK4 state. Maps to SBML '
                                            'symbol `species_2`; exposed as a traceable '
                                            'initial-condition perturbation.'),
     'initial_source_defined_lbp_state': ('species_3',
                                          1.0,
                                          'native SBML value',
                                          'Initial level of source-defined LBP state. Maps to SBML '
                                          'symbol `species_3`; exposed as a traceable '
                                          'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'CD14',
     'species_2': 'source-defined IRAK4 state',
     'species_3': 'source-defined LBP state',
     'species_4': 'source-defined LPS state',
     'species_5': 'LPS LBP CD14 TLR4 TIRAP My D88 IRAK4',
     'species_6': 'My D88',
     'species_7': 'TIRAP',
     'species_8': 'source-defined TLR4 state',
     'species_9': 'source-defined IRAK1 state',
     'species_10': 'source-defined TRAF6 state',
     'species_11': 'TRAF6 IRAK1 P',
     'species_12': 'TAK1 TAB1 TAB2',
     'species_13': 'TAK1 TAB1 TAB2 TRAF6',
     'species_14': 'source-defined IKK state',
     'species_15': 'source-defined IKK[P] state',
     'species_16': 'source-defined RIP1 state',
     'species_17': 'source-defined TRAM state',
     'species_18': 'source-defined TRIF state',
     'species_19': 'source-defined IRF3 state',
     'species_20': 'IRF3 P',
     'species_21': 'IRF3 P Nuc',
     'species_24': 'source-defined TNFA state',
     'species_25': 'TNF receptor 1',
     'species_26': 'TRADD',
     'species_27': 'source-defined TRAF2 state',
     'species_28': 'Tnfa TNF receptor 1 TRAF2 TRADD RIP1',
     'species_29': 'source-defined IKBA state',
     'species_30': 'Ik Ba Nfk B',
     'species_31': 'NF-kB',
     'species_32': 'IKK P Ik Ba Nfk B',
     'species_33': 'source-defined IKBB state',
     'species_34': 'Ik complement factor Bb Nfk B',
     'species_35': 'IKK P Ik complement factor Bb Nfk B',
     'species_36': 'source-defined IKBE state',
     'species_37': 'Ik Be Nfk B',
     'species_38': 'IKK P Ik Be Nfk B',
     'species_39': 'Nfk B Nuc',
     'species_40': 'Ik Ba Nuc',
     'species_41': 'Ik Ba Nfk B Nuc',
     'species_42': 'Ik complement factor Bb Nuc',
     'species_43': 'Ik complement factor Bb Nfk B Nuc',
     'species_44': 'Ik Be Nuc',
     'species_45': 'Ik Be Nfk B Nuc',
     'species_46': 'Ik Ba M RNA',
     'species_47': 'Ik complement factor Bb M RNA',
     'species_48': 'Ik Be M RNA',
     'species_49': 'IKK P Ik Ba',
     'species_50': 'IKK P Ik complement factor Bb',
     'species_51': 'IKK P Ik Be',
     'species_52': 'LPS LBP CD14 TLR4 RIP1 TRAM TRIF TBK Ikke',
     'species_53': 'TBK1 Ikke'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'cd14',
     'species_2': 'source_defined_irak4_state',
     'species_3': 'source_defined_lbp_state',
     'species_4': 'source_defined_lps_state',
     'species_5': 'lps_lbp_cd14_tlr4_tirap_my_d88_irak4',
     'species_6': 'my_d88',
     'species_7': 'tirap',
     'species_8': 'source_defined_tlr4_state',
     'species_9': 'source_defined_irak1_state',
     'species_10': 'source_defined_traf6_state',
     'species_11': 'traf6_irak1_p',
     'species_12': 'tak1_tab1_tab2',
     'species_13': 'tak1_tab1_tab2_traf6',
     'species_14': 'source_defined_ikk_state',
     'species_15': 'source_defined_ikk_p_state',
     'species_16': 'source_defined_rip1_state',
     'species_17': 'source_defined_tram_state',
     'species_18': 'source_defined_trif_state',
     'species_19': 'source_defined_irf3_state',
     'species_20': 'irf3_p',
     'species_21': 'irf3_p_nuc',
     'species_24': 'source_defined_tnfa_state',
     'species_25': 'tnf_receptor_1',
     'species_26': 'tradd',
     'species_27': 'source_defined_traf2_state',
     'species_28': 'tnfa_tnf_receptor_1_traf2_tradd_rip1',
     'species_29': 'source_defined_ikba_state',
     'species_30': 'ik_ba_nfk_b',
     'species_31': 'nfkb',
     'species_32': 'ikk_p_ik_ba_nfk_b',
     'species_33': 'source_defined_ikbb_state',
     'species_34': 'ik_complement_factor_bb_nfk_b',
     'species_35': 'ikk_p_ik_complement_factor_bb_nfk_b',
     'species_36': 'source_defined_ikbe_state',
     'species_37': 'ik_be_nfk_b',
     'species_38': 'ikk_p_ik_be_nfk_b',
     'species_39': 'nfk_b_nuc',
     'species_40': 'ik_ba_nuc',
     'species_41': 'ik_ba_nfk_b_nuc',
     'species_42': 'ik_complement_factor_bb_nuc',
     'species_43': 'ik_complement_factor_bb_nfk_b_nuc',
     'species_44': 'ik_be_nuc',
     'species_45': 'ik_be_nfk_b_nuc',
     'species_46': 'ik_ba_m_rna',
     'species_47': 'ik_complement_factor_bb_m_rna',
     'species_48': 'ik_be_m_rna',
     'species_49': 'ikk_p_ik_ba',
     'species_50': 'ikk_p_ik_complement_factor_bb',
     'species_51': 'ikk_p_ik_be',
     'species_52': 'lps_lbp_cd14_tlr4_rip1_tram_trif_tbk_ikke',
     'species_53': 'tbk1_ikke'}

    def __init__(self, model_path: str = 'data/BIOMD0000000489.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sharp2013LipopolysaccharideInducedNfkbActivaBiomd0000000489Model = Sharp2013LipopolysaccharideInducedNfkbActivaModel
