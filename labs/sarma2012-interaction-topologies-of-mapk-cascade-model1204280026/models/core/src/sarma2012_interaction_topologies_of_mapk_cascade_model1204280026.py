# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sarma2012 - Interaction topologies of MAPK cascade (M2_K2_USEQ_short_duration_signal)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sarma2012InteractionTopologiesOfMapkCascadeModel1204280026Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1204280026'
    _TITLE = 'Sarma2012 - Interaction topologies of MAPK cascade (M2_K2_USEQ_short_duration_signal)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapk_kinase_pp': ('species_2',
                        'native SBML value',
                        'MAPK kinase PP. Maps to SBML symbol `species_2` and is emitted in native SBML '
                        'units.'),
     'map_kinase_mapk_kinase_pp': ('species_3',
                                   'native SBML value',
                                   'MAP kinase MAPK kinase PP. Maps to SBML symbol `species_3` and is '
                                   'emitted in native SBML units.'),
     'source_defined_mk_p_state': ('species_4',
                                   'native SBML value',
                                   'source-defined MK-P state. Maps to SBML symbol `species_4` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_map_kinase': ('species_1',
                            0.0,
                            'native SBML value',
                            'Initial level of MAP kinase. Maps to SBML symbol `species_1`; exposed as '
                            'a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'MAP kinase',
     'species_2': 'MAPK kinase PP',
     'species_3': 'MAP kinase MAPK kinase PP',
     'species_4': 'source-defined MK-P state',
     'species_5': 'MAP kinase P MAPK kinase PP',
     'species_6': 'source-defined MK-PP state',
     'species_7': 'MAPK kinase',
     'species_8': 'MAPK kinase kinase P',
     'species_9': 'MAPK kinase MAPK kinase kinase P',
     'species_10': 'source-defined MKK-P state',
     'species_11': 'MAPK kinase P MAPK kinase kinase P',
     'species_12': 'source-defined P2 state',
     'species_13': 'MAPK kinase kinase',
     'species_14': 'MAPK kinase kinase Sig',
     'species_15': 'source-defined SIG state',
     'species_16': 'MAPK kinase kinase P P1',
     'species_17': 'source-defined P1 state',
     'species_18': 'MAPK kinase P P1',
     'species_19': 'MAPK kinase PP P1',
     'species_20': 'source-defined MKK_P1 state',
     'species_21': 'MAP kinase PP P2',
     'species_22': 'source-defined MK-P_P2 state',
     'species_23': 'source-defined MK_P2 state',
     'species_24': 'MAPK kinase kinase P1'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'map_kinase',
     'species_2': 'mapk_kinase_pp',
     'species_3': 'map_kinase_mapk_kinase_pp',
     'species_4': 'source_defined_mk_p_state',
     'species_5': 'map_kinase_p_mapk_kinase_pp',
     'species_6': 'source_defined_mk_pp_state',
     'species_7': 'mapk_kinase',
     'species_8': 'mapk_kinase_kinase_p',
     'species_9': 'mapk_kinase_mapk_kinase_kinase_p',
     'species_10': 'source_defined_mkk_p_state',
     'species_11': 'mapk_kinase_p_mapk_kinase_kinase_p',
     'species_12': 'source_defined_p2_state',
     'species_13': 'mapk_kinase_kinase',
     'species_14': 'mapk_kinase_kinase_sig',
     'species_15': 'source_defined_sig_state',
     'species_16': 'mapk_kinase_kinase_p_p1',
     'species_17': 'source_defined_p1_state',
     'species_18': 'mapk_kinase_p_p1',
     'species_19': 'mapk_kinase_pp_p1',
     'species_20': 'source_defined_mkk_p1_state',
     'species_21': 'map_kinase_pp_p2',
     'species_22': 'source_defined_mk_p_p2_state',
     'species_23': 'source_defined_mk_p2_state',
     'species_24': 'mapk_kinase_kinase_p1'}

    def __init__(self, model_path: str = 'data/MODEL1204280026.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sarma2012InteractionTopologiesOfMapkCascadeModel1204280026Model = Sarma2012InteractionTopologiesOfMapkCascadeModel1204280026Model
