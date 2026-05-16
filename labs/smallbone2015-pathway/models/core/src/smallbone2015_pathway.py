# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Smallbone2015 - pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2015PathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1503180003'
    _TITLE = 'Smallbone2015 - pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_x0_state': ('X0',
                                 'native SBML value',
                                 'Source Defined X0 State. Maps to SBML symbol `X0` and is emitted in '
                                 'native SBML units.'),
     'source_defined_x1_state': ('X1',
                                 'native SBML value',
                                 'Source Defined X1 State. Maps to SBML symbol `X1` and is emitted in '
                                 'native SBML units.'),
     'source_defined_x2_state': ('X2',
                                 'native SBML value',
                                 'Source Defined X2 State. Maps to SBML symbol `X2` and is emitted in '
                                 'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_x0_state': ('X0',
                                         1.0,
                                         'native SBML value',
                                         'Initial level of source-defined X0 state. Maps to SBML '
                                         'symbol `X0`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_source_defined_x4_state': ('X4',
                                         1.0,
                                         'native SBML value',
                                         'Initial level of source-defined X4 state. Maps to SBML '
                                         'symbol `X4`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'X0': 'Source Defined X0 State',
     'X1': 'Source Defined X1 State',
     'X2': 'Source Defined X2 State',
     'X3': 'Source Defined X3 State',
     'X4': 'Source Defined X4 State'}
    _STATE_OUTPUT_ALIASES = {'X0': 'source_defined_x0_state',
     'X1': 'source_defined_x1_state',
     'X2': 'source_defined_x2_state',
     'X3': 'source_defined_x3_state',
     'X4': 'source_defined_x4_state'}

    def __init__(self, model_path: str = 'data/MODEL1503180003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smallbone2015PathwayModel1503180003Model = Smallbone2015PathwayModel
