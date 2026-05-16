# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Trares2022 - Canonical NF-kB pathway, Petri net."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Trares2022CanonicalNfKbPathwayPetriNetModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2207210001'
    _TITLE = 'Trares2022 - Canonical NF-kB pathway, Petri net'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ikk_complex': ('P12',
                     'native SBML value',
                     'IKK Complex. Maps to SBML symbol `P12` and is emitted in native SBML units.'),
     'ikk_complex_activated': ('P13',
                               'native SBML value',
                               'IKK Complex Activated. Maps to SBML symbol `P13` and is emitted in '
                               'native SBML units.'),
     'p50_rel_a_n': ('P0',
                     'native SBML value',
                     'P50 Rel A N. Maps to SBML symbol `P0` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_p50_rel_a_n': ('P0',
                             0.0,
                             'native SBML value',
                             'Initial level of P50 Rel A N. Maps to SBML symbol `P0`; exposed as a '
                             'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'P50 Rel A N',
     'P1': 'Ik B Phos Ub P50 Rel A',
     'P2': 'CD40',
     'P3': 'CD40L',
     'P4': 'CD40 CD40L',
     'P5': 'source-defined TRAF6 state',
     'P6': 'CD40 CD40L TRAF6',
     'P7': 'source-defined TAK1 state',
     'P8': 'TAK1 Activated',
     'P9': 'Ikkalpha',
     'P10': 'source-defined NEMO state',
     'P11': 'Ikkbeta',
     'P12': 'IKK Complex',
     'P13': 'IKK Complex Activated',
     'P14': 'Ik B P50 Rel A',
     'P15': 'Ik B Phos P50 Rel A',
     'P16': 'IkB',
     'P17': 'P50 Rel A'}
    _STATE_OUTPUT_ALIASES = {'P0': 'p50_rel_a_n',
     'P1': 'ik_b_phos_ub_p50_rel_a',
     'P2': 'cd40',
     'P3': 'cd40l',
     'P4': 'cd40_cd40l',
     'P5': 'source_defined_traf6_state',
     'P6': 'cd40_cd40l_traf6',
     'P7': 'source_defined_tak1_state',
     'P8': 'tak1_activated',
     'P9': 'ikkalpha',
     'P10': 'source_defined_nemo_state',
     'P11': 'ikkbeta',
     'P12': 'ikk_complex',
     'P13': 'ikk_complex_activated',
     'P14': 'ik_b_p50_rel_a',
     'P15': 'ik_b_phos_p50_rel_a',
     'P16': 'ikb',
     'P17': 'p50_rel_a'}

    def __init__(self, model_path: str = 'data/MODEL2207210001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Trares2022CanonicalNfKbPathwayPetriNetModel2207210001Model = Trares2022CanonicalNfKbPathwayPetriNetModel
