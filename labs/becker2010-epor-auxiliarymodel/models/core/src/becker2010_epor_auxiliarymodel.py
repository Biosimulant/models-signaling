# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Becker2010_EpoR_AuxiliaryModel."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Becker2010EporAuxiliarymodelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000272'
    _TITLE = 'Becker2010_EpoR_AuxiliaryModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'epo_receptor': ('EpoR',
                      'native SBML value',
                      'EPO receptor. Maps to SBML symbol `EpoR` and is emitted in native SBML units.'),
     'source_defined_sav_state': ('SAv',
                                  'native SBML value',
                                  'source-defined SAV state. Maps to SBML symbol `SAv` and is emitted '
                                  'in native SBML units.'),
     'sav_erythropoietin_r': ('SAv_EpoR',
                              'native SBML value',
                              'Sav erythropoietin R. Maps to SBML symbol `SAv_EpoR` and is emitted in '
                              'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_epo_receptor': ('EpoR',
                              0.0,
                              'native SBML value',
                              'Initial level of EPO receptor. Maps to SBML symbol `EpoR`; exposed as a '
                              'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EpoR': 'EPO receptor',
     'SAv': 'source-defined SAV state',
     'SAv_EpoR': 'Sav erythropoietin R',
     'SAv_EpoRi': 'Sav erythropoietin Ri'}
    _STATE_OUTPUT_ALIASES = {'EpoR': 'epo_receptor',
     'SAv': 'source_defined_sav_state',
     'SAv_EpoR': 'sav_erythropoietin_r',
     'SAv_EpoRi': 'sav_erythropoietin_ri'}

    def __init__(self, model_path: str = 'data/BIOMD0000000272.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Becker2010EporAuxiliarymodelBiomd0000000272Model = Becker2010EporAuxiliarymodelModel
