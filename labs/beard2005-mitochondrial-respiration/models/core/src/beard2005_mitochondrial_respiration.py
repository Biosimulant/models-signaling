# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Beard2005_Mitochondrial_Respiration."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Beard2005MitochondrialRespirationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL4151491057'
    _TITLE = 'Beard2005_Mitochondrial_Respiration'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'H_x': 'source_defined_h_x_state',
     'K_x': 'source_defined_k_x_state',
     'Mg_x': 'source_defined_mg_x_state',
     'NADH_x': 'nadh_x',
     'QH2': 'source_defined_qh2_state',
     'Cred': 'source_defined_cred_state',
     'ATP_x': 'source_defined_atp_x_state',
     'ADP_x': 'source_defined_adp_x_state',
     'ATP_mx': 'atp_mx',
     'ADP_mx': 'adp_mx',
     'Pi_x': 'source_defined_pi_x_state',
     'ATP_i': 'intracellular_atp',
     'ADP_i': 'intracellular_adp',
     'AMP_i': 'source_defined_amp_i_state',
     'ATP_mi': 'atp_mi',
     'ADP_mi': 'adp_mi',
     'Pi_i': 'source_defined_pi_i_state',
     'dPsi': 'source_defined_dpsi_state',
     'O2': 'source_defined_o2_state'}
    _SPECIES_LABELS = {'H_x': 'Source Defined H X State',
     'K_x': 'Source Defined K X State',
     'Mg_x': 'Source Defined MG X State',
     'NADH_x': 'NADH X',
     'QH2': 'Source Defined QH2 State',
     'Cred': 'Source Defined CRED State',
     'ATP_x': 'Source Defined ATP X State',
     'ADP_x': 'Source Defined ADP X State',
     'ATP_mx': 'ATP Mx',
     'ADP_mx': 'ADP Mx',
     'Pi_x': 'Source Defined PI X State',
     'ATP_i': 'Intracellular ATP',
     'ADP_i': 'Intracellular ADP',
     'AMP_i': 'Source Defined AMP I State',
     'ATP_mi': 'ATP Mi',
     'ADP_mi': 'ADP Mi',
     'Pi_i': 'Source Defined PI I State',
     'dPsi': 'Source Defined DPSI State',
     'O2': 'Source Defined O2 State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_h_x_state': ('H_x',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined H_X state. Maps to SBML '
                                          'symbol `H_x`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_h_x_state': ('H_x',
                                  'native SBML value',
                                  'source-defined H_X state. Maps to SBML symbol `H_x` and is emitted '
                                  'in native SBML units.'),
     'source_defined_k_x_state': ('K_x',
                                  'native SBML value',
                                  'source-defined K_X state. Maps to SBML symbol `K_x` and is emitted '
                                  'in native SBML units.'),
     'source_defined_mg_x_state': ('Mg_x',
                                   'native SBML value',
                                   'source-defined MG_X state. Maps to SBML symbol `Mg_x` and is '
                                   'emitted in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL4151491057.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Beard2005MitochondrialRespirationModel4151491057Model = Beard2005MitochondrialRespirationModel
