# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Martinez-Guimera2017 - Generic redox signalling model without negative regulation (Model 1)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class MartinezGuimera2017GenericRedoxSignallingMoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1710260000'
    _TITLE = 'Martinez-Guimera2017 - Generic redox signalling model without negative regulation (Model 1)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'oxidant': ('Oxidant',
                 'native SBML value',
                 'Oxidant. Maps to SBML symbol `Oxidant` and is emitted in native SBML units.'),
     'source_defined_aox_state': ('AOX',
                                  'native SBML value',
                                  'source-defined AOX state. Maps to SBML symbol `AOX` and is emitted '
                                  'in native SBML units.'),
     'nil_source_state': ('Nil',
                          'native SBML value',
                          'nil source state. Maps to SBML symbol `Nil` and is emitted in native SBML '
                          'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_inhibitor': ('Inhibitor',
                           0.0,
                           'native SBML value',
                           'Initial level of Inhibitor. Maps to SBML symbol `Inhibitor`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Oxidant': 'Oxidant',
     'AOX': 'source-defined AOX state',
     'Nil': 'nil source state',
     'Activator': 'Activator',
     'Sensor': 'Sensor',
     'SensorOX': 'Sensor OX',
     'Function': 'Function',
     'Relay': 'Relay',
     'Intermediate': 'Intermediate',
     'Reductant': 'Reductant',
     'Inhibitor': 'Inhibitor',
     'ReductantOX': 'Reductant OX'}
    _STATE_OUTPUT_ALIASES = {'Oxidant': 'oxidant',
     'AOX': 'source_defined_aox_state',
     'Nil': 'nil_source_state',
     'Activator': 'activator',
     'Sensor': 'sensor',
     'SensorOX': 'sensor_ox',
     'Function': 'function',
     'Relay': 'relay',
     'Intermediate': 'intermediate',
     'Reductant': 'reductant',
     'Inhibitor': 'inhibitor',
     'ReductantOX': 'reductant_ox'}

    def __init__(self, model_path: str = 'data/MODEL1710260000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


MartinezGuimera2017GenericRedoxSignallingMoModel1710260000Model = MartinezGuimera2017GenericRedoxSignallingMoModel
