# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Brummel-Ziedins2012 - Contribution of the PC pathway to thrombin generation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class BrummelZiedins2012ContributionOfThePcPathwModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1807180002'
    _TITLE = 'Brummel-Ziedins2012 - Contribution of the PC pathway to thrombin generation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'viii_ica1': ('VIII_Ica1',
                   'native SBML value',
                   'VIII Ica1. Maps to SBML symbol `VIII_Ica1` and is emitted in native SBML units.'),
     'source_defined_lca1_state': ('LCA1',
                                   'native SBML value',
                                   'source-defined LCA1 state. Maps to SBML symbol `LCA1` and is '
                                   'emitted in native SBML units.'),
     'apc_lca1': ('APC_LCA1',
                  'native SBML value',
                  'APC LCA1. Maps to SBML symbol `APC_LCA1` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_tf_state': ('TF',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined TF state. Maps to SBML '
                                         'symbol `TF`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'TF': 'source-defined TF state',
     'TF_VII': 'TF VII',
     'VII': 'source-defined VII state',
     'TF_VIIa': 'TF Viia',
     'VIIa': 'source-defined VIIA state',
     'Xa': 'source-defined XA state',
     'IIa': 'source-defined IIA state',
     'TF_VIIa_X': 'TF Viia X',
     'X': 'response node X',
     'TF_VIIa_Xa': 'TF Viia Xa',
     'IX': 'source-defined IX state',
     'TF_VIIa_IX': 'TF Viia IX',
     'IXa': 'activated clotting factor IX',
     'II': 'source-defined II state',
     'VIII': 'source-defined VIII state',
     'VIIIa': 'Viiia',
     'IXa_VIIIa': 'activated clotting factor IX Viiia',
     'IXa_VIIIa_X': 'activated clotting factor IX Viiia X',
     'VIII_Ica1': 'VIII Ica1',
     'VIII_a2': 'VIII A2',
     'V': 'source-defined V state',
     'Va': 'source-defined VA state',
     'Xa_Va': 'source-defined XA_VA state',
     'Xa_Va_II': 'Xa Va II',
     'mIIa': 'source-defined MIIA state',
     'TFPI': 'source-defined TFPI state',
     'Xa_TFPI': 'Xa TFPI',
     'TF_VIIa_Xa_TFPI': 'TF Viia Xa TFPI',
     'ATIII': 'ATIII',
     'Xa_ATIII': 'Xa ATIII',
     'mIIa_ATIII': 'M Iia ATIII',
     'IXa_ATIII': 'activated clotting factor IX ATIII',
     'IIa_ATIII': 'Iia ATIII',
     'TF_VIIa_ATIII': 'TF Viia ATIII',
     'TM': 'source-defined TM state',
     'TM_IIa': 'TM Iia',
     'PC': 'source-defined PC state',
     'TM_IIa_PC': 'TM Iia PC',
     'APC': 'source-defined APC state',
     'APC_Va': 'APC Va',
     'Va5': 'source-defined VA5 state',
     'Va3': 'source-defined VA3 state',
     'APC_Va5': 'APC Va5',
     'APC_Va3': 'APC Va3',
     'Va53': 'Va53',
     'HCF': 'source-defined HCF state',
     'LCA1': 'source-defined LCA1 state',
     'APC_LCA1': 'APC LCA1',
     'TM_IIa_APC': 'TM Iia APC',
     'Xa_Va5': 'source-defined XA_VA5 state',
     'Xa_Va3': 'source-defined XA_VA3 state',
     'Xa_Va5_II': 'Xa Va5 II',
     'Xa_Va3_II': 'Xa Va3 II',
     'TM_mIIa': 'TM M Iia',
     'TM_mIIa_PC': 'TM M Iia PC',
     'Xa_Va53': 'Xa Va53',
     'Xa_Va53_II': 'Xa Va53 II',
     'II_Va': 'source-defined II_VA state'}
    _STATE_OUTPUT_ALIASES = {'TF': 'source_defined_tf_state',
     'TF_VII': 'tf_vii',
     'VII': 'source_defined_vii_state',
     'TF_VIIa': 'tf_viia',
     'VIIa': 'source_defined_viia_state',
     'Xa': 'source_defined_xa_state',
     'IIa': 'source_defined_iia_state',
     'TF_VIIa_X': 'tf_viia_x',
     'X': 'response_node_x',
     'TF_VIIa_Xa': 'tf_viia_xa',
     'IX': 'source_defined_ix_state',
     'TF_VIIa_IX': 'tf_viia_ix',
     'IXa': 'activated_clotting_factor_ix',
     'II': 'source_defined_ii_state',
     'VIII': 'source_defined_viii_state',
     'VIIIa': 'viiia',
     'IXa_VIIIa': 'activated_clotting_factor_ix_viiia',
     'IXa_VIIIa_X': 'activated_clotting_factor_ix_viiia_x',
     'VIII_Ica1': 'viii_ica1',
     'VIII_a2': 'viii_a2',
     'V': 'source_defined_v_state',
     'Va': 'source_defined_va_state',
     'Xa_Va': 'source_defined_xa_va_state',
     'Xa_Va_II': 'xa_va_ii',
     'mIIa': 'source_defined_miia_state',
     'TFPI': 'source_defined_tfpi_state',
     'Xa_TFPI': 'xa_tfpi',
     'TF_VIIa_Xa_TFPI': 'tf_viia_xa_tfpi',
     'ATIII': 'atiii',
     'Xa_ATIII': 'xa_atiii',
     'mIIa_ATIII': 'm_iia_atiii',
     'IXa_ATIII': 'activated_clotting_factor_ix_atiii',
     'IIa_ATIII': 'iia_atiii',
     'TF_VIIa_ATIII': 'tf_viia_atiii',
     'TM': 'source_defined_tm_state',
     'TM_IIa': 'tm_iia',
     'PC': 'source_defined_pc_state',
     'TM_IIa_PC': 'tm_iia_pc',
     'APC': 'source_defined_apc_state',
     'APC_Va': 'apc_va',
     'Va5': 'source_defined_va5_state',
     'Va3': 'source_defined_va3_state',
     'APC_Va5': 'apc_va5',
     'APC_Va3': 'apc_va3',
     'Va53': 'va53',
     'HCF': 'source_defined_hcf_state',
     'LCA1': 'source_defined_lca1_state',
     'APC_LCA1': 'apc_lca1',
     'TM_IIa_APC': 'tm_iia_apc',
     'Xa_Va5': 'source_defined_xa_va5_state',
     'Xa_Va3': 'source_defined_xa_va3_state',
     'Xa_Va5_II': 'xa_va5_ii',
     'Xa_Va3_II': 'xa_va3_ii',
     'TM_mIIa': 'tm_m_iia',
     'TM_mIIa_PC': 'tm_m_iia_pc',
     'Xa_Va53': 'xa_va53',
     'Xa_Va53_II': 'xa_va53_ii',
     'II_Va': 'source_defined_ii_va_state'}

    def __init__(self, model_path: str = 'data/MODEL1807180002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


BrummelZiedins2012ContributionOfThePcPathwModel1807180002Model = BrummelZiedins2012ContributionOfThePcPathwModel
