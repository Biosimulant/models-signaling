# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Iribe2006_CaMKIIkineticsModel."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Iribe2006CamkiikineticsmodelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1006230085'
    _TITLE = 'Iribe2006_CaMKIIkineticsModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'V_membrane_potential': 'v_membrane_potential',
     'm': 'source_defined_m_state',
     'h': 'source_defined_h_state',
     'x': 'response_node_x',
     's': 'source_defined_s_state',
     'r': 'source_defined_r_state',
     'd': 'source_defined_d_state',
     'f': 'source_defined_f_state',
     'F_CaMK': 'f_calcium_map_kinase',
     'F_1': 'source_defined_f_1_state',
     'F_2': 'source_defined_f_2_state',
     'F_SRCa_RyR': 'f_srca_ry_r',
     'Cmdn_Ca': 'cmdn_calcium',
     'Trpn_Ca': 'trpn_calcium',
     'Ca_i': 'intracellular_calcium',
     'Ca_SR': 'source_defined_calcium_sr_state',
     'Na_i': 'source_defined_na_i_state',
     'K_i': 'source_defined_k_i_state',
     'N_0': 'source_defined_n_0_state',
     'P_0': 'source_defined_p_0_state',
     'P_1': 'source_defined_p_1_state',
     'P_2': 'source_defined_p_2_state',
     'P_3': 'source_defined_p_3_state'}
    _SPECIES_LABELS = {'V_membrane_potential': 'V Membrane Potential',
     'm': 'Source Defined M State',
     'h': 'Source Defined H State',
     'x': 'Response Node X',
     's': 'Source Defined S State',
     'r': 'Source Defined R State',
     'd': 'Source Defined D State',
     'f': 'Source Defined F State',
     'F_CaMK': 'F Calcium MAP Kinase',
     'F_1': 'Source Defined F 1 State',
     'F_2': 'Source Defined F 2 State',
     'F_SRCa_RyR': 'F Srca Ry R',
     'Cmdn_Ca': 'Cmdn Calcium',
     'Trpn_Ca': 'Trpn Calcium',
     'Ca_i': 'Intracellular Calcium',
     'Ca_SR': 'Source Defined Calcium SR State',
     'Na_i': 'Source Defined NA I State',
     'K_i': 'Source Defined K I State',
     'N_0': 'Source Defined N 0 State',
     'P_0': 'Source Defined P 0 State',
     'P_1': 'Source Defined P 1 State',
     'P_2': 'Source Defined P 2 State',
     'P_3': 'Source Defined P 3 State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane_potential': ('V_membrane_potential',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of V Membrane Potential. Maps to SBML symbol '
                                      '`V_membrane_potential`; exposed as a traceable '
                                      'initial-condition perturbation.')}
    _HEADLINE_OUTPUTS = {'f_calcium_map_kinase': ('F_CaMK',
                              'native SBML value',
                              'F calcium MAP kinase. Maps to SBML symbol `F_CaMK` and is emitted in '
                              'native SBML units.'),
     'f_srca_ry_r': ('F_SRCa_RyR',
                     'native SBML value',
                     'F Srca Ry R. Maps to SBML symbol `F_SRCa_RyR` and is emitted in native SBML '
                     'units.'),
     'cmdn_calcium': ('Cmdn_Ca',
                      'native SBML value',
                      'Cmdn calcium. Maps to SBML symbol `Cmdn_Ca` and is emitted in native SBML '
                      'units.')}

    def __init__(self, model_path: str = 'data/MODEL1006230085.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Iribe2006CamkiikineticsmodelModel1006230085Model = Iribe2006CamkiikineticsmodelModel
