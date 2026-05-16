# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hodgson2018 - TGFbeta signalling and inflammatory response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hodgson2018TgfbetaSignallingAndInflammatoryModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1805080001'
    _TITLE = 'Hodgson2018 - TGFbeta signalling and inflammatory response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'stat3_nuc': ('Stat3_nuc',
                   'native SBML value',
                   'STAT3 Nuc. Maps to SBML symbol `Stat3_nuc` and is emitted in native SBML units.'),
     'stat3_cyt': ('Stat3_cyt',
                   'native SBML value',
                   'STAT3 Cyt. Maps to SBML symbol `Stat3_cyt` and is emitted in native SBML units.'),
     'smad7': ('Smad7',
               'native SBML value',
               'SMAD7. Maps to SBML symbol `Smad7` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sink_species': ('Sink',
                              1.0,
                              'native SBML value',
                              'Initial level of sink species. Maps to SBML symbol `Sink`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_source': ('Source',
                        1.0,
                        'native SBML value',
                        'Initial level of Source. Maps to SBML symbol `Source`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_tgf_beta_a': ('Tgfb_A',
                            0.0,
                            'native SBML value',
                            'Initial level of TGF-beta A. Maps to SBML symbol `Tgfb_A`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IL1': 'source-defined IL1 state',
     'Jnk_P': 'source-defined JNK_P state',
     'Jnk': 'source-defined JNK state',
     'IL1R': 'IL1R',
     'IL1RR': 'IL1RR',
     'IL1RR_int': 'IL1RR Int',
     'cJun': 'source-defined CJUN state',
     'cJun_P': 'C Jun P',
     'cJun_dimer': 'C Jun Dimer',
     'OSM': 'source-defined OSM state',
     'OSMR': 'source-defined OSMR state',
     'OSMRR': 'OSMRR',
     'Jak1': 'source-defined JAK1 state',
     'Jak1_P': 'Jak1 P',
     'Stat3_nuc': 'STAT3 Nuc',
     'cFos_mRNA': 'C Fos M RNA',
     'Stat3_cyt': 'STAT3 Cyt',
     'cFos': 'source-defined CFOS state',
     'p38': 'Abstract source state P38',
     'p38_P': 'P38 P',
     'cFos_P': 'C Fos P',
     'cFos_cJun': 'C Fos C Jun',
     'Block': 'Block',
     'MMP13_mRNA': 'MMP13 M RNA',
     'Integrin': 'Integrin',
     'Source': 'Source',
     'Sink': 'sink species',
     'Alk5': 'source-defined ALK5 state',
     'Tgfb_A': 'TGF-beta A',
     'Tgfb_I': 'TGF-beta I',
     'Alk5_dimer': 'Alk5 Dimer',
     'Alk1': 'source-defined ALK1 state',
     'Alk1_Alk5': 'Alk1 Alk5',
     'Tgfb_Alk5_dimer': 'TGF-beta Alk5 Dimer',
     'Smad7': 'SMAD7',
     'Tgfb_Alk5_dimer_Smad7': 'TGF-beta Alk5 Dimer SMAD7',
     'Tgfb_Alk1_Alk5': 'TGF-beta Alk1 Alk5',
     'Smad2_3': 'Smad2 3',
     'Smad2_3_P': 'Smad2 3 P',
     'Smad2_3_P_Smad4': 'Smad2 3 P Smad4',
     'Smad4': 'source-defined SMAD4 state',
     'Runx2_A': 'Runx2 A',
     'Runx2_I': 'Runx2 I',
     'Smad1_5_8': 'Smad1 5 8',
     'Smad1_5_8_P': 'Smad1 5 8 P',
     'Smad1_5_8_P_Smad4': 'Smad1 5 8 P Smad4',
     'Tgfb_Alk1_Alk5_Smad7': 'TGF-beta Alk1 Alk5 SMAD7',
     'JunB_mRNA': 'Jun B M RNA',
     'JunB': 'source-defined JUNB state',
     'JunB_cJun': 'Jun B C Jun',
     'A': 'source-defined A state',
     'Dummy_mRNA': 'Dummy M RNA',
     'Dummy': 'Dummy',
     'A_phos': 'A Phos'}
    _STATE_OUTPUT_ALIASES = {'IL1': 'source_defined_il1_state',
     'Jnk_P': 'source_defined_jnk_p_state',
     'Jnk': 'source_defined_jnk_state',
     'IL1R': 'il1r',
     'IL1RR': 'il1rr',
     'IL1RR_int': 'il1rr_int',
     'cJun': 'source_defined_cjun_state',
     'cJun_P': 'c_jun_p',
     'cJun_dimer': 'c_jun_dimer',
     'OSM': 'source_defined_osm_state',
     'OSMR': 'source_defined_osmr_state',
     'OSMRR': 'osmrr',
     'Jak1': 'source_defined_jak1_state',
     'Jak1_P': 'jak1_p',
     'Stat3_nuc': 'stat3_nuc',
     'cFos_mRNA': 'c_fos_m_rna',
     'Stat3_cyt': 'stat3_cyt',
     'cFos': 'source_defined_cfos_state',
     'p38': 'abstract_source_state_p38',
     'p38_P': 'p38_p',
     'cFos_P': 'c_fos_p',
     'cFos_cJun': 'c_fos_c_jun',
     'Block': 'block',
     'MMP13_mRNA': 'mmp13_m_rna',
     'Integrin': 'integrin',
     'Source': 'source',
     'Sink': 'sink_species',
     'Alk5': 'source_defined_alk5_state',
     'Tgfb_A': 'tgf_beta_a',
     'Tgfb_I': 'tgf_beta_i',
     'Alk5_dimer': 'alk5_dimer',
     'Alk1': 'source_defined_alk1_state',
     'Alk1_Alk5': 'alk1_alk5',
     'Tgfb_Alk5_dimer': 'tgf_beta_alk5_dimer',
     'Smad7': 'smad7',
     'Tgfb_Alk5_dimer_Smad7': 'tgf_beta_alk5_dimer_smad7',
     'Tgfb_Alk1_Alk5': 'tgf_beta_alk1_alk5',
     'Smad2_3': 'smad2_3',
     'Smad2_3_P': 'smad2_3_p',
     'Smad2_3_P_Smad4': 'smad2_3_p_smad4',
     'Smad4': 'source_defined_smad4_state',
     'Runx2_A': 'runx2_a',
     'Runx2_I': 'runx2_i',
     'Smad1_5_8': 'smad1_5_8',
     'Smad1_5_8_P': 'smad1_5_8_p',
     'Smad1_5_8_P_Smad4': 'smad1_5_8_p_smad4',
     'Tgfb_Alk1_Alk5_Smad7': 'tgf_beta_alk1_alk5_smad7',
     'JunB_mRNA': 'jun_b_m_rna',
     'JunB': 'source_defined_junb_state',
     'JunB_cJun': 'jun_b_c_jun',
     'A': 'source_defined_a_state',
     'Dummy_mRNA': 'dummy_m_rna',
     'Dummy': 'dummy',
     'A_phos': 'a_phos'}

    def __init__(self, model_path: str = 'data/MODEL1805080001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hodgson2018TgfbetaSignallingAndInflammatoryModel1805080001Model = Hodgson2018TgfbetaSignallingAndInflammatoryModel
