# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Trares2022CrosstalkBetweenTheCanonicalAndNModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2207210003'
    _TITLE = 'Trares2022 - Crosstalk between the canonical and non-canonical NF-kB pathways, Petri net'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ikk_complex_c': ('P13',
                       'native SBML value',
                       'IKK Complex C. Maps to SBML symbol `P13` and is emitted in native SBML units.'),
     'ikk_complex': ('P22',
                     'native SBML value',
                     'IKK Complex. Maps to SBML symbol `P22` and is emitted in native SBML units.'),
     'ikk_complex_activated': ('P24',
                               'native SBML value',
                               'IKK Complex Activated. Maps to SBML symbol `P24` and is emitted in '
                               'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cd40': ('P0',
                      0.0,
                      'native SBML value',
                      'Initial level of CD40. Maps to SBML symbol `P0`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'CD40',
     'P1': 'C IAP1 2 Ub',
     'P2': 'CD40L',
     'P3': 'source-defined TRAF3 state',
     'P4': 'CD40 CD40L',
     'P5': 'P100 Phos Rel B',
     'P6': 'TRAF3 Ub',
     'P7': 'source-defined TRAF6 state',
     'P8': 'P100 Phos Ub Rel B',
     'P9': 'source-defined TRAF2 state',
     'P10': 'P52 Rel B',
     'P11': 'CD40 CD40L TRAF6',
     'P12': 'C IAP1 2',
     'P13': 'IKK Complex C',
     'P14': 'source-defined TAK1 state',
     'P15': 'TAK1 Activated',
     'P16': 'Ikkalpha',
     'P17': 'Ikkbeta',
     'P18': 'OTUD7B TRAF3 Ub',
     'P19': 'OTUD7B',
     'P20': 'P100 P50 Rel A C',
     'P21': 'source-defined NEMO state',
     'P22': 'IKK Complex',
     'P23': 'source-defined NIK state',
     'P24': 'IKK Complex Activated',
     'P25': 'TRAF3 Deg',
     'P26': 'P50 Rel A',
     'P27': 'NIK Stab',
     'P28': 'Ik B P50 Rel A',
     'P29': 'Ik B Phos P50 Rel A',
     'P30': 'IkB',
     'P31': 'P50 Rel A N',
     'P32': 'source-defined TBK1 state',
     'P33': 'Ik B Phos Ub P50 Rel A',
     'P34': 'NIK Phos',
     'P35': 'Ikkalpha Phos NIK Stab',
     'P36': 'P100 Phos Ub P50 Rel A C',
     'P37': 'source-defined RELB state',
     'P38': 'P100 Phos P50 Rel A C',
     'P39': 'Abstract source state P100',
     'P40': 'TRAF2 Ub',
     'P41': 'P100 Rel B',
     'P42': 'TRAF2 TRAF3 C IAP1 2'}
    _STATE_OUTPUT_ALIASES = {'P0': 'cd40',
     'P1': 'c_iap1_2_ub',
     'P2': 'cd40l',
     'P3': 'source_defined_traf3_state',
     'P4': 'cd40_cd40l',
     'P5': 'p100_phos_rel_b',
     'P6': 'traf3_ub',
     'P7': 'source_defined_traf6_state',
     'P8': 'p100_phos_ub_rel_b',
     'P9': 'source_defined_traf2_state',
     'P10': 'p52_rel_b',
     'P11': 'cd40_cd40l_traf6',
     'P12': 'c_iap1_2',
     'P13': 'ikk_complex_c',
     'P14': 'source_defined_tak1_state',
     'P15': 'tak1_activated',
     'P16': 'ikkalpha',
     'P17': 'ikkbeta',
     'P18': 'otud7b_traf3_ub',
     'P19': 'otud7b',
     'P20': 'p100_p50_rel_a_c',
     'P21': 'source_defined_nemo_state',
     'P22': 'ikk_complex',
     'P23': 'source_defined_nik_state',
     'P24': 'ikk_complex_activated',
     'P25': 'traf3_deg',
     'P26': 'p50_rel_a',
     'P27': 'nik_stab',
     'P28': 'ik_b_p50_rel_a',
     'P29': 'ik_b_phos_p50_rel_a',
     'P30': 'ikb',
     'P31': 'p50_rel_a_n',
     'P32': 'source_defined_tbk1_state',
     'P33': 'ik_b_phos_ub_p50_rel_a',
     'P34': 'nik_phos',
     'P35': 'ikkalpha_phos_nik_stab',
     'P36': 'p100_phos_ub_p50_rel_a_c',
     'P37': 'source_defined_relb_state',
     'P38': 'p100_phos_p50_rel_a_c',
     'P39': 'abstract_source_state_p100',
     'P40': 'traf2_ub',
     'P41': 'p100_rel_b',
     'P42': 'traf2_traf3_c_iap1_2'}

    def __init__(self, model_path: str = 'data/MODEL2207210003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Trares2022CrosstalkBetweenTheCanonicalAndNModel2207210003Model = Trares2022CrosstalkBetweenTheCanonicalAndNModel
