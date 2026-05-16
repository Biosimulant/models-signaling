# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gupta2007_HypothalamicPituitaryAdrenal_ModelB."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gupta2007HypothalamicpituitaryadrenalModelbModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1006230036'
    _TITLE = 'Gupta2007_HypothalamicPituitaryAdrenal_ModelB'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'c': 'source_defined_c_state',
     'a': 'source_defined_a_state',
     'r': 'source_defined_r_state',
     'o': 'source_defined_o_state'}
    _SPECIES_LABELS = {'c': 'Source Defined C State',
     'a': 'Source Defined A State',
     'r': 'Source Defined R State',
     'o': 'Source Defined O State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_c_state': ('c',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined C state. Maps to SBML symbol '
                                        '`c`; exposed as a traceable initial-condition perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_c_state': ('c',
                                'native SBML value',
                                'source-defined C state. Maps to SBML symbol `c` and is emitted in '
                                'native SBML units.'),
     'source_defined_a_state': ('a',
                                'native SBML value',
                                'source-defined A state. Maps to SBML symbol `a` and is emitted in '
                                'native SBML units.'),
     'source_defined_r_state': ('r',
                                'native SBML value',
                                'source-defined R state. Maps to SBML symbol `r` and is emitted in '
                                'native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL1006230036.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gupta2007HypothalamicpituitaryadrenalModelbModel1006230036Model = Gupta2007HypothalamicpituitaryadrenalModelbModel
