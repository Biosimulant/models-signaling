# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_QSS_PSEQ)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sarma2012InteractionTopologiesOfMapkCascadeModel1204280037Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1204280037'
    _TITLE = 'Sarma2012 - Interaction topologies of MAPK cascade (M1_K2_QSS_PSEQ)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapk_kinase_kinase': ('species_1',
                            'native SBML value',
                            'MAPK kinase kinase. Maps to SBML symbol `species_1` and is emitted in '
                            'native SBML units.'),
     'mapk_kinase_kinase_p': ('species_2',
                              'native SBML value',
                              'MAPK kinase kinase P. Maps to SBML symbol `species_2` and is emitted in '
                              'native SBML units.'),
     'mapk_kinase': ('species_3',
                     'native SBML value',
                     'MAPK kinase. Maps to SBML symbol `species_3` and is emitted in native SBML '
                     'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_mapk_kinase_kinase': ('species_1',
                                    0.0,
                                    'native SBML value',
                                    'Initial level of MAPK kinase kinase. Maps to SBML symbol '
                                    '`species_1`; exposed as a traceable initial-condition '
                                    'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'MAPK kinase kinase',
     'species_2': 'MAPK kinase kinase P',
     'species_3': 'MAPK kinase',
     'species_4': 'source-defined MKK_P state',
     'species_5': 'MAPK kinase PP',
     'species_6': 'MAP kinase',
     'species_7': 'source-defined MK_P state',
     'species_8': 'source-defined MK_PP state',
     'species_9': 'source-defined P1 state',
     'species_10': 'source-defined P2 state',
     'species_11': 'source-defined P3 state',
     'species_12': 'source-defined SIG state'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'mapk_kinase_kinase',
     'species_2': 'mapk_kinase_kinase_p',
     'species_3': 'mapk_kinase',
     'species_4': 'source_defined_mkk_p_state',
     'species_5': 'mapk_kinase_pp',
     'species_6': 'map_kinase',
     'species_7': 'source_defined_mk_p_state',
     'species_8': 'source_defined_mk_pp_state',
     'species_9': 'source_defined_p1_state',
     'species_10': 'source_defined_p2_state',
     'species_11': 'source_defined_p3_state',
     'species_12': 'source_defined_sig_state'}

    def __init__(self, model_path: str = 'data/MODEL1204280037.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sarma2012InteractionTopologiesOfMapkCascadeModel1204280037Model = Sarma2012InteractionTopologiesOfMapkCascadeModel1204280037Model
