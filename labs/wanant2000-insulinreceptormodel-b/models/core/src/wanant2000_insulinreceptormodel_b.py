# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wanant2000_InsulinReceptorModel_B."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wanant2000InsulinreceptormodelBModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1201140006'
    _TITLE = 'Wanant2000_InsulinReceptorModel_B'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'x1': 'source_defined_x1_state',
     'x2': 'source_defined_x2_state',
     'x3': 'source_defined_x3_state',
     'x4': 'source_defined_x4_state',
     'x5': 'source_defined_x5_state',
     'x6': 'source_defined_x6_state',
     'x7': 'source_defined_x7_state',
     'x8': 'source_defined_x8_state',
     'x9': 'source_defined_x9_state'}
    _SPECIES_LABELS = {'x1': 'Source Defined X1 State',
     'x2': 'Source Defined X2 State',
     'x3': 'Source Defined X3 State',
     'x4': 'Source Defined X4 State',
     'x5': 'Source Defined X5 State',
     'x6': 'Source Defined X6 State',
     'x7': 'Source Defined X7 State',
     'x8': 'Source Defined X8 State',
     'x9': 'Source Defined X9 State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_x1_state': ('x1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X1 state. Maps to SBML '
                                         'symbol `x1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_x1_state': ('x1',
                                 'native SBML value',
                                 'source-defined X1 state. Maps to SBML symbol `x1` and is emitted in '
                                 'native SBML units.'),
     'source_defined_x2_state': ('x2',
                                 'native SBML value',
                                 'source-defined X2 state. Maps to SBML symbol `x2` and is emitted in '
                                 'native SBML units.'),
     'source_defined_x3_state': ('x3',
                                 'native SBML value',
                                 'source-defined X3 state. Maps to SBML symbol `x3` and is emitted in '
                                 'native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL1201140006.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Wanant2000InsulinreceptormodelBModel1201140006Model = Wanant2000InsulinreceptormodelBModel
