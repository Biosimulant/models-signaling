# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Cao2013 - Application of ABSIS in the the enzymatic futile cycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2013ApplicationOfAbsisInTheTheEnzymatiModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000487'
    _TITLE = 'Cao2013 - Application of ABSIS in the the enzymatic futile cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_s1_state': ('S1',
                                 'native SBML value',
                                 'source-defined S1 state. Maps to SBML symbol `S1` and is emitted in '
                                 'native SBML units.'),
     'source_defined_s2_state': ('S2',
                                 'native SBML value',
                                 'source-defined S2 state. Maps to SBML symbol `S2` and is emitted in '
                                 'native SBML units.'),
     'source_defined_s3_state': ('S3',
                                 'native SBML value',
                                 'source-defined S3 state. Maps to SBML symbol `S3` and is emitted in '
                                 'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_s1_state': ('S1',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined S1 state. Maps to SBML '
                                         'symbol `S1`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'S1': 'source-defined S1 state',
     'S2': 'source-defined S2 state',
     'S3': 'source-defined S3 state',
     'S4': 'source-defined S4 state',
     'S5': 'source-defined S5 state',
     'S6': 'source-defined S6 state'}
    _STATE_OUTPUT_ALIASES = {'S1': 'source_defined_s1_state',
     'S2': 'source_defined_s2_state',
     'S3': 'source_defined_s3_state',
     'S4': 'source_defined_s4_state',
     'S5': 'source_defined_s5_state',
     'S6': 'source_defined_s6_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000487.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cao2013ApplicationOfAbsisInTheTheEnzymatiBiomd0000000487Model = Cao2013ApplicationOfAbsisInTheTheEnzymatiModel
