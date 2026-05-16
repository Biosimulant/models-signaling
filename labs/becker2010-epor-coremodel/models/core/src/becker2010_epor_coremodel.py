# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Becker2010_EpoR_CoreModel."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Becker2010EporCoremodelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000271'
    _TITLE = 'Becker2010_EpoR_CoreModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'epo_receptor': ('EpoR',
                      'native SBML value',
                      'EPO receptor. Maps to SBML symbol `EpoR` and is emitted in native SBML units.'),
     'erythropoietin': ('Epo',
                        'native SBML value',
                        'erythropoietin. Maps to SBML symbol `Epo` and is emitted in native SBML '
                        'units.'),
     'erythropoietin_erythropoietin_r': ('Epo_EpoR',
                                         'native SBML value',
                                         'erythropoietin erythropoietin R. Maps to SBML symbol '
                                         '`Epo_EpoR` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_epo_receptor': ('EpoR',
                              0.0,
                              'native SBML value',
                              'Initial level of EPO receptor. Maps to SBML symbol `EpoR`; exposed as a '
                              'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EpoR': 'EPO receptor',
     'Epo': 'erythropoietin',
     'Epo_EpoR': 'erythropoietin erythropoietin R',
     'Epo_EpoRi': 'erythropoietin erythropoietin Ri'}
    _STATE_OUTPUT_ALIASES = {'EpoR': 'epo_receptor',
     'Epo': 'erythropoietin',
     'Epo_EpoR': 'erythropoietin_erythropoietin_r',
     'Epo_EpoRi': 'erythropoietin_erythropoietin_ri'}

    def __init__(self, model_path: str = 'data/BIOMD0000000271.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Becker2010EporCoremodelBiomd0000000271Model = Becker2010EporCoremodelModel
