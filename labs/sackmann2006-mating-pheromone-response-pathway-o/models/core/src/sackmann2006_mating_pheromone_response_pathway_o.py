# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sackmann2006 - mating pheromone response pathway of S.cerevisiae."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sackmann2006MatingPheromoneResponsePathwayOModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1403040000'
    _TITLE = 'Sackmann2006 - mating pheromone response pathway of S.cerevisiae'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ste2_receptor': ('P1',
                       'native SBML value',
                       'Ste2 Receptor. Maps to SBML symbol `P1` and is emitted in native SBML units.'),
     'receptor_factor_complex': ('P2',
                                 'native SBML value',
                                 'Receptor Factor Complex. Maps to SBML symbol `P2` and is emitted in '
                                 'native SBML units.'),
     'receptor_complex': ('P3',
                          'native SBML value',
                          'Receptor Complex. Maps to SBML symbol `P3` and is emitted in native SBML '
                          'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha_factor': ('P0',
                              0.0,
                              'native SBML value',
                              'Initial level of Alpha Factor. Maps to SBML symbol `P0`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_receptor_factor_complex': ('P2',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of Receptor Factor Complex. Maps to SBML '
                                         'symbol `P2`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'Alpha Factor',
     'P1': 'Ste2 Receptor',
     'P2': 'Receptor Factor Complex',
     'P3': 'Receptor Complex',
     'P4': 'Trimer bound To Receptor',
     'P5': 'G Alpha GTP',
     'P6': 'G beta response parameter Gamma Dimer',
     'P7': 'Cdc24',
     'P8': 'Cdc42 At Pm',
     'P9': 'Ste20',
     'P10': 'Ste5 Scaffold',
     'P11': 'Ste5 Ste11',
     'P12': 'source-defined FUS3 state',
     'P13': 'Ste7 Fus3',
     'P14': 'MAPK Complex1',
     'P15': 'Ste20 At Pm',
     'P17': 'Complex3',
     'P16': 'Complex2',
     'P19': 'Fus3pp',
     'P18': 'Complex4',
     'P21': 'Repr Complex',
     'P20': 'Compl Without Fus3',
     'P23': 'free Ste12',
     'P22': 'Dig1 Dig2',
     'P25': 'source-defined MSG5 state',
     'P24': 'Ste12',
     'P27': 'Other Genes',
     'P26': 'Fus3 Dephos',
     'P29': 'source-defined BAR1 state',
     'P28': 'Bar1 In Nucleus',
     'P31': 'source-defined FAR1 state',
     'P30': 'Inact Far1',
     'P34': 'Phos Sst2',
     'P35': 'source-defined SST2 state',
     'P32': 'Far1 In Cytosol',
     'P33': 'Sst2 In Nucleus',
     'P38': 'Unphos Kss1',
     'P39': 'source-defined AKR1 state',
     'P36': 'Inact Component',
     'P37': 'Phos Kss1',
     'P40': 'Yck1 Yck2 At Pm',
     'P41': 'Inact Receptor'}
    _STATE_OUTPUT_ALIASES = {'P0': 'alpha_factor',
     'P1': 'ste2_receptor',
     'P2': 'receptor_factor_complex',
     'P3': 'receptor_complex',
     'P4': 'trimer_bound_to_receptor',
     'P5': 'g_alpha_gtp',
     'P6': 'g_beta_response_parameter_gamma_dimer',
     'P7': 'cdc24',
     'P8': 'cdc42_at_pm',
     'P9': 'ste20',
     'P10': 'ste5_scaffold',
     'P11': 'ste5_ste11',
     'P12': 'source_defined_fus3_state',
     'P13': 'ste7_fus3',
     'P14': 'mapk_complex1',
     'P15': 'ste20_at_pm',
     'P17': 'complex3',
     'P16': 'complex2',
     'P19': 'fus3pp',
     'P18': 'complex4',
     'P21': 'repr_complex',
     'P20': 'compl_without_fus3',
     'P23': 'free_ste12',
     'P22': 'dig1_dig2',
     'P25': 'source_defined_msg5_state',
     'P24': 'ste12',
     'P27': 'other_genes',
     'P26': 'fus3_dephos',
     'P29': 'source_defined_bar1_state',
     'P28': 'bar1_in_nucleus',
     'P31': 'source_defined_far1_state',
     'P30': 'inact_far1',
     'P34': 'phos_sst2',
     'P35': 'source_defined_sst2_state',
     'P32': 'far1_in_cytosol',
     'P33': 'sst2_in_nucleus',
     'P38': 'unphos_kss1',
     'P39': 'source_defined_akr1_state',
     'P36': 'inact_component',
     'P37': 'phos_kss1',
     'P40': 'yck1_yck2_at_pm',
     'P41': 'inact_receptor'}

    def __init__(self, model_path: str = 'data/MODEL1403040000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sackmann2006MatingPheromoneResponsePathwayOModel1403040000Model = Sackmann2006MatingPheromoneResponsePathwayOModel
