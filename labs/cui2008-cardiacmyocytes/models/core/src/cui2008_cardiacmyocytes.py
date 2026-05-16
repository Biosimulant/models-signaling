# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Cui2008_CardiacMyocytes."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cui2008CardiacmyocytesModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1172425728'
    _TITLE = 'Cui2008_CardiacMyocytes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'BMK1': 'source_defined_bmk1_state',
     'MRNA': 'source_defined_mrna_state',
     'NFATc': 'nfatc',
     'NFATn': 'nfatn',
     'NFATpc': 'nfatpc',
     'NFATpn': 'nfatpn',
     'GSK3betac': 'gsk3betac',
     'GSK3betan': 'gsk3betan',
     'CaNc': 'source_defined_canc_state',
     'CaNc_star': 'calcium_nc_star',
     'CaNn_star': 'calcium_nn_star',
     'CaNn': 'source_defined_cann_state',
     'CaM': 'source_defined_calmodulin_state',
     'CaMCa': 'calcium_mca',
     'MCIP': 'source_defined_mcip_state',
     'MCIPp': 'mcipp',
     'MCIPpp': 'mcippp',
     'Comp1': 'source_defined_comp1_state',
     'Comp2': 'source_defined_comp2_state',
     'Comp3': 'source_defined_comp3_state',
     'P1433': 'abstract_source_state_p1433',
     'MCIP_BMK1': 'mcip_bmk1',
     'MCIPp_CaNc_star': 'mcipp_calcium_nc_star',
     'MCIPp_GSK3betac': 'mcipp_gsk3betac',
     'MCIPpp_CaNc_star': 'mcippp_calcium_nc_star',
     'NFATpc_CaNc_star': 'nfatpc_calcium_nc_star',
     'NFATc_GSK3betac': 'nfatc_gsk3betac',
     'NFATpn_CaNn_star': 'nfatpn_calcium_nn_star',
     'NFATn_GSK3betan': 'nfatn_gsk3betan'}
    _SPECIES_LABELS = {'BMK1': 'Source Defined BMK1 State',
     'MRNA': 'Source Defined MRNA State',
     'NFATc': 'Nfatc',
     'NFATn': 'Nfatn',
     'NFATpc': 'Nfatpc',
     'NFATpn': 'Nfatpn',
     'GSK3betac': 'Gsk3betac',
     'GSK3betan': 'Gsk3betan',
     'CaNc': 'Source Defined CANC State',
     'CaNc_star': 'Calcium Nc Star',
     'CaNn_star': 'Calcium Nn Star',
     'CaNn': 'Source Defined CANN State',
     'CaM': 'Source Defined Calmodulin State',
     'CaMCa': 'Calcium Mca',
     'MCIP': 'Source Defined MCIP State',
     'MCIPp': 'Mcipp',
     'MCIPpp': 'Mcippp',
     'Comp1': 'Source Defined COMP1 State',
     'Comp2': 'Source Defined COMP2 State',
     'Comp3': 'Source Defined COMP3 State',
     'P1433': 'Abstract Source State P1433',
     'MCIP_BMK1': 'MCIP BMK1',
     'MCIPp_CaNc_star': 'Mcipp Calcium Nc Star',
     'MCIPp_GSK3betac': 'Mcipp Gsk3betac',
     'MCIPpp_CaNc_star': 'Mcippp Calcium Nc Star',
     'NFATpc_CaNc_star': 'Nfatpc Calcium Nc Star',
     'NFATc_GSK3betac': 'Nfatc Gsk3betac',
     'NFATpn_CaNn_star': 'Nfatpn Calcium Nn Star',
     'NFATn_GSK3betan': 'Nfatn Gsk3betan'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_bmk1_state': ('BMK1',
                                           0.0,
                                           'native SBML value',
                                           'Initial level of source-defined BMK1 state. Maps to SBML '
                                           'symbol `BMK1`; exposed as a traceable initial-condition '
                                           'perturbation.')}
    _HEADLINE_OUTPUTS = {'nfatc': ('NFATc',
               'native SBML value',
               'Nfatc. Maps to SBML symbol `NFATc` and is emitted in native SBML units.'),
     'nfatn': ('NFATn',
               'native SBML value',
               'Nfatn. Maps to SBML symbol `NFATn` and is emitted in native SBML units.'),
     'nfatpc': ('NFATpc',
                'native SBML value',
                'Nfatpc. Maps to SBML symbol `NFATpc` and is emitted in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL1172425728.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cui2008CardiacmyocytesModel1172425728Model = Cui2008CardiacmyocytesModel
