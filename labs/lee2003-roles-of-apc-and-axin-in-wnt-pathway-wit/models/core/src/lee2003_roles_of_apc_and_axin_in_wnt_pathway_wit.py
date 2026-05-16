# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lee2003 - Roles of APC and Axin in Wnt Pathway (without regulatory loop)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2003RolesOfApcAndAxinInWntPathwayWitModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000658'
    _TITLE = 'Lee2003 - Roles of APC and Axin in Wnt Pathway (without regulatory loop)'
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
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_w_state': ('W',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined W state. Maps to SBML symbol '
                                        '`W`; exposed as a traceable initial-condition perturbation.')}
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
     'W': 'source-defined W state'}
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
     'W': 'source_defined_w_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000658.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Lee2003RolesOfApcAndAxinInWntPathwayWitBiomd0000000658Model = Lee2003RolesOfApcAndAxinInWntPathwayWitModel
