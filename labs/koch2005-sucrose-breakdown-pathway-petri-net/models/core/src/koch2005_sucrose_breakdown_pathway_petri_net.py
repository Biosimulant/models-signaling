# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Koch2005 - Sucrose breakdown pathway - Petri net."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koch2005SucroseBreakdownPathwayPetriNetModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1308080002'
    _TITLE = 'Koch2005 - Sucrose breakdown pathway - Petri net'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'sucrose': ('P0',
                 'native SBML value',
                 'sucrose. Maps to SBML symbol `P0` and is emitted in native SBML units.'),
     'source_defined_esuc_state': ('P1',
                                   'native SBML value',
                                   'source-defined ESUC state. Maps to SBML symbol `P1` and is emitted '
                                   'in native SBML units.'),
     'glucose': ('P2',
                 'native SBML value',
                 'glucose. Maps to SBML symbol `P2` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sucrose': ('P0',
                         0.0,
                         'native SBML value',
                         'Initial level of sucrose. Maps to SBML symbol `P0`; exposed as a traceable '
                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P0': 'sucrose',
     'P1': 'source-defined ESUC state',
     'P2': 'glucose',
     'P3': 'source-defined FRC state',
     'P4': 'Udpglc',
     'P5': 'G6P',
     'P6': 'F6P',
     'P7': 'G1P',
     'P8': 'source-defined UDP state',
     'P9': 'source-defined UTP state',
     'P10': 'ATP',
     'P11': 'ADP',
     'P12': 'S6P',
     'P13': 'source-defined PI state',
     'P14': 'source-defined PP state',
     'P15': 'Starch',
     'P16': 'AMP'}
    _STATE_OUTPUT_ALIASES = {'P0': 'sucrose',
     'P1': 'source_defined_esuc_state',
     'P2': 'glucose',
     'P3': 'source_defined_frc_state',
     'P4': 'udpglc',
     'P5': 'g6p',
     'P6': 'f6p',
     'P7': 'g1p',
     'P8': 'source_defined_udp_state',
     'P9': 'source_defined_utp_state',
     'P10': 'atp',
     'P11': 'adp',
     'P12': 's6p',
     'P13': 'source_defined_pi_state',
     'P14': 'source_defined_pp_state',
     'P15': 'starch',
     'P16': 'amp'}

    def __init__(self, model_path: str = 'data/MODEL1308080002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Koch2005SucroseBreakdownPathwayPetriNetModel1308080002Model = Koch2005SucroseBreakdownPathwayPetriNetModel
