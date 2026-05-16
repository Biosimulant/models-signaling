# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dupeux2011_ABAreceptor_Monomer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dupeux2011AbareceptorMonomerModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1202030001'
    _TITLE = 'Dupeux2011_ABAreceptor_Monomer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_h_h_r_r_state': ('s0_1',
                                      'native SBML value',
                                      'source-defined H.H.R.R state. Maps to SBML symbol `s0_1` and is '
                                      'emitted in native SBML units.'),
     'source_defined_h_r_state': ('s0_2',
                                  'native SBML value',
                                  'source-defined H.R state. Maps to SBML symbol `s0_2` and is emitted '
                                  'in native SBML units.'),
     'source_defined_h_r_r_state': ('s0_3',
                                    'native SBML value',
                                    'source-defined H.R.R state. Maps to SBML symbol `s0_3` and is '
                                    'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_s0_0': ('s0_0',
                      0.0,
                      'native SBML value',
                      'Initial level of S0 0. Maps to SBML symbol `s0_0`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s0_0': 'S0 0',
     's0_1': 'source-defined H.H.R.R state',
     's0_2': 'source-defined H.R state',
     's0_3': 'source-defined H.R.R state',
     's0_4': 'S0 4',
     's0_5': 'source-defined P.H.R state',
     's0_6': 'S0 6',
     's0_7': 'source-defined R.R state'}
    _STATE_OUTPUT_ALIASES = {'s0_0': 's0_0',
     's0_1': 'source_defined_h_h_r_r_state',
     's0_2': 'source_defined_h_r_state',
     's0_3': 'source_defined_h_r_r_state',
     's0_4': 's0_4',
     's0_5': 'source_defined_p_h_r_state',
     's0_6': 's0_6',
     's0_7': 'source_defined_r_r_state'}

    def __init__(self, model_path: str = 'data/MODEL1202030001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dupeux2011AbareceptorMonomerModel1202030001Model = Dupeux2011AbareceptorMonomerModel
