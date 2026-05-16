# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dutta-Roy2015 - Opening of the multiple AMPA receptor conductance states."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class DuttaRoy2015OpeningOfTheMultipleAmpaRecepModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000569'
    _TITLE = 'Dutta-Roy2015 - Opening of the multiple AMPA receptor conductance states'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glutamate': ('glu',
                   'native SBML value',
                   'glutamate. Maps to SBML symbol `glu` and is emitted in native SBML units.'),
     'source_defined_b0_state': ('B0',
                                 'native SBML value',
                                 'source-defined B0 state. Maps to SBML symbol `B0` and is emitted in '
                                 'native SBML units.'),
     'source_defined_s0_state': ('S0',
                                 'native SBML value',
                                 'source-defined S0 state. Maps to SBML symbol `S0` and is emitted in '
                                 'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_b0_state': ('B0',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined B0 state. Maps to SBML '
                                         'symbol `B0`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'B0': 'source-defined B0 state',
     'S0': 'source-defined S0 state',
     'B1': 'source-defined B1 state',
     'S1': 'source-defined S1 state',
     'B2': 'source-defined B2 state',
     'S2': 'source-defined S2 state',
     'B3': 'source-defined B3 state',
     'S3': 'source-defined S3 state',
     'B4': 'source-defined B4 state',
     'S4': 'source-defined S4 state',
     'M0': 'source-defined M0 state',
     'M1': 'source-defined M1 state',
     'M2': 'source-defined M2 state',
     'M3': 'source-defined M3 state',
     'M4': 'source-defined M4 state',
     'L0': 'source-defined L0 state',
     'L1': 'source-defined L1 state',
     'L2': 'source-defined L2 state',
     'L3': 'source-defined L3 state',
     'L4': 'source-defined L4 state',
     'glu': 'glutamate'}
    _STATE_OUTPUT_ALIASES = {'B0': 'source_defined_b0_state',
     'S0': 'source_defined_s0_state',
     'B1': 'source_defined_b1_state',
     'S1': 'source_defined_s1_state',
     'B2': 'source_defined_b2_state',
     'S2': 'source_defined_s2_state',
     'B3': 'source_defined_b3_state',
     'S3': 'source_defined_s3_state',
     'B4': 'source_defined_b4_state',
     'S4': 'source_defined_s4_state',
     'M0': 'source_defined_m0_state',
     'M1': 'source_defined_m1_state',
     'M2': 'source_defined_m2_state',
     'M3': 'source_defined_m3_state',
     'M4': 'source_defined_m4_state',
     'L0': 'source_defined_l0_state',
     'L1': 'source_defined_l1_state',
     'L2': 'source_defined_l2_state',
     'L3': 'source_defined_l3_state',
     'L4': 'source_defined_l4_state',
     'glu': 'glutamate'}

    def __init__(self, model_path: str = 'data/BIOMD0000000569.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


DuttaRoy2015OpeningOfTheMultipleAmpaRecepBiomd0000000569Model = DuttaRoy2015OpeningOfTheMultipleAmpaRecepModel
