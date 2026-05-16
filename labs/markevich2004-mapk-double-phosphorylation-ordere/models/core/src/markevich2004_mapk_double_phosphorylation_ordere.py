# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Markevich2004 - MAPK double phosphorylation, ordered Michaelis-Menton."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Markevich2004MapkDoublePhosphorylationOrdereModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000027'
    _TITLE = 'Markevich2004 - MAPK double phosphorylation, ordered Michaelis-Menton'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapkk': ('MAPKK',
               'native SBML value',
               'MAPKK. Maps to SBML symbol `MAPKK` and is emitted in native SBML units.'),
     'dual_phosphorylated_mapk': ('Mpp',
                                  'native SBML value',
                                  'Dual Phosphorylated MAPK. Maps to SBML symbol `Mpp` and is emitted '
                                  'in native SBML units.'),
     'source_defined_mkp3_state': ('MKP3',
                                   'native SBML value',
                                   'Source Defined MKP3 State. Maps to SBML symbol `MKP3` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_m_state': ('M',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined M state. Maps to SBML symbol '
                                        '`M`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'M': 'Source Defined M State',
     'Mp': 'Source Defined MP State',
     'Mpp': 'Dual Phosphorylated MAPK',
     'MAPKK': 'MAPKK',
     'MKP3': 'Source Defined MKP3 State'}
    _STATE_OUTPUT_ALIASES = {'M': 'source_defined_m_state',
     'Mp': 'source_defined_mp_state',
     'Mpp': 'dual_phosphorylated_mapk',
     'MAPKK': 'mapkk',
     'MKP3': 'source_defined_mkp3_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000027.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Markevich2004MapkDoublePhosphorylationOrdereBiomd0000000027Model = Markevich2004MapkDoublePhosphorylationOrdereModel
