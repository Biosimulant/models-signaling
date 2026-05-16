# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Trares2022 - Non-canonical NF-kB pathway, Petri net."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Trares2022NonCanonicalNfKbPathwayPetriNetModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2207210002'
    _TITLE = 'Trares2022 - Non-canonical NF-kB pathway, Petri net'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_nik_state': ('P0',
                                  'native SBML value',
                                  'source-defined NIK state. Maps to SBML symbol `P0` and is emitted '
                                  'in native SBML units.'),
     'cd40': ('P1',
              'native SBML value',
              'CD40. Maps to SBML symbol `P1` and is emitted in native SBML units.'),
     'cd40l': ('P2',
               'native SBML value',
               'CD40L. Maps to SBML symbol `P2` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_nik_state': ('P0',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined NIK state. Maps to SBML '
                                          'symbol `P0`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'source-defined NIK state',
     'P1': 'CD40',
     'P2': 'CD40L',
     'P3': 'Ikkalpha',
     'P4': 'OTUD7B TRAF3 Ub',
     'P5': 'CD40 CD40L',
     'P6': 'NIK Stab',
     'P7': 'source-defined TRAF2 state',
     'P8': 'source-defined TRAF3 state',
     'P9': 'source-defined TBK1 state',
     'P10': 'C IAP1 2',
     'P11': 'Ikkalpha Phos NIK Stab',
     'P12': 'TRAF2 TRAF3 C IAP1 2',
     'P13': 'NIK Phos',
     'P14': 'TRAF2 Ub',
     'P15': 'P100 Phos Rel B',
     'P16': 'C IAP1 2 Ub',
     'P17': 'P100 Rel B',
     'P18': 'P52 Rel B',
     'P19': 'TRAF3 Ub',
     'P20': 'P100 Phos Ub Rel B',
     'P21': 'OTUD7B',
     'P22': 'TRAF3 Deg'}
    _STATE_OUTPUT_ALIASES = {'P0': 'source_defined_nik_state',
     'P1': 'cd40',
     'P2': 'cd40l',
     'P3': 'ikkalpha',
     'P4': 'otud7b_traf3_ub',
     'P5': 'cd40_cd40l',
     'P6': 'nik_stab',
     'P7': 'source_defined_traf2_state',
     'P8': 'source_defined_traf3_state',
     'P9': 'source_defined_tbk1_state',
     'P10': 'c_iap1_2',
     'P11': 'ikkalpha_phos_nik_stab',
     'P12': 'traf2_traf3_c_iap1_2',
     'P13': 'nik_phos',
     'P14': 'traf2_ub',
     'P15': 'p100_phos_rel_b',
     'P16': 'c_iap1_2_ub',
     'P17': 'p100_rel_b',
     'P18': 'p52_rel_b',
     'P19': 'traf3_ub',
     'P20': 'p100_phos_ub_rel_b',
     'P21': 'otud7b',
     'P22': 'traf3_deg'}

    def __init__(self, model_path: str = 'data/MODEL2207210002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Trares2022NonCanonicalNfKbPathwayPetriNetModel2207210002Model = Trares2022NonCanonicalNfKbPathwayPetriNetModel
