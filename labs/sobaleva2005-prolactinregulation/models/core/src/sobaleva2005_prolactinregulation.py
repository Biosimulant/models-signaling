# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sobaleva2005_ProlactinRegulation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sobaleva2005ProlactinregulationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL7896869925'
    _TITLE = 'Sobaleva2005_ProlactinRegulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'R': 'source_defined_r_state',
     'U': 'source_defined_u_state',
     'B1': 'source_defined_b1_state',
     'B2': 'source_defined_b2_state',
     'x': 'response_node_x'}
    _SPECIES_LABELS = {'R': 'Source Defined R State',
     'U': 'Source Defined U State',
     'B1': 'Source Defined B1 State',
     'B2': 'Source Defined B2 State',
     'x': 'Response Node X'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_r_state': ('R',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined R state. Maps to SBML symbol '
                                        '`R`; exposed as a traceable initial-condition perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_r_state': ('R',
                                'native SBML value',
                                'source-defined R state. Maps to SBML symbol `R` and is emitted in '
                                'native SBML units.'),
     'source_defined_u_state': ('U',
                                'native SBML value',
                                'source-defined U state. Maps to SBML symbol `U` and is emitted in '
                                'native SBML units.'),
     'source_defined_b1_state': ('B1',
                                 'native SBML value',
                                 'source-defined B1 state. Maps to SBML symbol `B1` and is emitted in '
                                 'native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL7896869925.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sobaleva2005ProlactinregulationModel7896869925Model = Sobaleva2005ProlactinregulationModel
