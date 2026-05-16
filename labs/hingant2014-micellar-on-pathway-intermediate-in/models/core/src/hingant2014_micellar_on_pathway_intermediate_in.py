# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hingant2014 - Micellar On-Pathway Intermediate in Prion Amyloid Formation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hingant2014MicellarOnPathwayIntermediateInModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1409230001'
    _TITLE = 'Hingant2014 - Micellar On-Pathway Intermediate in Prion Amyloid Formation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_mi_1_state': ('Mi_1',
                                   'native SBML value',
                                   'source-defined MI+1 state. Maps to SBML symbol `Mi_1` and is '
                                   'emitted in native SBML units.'),
     'source_defined_pi_1_state': ('Pi_1',
                                   'native SBML value',
                                   'source-defined PI+1 state. Maps to SBML symbol `Pi_1` and is '
                                   'emitted in native SBML units.'),
     'source_defined_pi_j_state': ('Pi_j',
                                   'native SBML value',
                                   'source-defined PI-J state. Maps to SBML symbol `Pi_j` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_m1_state': ('M1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined M1 state. Maps to SBML '
                                         'symbol `M1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'M1': 'source-defined M1 state',
     'P1': 'source-defined P1 state',
     'Pn': 'source-defined PN state',
     'Mi': 'source-defined MI state',
     'Mi_1': 'source-defined MI+1 state',
     'Pi': 'source-defined PI state',
     'Pi_1': 'source-defined PI+1 state',
     'Pi_j': 'source-defined PI-J state',
     'Pj': 'source-defined PJ state'}
    _STATE_OUTPUT_ALIASES = {'M1': 'source_defined_m1_state',
     'P1': 'source_defined_p1_state',
     'Pn': 'source_defined_pn_state',
     'Mi': 'source_defined_mi_state',
     'Mi_1': 'source_defined_mi_1_state',
     'Pi': 'source_defined_pi_state',
     'Pi_1': 'source_defined_pi_1_state',
     'Pi_j': 'source_defined_pi_j_state',
     'Pj': 'source_defined_pj_state'}

    def __init__(self, model_path: str = 'data/MODEL1409230001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hingant2014MicellarOnPathwayIntermediateInModel1409230001Model = Hingant2014MicellarOnPathwayIntermediateInModel
