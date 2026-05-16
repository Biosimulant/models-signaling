# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Pokhilko2013 - TOC1 signalling in Arabidopsis circadian clock."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pokhilko2013Toc1SignallingInArabidopsisCircModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000445'
    _TITLE = 'Pokhilko2013 - TOC1 signalling in Arabidopsis circadian clock'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'c_abar_m': ('species_1',
                  'native SBML value',
                  'C ABAR M. Maps to SBML symbol `species_1` and is emitted in native SBML units.'),
     'c_pp2c': ('species_2',
                'native SBML value',
                'C PP2C. Maps to SBML symbol `species_2` and is emitted in native SBML units.'),
     'c_sn_rk2': ('species_3',
                  'native SBML value',
                  'C Sn RK2. Maps to SBML symbol `species_3` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_c_abar_m': ('species_1',
                          0.999999951844376,
                          'native SBML value',
                          'Initial level of C ABAR M. Maps to SBML symbol `species_1`; exposed as a '
                          'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'C ABAR M',
     'species_2': 'C PP2C',
     'species_3': 'C Sn RK2',
     'species_4': 'source-defined CS state',
     'cCOP1c': 'C Cop1c',
     'cCOP1d': 'C Cop1d',
     'cCOP1n': 'C Cop1n',
     'cE3': 'source-defined CE3 state',
     'cE3_m': 'C E3 M',
     'cE3n': 'C E3n',
     'cE4': 'source-defined CE4 state',
     'cE4_m': 'C E4 M',
     'cEC': 'source-defined CEC state',
     'cEG': 'source-defined CEG state',
     'cG': 'source-defined CG state',
     'cG_m': 'source-defined CG_M state',
     'cL': 'source-defined CL state',
     'cLUX': 'source-defined CLUX state',
     'cLUX_m': 'C LUX M',
     'cL_m': 'source-defined CL_M state',
     'cLm': 'source-defined CLM state',
     'cNI': 'source-defined CNI state',
     'cNI_m': 'source-defined CNI_M state',
     'cP': 'source-defined CP state',
     'cP7': 'source-defined CP7 state',
     'cP7_m': 'C P7 M',
     'cP9': 'source-defined CP9 state',
     'cP9_m': 'C P9 M',
     'cT': 'source-defined CT state',
     'cT_m': 'source-defined CT_M state',
     'cZG': 'source-defined CZG state',
     'cZTL': 'source-defined CZTL state'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'c_abar_m',
     'species_2': 'c_pp2c',
     'species_3': 'c_sn_rk2',
     'species_4': 'source_defined_cs_state',
     'cCOP1c': 'c_cop1c',
     'cCOP1d': 'c_cop1d',
     'cCOP1n': 'c_cop1n',
     'cE3': 'source_defined_ce3_state',
     'cE3_m': 'c_e3_m',
     'cE3n': 'c_e3n',
     'cE4': 'source_defined_ce4_state',
     'cE4_m': 'c_e4_m',
     'cEC': 'source_defined_cec_state',
     'cEG': 'source_defined_ceg_state',
     'cG': 'source_defined_cg_state',
     'cG_m': 'source_defined_cg_m_state',
     'cL': 'source_defined_cl_state',
     'cLUX': 'source_defined_clux_state',
     'cLUX_m': 'c_lux_m',
     'cL_m': 'source_defined_cl_m_state',
     'cLm': 'source_defined_clm_state',
     'cNI': 'source_defined_cni_state',
     'cNI_m': 'source_defined_cni_m_state',
     'cP': 'source_defined_cp_state',
     'cP7': 'source_defined_cp7_state',
     'cP7_m': 'c_p7_m',
     'cP9': 'source_defined_cp9_state',
     'cP9_m': 'c_p9_m',
     'cT': 'source_defined_ct_state',
     'cT_m': 'source_defined_ct_m_state',
     'cZG': 'source_defined_czg_state',
     'cZTL': 'source_defined_cztl_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000445.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Pokhilko2013Toc1SignallingInArabidopsisCircBiomd0000000445Model = Pokhilko2013Toc1SignallingInArabidopsisCircModel
