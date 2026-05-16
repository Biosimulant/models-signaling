# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yan2012 - Rb-E2F pathway dynamics with miR449."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yan2012RbE2fPathwayDynamicsWithMir449Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000720'
    _TITLE = 'Yan2012 - Rb-E2F pathway dynamics with miR449'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'e2f': ('E2F',
             'native SBML value',
             'E2F. Maps to SBML symbol `E2F` and is emitted in native SBML units.'),
     'myc_transcription_factor': ('Myc',
                                  'native SBML value',
                                  'MYC transcription factor. Maps to SBML symbol `Myc` and is emitted '
                                  'in native SBML units.'),
     'source_defined_cycd_state': ('CycD',
                                   'native SBML value',
                                   'source-defined CYCD state. Maps to SBML symbol `CycD` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_s_state': ('S',
                                        3.0,
                                        'native SBML value',
                                        'Initial level of source-defined S state. Maps to SBML symbol '
                                        '`S`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'E2F': 'E2F',
     'Myc': 'MYC transcription factor',
     'CycD': 'source-defined CYCD state',
     'RE': 'source-defined RE state',
     'CycE': 'source-defined CYCE state',
     'RB': 'source-defined RB state',
     'miR449': 'Mi R449',
     'S': 'source-defined S state',
     'PRB': 'source-defined PRB state'}
    _STATE_OUTPUT_ALIASES = {'E2F': 'e2f',
     'Myc': 'myc_transcription_factor',
     'CycD': 'source_defined_cycd_state',
     'RE': 'source_defined_re_state',
     'CycE': 'source_defined_cyce_state',
     'RB': 'source_defined_rb_state',
     'miR449': 'mi_r449',
     'S': 'source_defined_s_state',
     'PRB': 'source_defined_prb_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000720.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Yan2012RbE2fPathwayDynamicsWithMir449Biomd0000000720Model = Yan2012RbE2fPathwayDynamicsWithMir449Model
