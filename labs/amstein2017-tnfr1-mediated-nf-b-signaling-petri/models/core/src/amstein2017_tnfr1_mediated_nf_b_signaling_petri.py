# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Amstein2017 - TNFR1-mediated Nf-κB signaling, Petri Net."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Amstein2017Tnfr1MediatedNfBSignalingPetriModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2312010001'
    _TITLE = 'Amstein2017 - TNFR1-mediated Nf-κB signaling, Petri Net'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nf_b_n_gen_a20': ('P0',
                        'native SBML value',
                        'NF B N Gen A20. Maps to SBML symbol `P0` and is emitted in native SBML '
                        'units.'),
     'nf_b_n_gen_i_b': ('P2',
                        'native SBML value',
                        'NF B N Gen I B. Maps to SBML symbol `P2` and is emitted in native SBML '
                        'units.'),
     'tnf_receptor_1': ('P4',
                        'native SBML value',
                        'TNF receptor 1. Maps to SBML symbol `P4` and is emitted in native SBML '
                        'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tnf': ('P5',
                     0.0,
                     'native SBML value',
                     'Initial level of TNF. Maps to SBML symbol `P5`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_tnf_receptor_1': ('P4',
                                0.0,
                                'native SBML value',
                                'Initial level of TNF receptor 1. Maps to SBML symbol `P4`; exposed as '
                                'a traceable initial-condition perturbation.'),
     'initial_tnf_receptor_1_tnf': ('P6',
                                    0.0,
                                    'native SBML value',
                                    'Initial level of TNF receptor 1 TNF. Maps to SBML symbol `P6`; '
                                    'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'NF B N Gen A20',
     'P1': 'Gen A20',
     'P2': 'NF B N Gen I B',
     'P3': 'Gen I B',
     'P4': 'TNF receptor 1',
     'P5': 'TNF',
     'P6': 'TNF receptor 1 TNF',
     'P7': 'TRADD',
     'P8': 'TNF receptor 1 TNF TRADD',
     'P9': 'source-defined RIP1 state',
     'P10': 'TNF receptor 1 TNF TRADD RIP1',
     'P11': 'TNF receptor 1 TNF TRADD RIP1 TRAF2',
     'P12': 'source-defined TRAF2 state',
     'P13': 'C Iaps',
     'P14': 'TNF receptor 1 TNF TRADD RIP1 TRAF2 C Iaps',
     'P15': 'RSC Ub',
     'P16': 'source-defined IKK state',
     'P17': 'source-defined TAK1 state',
     'P18': 'RSC Ub TAK1 IKK',
     'P19': 'RSC Ub TAK1 IKK A20',
     'P20': 'RSC Ub TAK1 IKK NF B I B',
     'P21': 'NF B I B',
     'P22': 'NF B I B N',
     'P23': 'source-defined NF-ΚB state',
     'P24': 'source-defined NF-ΚB_N state',
     'P25': 'source-defined IΚB state',
     'P26': 'source-defined IΚB_N state',
     'P27': 'source-defined IΚB_P state',
     'P28': 'Abstract source state A20'}
    _STATE_OUTPUT_ALIASES = {'P0': 'nf_b_n_gen_a20',
     'P1': 'gen_a20',
     'P2': 'nf_b_n_gen_i_b',
     'P3': 'gen_i_b',
     'P4': 'tnf_receptor_1',
     'P5': 'tnf',
     'P6': 'tnf_receptor_1_tnf',
     'P7': 'tradd',
     'P8': 'tnf_receptor_1_tnf_tradd',
     'P9': 'source_defined_rip1_state',
     'P10': 'tnf_receptor_1_tnf_tradd_rip1',
     'P11': 'tnf_receptor_1_tnf_tradd_rip1_traf2',
     'P12': 'source_defined_traf2_state',
     'P13': 'c_iaps',
     'P14': 'tnf_receptor_1_tnf_tradd_rip1_traf2_c_iaps',
     'P15': 'rsc_ub',
     'P16': 'source_defined_ikk_state',
     'P17': 'source_defined_tak1_state',
     'P18': 'rsc_ub_tak1_ikk',
     'P19': 'rsc_ub_tak1_ikk_a20',
     'P20': 'rsc_ub_tak1_ikk_nf_b_i_b',
     'P21': 'nf_b_i_b',
     'P22': 'nf_b_i_b_n',
     'P23': 'source_defined_nf_b_state',
     'P24': 'source_defined_nf_b_n_state',
     'P25': 'source_defined_i_b_state',
     'P26': 'source_defined_i_b_n_state',
     'P27': 'source_defined_i_b_p_state',
     'P28': 'abstract_source_state_a20'}

    def __init__(self, model_path: str = 'data/MODEL2312010001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Amstein2017Tnfr1MediatedNfBSignalingPetriModel2312010001Model = Amstein2017Tnfr1MediatedNfBSignalingPetriModel
