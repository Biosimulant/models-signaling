# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gray2016 - The Akt switch model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gray2016TheAktSwitchModelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000854'
    _TITLE = 'Gray2016 - The Akt switch model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_ac_state': ('Ac',
                                 'native SBML value',
                                 'source-defined AC state. Maps to SBML symbol `Ac` and is emitted in '
                                 'native SBML units.'),
     'source_defined_pc_state': ('Pc',
                                 'native SBML value',
                                 'source-defined PC state. Maps to SBML symbol `Pc` and is emitted in '
                                 'native SBML units.'),
     'source_defined_ap_state': ('Ap',
                                 'native SBML value',
                                 'source-defined AP state. Maps to SBML symbol `Ap` and is emitted in '
                                 'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_ac_state': ('Ac',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined AC state. Maps to SBML '
                                         'symbol `Ac`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Ac': 'source-defined AC state',
     'Pc': 'source-defined PC state',
     'Ap': 'source-defined AP state',
     'Pp': 'source-defined PP state'}
    _STATE_OUTPUT_ALIASES = {'Ac': 'source_defined_ac_state',
     'Pc': 'source_defined_pc_state',
     'Ap': 'source_defined_ap_state',
     'Pp': 'source_defined_pp_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000854.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gray2016TheAktSwitchModelBiomd0000000854Model = Gray2016TheAktSwitchModelModel
