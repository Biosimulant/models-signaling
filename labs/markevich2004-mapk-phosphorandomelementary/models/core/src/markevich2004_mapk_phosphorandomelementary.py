# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Markevich2004_MAPK_phosphoRandomElementary."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Markevich2004MapkPhosphorandomelementaryModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000028'
    _TITLE = 'Markevich2004_MAPK_phosphoRandomElementary'
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
     'MKP3': 'source-defined MKP3 state',
     'MpY_MEK': 'ERK PY MEK',
     'MpT_MEK': 'ERK PT MEK',
     'M_MEK_Y': 'ERK MEK Y',
     'M_MEK_T': 'ERK MEK T',
     'Mpp_MKP3': 'ERK PP MKP3',
     'MpY_MKP3': 'ERK PY MKP3',
     'MpT_MKP3_Y': 'ERK PT MKP3 Y',
     'MpT_MKP3_T': 'ERK PT MKP3 T',
     'M_MKP3_T': 'ERK MKP3 T',
     'M_MKP3_Y': 'ERK MKP3 Y'}
    _STATE_OUTPUT_ALIASES = {'M': 'erk',
     'MpY': 'erk_py',
     'MpT': 'erk_pt',
     'Mpp': 'erk_pp',
     'MEK': 'mek',
     'MKP3': 'source_defined_mkp3_state',
     'MpY_MEK': 'erk_py_mek',
     'MpT_MEK': 'erk_pt_mek',
     'M_MEK_Y': 'erk_mek_y',
     'M_MEK_T': 'erk_mek_t',
     'Mpp_MKP3': 'erk_pp_mkp3',
     'MpY_MKP3': 'erk_py_mkp3',
     'MpT_MKP3_Y': 'erk_pt_mkp3_y',
     'MpT_MKP3_T': 'erk_pt_mkp3_t',
     'M_MKP3_T': 'erk_mkp3_t',
     'M_MKP3_Y': 'erk_mkp3_y'}

    def __init__(self, model_path: str = 'data/BIOMD0000000028.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Markevich2004MapkPhosphorandomelementaryBiomd0000000028Model = Markevich2004MapkPhosphorandomelementaryModel
