# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Xu2005BloodCoagulationModelOfActivatedFactModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1806130002'
    _TITLE = 'Xu2005 - Blood Coagulation Model of Activated Factors of Extrinsic Pathway and TFPI'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
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
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_x1_state': ('x1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X1 state. Maps to SBML '
                                         'symbol `x1`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_source_defined_x2_state': ('x2',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X2 state. Maps to SBML '
                                         'symbol `x2`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_source_defined_x3_state': ('x3',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X3 state. Maps to SBML '
                                         'symbol `x3`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x1': 'source-defined X1 state',
     'x2': 'source-defined X2 state',
     'x3': 'source-defined X3 state',
     'x4': 'source-defined X4 state',
     'x5': 'source-defined X5 state',
     'x6': 'source-defined X6 state',
     'x7': 'source-defined X7 state'}
    _STATE_OUTPUT_ALIASES = {'x1': 'source_defined_x1_state',
     'x2': 'source_defined_x2_state',
     'x3': 'source_defined_x3_state',
     'x4': 'source_defined_x4_state',
     'x5': 'source_defined_x5_state',
     'x6': 'source_defined_x6_state',
     'x7': 'source_defined_x7_state'}

    def __init__(self, model_path: str = 'data/MODEL1806130002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Xu2005BloodCoagulationModelOfActivatedFactModel1806130002Model = Xu2005BloodCoagulationModelOfActivatedFactModel
