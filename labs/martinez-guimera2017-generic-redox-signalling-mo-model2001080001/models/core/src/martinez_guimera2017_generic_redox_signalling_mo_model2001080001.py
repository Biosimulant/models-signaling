# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Martinez-Guimera2017 - Generic redox signalling model with negative feedback regulation (Model 2)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class MartinezGuimera2017GenericRedoxSignallingMoModel2001080001Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2001080001'
    _TITLE = 'Martinez-Guimera2017 - Generic redox signalling model with negative feedback regulation (Model 2)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'inactive': ('Inactive',
                  'native SBML value',
                  'Inactive. Maps to SBML symbol `Inactive` and is emitted in native SBML units.'),
     'oxidant': ('Oxidant',
                 'native SBML value',
                 'Oxidant. Maps to SBML symbol `Oxidant` and is emitted in native SBML units.'),
     'source_defined_aox_state': ('AOX',
                                  'native SBML value',
                                  'source-defined AOX state. Maps to SBML symbol `AOX` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_inhibitor': ('Inhibitor',
                           0.0,
                           'native SBML value',
                           'Initial level of Inhibitor. Maps to SBML symbol `Inhibitor`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Oxidant': 'Oxidant',
     'AOX': 'source-defined AOX state',
     'Activator': 'Activator',
     'Sensor': 'Sensor',
     'SensorOX': 'Sensor OX',
     'Function': 'Function',
     'Relay': 'Relay',
     'Intermediate': 'Intermediate',
     'Reductant': 'Reductant',
     'Inhibitor': 'Inhibitor',
     'ReductantOX': 'Reductant OX',
     'NegReg': 'Neg Reg',
     'Relay2': 'Relay2',
     'Inactive': 'Inactive'}
    _STATE_OUTPUT_ALIASES = {'Oxidant': 'oxidant',
     'AOX': 'source_defined_aox_state',
     'Activator': 'activator',
     'Sensor': 'sensor',
     'SensorOX': 'sensor_ox',
     'Function': 'function',
     'Relay': 'relay',
     'Intermediate': 'intermediate',
     'Reductant': 'reductant',
     'Inhibitor': 'inhibitor',
     'ReductantOX': 'reductant_ox',
     'NegReg': 'neg_reg',
     'Relay2': 'relay2',
     'Inactive': 'inactive'}

    def __init__(self, model_path: str = 'data/MODEL2001080001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


MartinezGuimera2017GenericRedoxSignallingMoModel2001080001Model = MartinezGuimera2017GenericRedoxSignallingMoModel2001080001Model
