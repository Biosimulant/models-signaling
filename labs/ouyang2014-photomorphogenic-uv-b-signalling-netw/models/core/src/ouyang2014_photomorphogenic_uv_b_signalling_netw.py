# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ouyang2014 - photomorphogenic UV-B signalling network."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ouyang2014PhotomorphogenicUvBSignallingNetwModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000545'
    _TITLE = 'Ouyang2014 - photomorphogenic UV-B signalling network'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_cdcs_state': ('CDCS',
                                   'mole',
                                   'source-defined CDCS state. Maps to SBML symbol `CDCS` and is '
                                   'emitted in native SBML units.'),
     'uvr8m': ('UVR8M',
               'mole',
               'UVR8M. Maps to SBML symbol `UVR8M` and is emitted in native SBML units.'),
     'source_defined_ucs_state': ('UCS',
                                  'mole',
                                  'source-defined UCS state. Maps to SBML symbol `UCS` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_uvr8_m': ('UVR8_M',
                        0.0,
                        'mole',
                        'Initial level of UVR8 M. Maps to SBML symbol `UVR8_M`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_uvr8d': ('UVR8D',
                       20.0,
                       'mole',
                       'Initial level of UVR8D. Maps to SBML symbol `UVR8D`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_source_defined_uv_state_level': ('UV',
                                               1.0,
                                               'native SBML value',
                                               'source-defined UV state source parameter. Maps to SBML '
                                               'symbol `UV` and preserves the bundled default.')}
    _SPECIES_LABELS = {'CS': 'source-defined CS state',
     'CD': 'source-defined CD state',
     'CDCS': 'source-defined CDCS state',
     'UVR8M': 'UVR8M',
     'UCS': 'source-defined UCS state',
     'UVR8D': 'UVR8D',
     'RUP': 'source-defined RUP state',
     'UR': 'source-defined UR state',
     'UVR8_M': 'UVR8 M',
     'COP1': 'source-defined COP1 state',
     'HY5': 'source-defined HY5 state',
     'FHY3': 'source-defined FHY3 state',
     'DWD': 'source-defined DWD state',
     'CDW': 'source-defined CDW state'}
    _STATE_OUTPUT_ALIASES = {'CS': 'source_defined_cs_state',
     'CD': 'source_defined_cd_state',
     'CDCS': 'source_defined_cdcs_state',
     'UVR8M': 'uvr8m',
     'UCS': 'source_defined_ucs_state',
     'UVR8D': 'uvr8d',
     'RUP': 'source_defined_rup_state',
     'UR': 'source_defined_ur_state',
     'UVR8_M': 'uvr8_m',
     'COP1': 'source_defined_cop1_state',
     'HY5': 'source_defined_hy5_state',
     'FHY3': 'source_defined_fhy3_state',
     'DWD': 'source_defined_dwd_state',
     'CDW': 'source_defined_cdw_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000545.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Ouyang2014PhotomorphogenicUvBSignallingNetwBiomd0000000545Model = Ouyang2014PhotomorphogenicUvBSignallingNetwModel
