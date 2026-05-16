# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Maurya2005_GTPaseCycle_reducedOrder."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Maurya2005GtpasecycleReducedorderModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000085'
    _TITLE = 'Maurya2005_GTPaseCycle_reducedOrder'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_g_t_state': ('species_5',
                                  'native SBML value',
                                  'source-defined G*T state. Maps to SBML symbol `species_5` and is '
                                  'emitted in native SBML units.'),
     'source_defined_rg_t_state': ('species_10',
                                   'native SBML value',
                                   'source-defined RG*T state. Maps to SBML symbol `species_10` and is '
                                   'emitted in native SBML units.'),
     'source_defined_g_at_state': ('species_11',
                                   'native SBML value',
                                   'source-defined G*AT state. Maps to SBML symbol `species_11` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_a_state': ('species_0',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined A state. Maps to SBML symbol '
                                        '`species_0`; exposed as a traceable initial-condition '
                                        'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_0': 'source-defined A state',
     'species_1': 'source-defined G state',
     'species_2': 'source-defined GA state',
     'species_3': 'source-defined T state',
     'species_4': 'source-defined R state',
     'species_5': 'source-defined G*T state',
     'species_6': 'source-defined GD state',
     'species_7': 'source-defined PI state',
     'species_8': 'source-defined D state',
     'species_9': 'source-defined RG state',
     'species_10': 'source-defined RG*T state',
     'species_11': 'source-defined G*AT state',
     'species_12': 'source-defined GAD state',
     'species_13': 'source-defined RGD state',
     'species_14': 'source-defined RGA state',
     'species_15': 'source-defined RG*AT state',
     'species_16': 'source-defined RGAD state'}
    _STATE_OUTPUT_ALIASES = {'species_0': 'source_defined_a_state',
     'species_1': 'source_defined_g_state',
     'species_2': 'source_defined_ga_state',
     'species_3': 'source_defined_t_state',
     'species_4': 'source_defined_r_state',
     'species_5': 'source_defined_g_t_state',
     'species_6': 'source_defined_gd_state',
     'species_7': 'source_defined_pi_state',
     'species_8': 'source_defined_d_state',
     'species_9': 'source_defined_rg_state',
     'species_10': 'source_defined_rg_t_state',
     'species_11': 'source_defined_g_at_state',
     'species_12': 'source_defined_gad_state',
     'species_13': 'source_defined_rgd_state',
     'species_14': 'source_defined_rga_state',
     'species_15': 'source_defined_rg_at_state',
     'species_16': 'source_defined_rgad_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000085.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Maurya2005GtpasecycleReducedorderBiomd0000000085Model = Maurya2005GtpasecycleReducedorderModel
