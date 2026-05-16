# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dupeux2011_ABAreceptor_Dimer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dupeux2011AbareceptorDimerModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1202030000'
    _TITLE = 'Dupeux2011_ABAreceptor_Dimer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'h_h_ra_ra': ('s0_1',
                   'native SBML value',
                   'H H RA RA. Maps to SBML symbol `s0_1` and is emitted in native SBML units.'),
     'h_h_rb_rb': ('s0_2',
                   'native SBML value',
                   'H H RB RB. Maps to SBML symbol `s0_2` and is emitted in native SBML units.'),
     'source_defined_h_ra_state': ('s0_3',
                                   'native SBML value',
                                   'source-defined H.RA state. Maps to SBML symbol `s0_3` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_s0_0': ('s0_0',
                      0.0,
                      'native SBML value',
                      'Initial level of S0 0. Maps to SBML symbol `s0_0`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s0_0': 'S0 0',
     's0_1': 'H H RA RA',
     's0_2': 'H H RB RB',
     's0_3': 'source-defined H.RA state',
     's0_4': 'H RA RA',
     's0_5': 'source-defined H.RB state',
     's0_6': 'H RB RB',
     's0_7': 'S0 7',
     's0_8': 'source-defined P.H.RA state',
     's0_9': 'source-defined P.H.RB state',
     's0_10': 'source-defined RA state',
     's0_11': 'source-defined RA.RA state',
     's0_12': 'source-defined RB state',
     's0_13': 'source-defined RB.RB state'}
    _STATE_OUTPUT_ALIASES = {'s0_0': 's0_0',
     's0_1': 'h_h_ra_ra',
     's0_2': 'h_h_rb_rb',
     's0_3': 'source_defined_h_ra_state',
     's0_4': 'h_ra_ra',
     's0_5': 'source_defined_h_rb_state',
     's0_6': 'h_rb_rb',
     's0_7': 's0_7',
     's0_8': 'source_defined_p_h_ra_state',
     's0_9': 'source_defined_p_h_rb_state',
     's0_10': 'source_defined_ra_state',
     's0_11': 'source_defined_ra_ra_state',
     's0_12': 'source_defined_rb_state',
     's0_13': 'source_defined_rb_rb_state'}

    def __init__(self, model_path: str = 'data/MODEL1202030000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dupeux2011AbareceptorDimerModel1202030000Model = Dupeux2011AbareceptorDimerModel
