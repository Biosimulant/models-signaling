# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hui2016 - Age-related changes in articular cartilage."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hui2016AgeRelatedChangesInArticularCartilaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000560'
    _TITLE = 'Hui2016 - Age-related changes in articular cartilage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'acanm_rna': ('AcanmRNA',
                   'native SBML value',
                   'Acanm RNA. Maps to SBML symbol `AcanmRNA` and is emitted in native SBML units.'),
     'caspase_a': ('Caspase_A',
                   'native SBML value',
                   'Caspase A. Maps to SBML symbol `Caspase_A` and is emitted in native SBML units.'),
     'caspase_i': ('Caspase_I',
                   'native SBML value',
                   'Caspase I. Maps to SBML symbol `Caspase_I` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_natp_state': ('NatP',
                                           1500.0,
                                           'native SBML value',
                                           'Initial level of source-defined NATP state. Maps to SBML '
                                           'symbol `NatP`; exposed as a traceable initial-condition '
                                           'perturbation.'),
     'initial_sink_species': ('Sink',
                              0.0,
                              'native SBML value',
                              'Initial level of sink species. Maps to SBML symbol `Sink`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_source': ('Source',
                        1.0,
                        'native SBML value',
                        'Initial level of Source. Maps to SBML symbol `Source`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'AcanmRNA': 'Acanm RNA',
     'ADAMTS5': 'ADAMTS5',
     'AGEprod': 'Ageprod',
     'Alk1': 'Source Defined ALK1 State',
     'Alk1_Alk5': 'ALK1 ALK5',
     'Alk5': 'Source Defined ALK5 State',
     'Alk5_dimer': 'ALK5 Dimer',
     'Bax': 'Source Defined BAX State',
     'Bax_Bcl2': 'Bax BCL2',
     'Bax_Bcl2_Beclin': 'Bax BCL2 Beclin',
     'Bax_Bcl2_Beclin_I': 'Bax BCL2 Beclin I',
     'Bcl2': 'Source Defined BCL2 State',
     'Bcl2_Beclin': 'BCL2 Beclin',
     'Bcl2_Beclin_I': 'BCL2 Beclin I',
     'Beclin': 'Beclin',
     'Beclin_I': 'Beclin I',
     'Caspase_A': 'Caspase A',
     'Caspase_I': 'Caspase I',
     'Col2mRNA': 'Col2m RNA',
     'DamP': 'Source Defined DAMP State',
     'IkB': 'IkB',
     'IkB_NFkB': 'Ik B NF K B',
     'IL1': 'Source Defined IL1 State',
     'Lys_A': 'Source Defined LYS A State',
     'Lys_I': 'Source Defined LYS I State',
     'MMP13': 'MMP13',
     'MMP2': 'Source Defined MMP2 State',
     'NatP': 'Source Defined nuclear ATP State',
     'NFkB': 'NF-kB',
     'NFkB_P': 'NF K B P',
     'p38': 'Abstract Source State P38',
     'p38_P': 'P38 P',
     'proMMP13': 'PROMMP13',
     'proMMP2': 'PROMMP2',
     'RAGE': 'Source Defined RAGE State',
     'ROS': 'Source Defined ROS State',
     'Runx2_A': 'RUNX2 A',
     'Runx2_I': 'RUNX2 I',
     'Smad1': 'Source Defined SMAD1 State',
     'Smad1_P': 'SMAD1 P',
     'Smad1_P_Smad4': 'SMAD1 P SMAD4',
     'Smad2': 'Source Defined SMAD2 State',
     'Smad2_P': 'SMAD2 P',
     'Smad2_P_Smad4': 'SMAD2 P SMAD4',
     'Smad4': 'Source Defined SMAD4 State',
     'Smad7': 'SMAD7',
     'SOD': 'Source Defined SOD State',
     'Sox9': 'Source Defined SOX9 State',
     'Sox9_A': 'SOX9 A',
     'Sox9mRNA': 'Sox9m RNA',
     'Tgfb_A': 'TGF beta response parameter Response Parameter Response Parameter Response Parameter '
               'Response Parameter A',
     'Tgfb_Alk1_Alk5': 'TGF beta response parameter Response Parameter Response Parameter Response '
                       'Parameter Response Parameter ALK1 ALK5',
     'Tgfb_Alk1_Alk5_Smad7': 'TGF beta response parameter Response Parameter Response Parameter '
                             'Response Parameter Response Parameter ALK1 ALK5 SMAD7',
     'Tgfb_Alk5_dimer': 'TGF beta response parameter Response Parameter Response Parameter Response '
                        'Parameter Response Parameter ALK5 Dimer',
     'Tgfb_Alk5_dimer_Smad7': 'TGF beta response parameter Response Parameter Response Parameter '
                              'Response Parameter Response Parameter ALK5 Dimer SMAD7',
     'AggFrag': 'Agg Frag',
     'Aggrecan': 'Aggrecan',
     'Aggrecan_Collagen2': 'Aggrecan COLLAGEN2',
     'ColFrag': 'Col Frag',
     'Collagen2': 'COLLAGEN2',
     'Integrin': 'Integrin',
     'Tgfb_I': 'TGF beta response parameter Response Parameter Response Parameter Response Parameter '
               'Response Parameter I',
     'IntegrinCount': 'Integrin Count'}
    _STATE_OUTPUT_ALIASES = {'AcanmRNA': 'acanm_rna',
     'ADAMTS5': 'adamts5',
     'AGEprod': 'ageprod',
     'Alk1': 'source_defined_alk1_state',
     'Alk1_Alk5': 'alk1_alk5',
     'Alk5': 'source_defined_alk5_state',
     'Alk5_dimer': 'alk5_dimer',
     'Bax': 'source_defined_bax_state',
     'Bax_Bcl2': 'bax_bcl2',
     'Bax_Bcl2_Beclin': 'bax_bcl2_beclin',
     'Bax_Bcl2_Beclin_I': 'bax_bcl2_beclin_i',
     'Bcl2': 'source_defined_bcl2_state',
     'Bcl2_Beclin': 'bcl2_beclin',
     'Bcl2_Beclin_I': 'bcl2_beclin_i',
     'Beclin': 'beclin',
     'Beclin_I': 'beclin_i',
     'Caspase_A': 'caspase_a',
     'Caspase_I': 'caspase_i',
     'Col2mRNA': 'col2m_rna',
     'DamP': 'source_defined_damp_state',
     'IkB': 'ikb',
     'IkB_NFkB': 'ik_b_nf_k_b',
     'IL1': 'source_defined_il1_state',
     'Lys_A': 'source_defined_lys_a_state',
     'Lys_I': 'source_defined_lys_i_state',
     'MMP13': 'mmp13',
     'MMP2': 'source_defined_mmp2_state',
     'NatP': 'source_defined_nuclear_atp_state',
     'NFkB': 'nfkb',
     'NFkB_P': 'nf_k_b_p',
     'p38': 'abstract_source_state_p38',
     'p38_P': 'p38_p',
     'proMMP13': 'prommp13',
     'proMMP2': 'prommp2',
     'RAGE': 'source_defined_rage_state',
     'ROS': 'source_defined_ros_state',
     'Runx2_A': 'runx2_a',
     'Runx2_I': 'runx2_i',
     'Smad1': 'source_defined_smad1_state',
     'Smad1_P': 'smad1_p',
     'Smad1_P_Smad4': 'smad1_p_smad4',
     'Smad2': 'source_defined_smad2_state',
     'Smad2_P': 'smad2_p',
     'Smad2_P_Smad4': 'smad2_p_smad4',
     'Smad4': 'source_defined_smad4_state',
     'Smad7': 'smad7',
     'SOD': 'source_defined_sod_state',
     'Sox9': 'source_defined_sox9_state',
     'Sox9_A': 'sox9_a',
     'Sox9mRNA': 'sox9m_rna',
     'Tgfb_A': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_a',
     'Tgfb_Alk1_Alk5': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_alk1_alk5',
     'Tgfb_Alk1_Alk5_Smad7': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_alk1_alk5_smad7',
     'Tgfb_Alk5_dimer': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_alk5_dimer',
     'Tgfb_Alk5_dimer_Smad7': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_alk5_dimer_smad7',
     'AggFrag': 'agg_frag',
     'Aggrecan': 'aggrecan',
     'Aggrecan_Collagen2': 'aggrecan_collagen2',
     'ColFrag': 'col_frag',
     'Collagen2': 'collagen2',
     'Integrin': 'integrin',
     'Tgfb_I': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_i',
     'IntegrinCount': 'integrin_count'}

    def __init__(self, model_path: str = 'data/BIOMD0000000560.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hui2016AgeRelatedChangesInArticularCartilaBiomd0000000560Model = Hui2016AgeRelatedChangesInArticularCartilaModel
