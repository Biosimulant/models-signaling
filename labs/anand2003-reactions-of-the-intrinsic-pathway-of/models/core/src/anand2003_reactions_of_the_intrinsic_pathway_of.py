# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Anand2003 - Reactions of the Intrinsic Pathway of Blood Coagulation with Platelet Activation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Anand2003ReactionsOfTheIntrinsicPathwayOfModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1806130003'
    _TITLE = 'Anand2003 - Reactions of the Intrinsic Pathway of Blood Coagulation with Platelet Activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'activated_clotting_factor_ix': ('IXa',
                                      'native SBML value',
                                      'activated clotting factor IX. Maps to SBML symbol `IXa` and is '
                                      'emitted in native SBML units.'),
     'activated_clotting_factor_xi': ('XIa',
                                      'native SBML value',
                                      'activated clotting factor XI. Maps to SBML symbol `XIa` and is '
                                      'emitted in native SBML units.'),
     'atiii': ('ATIII',
               'native SBML value',
               'ATIII. Maps to SBML symbol `ATIII` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_ix_state': ('IX',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined IX state. Maps to SBML '
                                         'symbol `IX`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IX': 'source-defined IX state',
     'IXa': 'activated clotting factor IX',
     'XIa': 'activated clotting factor XI',
     'ATIII': 'ATIII',
     'IXa_ATIII': 'activated clotting factor IX ATIII',
     'IIa': 'source-defined IIA state',
     'VIII': 'source-defined VIII state',
     'VIIIa': 'Viiia',
     'VIIIa_i': 'Viiia I',
     'APC': 'source-defined APC state',
     'V': 'source-defined V state',
     'Va': 'source-defined VA state',
     'Va_i': 'source-defined VA_I state',
     'AP': 'source-defined AP state',
     'VIIIa_IXa_AP': 'Viiia activated clotting factor IX AP',
     'VIIIa_IXa': 'Viiia activated clotting factor IX',
     'Va_Xa_AP': 'Va Xa AP',
     'Xa': 'source-defined XA state',
     'Va_Xa': 'source-defined VA_XA state',
     'X': 'response node X',
     'Xa_ATIII': 'Xa ATIII',
     'TFPI': 'source-defined TFPI state',
     'Xa_TFPI': 'Xa TFPI',
     'II': 'source-defined II state',
     'IIa_ATIII': 'Iia ATIII',
     'PC': 'source-defined PC state',
     'APC_L1AT': 'APC L1AT',
     'L1AT': 'L1AT',
     'I': 'source-defined I state',
     'Ia': 'source-defined IA state',
     'Ia_i': 'source-defined IA_I state',
     'PLA': 'source-defined PLA state',
     'XI': 'source-defined XI state',
     'XIa_i': 'source-defined XIA_I state',
     'RP': 'source-defined RP state',
     'PLS': 'source-defined PLS state',
     'tPA_Ia': 'T PA Ia',
     'L2AP': 'L2AP',
     'PLA_L2AP': 'PLA L2AP',
     'tPA': 'source-defined TPA state'}
    _STATE_OUTPUT_ALIASES = {'IX': 'source_defined_ix_state',
     'IXa': 'activated_clotting_factor_ix',
     'XIa': 'activated_clotting_factor_xi',
     'ATIII': 'atiii',
     'IXa_ATIII': 'activated_clotting_factor_ix_atiii',
     'IIa': 'source_defined_iia_state',
     'VIII': 'source_defined_viii_state',
     'VIIIa': 'viiia',
     'VIIIa_i': 'viiia_i',
     'APC': 'source_defined_apc_state',
     'V': 'source_defined_v_state',
     'Va': 'source_defined_va_state',
     'Va_i': 'source_defined_va_i_state',
     'AP': 'source_defined_ap_state',
     'VIIIa_IXa_AP': 'viiia_activated_clotting_factor_ix_ap',
     'VIIIa_IXa': 'viiia_activated_clotting_factor_ix',
     'Va_Xa_AP': 'va_xa_ap',
     'Xa': 'source_defined_xa_state',
     'Va_Xa': 'source_defined_va_xa_state',
     'X': 'response_node_x',
     'Xa_ATIII': 'xa_atiii',
     'TFPI': 'source_defined_tfpi_state',
     'Xa_TFPI': 'xa_tfpi',
     'II': 'source_defined_ii_state',
     'IIa_ATIII': 'iia_atiii',
     'PC': 'source_defined_pc_state',
     'APC_L1AT': 'apc_l1at',
     'L1AT': 'l1at',
     'I': 'source_defined_i_state',
     'Ia': 'source_defined_ia_state',
     'Ia_i': 'source_defined_ia_i_state',
     'PLA': 'source_defined_pla_state',
     'XI': 'source_defined_xi_state',
     'XIa_i': 'source_defined_xia_i_state',
     'RP': 'source_defined_rp_state',
     'PLS': 'source_defined_pls_state',
     'tPA_Ia': 't_pa_ia',
     'L2AP': 'l2ap',
     'PLA_L2AP': 'pla_l2ap',
     'tPA': 'source_defined_tpa_state'}

    def __init__(self, model_path: str = 'data/MODEL1806130003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Anand2003ReactionsOfTheIntrinsicPathwayOfModel1806130003Model = Anand2003ReactionsOfTheIntrinsicPathwayOfModel
