# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kubota2012_InsulinAction_AKTpathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kubota2012InsulinactionAktpathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1204060000'
    _TITLE = 'Kubota2012_InsulinAction_AKTpathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pro_insulin_receptor_complex': ('proIR_complex',
                                      'native SBML value',
                                      'Pro insulin receptor Complex. Maps to SBML symbol '
                                      '`proIR_complex` and is emitted in native SBML units.'),
     'insulin_receptor_complex': ('IR_complex',
                                  'native SBML value',
                                  'insulin receptor Complex. Maps to SBML symbol `IR_complex` and is '
                                  'emitted in native SBML units.'),
     'p2ir_complex': ('p2IR_complex',
                      'native SBML value',
                      'P2ir Complex. Maps to SBML symbol `p2IR_complex` and is emitted in native SBML '
                      'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_insulin': ('insulin',
                         1.0,
                         'native SBML value',
                         'Initial level of Insulin. Maps to SBML symbol `insulin`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'proIR_complex': 'Pro insulin receptor Complex',
     'IR_complex': 'insulin receptor Complex',
     'p2IR_complex': 'P2ir Complex',
     'p1p2IR_complex': 'P1p2ir Complex',
     'p1IR_complex': 'P1ir Complex',
     'pAKT': 'source-defined PAKT state',
     'AKT': 'AKT',
     'pGSK3b': 'P Gsk3b',
     'GSK3b': 'Gsk3b',
     'pmTOR': 'Pm TOR',
     'mTOR': 'mTOR',
     'pS6K': 'P S6K',
     'S6K': 'S6K',
     'pX': 'source-defined PX state',
     'X': 'response node X',
     'pFOX01': 'P FOX01',
     'FOX01': 'FOX01',
     'G6Pase': 'G6pase',
     'phi_2': 'source-defined PHI_2 state',
     'phi_3': 'source-defined PHI_3 state',
     'insulin': 'Insulin',
     'phi_1': 'source-defined PHI_1 state',
     'phi_4': 'source-defined PHI_4 state'}
    _STATE_OUTPUT_ALIASES = {'proIR_complex': 'pro_insulin_receptor_complex',
     'IR_complex': 'insulin_receptor_complex',
     'p2IR_complex': 'p2ir_complex',
     'p1p2IR_complex': 'p1p2ir_complex',
     'p1IR_complex': 'p1ir_complex',
     'pAKT': 'source_defined_pakt_state',
     'AKT': 'akt',
     'pGSK3b': 'p_gsk3b',
     'GSK3b': 'gsk3b',
     'pmTOR': 'pm_tor',
     'mTOR': 'mtor',
     'pS6K': 'p_s6k',
     'S6K': 's6k',
     'pX': 'source_defined_px_state',
     'X': 'response_node_x',
     'pFOX01': 'p_fox01',
     'FOX01': 'fox01',
     'G6Pase': 'g6pase',
     'phi_2': 'source_defined_phi_2_state',
     'phi_3': 'source_defined_phi_3_state',
     'insulin': 'insulin',
     'phi_1': 'source_defined_phi_1_state',
     'phi_4': 'source_defined_phi_4_state'}

    def __init__(self, model_path: str = 'data/MODEL1204060000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kubota2012InsulinactionAktpathwayModel1204060000Model = Kubota2012InsulinactionAktpathwayModel
