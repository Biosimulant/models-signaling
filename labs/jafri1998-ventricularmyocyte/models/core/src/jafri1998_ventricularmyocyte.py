# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jafri1998_VentricularMyocyte."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jafri1998VentricularmyocyteModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL0847869198'
    _TITLE = 'Jafri1998_VentricularMyocyte'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'V_membrane': 'v_membrane',
     'm': 'source_defined_m_state',
     'h': 'source_defined_h_state',
     'j': 'source_defined_j_state',
     'C0': 'source_defined_c0_state',
     'C1': 'source_defined_c1_state',
     'C2': 'source_defined_c2_state',
     'C3': 'complement_complement_complement_complement_complement_complement_c3',
     'C4': 'source_defined_c4_state',
     'O': 'source_defined_o_state',
     'C_Ca0': 'source_defined_c_ca0_state',
     'C_Ca1': 'source_defined_c_ca1_state',
     'C_Ca2': 'source_defined_c_ca2_state',
     'C_Ca3': 'source_defined_c_ca3_state',
     'C_Ca4': 'source_defined_c_ca4_state',
     'O_Ca': 'source_defined_o_calcium_state',
     'y': 'source_defined_y_state',
     'X': 'response_node_x',
     'P_C1': 'source_defined_p_c1_state',
     'P_O1': 'source_defined_p_o1_state',
     'P_O2': 'source_defined_p_o2_state',
     'P_C2': 'source_defined_p_c2_state',
     'HTRPNCa': 'htrpnca',
     'LTRPNCa': 'ltrpnca',
     'Cai': 'intracellular_calcium',
     'Ca_SS': 'source_defined_calcium_ss_state',
     'Ca_JSR': 'calcium_jsr',
     'Ca_NSR': 'calcium_nsr',
     'Nai': 'source_defined_nai_state',
     'Ki': 'source_defined_ki_state',
     'Ko': 'source_defined_ko_state'}
    _SPECIES_LABELS = {'V_membrane': 'V Membrane',
     'm': 'Source Defined M State',
     'h': 'Source Defined H State',
     'j': 'Source Defined J State',
     'C0': 'Source Defined C0 State',
     'C1': 'Source Defined C1 State',
     'C2': 'Source Defined C2 State',
     'C3': 'Complement Complement Complement Complement Complement complement C3',
     'C4': 'Source Defined C4 State',
     'O': 'Source Defined O State',
     'C_Ca0': 'Source Defined C CA0 State',
     'C_Ca1': 'Source Defined C CA1 State',
     'C_Ca2': 'Source Defined C CA2 State',
     'C_Ca3': 'Source Defined C CA3 State',
     'C_Ca4': 'Source Defined C CA4 State',
     'O_Ca': 'Source Defined O Calcium State',
     'y': 'Source Defined Y State',
     'X': 'Response Node X',
     'P_C1': 'Source Defined P C1 State',
     'P_O1': 'Source Defined P O1 State',
     'P_O2': 'Source Defined P O2 State',
     'P_C2': 'Source Defined P C2 State',
     'HTRPNCa': 'Htrpnca',
     'LTRPNCa': 'Ltrpnca',
     'Cai': 'Intracellular Calcium',
     'Ca_SS': 'Source Defined Calcium SS State',
     'Ca_JSR': 'Calcium JSR',
     'Ca_NSR': 'Calcium NSR',
     'Nai': 'Source Defined NAI State',
     'Ki': 'Source Defined KI State',
     'Ko': 'Source Defined KO State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_v_membrane': ('V_membrane',
                            0.0,
                            'native SBML value',
                            'Initial level of V Membrane. Maps to SBML symbol `V_membrane`; exposed as '
                            'a traceable initial-condition perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_c_ca0_state': ('C_Ca0',
                                    'native SBML value',
                                    'source-defined C_CA0 state. Maps to SBML symbol `C_Ca0` and is '
                                    'emitted in native SBML units.'),
     'source_defined_c_ca1_state': ('C_Ca1',
                                    'native SBML value',
                                    'source-defined C_CA1 state. Maps to SBML symbol `C_Ca1` and is '
                                    'emitted in native SBML units.'),
     'source_defined_c_ca2_state': ('C_Ca2',
                                    'native SBML value',
                                    'source-defined C_CA2 state. Maps to SBML symbol `C_Ca2` and is '
                                    'emitted in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL0847869198.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Jafri1998VentricularmyocyteModel0847869198Model = Jafri1998VentricularmyocyteModel
