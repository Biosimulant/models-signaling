# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for TLR4-NFkB-phospho-NF-kB signaling in BMDM."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tlr4NfkbPhosphoNfKbSignalingInBmdmModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1809230001'
    _TITLE = 'TLR4-NFkB-phospho-NF-kB signaling in BMDM'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ik_ba_nfk_b': ('species_30',
                     'native SBML value',
                     'Ik Ba Nfk B. Maps to SBML symbol `species_30` and is emitted in native SBML '
                     'units.'),
     'nfkb': ('species_31',
              'native SBML value',
              'NF-kB. Maps to SBML symbol `species_31` and is emitted in native SBML units.'),
     'ikk_p_ik_ba_nfk_b': ('species_32',
                           'native SBML value',
                           'IKK P Ik Ba Nfk B. Maps to SBML symbol `species_32` and is emitted in '
                           'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sink_species': ('species_23',
                              0.0,
                              'native SBML value',
                              'Initial level of sink species. Maps to SBML symbol `species_23`; '
                              'exposed as a traceable initial-condition perturbation.'),
     'initial_source_dna': ('species_22',
                            1.0,
                            'native SBML value',
                            'Initial level of Source DNA. Maps to SBML symbol `species_22`; exposed as '
                            'a traceable initial-condition perturbation.'),
     'initial_cd14lps': ('CD14LPS',
                         0.0,
                         'native SBML value',
                         'Initial level of CD14LPS. Maps to SBML symbol `CD14LPS`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'CD14',
     'species_10': 'source-defined TRAF6 state',
     'species_14': 'source-defined IKK state',
     'species_15': 'source-defined IKK[P] state',
     'species_22': 'Source DNA',
     'species_23': 'sink species',
     'species_29': 'source-defined IKBA state',
     'species_30': 'Ik Ba Nfk B',
     'species_31': 'NF-kB',
     'species_32': 'IKK P Ik Ba Nfk B',
     'species_39': 'Nfk B Nuc',
     'species_40': 'Ik Ba Nuc',
     'species_41': 'Ik Ba Nfk B Nuc',
     'species_46': 'Ik Ba M RNA',
     'species_49': 'IKK P Ik Ba',
     'TAK1': 'source-defined TAK1 state',
     'CD14LPS': 'CD14LPS',
     'TLR4LPS_memb': 'TLR4LPS Memb',
     'TLR4_memb': 'TLR4 Memb',
     'CD14LPS_endo': 'CD14LPS Endo',
     'TLR4LPS_endo': 'TLR4LPS Endo',
     'TLR4_endo': 'TLR4 Endo',
     'MYD88': 'MYD88',
     'MYD88_0': 'MYD88',
     'TRIF': 'source-defined TRIF state',
     'TRIF_0': 'source-defined TRIF* state',
     'TRAF6_P': 'TRAF6 P',
     'TAK1_P': 'TAK1 P',
     'IkBb': 'source-defined IKBB state',
     'IkBb_NFkB': 'Ik complement factor Bb Nfk B',
     'IkBe': 'source-defined IKBE state',
     'IkBe_NFkB': 'Ik Be Nfk B',
     'IKK_P__IkBb_NFkB': 'IKK P Ik complement factor Bb Nfk B',
     'IKK_P__IkBe_NFkB': 'IKK P Ik Be Nfk B',
     'IkBb_nuc': 'Ik complement factor Bb Nuc',
     'IkBb_NFkB_nuc': 'Ik complement factor Bb Nfk B Nuc',
     'IkBe_nuc': 'Ik Be Nuc',
     'IkBe_NFkB_nuc': 'Ik Be Nfk B Nuc',
     'IkBb_mRNA': 'Ik complement factor Bb M RNA',
     'IkBe_mRNA': 'Ik Be M RNA',
     'IKK_P__IkBb': 'IKK P Ik complement factor Bb',
     'IKK_P__IkBe': 'IKK P Ik Be',
     'dimerTLR4LPS_memb': 'Dimer TLR4LPS Memb',
     'dimerTLR4LPS_endo': 'Dimer TLR4LPS Endo',
     'NFkBDNA_nuc': 'Nfk BDNA Nuc',
     'NFkB_P': 'Nfk B P',
     'NFkB_P__nuc': 'Nfk B P Nuc',
     'IKK_P__IkBa_NFkB_P': 'IKK P Ik Ba Nfk B P',
     'NFkBDNA_P__nuc': 'Nfk BDNA P Nuc',
     'WIP1': 'source-defined WIP1 state',
     'WIP1_mRNA': 'WIP1 M RNA',
     'species_4': 'source-defined LPS state'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'cd14',
     'species_10': 'source_defined_traf6_state',
     'species_14': 'source_defined_ikk_state',
     'species_15': 'source_defined_ikk_p_state',
     'species_22': 'source_dna',
     'species_23': 'sink_species',
     'species_29': 'source_defined_ikba_state',
     'species_30': 'ik_ba_nfk_b',
     'species_31': 'nfkb',
     'species_32': 'ikk_p_ik_ba_nfk_b',
     'species_39': 'nfk_b_nuc',
     'species_40': 'ik_ba_nuc',
     'species_41': 'ik_ba_nfk_b_nuc',
     'species_46': 'ik_ba_m_rna',
     'species_49': 'ikk_p_ik_ba',
     'TAK1': 'source_defined_tak1_state',
     'CD14LPS': 'cd14lps',
     'TLR4LPS_memb': 'tlr4lps_memb',
     'TLR4_memb': 'tlr4_memb',
     'CD14LPS_endo': 'cd14lps_endo',
     'TLR4LPS_endo': 'tlr4lps_endo',
     'TLR4_endo': 'tlr4_endo',
     'MYD88': 'myd88',
     'MYD88_0': 'myd88_2',
     'TRIF': 'source_defined_trif_state',
     'TRIF_0': 'source_defined_trif_state_2',
     'TRAF6_P': 'traf6_p',
     'TAK1_P': 'tak1_p',
     'IkBb': 'source_defined_ikbb_state',
     'IkBb_NFkB': 'ik_complement_factor_bb_nfk_b',
     'IkBe': 'source_defined_ikbe_state',
     'IkBe_NFkB': 'ik_be_nfk_b',
     'IKK_P__IkBb_NFkB': 'ikk_p_ik_complement_factor_bb_nfk_b',
     'IKK_P__IkBe_NFkB': 'ikk_p_ik_be_nfk_b',
     'IkBb_nuc': 'ik_complement_factor_bb_nuc',
     'IkBb_NFkB_nuc': 'ik_complement_factor_bb_nfk_b_nuc',
     'IkBe_nuc': 'ik_be_nuc',
     'IkBe_NFkB_nuc': 'ik_be_nfk_b_nuc',
     'IkBb_mRNA': 'ik_complement_factor_bb_m_rna',
     'IkBe_mRNA': 'ik_be_m_rna',
     'IKK_P__IkBb': 'ikk_p_ik_complement_factor_bb',
     'IKK_P__IkBe': 'ikk_p_ik_be',
     'dimerTLR4LPS_memb': 'dimer_tlr4lps_memb',
     'dimerTLR4LPS_endo': 'dimer_tlr4lps_endo',
     'NFkBDNA_nuc': 'nfk_bdna_nuc',
     'NFkB_P': 'nfk_b_p',
     'NFkB_P__nuc': 'nfk_b_p_nuc',
     'IKK_P__IkBa_NFkB_P': 'ikk_p_ik_ba_nfk_b_p',
     'NFkBDNA_P__nuc': 'nfk_bdna_p_nuc',
     'WIP1': 'source_defined_wip1_state',
     'WIP1_mRNA': 'wip1_m_rna',
     'species_4': 'source_defined_lps_state'}

    def __init__(self, model_path: str = 'data/MODEL1809230001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Tlr4NfkbPhosphoNfKbSignalingInBmdmModel1809230001Model = Tlr4NfkbPhosphoNfKbSignalingInBmdmModel
