# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nakakuki2010_CellFateDecision_Mechanistic."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nakakuki2010CellfatedecisionMechanisticModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000250'
    _TITLE = 'Nakakuki2010_CellFateDecision_Mechanistic'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytosolic_phosphorylated_erk': ('ERK_c',
                                      'native SBML value',
                                      'cytosolic phosphorylated ERK. Maps to SBML symbol `ERK_c` and '
                                      'is emitted in native SBML units.'),
     'p_erk_c': ('pERK_c',
                 'native SBML value',
                 'P ERK C. Maps to SBML symbol `pERK_c` and is emitted in native SBML units.'),
     'pp_erk_c': ('ppERK_c',
                  'native SBML value',
                  'Pp ERK C. Maps to SBML symbol `ppERK_c` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_egf': ('EGF',
                     0.0,
                     'native SBML value',
                     'Initial level of EGF. Maps to SBML symbol `EGF`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_heregulin': ('HRG',
                           10.0,
                           'native SBML value',
                           'Initial level of heregulin. Maps to SBML symbol `HRG`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EGF': 'EGF',
     'HRG': 'heregulin',
     'A1': 'source-defined A1 state',
     'A1_2': 'A1 2',
     'A2': 'source-defined A2 state',
     'A2_2': 'A2 2',
     'A3': 'source-defined A3 state',
     'A3_2': 'A3 2',
     'DUSPmRNA': 'Duspm RNA',
     'ERK_c': 'cytosolic phosphorylated ERK',
     'pERK_c': 'P ERK C',
     'ppERK_c': 'Pp ERK C',
     'F': 'source-defined F state',
     'c_FOS_c': 'C FOS C',
     'pc_FOS_c': 'Pc FOS C',
     'c_FOSmRNA': 'C Fosm RNA',
     'FmRNA': 'Fm RNA',
     'Kin': 'source-defined KIN state',
     'Kin_2': 'source-defined KIN_2 state',
     'pMEK': 'source-defined PMEK state',
     'MEK': 'MEK',
     'DUSP_c': 'DUSP C',
     'pDUSP_c': 'P DUSP C',
     'RSK_c': 'source-defined RSK_C state',
     'pRSK_c': 'P RSK C',
     'RsD': 'source-defined RSD state',
     'RsT': 'source-defined RST state',
     'CREB_n': 'CREB N',
     'pCREB_n': 'P CREB N',
     'ERK_n': 'nuclear phosphorylated ERK',
     'pERK_n': 'P ERK N',
     'ppERK_n': 'Pp ERK N',
     'Elk1_n': 'Elk1 N',
     'pElk1_n': 'P Elk1 N',
     'FOSn': 'source-defined FOSN state',
     'FOSn_2': 'source-defined FOSN_2 state',
     'Fn': 'source-defined FN state',
     'DUSP_n': 'DUSP N',
     'pDUSP_n': 'P DUSP N',
     'pDUSP_n_ERK_n': 'P DUSP N ERK N',
     'pDUSP_n_pERK_n': 'P DUSP N P ERK N',
     'pDUSP_n_ppERK_n': 'P DUSP N Pp ERK N',
     'DUSP_n_ERK_n': 'DUSP N ERK N',
     'DUSP_n_pERK_n': 'DUSP N P ERK N',
     'DUSP_n_ppERK_n': 'DUSP N Pp ERK N',
     'PreDUSPmRNA': 'Pre Duspm RNA',
     'PreFOSmRNA': 'Pre Fosm RNA',
     'PreFmRNA': 'Pre Fm RNA',
     'pRSK_n': 'P RSK N'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'egf',
     'HRG': 'heregulin',
     'A1': 'source_defined_a1_state',
     'A1_2': 'a1_2',
     'A2': 'source_defined_a2_state',
     'A2_2': 'a2_2',
     'A3': 'source_defined_a3_state',
     'A3_2': 'a3_2',
     'DUSPmRNA': 'duspm_rna',
     'ERK_c': 'cytosolic_phosphorylated_erk',
     'pERK_c': 'p_erk_c',
     'ppERK_c': 'pp_erk_c',
     'F': 'source_defined_f_state',
     'c_FOS_c': 'c_fos_c',
     'pc_FOS_c': 'pc_fos_c',
     'c_FOSmRNA': 'c_fosm_rna',
     'FmRNA': 'fm_rna',
     'Kin': 'source_defined_kin_state',
     'Kin_2': 'source_defined_kin_2_state',
     'pMEK': 'source_defined_pmek_state',
     'MEK': 'mek',
     'DUSP_c': 'dusp_c',
     'pDUSP_c': 'p_dusp_c',
     'RSK_c': 'source_defined_rsk_c_state',
     'pRSK_c': 'p_rsk_c',
     'RsD': 'source_defined_rsd_state',
     'RsT': 'source_defined_rst_state',
     'CREB_n': 'creb_n',
     'pCREB_n': 'p_creb_n',
     'ERK_n': 'nuclear_phosphorylated_erk',
     'pERK_n': 'p_erk_n',
     'ppERK_n': 'pp_erk_n',
     'Elk1_n': 'elk1_n',
     'pElk1_n': 'p_elk1_n',
     'FOSn': 'source_defined_fosn_state',
     'FOSn_2': 'source_defined_fosn_2_state',
     'Fn': 'source_defined_fn_state',
     'DUSP_n': 'dusp_n',
     'pDUSP_n': 'p_dusp_n',
     'pDUSP_n_ERK_n': 'p_dusp_n_erk_n',
     'pDUSP_n_pERK_n': 'p_dusp_n_p_erk_n',
     'pDUSP_n_ppERK_n': 'p_dusp_n_pp_erk_n',
     'DUSP_n_ERK_n': 'dusp_n_erk_n',
     'DUSP_n_pERK_n': 'dusp_n_p_erk_n',
     'DUSP_n_ppERK_n': 'dusp_n_pp_erk_n',
     'PreDUSPmRNA': 'pre_duspm_rna',
     'PreFOSmRNA': 'pre_fosm_rna',
     'PreFmRNA': 'pre_fm_rna',
     'pRSK_n': 'p_rsk_n'}

    def __init__(self, model_path: str = 'data/BIOMD0000000250.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Nakakuki2010CellfatedecisionMechanisticBiomd0000000250Model = Nakakuki2010CellfatedecisionMechanisticModel
