# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zarnitsina1996 - Reactions of the Intrinsic Pathway of Blood Coagulation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zarnitsina1996ReactionsOfTheIntrinsicPathwaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1806140001'
    _TITLE = 'Zarnitsina1996 - Reactions of the Intrinsic Pathway of Blood Coagulation'
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
     'activated_clotting_factor_ix_at': ('IXa_AT',
                                         'native SBML value',
                                         'activated clotting factor IX AT. Maps to SBML symbol '
                                         '`IXa_AT` and is emitted in native SBML units.')}
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
     'AT': 'source-defined AT state',
     'IXa_AT': 'activated clotting factor IX AT',
     'IIa': 'source-defined IIA state',
     'VIII': 'source-defined VIII state',
     'VIIIa': 'Viiia',
     'VIIIi': 'Viiii',
     'APC': 'source-defined APC state',
     'V': 'source-defined V state',
     'Va': 'source-defined VA state',
     'Vi': 'source-defined VI state',
     'VIIIa_IXa': 'Viiia activated clotting factor IX',
     'Va_Xa': 'source-defined VA_XA state',
     'Xa': 'source-defined XA state',
     'X': 'response node X',
     'IXa_VIIIa': 'activated clotting factor IX Viiia',
     'Xa_AT': 'source-defined XA_AT state',
     'II': 'source-defined II state',
     'IIa_AT': 'Iia AT',
     'PC': 'source-defined PC state',
     'APC_L1_AT': 'APC L1 AT',
     'L1_AT': 'L1 AT',
     'Fibrin': 'Fibrin',
     'Fibrinogen': 'Fibrinogen',
     'XI': 'source-defined XI state',
     'XIi': 'source-defined XII state'}
    _STATE_OUTPUT_ALIASES = {'IX': 'source_defined_ix_state',
     'IXa': 'activated_clotting_factor_ix',
     'XIa': 'activated_clotting_factor_xi',
     'AT': 'source_defined_at_state',
     'IXa_AT': 'activated_clotting_factor_ix_at',
     'IIa': 'source_defined_iia_state',
     'VIII': 'source_defined_viii_state',
     'VIIIa': 'viiia',
     'VIIIi': 'viiii',
     'APC': 'source_defined_apc_state',
     'V': 'source_defined_v_state',
     'Va': 'source_defined_va_state',
     'Vi': 'source_defined_vi_state',
     'VIIIa_IXa': 'viiia_activated_clotting_factor_ix',
     'Va_Xa': 'source_defined_va_xa_state',
     'Xa': 'source_defined_xa_state',
     'X': 'response_node_x',
     'IXa_VIIIa': 'activated_clotting_factor_ix_viiia',
     'Xa_AT': 'source_defined_xa_at_state',
     'II': 'source_defined_ii_state',
     'IIa_AT': 'iia_at',
     'PC': 'source_defined_pc_state',
     'APC_L1_AT': 'apc_l1_at',
     'L1_AT': 'l1_at',
     'Fibrin': 'fibrin',
     'Fibrinogen': 'fibrinogen',
     'XI': 'source_defined_xi_state',
     'XIi': 'source_defined_xii_state'}

    def __init__(self, model_path: str = 'data/MODEL1806140001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Zarnitsina1996ReactionsOfTheIntrinsicPathwaModel1806140001Model = Zarnitsina1996ReactionsOfTheIntrinsicPathwaModel
