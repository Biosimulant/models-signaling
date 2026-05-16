# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Messiha2013 - Pentose phosphate pathway model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Messiha2013PentosePhosphatePathwayModelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000502'
    _TITLE = 'Messiha2013 - Pentose phosphate pathway model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'e4p': ('E4P',
             'native SBML value',
             'E4P. Maps to SBML symbol `E4P` and is emitted in native SBML units.'),
     'g6l': ('G6L',
             'native SBML value',
             'G6L. Maps to SBML symbol `G6L` and is emitted in native SBML units.'),
     'nadph': ('NADPH',
               'native SBML value',
               'NADPH. Maps to SBML symbol `NADPH` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_f6p': ('F6P',
                     0.325,
                     'native SBML value',
                     'Initial level of F6P. Maps to SBML symbol `F6P`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_g6p': ('G6P',
                     0.9,
                     'native SBML value',
                     'Initial level of G6P. Maps to SBML symbol `G6P`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_source_defined_gap_state': ('GAP',
                                          0.067,
                                          'native SBML value',
                                          'Initial level of source-defined GAP state. Maps to SBML '
                                          'symbol `GAP`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'E4P': 'E4P',
     'G6L': 'G6L',
     'NADPH': 'NADPH',
     'P6G': 'P6G',
     'R5P': 'R5P',
     'Ru5P': 'Ru5p',
     'S7P': 'S7P',
     'X5P': 'X5P',
     'NADP': 'source-defined NADP state',
     'G6P': 'G6P',
     'F6P': 'F6P',
     'GAP': 'source-defined GAP state',
     'GND1': 'source-defined GND1 state',
     'GND2': 'source-defined GND2 state',
     'NQM1': 'source-defined NQM1 state',
     'RKI1': 'source-defined RKI1 state',
     'RPE1': 'source-defined RPE1 state',
     'SOL3': 'source-defined SOL3 state',
     'TAL1': 'source-defined TAL1 state',
     'TKL1': 'source-defined TKL1 state',
     'ZWF1': 'source-defined ZWF1 state'}
    _STATE_OUTPUT_ALIASES = {'E4P': 'e4p',
     'G6L': 'g6l',
     'NADPH': 'nadph',
     'P6G': 'p6g',
     'R5P': 'r5p',
     'Ru5P': 'ru5p',
     'S7P': 's7p',
     'X5P': 'x5p',
     'NADP': 'source_defined_nadp_state',
     'G6P': 'g6p',
     'F6P': 'f6p',
     'GAP': 'source_defined_gap_state',
     'GND1': 'source_defined_gnd1_state',
     'GND2': 'source_defined_gnd2_state',
     'NQM1': 'source_defined_nqm1_state',
     'RKI1': 'source_defined_rki1_state',
     'RPE1': 'source_defined_rpe1_state',
     'SOL3': 'source_defined_sol3_state',
     'TAL1': 'source_defined_tal1_state',
     'TKL1': 'source_defined_tkl1_state',
     'ZWF1': 'source_defined_zwf1_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000502.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Messiha2013PentosePhosphatePathwayModelBiomd0000000502Model = Messiha2013PentosePhosphatePathwayModelModel
