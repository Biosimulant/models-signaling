# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for McClean2007_CrossTalk."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mcclean2007CrosstalkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000116'
    _TITLE = 'McClean2007_CrossTalk'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'x1p': ('species_0',
             'native SBML value',
             'X1p. Maps to SBML symbol `species_0` and is emitted in native SBML units.'),
     'x2p': ('species_1',
             'native SBML value',
             'X2p. Maps to SBML symbol `species_1` and is emitted in native SBML units.'),
     'x3p': ('species_2',
             'native SBML value',
             'X3p. Maps to SBML symbol `species_2` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_x1p': ('species_0',
                     0.0,
                     'native SBML value',
                     'Initial level of X1p. Maps to SBML symbol `species_0`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_0': 'X1p',
     'species_1': 'X2p',
     'species_2': 'X3p',
     'species_3': 'Y1p',
     'species_4': 'Y2p',
     'species_5': 'Y3p'}
    _STATE_OUTPUT_ALIASES = {'species_0': 'x1p',
     'species_1': 'x2p',
     'species_2': 'x3p',
     'species_3': 'y1p',
     'species_4': 'y2p',
     'species_5': 'y3p'}

    def __init__(self, model_path: str = 'data/BIOMD0000000116.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Mcclean2007CrosstalkBiomd0000000116Model = Mcclean2007CrosstalkModel
