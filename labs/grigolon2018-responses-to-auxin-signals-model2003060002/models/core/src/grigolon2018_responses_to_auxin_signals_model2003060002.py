# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Grigolon2018 - Responses to auxin signals."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Grigolon2018ResponsesToAuxinSignalsModel2003060002Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2003060002'
    _TITLE = 'Grigolon2018 - Responses to auxin signals'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'auxin': ('auxin',
               'native SBML value',
               'Auxin. Maps to SBML symbol `auxin` and is emitted in native SBML units.'),
     'indole_3_acetic_acid': ('IAA',
                              'native SBML value',
                              'indole-3-acetic acid. Maps to SBML symbol `IAA` and is emitted in '
                              'native SBML units.'),
     'auxin_response_factor': ('ARF',
                               'native SBML value',
                               'auxin response factor. Maps to SBML symbol `ARF` and is emitted in '
                               'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_auxin': ('auxin',
                       1.0,
                       'native SBML value',
                       'Initial level of Auxin. Maps to SBML symbol `auxin`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_sauxin_level': ('Sauxin',
                              0.02,
                              'native SBML value',
                              'Sauxin source parameter. Maps to SBML symbol `Sauxin` and preserves the '
                              'bundled default.'),
     'initial_tauxin_level': ('Tauxin',
                              10.0,
                              'native SBML value',
                              'Tauxin source parameter. Maps to SBML symbol `Tauxin` and preserves the '
                              'bundled default.')}
    _SPECIES_LABELS = {'auxin': 'Auxin', 'IAA': 'indole-3-acetic acid', 'ARF': 'auxin response factor'}
    _STATE_OUTPUT_ALIASES = {'auxin': 'auxin', 'IAA': 'indole_3_acetic_acid', 'ARF': 'auxin_response_factor'}

    def __init__(self, model_path: str = 'data/MODEL2003060002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Grigolon2018ResponsesToAuxinSignalsModel2003060002Model = Grigolon2018ResponsesToAuxinSignalsModel2003060002Model
