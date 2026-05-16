# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lemon2003_Ca2Dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lemon2003Ca2dynamicsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1006230039'
    _TITLE = 'Lemon2003_Ca2Dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'RS': 'source_defined_rs_state',
     'RS_p': 'source_defined_rs_p_state',
     'G': 'source_defined_g_state',
     'IP_3': 'ip3',
     'PIP_2': 'source_defined_pip_2_state',
     'C': 'source_defined_c_state',
     'h': 'source_defined_h_state'}
    _SPECIES_LABELS = {'RS': 'Source Defined RS State',
     'RS_p': 'Source Defined RS P State',
     'G': 'Source Defined G State',
     'IP_3': 'IP3',
     'PIP_2': 'Source Defined PIP 2 State',
     'C': 'Source Defined C State',
     'h': 'Source Defined H State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_rs_state': ('RS',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined RS state. Maps to SBML '
                                         'symbol `RS`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_rs_p_state': ('RS_p',
                                   'native SBML value',
                                   'source-defined RS_P state. Maps to SBML symbol `RS_p` and is '
                                   'emitted in native SBML units.'),
     'ip3': ('IP_3',
             'native SBML value',
             'IP3. Maps to SBML symbol `IP_3` and is emitted in native SBML units.'),
     'source_defined_pip_2_state': ('PIP_2',
                                    'native SBML value',
                                    'source-defined PIP_2 state. Maps to SBML symbol `PIP_2` and is '
                                    'emitted in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL1006230039.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Lemon2003Ca2dynamicsModel1006230039Model = Lemon2003Ca2dynamicsModel
