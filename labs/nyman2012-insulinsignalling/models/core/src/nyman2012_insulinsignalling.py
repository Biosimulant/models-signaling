# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nyman2012_InsulinSignalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nyman2012InsulinsignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000423'
    _TITLE = 'Nyman2012_InsulinSignalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'insulin_bound_insulin_receptor': ('IRins',
                                        'native SBML value',
                                        'insulin-bound insulin receptor. Maps to SBML symbol `IRins` '
                                        'and is emitted in native SBML units.'),
     'phosphorylated_insulin_receptor': ('IRp',
                                         'native SBML value',
                                         'phosphorylated insulin receptor. Maps to SBML symbol `IRp` '
                                         'and is emitted in native SBML units.'),
     'internalized_phosphorylated_insulin_receptor': ('IRiP',
                                                      'native SBML value',
                                                      'internalized phosphorylated insulin receptor. '
                                                      'Maps to SBML symbol `IRiP` and is emitted in '
                                                      'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_k1a_basic_level': ('k1aBasic',
                                 0.0383389,
                                 'native SBML value',
                                 'K1a Basic source parameter. Maps to SBML symbol `k1aBasic` and '
                                 'preserves the bundled default.')}
    _SPECIES_LABELS = {'IR': 'insulin receptor',
     'IRins': 'insulin-bound insulin receptor',
     'IRp': 'phosphorylated insulin receptor',
     'IRiP': 'internalized phosphorylated insulin receptor',
     'IRi': 'internalized insulin receptor',
     'IRS': 'IRS',
     'IRSiP': 'Irsi P',
     'X': 'response node X',
     'Xp': 'phosphorylated response node X'}
    _STATE_OUTPUT_ALIASES = {'IR': 'insulin_receptor',
     'IRins': 'insulin_bound_insulin_receptor',
     'IRp': 'phosphorylated_insulin_receptor',
     'IRiP': 'internalized_phosphorylated_insulin_receptor',
     'IRi': 'internalized_insulin_receptor',
     'IRS': 'irs',
     'IRSiP': 'irsi_p',
     'X': 'response_node_x',
     'Xp': 'phosphorylated_response_node_x'}

    def __init__(self, model_path: str = 'data/BIOMD0000000423.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Nyman2012InsulinsignallingBiomd0000000423Model = Nyman2012InsulinsignallingModel
