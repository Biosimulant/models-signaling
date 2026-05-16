# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Araujo2016 - Positive feedback in Cdk1 signalling keeps mitotic duration short and constant."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Araujo2016PositiveFeedbackInCdk1SignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000657'
    _TITLE = 'Araujo2016 - Positive feedback in Cdk1 signalling keeps mitotic duration short and constant'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cdk1cyc_b': ('Cdk1CycB',
                   'native SBML value',
                   'Cdk1cyc B. Maps to SBML symbol `Cdk1CycB` and is emitted in native SBML units.'),
     'source_defined_apc_state': ('APC',
                                  'native SBML value',
                                  'source-defined APC state. Maps to SBML symbol `APC` and is emitted '
                                  'in native SBML units.'),
     'source_defined_cycb_state': ('CycB',
                                   'native SBML value',
                                   'source-defined CYCB state. Maps to SBML symbol `CycB` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cdk1cyc_b': ('Cdk1CycB',
                           0.0,
                           'native SBML value',
                           'Initial level of Cdk1cyc B. Maps to SBML symbol `Cdk1CycB`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Cdk1CycB': 'Cdk1cyc B', 'APC': 'source-defined APC state', 'CycB': 'source-defined CYCB state'}
    _STATE_OUTPUT_ALIASES = {'Cdk1CycB': 'cdk1cyc_b', 'APC': 'source_defined_apc_state', 'CycB': 'source_defined_cycb_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000657.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Araujo2016PositiveFeedbackInCdk1SignallingBiomd0000000657Model = Araujo2016PositiveFeedbackInCdk1SignallingModel
