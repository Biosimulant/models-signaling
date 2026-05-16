# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yao2016_Calcium_Signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yao2016CalciumSignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1611150001'
    _TITLE = 'Yao2016_Calcium_Signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'PLC': 'source_defined_plc_state', 'IP3': 'ip3', 'h': 'source_defined_h_state', 'ca': 'calcium'}
    _SPECIES_LABELS = {'PLC': 'Source Defined PLC State', 'IP3': 'IP3', 'h': 'Source Defined H State', 'ca': 'Calcium'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_plc_state': ('PLC',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined PLC state. Maps to SBML '
                                          'symbol `PLC`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _HEADLINE_OUTPUTS = {'calcium': ('ca',
                 'native SBML value',
                 'Calcium. Maps to SBML symbol `ca` and is emitted in native SBML units.'),
     'source_defined_plc_state': ('PLC',
                                  'native SBML value',
                                  'Source Defined PLC State. Maps to SBML symbol `PLC` and is emitted '
                                  'in native SBML units.'),
     'ip3': ('IP3',
             'native SBML value',
             'IP3. Maps to SBML symbol `IP3` and is emitted in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL1611150001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Yao2016CalciumSignalingModel1611150001Model = Yao2016CalciumSignalingModel
