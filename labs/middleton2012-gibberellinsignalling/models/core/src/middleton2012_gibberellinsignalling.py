# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Middleton2012_GibberellinSignalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Middleton2012GibberellinsignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000422'
    _TITLE = 'Middleton2012_GibberellinSignalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_ga4_state': ('s1',
                                  'native SBML value',
                                  'source-defined GA4 state. Maps to SBML symbol `s1` and is emitted '
                                  'in native SBML units.'),
     'source_defined_gid_state': ('s2',
                                  'native SBML value',
                                  'source-defined GID state. Maps to SBML symbol `s2` and is emitted '
                                  'in native SBML units.'),
     'della': ('s16',
               'native SBML value',
               'DELLA. Maps to SBML symbol `s16` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_della_source': ('s7',
                              0.0,
                              'native SBML value',
                              'Initial level of DELLA Source. Maps to SBML symbol `s7`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_della_source_2': ('s34',
                                0.0,
                                'native SBML value',
                                'Initial level of Della Source. Maps to SBML symbol `s34`; exposed as '
                                'a traceable initial-condition perturbation.'),
     'initial_ga12_source': ('s3',
                             0.0,
                             'native SBML value',
                             'Initial level of GA12 Source. Maps to SBML symbol `s3`; exposed as a '
                             'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s1': 'source-defined GA4 state',
     's2': 'source-defined GID state',
     's16': 'DELLA',
     's22': 'DELLA U',
     's23': 'GA12',
     's24': 'GA15',
     's25': 'GA24',
     's26': 'source-defined GA9 state',
     's27': 'Ga20ox',
     's28': 'Ga3ox',
     's39': 'Ga20ox',
     's40': 'Della',
     's41': 'Ga3ox',
     's42': 'source-defined GID state',
     's65': 'GA4 GID',
     's29': 'GA9 Ga3ox',
     's30': 'GA24 Ga20ox',
     's31': 'GA15 Ga20ox',
     's32': 'GA12 Ga20ox',
     's62': 'GA4 GID closed',
     's36': 'GA4 GID DELLA2',
     's45': 'GA4 GID DELLA1'}
    _STATE_OUTPUT_ALIASES = {'s1': 'source_defined_ga4_state',
     's2': 'source_defined_gid_state',
     's16': 'della',
     's22': 'della_u',
     's23': 'ga12',
     's24': 'ga15',
     's25': 'ga24',
     's26': 'source_defined_ga9_state',
     's27': 'ga20ox',
     's28': 'ga3ox',
     's39': 'ga20ox_2',
     's40': 'della_2',
     's41': 'ga3ox_2',
     's42': 'source_defined_gid_state_2',
     's65': 'ga4_gid',
     's29': 'ga9_ga3ox',
     's30': 'ga24_ga20ox',
     's31': 'ga15_ga20ox',
     's32': 'ga12_ga20ox',
     's62': 'ga4_gid_closed',
     's36': 'ga4_gid_della2',
     's45': 'ga4_gid_della1'}

    def __init__(self, model_path: str = 'data/BIOMD0000000422.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Middleton2012GibberellinsignallingBiomd0000000422Model = Middleton2012GibberellinsignallingModel
