# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Cookson2011_EnzymaticQueueingCoupling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cookson2011EnzymaticqueueingcouplingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000405'
    _TITLE = 'Cookson2011_EnzymaticQueueingCoupling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_e_x1_state': ('species_6',
                                   'native SBML value',
                                   'source-defined E+X1 state. Maps to SBML symbol `species_6` and is '
                                   'emitted in native SBML units.'),
     'source_defined_x1_state': ('species_1',
                                 'native SBML value',
                                 'source-defined X1 state. Maps to SBML symbol `species_1` and is '
                                 'emitted in native SBML units.'),
     'source_defined_x2_state': ('species_2',
                                 'native SBML value',
                                 'source-defined X2 state. Maps to SBML symbol `species_2` and is '
                                 'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_x1_state': ('species_1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X1 state. Maps to SBML '
                                         'symbol `species_1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'source-defined X1 state',
     'species_2': 'source-defined X2 state',
     'species_3': 'source-defined E1 state',
     'species_4': 'source-defined E2 state',
     'species_5': 'source-defined E state',
     'species_6': 'source-defined E+X1 state'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'source_defined_x1_state',
     'species_2': 'source_defined_x2_state',
     'species_3': 'source_defined_e1_state',
     'species_4': 'source_defined_e2_state',
     'species_5': 'source_defined_e_state',
     'species_6': 'source_defined_e_x1_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000405.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cookson2011EnzymaticqueueingcouplingBiomd0000000405Model = Cookson2011EnzymaticqueueingcouplingModel
