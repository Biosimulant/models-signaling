# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Platelet PAR1 with SOCE."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class PlateletPar1WithSoceModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1807190001'
    _TITLE = 'Platelet PAR1 with SOCE'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'calcium_cyt': ('species_1',
                     'native SBML value',
                     'calcium Cyt. Maps to SBML symbol `species_1` and is emitted in native SBML '
                     'units.'),
     'calcium_prp': ('species_9',
                     'native SBML value',
                     'calcium Prp. Maps to SBML symbol `species_9` and is emitted in native SBML '
                     'units.'),
     'calcium_dts': ('species_11',
                     'native SBML value',
                     'calcium Dts. Maps to SBML symbol `species_11` and is emitted in native SBML '
                     'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_prp': ('species_9',
                             6e-12,
                             'native SBML value',
                             'Initial level of calcium Prp. Maps to SBML symbol `species_9`; exposed '
                             'as a traceable initial-condition perturbation.'),
     'initial_par1ap': ('species_15',
                        6e-11,
                        'native SBML value',
                        'Initial level of PAR1AP. Maps to SBML symbol `species_15`; exposed as a '
                        'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'calcium Cyt',
     'species_2': 'IP3',
     'species_3': 'Ip3ra',
     'species_4': 'Ip3ri1',
     'species_5': 'Ip3ri2',
     'species_6': 'Ip3rn',
     'species_7': 'Ip3ro',
     'species_8': 'Ip3rs',
     'species_9': 'calcium Prp',
     'species_10': 'Delta Psi',
     'so_1': 'source-defined SO_1 state',
     'so': 'source-defined SO state',
     'species_11': 'calcium Dts',
     'stim': 'STIM calcium sensor',
     'stimCa': 'STIM calcium sensor calcium',
     'species_12': 'calcium Mit',
     'species_13': 'source-defined TCL state',
     'species_14': 'source-defined TOP state',
     'species_15': 'PAR1AP',
     'species_16': 'source-defined PAR state',
     'species_17': 'source-defined PAR* state',
     'species_18': 'PAR Gq',
     'species_19': 'PAR Gq GDP',
     'species_20': 'PAR Gq GTP',
     'species_21': 'source-defined PIP2 state',
     'species_22': 'source-defined PLC state',
     'species_23': 'Plcgq GDP',
     'species_24': 'Plcgq GTP',
     'species_25': 'Plcgq GTPPIP2',
     'species_26': 'GDP',
     'species_27': 'Gq GDP',
     'species_28': 'Gq GTP',
     'species_29': 'GTP'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'calcium_cyt',
     'species_2': 'ip3',
     'species_3': 'ip3ra',
     'species_4': 'ip3ri1',
     'species_5': 'ip3ri2',
     'species_6': 'ip3rn',
     'species_7': 'ip3ro',
     'species_8': 'ip3rs',
     'species_9': 'calcium_prp',
     'species_10': 'delta_psi',
     'so_1': 'source_defined_so_1_state',
     'so': 'source_defined_so_state',
     'species_11': 'calcium_dts',
     'stim': 'stim_calcium_sensor',
     'stimCa': 'stim_calcium_sensor_calcium',
     'species_12': 'calcium_mit',
     'species_13': 'source_defined_tcl_state',
     'species_14': 'source_defined_top_state',
     'species_15': 'par1ap',
     'species_16': 'source_defined_par_state',
     'species_17': 'source_defined_par_state_2',
     'species_18': 'par_gq',
     'species_19': 'par_gq_gdp',
     'species_20': 'par_gq_gtp',
     'species_21': 'source_defined_pip2_state',
     'species_22': 'source_defined_plc_state',
     'species_23': 'plcgq_gdp',
     'species_24': 'plcgq_gtp',
     'species_25': 'plcgq_gtppip2',
     'species_26': 'gdp',
     'species_27': 'gq_gdp',
     'species_28': 'gq_gtp',
     'species_29': 'gtp'}

    def __init__(self, model_path: str = 'data/MODEL1807190001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


PlateletPar1WithSoceModel1807190001Model = PlateletPar1WithSoceModel
