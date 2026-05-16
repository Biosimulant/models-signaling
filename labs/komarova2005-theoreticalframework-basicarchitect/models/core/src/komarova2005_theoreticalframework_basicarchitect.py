# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Komarova2005_TheoreticalFramework_BasicArchitecture."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Komarova2005TheoreticalframeworkBasicarchitectModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000125'
    _TITLE = 'Komarova2005_TheoreticalFramework_BasicArchitecture'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_x1_state': ('x1',
                                 'native SBML value',
                                 'Source Defined X1 State. Maps to SBML symbol `x1` and is emitted in '
                                 'native SBML units.'),
     'source_defined_x2_state': ('x2',
                                 'native SBML value',
                                 'Source Defined X2 State. Maps to SBML symbol `x2` and is emitted in '
                                 'native SBML units.'),
     'source_defined_y2_state': ('y2',
                                 'native SBML value',
                                 'Source Defined Y2 State. Maps to SBML symbol `y2` and is emitted in '
                                 'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_x1_state': ('x1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined X1 state. Maps to SBML '
                                         'symbol `x1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x1': 'Source Defined X1 State',
     'x2': 'Source Defined X2 State',
     'y2': 'Source Defined Y2 State',
     'x0': 'Source Defined X0 State',
     'y0': 'Source Defined Y0 State'}
    _STATE_OUTPUT_ALIASES = {'x1': 'source_defined_x1_state',
     'x2': 'source_defined_x2_state',
     'y2': 'source_defined_y2_state',
     'x0': 'source_defined_x0_state',
     'y0': 'source_defined_y0_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000125.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Komarova2005TheoreticalframeworkBasicarchitectBiomd0000000125Model = Komarova2005TheoreticalframeworkBasicarchitectModel
