# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kessler2025 - IL-6 and IL-22 pathway in human hepatocytes."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kessler2025Il6AndIl22PathwayInHumanHepaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2509100001'
    _TITLE = 'Kessler2025 - IL-6 and IL-22 pathway in human hepatocytes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'stat3': ('P8',
               'native SBML value',
               'STAT3. Maps to SBML symbol `P8` and is emitted in native SBML units.'),
     'stat1': ('P9',
               'native SBML value',
               'STAT1. Maps to SBML symbol `P9` and is emitted in native SBML units.'),
     'il6rc_dimer_stat1': ('P11',
                           'native SBML value',
                           'IL6RC Dimer STAT1. Maps to SBML symbol `P11` and is emitted in native SBML '
                           'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_il6rc_dimer_shp2': ('P0',
                                  0.0,
                                  'native SBML value',
                                  'Initial level of IL6RC Dimer SHP2. Maps to SBML symbol `P0`; '
                                  'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'IL6RC Dimer SHP2',
     'P1': 'IL22 IL22R1',
     'P2': 'IL6R',
     'P3': 'source-defined IL6 state',
     'P4': 'IL6 IL6R',
     'P5': 'IL6ST JAK',
     'P6': 'IL6RC',
     'P7': 'IL6RC Dimer',
     'P8': 'STAT3',
     'P9': 'STAT1',
     'P10': 'S IL6R',
     'P11': 'IL6RC Dimer STAT1',
     'P12': 'IL6 S IL6R',
     'P13': 'IL6RC Dimer STAT3',
     'P14': 'Sgp130',
     'P15': 'P STAT1',
     'P16': 'IL6 S IL6R Sgp130',
     'P17': 'P STAT3',
     'P18': 'P STAT1 Dimer Cytosol',
     'P19': 'P STAT Heterodimer Cytosol',
     'P20': 'P STAT3 Dimer Cytosol',
     'P21': 'Importin',
     'P22': 'Twop STAT1 Importin',
     'P23': 'P STAT1 3 Importin',
     'P24': 'Twop STAT3 Importin',
     'P25': 'P STAT1 Dimer Nucleus',
     'P26': 'P STAT Heterodimer Nucleus',
     'P27': 'P STAT3 Dimer Nucleus',
     'P28': 'Twop STAT1 DNA',
     'P29': 'P STAT1 3 DNA',
     'P30': 'Twop STAT3 DNA',
     'P31': 'source-defined SOCS1 state',
     'P32': 'SOCS3',
     'P33': 'IL6RC Dimer SOCS1',
     'P34': 'IL6RC Dimer SOCS3',
     'P35': 'source-defined SHP2 state',
     'P36': 'Twop STAT3 DNA Inactive',
     'P37': 'Twop STAT1 DNA Inactive',
     'P38': 'IL22',
     'P39': 'IL22RC',
     'P40': 'IL22R1',
     'P41': 'IL10R2',
     'P42': 'IL22RC STAT3',
     'P43': 'IL22RC STAT1',
     'P44': 'IL22RC SOCS3',
     'P45': 'IL22RC SOCS1',
     'P46': 'IL22BP',
     'P47': 'IL22 IL22BP'}
    _STATE_OUTPUT_ALIASES = {'P0': 'il6rc_dimer_shp2',
     'P1': 'il22_il22r1',
     'P2': 'il6r',
     'P3': 'source_defined_il6_state',
     'P4': 'il6_il6r',
     'P5': 'il6st_jak',
     'P6': 'il6rc',
     'P7': 'il6rc_dimer',
     'P8': 'stat3',
     'P9': 'stat1',
     'P10': 's_il6r',
     'P11': 'il6rc_dimer_stat1',
     'P12': 'il6_s_il6r',
     'P13': 'il6rc_dimer_stat3',
     'P14': 'sgp130',
     'P15': 'p_stat1',
     'P16': 'il6_s_il6r_sgp130',
     'P17': 'p_stat3',
     'P18': 'p_stat1_dimer_cytosol',
     'P19': 'p_stat_heterodimer_cytosol',
     'P20': 'p_stat3_dimer_cytosol',
     'P21': 'importin',
     'P22': 'twop_stat1_importin',
     'P23': 'p_stat1_3_importin',
     'P24': 'twop_stat3_importin',
     'P25': 'p_stat1_dimer_nucleus',
     'P26': 'p_stat_heterodimer_nucleus',
     'P27': 'p_stat3_dimer_nucleus',
     'P28': 'twop_stat1_dna',
     'P29': 'p_stat1_3_dna',
     'P30': 'twop_stat3_dna',
     'P31': 'source_defined_socs1_state',
     'P32': 'socs3',
     'P33': 'il6rc_dimer_socs1',
     'P34': 'il6rc_dimer_socs3',
     'P35': 'source_defined_shp2_state',
     'P36': 'twop_stat3_dna_inactive',
     'P37': 'twop_stat1_dna_inactive',
     'P38': 'il22',
     'P39': 'il22rc',
     'P40': 'il22r1',
     'P41': 'il10r2',
     'P42': 'il22rc_stat3',
     'P43': 'il22rc_stat1',
     'P44': 'il22rc_socs3',
     'P45': 'il22rc_socs1',
     'P46': 'il22bp',
     'P47': 'il22_il22bp'}

    def __init__(self, model_path: str = 'data/MODEL2509100001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kessler2025Il6AndIl22PathwayInHumanHepaModel2509100001Model = Kessler2025Il6AndIl22PathwayInHumanHepaModel
