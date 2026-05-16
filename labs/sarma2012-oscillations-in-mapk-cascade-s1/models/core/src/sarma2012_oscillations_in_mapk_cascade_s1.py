# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sarma2012 - Oscillations in MAPK cascade (S1)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sarma2012OscillationsInMapkCascadeS1Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000440'
    _TITLE = 'Sarma2012 - Oscillations in MAPK cascade (S1)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapk_kinase_kinase': ('species_0',
                            'native SBML value',
                            'MAPK kinase kinase. Maps to SBML symbol `species_0` and is emitted in '
                            'native SBML units.'),
     'mapk_kinase_kinase_p': ('species_1',
                              'native SBML value',
                              'MAPK kinase kinase P. Maps to SBML symbol `species_1` and is emitted in '
                              'native SBML units.'),
     'mapk_kinase': ('species_2',
                     'native SBML value',
                     'MAPK kinase. Maps to SBML symbol `species_2` and is emitted in native SBML '
                     'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_mapk_kinase_kinase': ('species_0',
                                    0.0,
                                    'native SBML value',
                                    'Initial level of MAPK kinase kinase. Maps to SBML symbol '
                                    '`species_0`; exposed as a traceable initial-condition '
                                    'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_0': 'MAPK kinase kinase',
     'species_1': 'MAPK kinase kinase P',
     'species_2': 'MAPK kinase',
     'species_3': 'source-defined MKK_P state',
     'species_4': 'MAPK kinase PP',
     'species_5': 'source-defined M state',
     'species_6': 'source-defined M_P state',
     'species_7': 'dual-phosphorylated MAPK',
     'species_8': 'source-defined P1 state',
     'species_9': 'source-defined P2 state',
     'species_10': 'source-defined P3 state'}
    _STATE_OUTPUT_ALIASES = {'species_0': 'mapk_kinase_kinase',
     'species_1': 'mapk_kinase_kinase_p',
     'species_2': 'mapk_kinase',
     'species_3': 'source_defined_mkk_p_state',
     'species_4': 'mapk_kinase_pp',
     'species_5': 'source_defined_m_state',
     'species_6': 'source_defined_m_p_state',
     'species_7': 'dual_phosphorylated_mapk',
     'species_8': 'source_defined_p1_state',
     'species_9': 'source_defined_p2_state',
     'species_10': 'source_defined_p3_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000440.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sarma2012OscillationsInMapkCascadeS1Biomd0000000440Model = Sarma2012OscillationsInMapkCascadeS1Model
