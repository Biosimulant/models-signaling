# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Markevich2004_MAPK_phosphoRandomMM."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Markevich2004MapkPhosphorandommmModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000029'
    _TITLE = 'Markevich2004_MAPK_phosphoRandomMM'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'erk': ('M',
             'native SBML value',
             'ERK. Maps to SBML symbol `M` and is emitted in native SBML units.'),
     'erk_py': ('MpY',
                'native SBML value',
                'ERK PY. Maps to SBML symbol `MpY` and is emitted in native SBML units.'),
     'erk_pt': ('MpT',
                'native SBML value',
                'ERK PT. Maps to SBML symbol `MpT` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_erk': ('M',
                     0.0,
                     'native SBML value',
                     'Initial level of ERK. Maps to SBML symbol `M`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'M': 'ERK',
     'MpY': 'ERK PY',
     'MpT': 'ERK PT',
     'Mpp': 'ERK PP',
     'MEK': 'MEK',
     'MKP3': 'source-defined MKP3 state'}
    _STATE_OUTPUT_ALIASES = {'M': 'erk',
     'MpY': 'erk_py',
     'MpT': 'erk_pt',
     'Mpp': 'erk_pp',
     'MEK': 'mek',
     'MKP3': 'source_defined_mkp3_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000029.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Markevich2004MapkPhosphorandommmBiomd0000000029Model = Markevich2004MapkPhosphorandommmModel
