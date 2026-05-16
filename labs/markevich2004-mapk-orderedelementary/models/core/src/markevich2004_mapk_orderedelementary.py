# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Markevich2004_MAPK_orderedElementary."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Markevich2004MapkOrderedelementaryModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000026'
    _TITLE = 'Markevich2004_MAPK_orderedElementary'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapkk': ('MAPKK',
               'native SBML value',
               'MAPKK. Maps to SBML symbol `MAPKK` and is emitted in native SBML units.'),
     'm_mapkk': ('M_MAPKK',
                 'native SBML value',
                 'M MAPKK. Maps to SBML symbol `M_MAPKK` and is emitted in native SBML units.'),
     'mp_mapkk': ('Mp_MAPKK',
                  'native SBML value',
                  'Mp MAPKK. Maps to SBML symbol `Mp_MAPKK` and is emitted in native SBML units.')}
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
     'MKP3': 'source-defined MKP state',
     'M_MAPKK': 'M MAPKK',
     'Mp_MAPKK': 'Mp MAPKK',
     'Mpp_MKP3': 'dual-phosphorylated MAPK MKP',
     'Mp_MKP3_dep': 'Mp MKP',
     'Mp_MKP3': 'Mp MKP',
     'M_MKP3': 'source-defined M_MKP state'}
    _STATE_OUTPUT_ALIASES = {'M': 'source_defined_m_state',
     'Mp': 'source_defined_mp_state',
     'Mpp': 'dual_phosphorylated_mapk',
     'MAPKK': 'mapkk',
     'MKP3': 'source_defined_mkp_state',
     'M_MAPKK': 'm_mapkk',
     'Mp_MAPKK': 'mp_mapkk',
     'Mpp_MKP3': 'dual_phosphorylated_mapk_mkp',
     'Mp_MKP3_dep': 'mp_mkp',
     'Mp_MKP3': 'mp_mkp_2',
     'M_MKP3': 'source_defined_m_mkp_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000026.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Markevich2004MapkOrderedelementaryBiomd0000000026Model = Markevich2004MapkOrderedelementaryModel
