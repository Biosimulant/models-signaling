# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Benary2015FeedbackRegulationOfBetaCateninPModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1908050003'
    _TITLE = 'Benary2015 - feedback regulation of beta-catenin pathway by HOS and FWD1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'b_catenin_apc_axin_gsk3': ('B_catenin_APC__axin__GSK3',
                                 'native SBML value',
                                 'B Catenin APC Axin GSK3. Maps to SBML symbol '
                                 '`B_catenin_APC__axin__GSK3` and is emitted in native SBML units.'),
     'b_catenin_apc_axin_gsk3_2': ('B_catenin__APC__axin__GSK3',
                                   'native SBML value',
                                   'B Catenin APC Axin GSK3. Maps to SBML symbol '
                                   '`B_catenin__APC__axin__GSK3` and is emitted in native SBML units.'),
     'b_catenin': ('B_catenin',
                   'native SBML value',
                   'B Catenin. Maps to SBML symbol `B_catenin` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_wnt_state': ('Wnt',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined WNT state. Maps to SBML '
                                          'symbol `Wnt`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Dsh_i': 'source-defined DSH_I state',
     'Dsh_a': 'source-defined DSH_A state',
     'APC__axin__GSK3': 'APC Axin GSK3',
     'APC_axin_GSK3': 'APC Axin GSK3',
     'GSK3': 'source-defined GSK3 state',
     'APC_axin': 'APC Axin',
     'APC': 'source-defined APC state',
     'B_catenin_APC__axin__GSK3': 'B Catenin APC Axin GSK3',
     'B_catenin__APC__axin__GSK3': 'B Catenin APC Axin GSK3',
     'B_catenin': 'B Catenin',
     'B_catenin_0': 'B Catenin',
     'Axin': 'source-defined AXIN state',
     'TCF': 'source-defined TCF state',
     'B_catenin_TCF': 'B Catenin TCF',
     'B_catenin_APC': 'B Catenin APC',
     'Wnt': 'source-defined WNT state',
     'HOS_mRNA': 'HOS M RNA',
     'HOS': 'source-defined HOS state',
     'CRD_BP_mRNA': 'CRD BP M RNA',
     'CRD_BP': 'CRD BP',
     'FWD1_mRNA': 'FWD1 M RNA',
     'FWD1': 'source-defined FWD1 state',
     'B_catenin__APC__axin__GSK3_HOS': 'B Catenin APC Axin GSK3 HOS',
     'B_catenin__APC__axin__GSK3_FWD': 'B Catenin APC Axin GSK3 FWD1'}
    _STATE_OUTPUT_ALIASES = {'Dsh_i': 'source_defined_dsh_i_state',
     'Dsh_a': 'source_defined_dsh_a_state',
     'APC__axin__GSK3': 'apc_axin_gsk3',
     'APC_axin_GSK3': 'apc_axin_gsk3_2',
     'GSK3': 'source_defined_gsk3_state',
     'APC_axin': 'apc_axin',
     'APC': 'source_defined_apc_state',
     'B_catenin_APC__axin__GSK3': 'b_catenin_apc_axin_gsk3',
     'B_catenin__APC__axin__GSK3': 'b_catenin_apc_axin_gsk3_2',
     'B_catenin': 'b_catenin',
     'B_catenin_0': 'b_catenin_2',
     'Axin': 'source_defined_axin_state',
     'TCF': 'source_defined_tcf_state',
     'B_catenin_TCF': 'b_catenin_tcf',
     'B_catenin_APC': 'b_catenin_apc',
     'Wnt': 'source_defined_wnt_state',
     'HOS_mRNA': 'hos_m_rna',
     'HOS': 'source_defined_hos_state',
     'CRD_BP_mRNA': 'crd_bp_m_rna',
     'CRD_BP': 'crd_bp',
     'FWD1_mRNA': 'fwd1_m_rna',
     'FWD1': 'source_defined_fwd1_state',
     'B_catenin__APC__axin__GSK3_HOS': 'b_catenin_apc_axin_gsk3_hos',
     'B_catenin__APC__axin__GSK3_FWD': 'b_catenin_apc_axin_gsk3_fwd1'}

    def __init__(self, model_path: str = 'data/MODEL1908050003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Benary2015FeedbackRegulationOfBetaCateninPModel1908050003Model = Benary2015FeedbackRegulationOfBetaCateninPModel
