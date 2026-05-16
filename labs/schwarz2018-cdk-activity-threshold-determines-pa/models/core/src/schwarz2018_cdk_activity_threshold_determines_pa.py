# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schwarz2018-Cdk Activity Threshold Determines Passage through the Restriction Point."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schwarz2018CdkActivityThresholdDeterminesPaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000918'
    _TITLE = 'Schwarz2018-Cdk Activity Threshold Determines Passage through the Restriction Point'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphorylated_rb': ('Phosphorylated_Rb',
                           'native SBML value',
                           'Phosphorylated Rb. Maps to SBML symbol `Phosphorylated_Rb` and is emitted '
                           'in native SBML units.'),
     'rb_e2f_complex': ('Rb_E2F_complex',
                        'native SBML value',
                        'Rb E2F Complex. Maps to SBML symbol `Rb_E2F_complex` and is emitted in native '
                        'SBML units.'),
     'myc_transcription_factor': ('Myc',
                                  'native SBML value',
                                  'MYC transcription factor. Maps to SBML symbol `Myc` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_myc_transcription_factor': ('Myc',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of MYC transcription factor. Maps to SBML '
                                          'symbol `Myc`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Myc': 'MYC transcription factor',
     'E2F': 'E2F',
     'CycD': 'source-defined CYCD state',
     'CycE': 'source-defined CYCE state',
     'Rb': 'source-defined RB state',
     'Phosphorylated_Rb': 'Phosphorylated Rb',
     'Rb_E2F_complex': 'Rb E2F Complex',
     'serum': 'Serum'}
    _STATE_OUTPUT_ALIASES = {'Myc': 'myc_transcription_factor',
     'E2F': 'e2f',
     'CycD': 'source_defined_cycd_state',
     'CycE': 'source_defined_cyce_state',
     'Rb': 'source_defined_rb_state',
     'Phosphorylated_Rb': 'phosphorylated_rb',
     'Rb_E2F_complex': 'rb_e2f_complex',
     'serum': 'serum'}

    def __init__(self, model_path: str = 'data/BIOMD0000000918.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Schwarz2018CdkActivityThresholdDeterminesPaBiomd0000000918Model = Schwarz2018CdkActivityThresholdDeterminesPaModel
