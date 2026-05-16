# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Haugh2004_hGH."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Haugh2004HghModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL0848676877'
    _TITLE = 'Haugh2004_hGH'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'C': 'source_defined_c_state',
     'D': 'source_defined_d_state',
     'R': 'source_defined_r_state',
     'Ri': 'source_defined_ri_state'}
    _SPECIES_LABELS = {'C': 'Source Defined C State',
     'D': 'Source Defined D State',
     'R': 'Source Defined R State',
     'Ri': 'Source Defined RI State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_c_state': ('C',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined C state. Maps to SBML symbol '
                                        '`C`; exposed as a traceable initial-condition perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_c_state': ('C',
                                'native SBML value',
                                'source-defined C state. Maps to SBML symbol `C` and is emitted in '
                                'native SBML units.'),
     'source_defined_d_state': ('D',
                                'native SBML value',
                                'source-defined D state. Maps to SBML symbol `D` and is emitted in '
                                'native SBML units.'),
     'source_defined_r_state': ('R',
                                'native SBML value',
                                'source-defined R state. Maps to SBML symbol `R` and is emitted in '
                                'native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL0848676877.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Haugh2004HghModel0848676877Model = Haugh2004HghModel
