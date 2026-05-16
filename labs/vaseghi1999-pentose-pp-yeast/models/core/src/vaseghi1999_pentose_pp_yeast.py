# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Vaseghi1999_Pentose_PP_yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vaseghi1999PentosePpYeastModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1004070001'
    _TITLE = 'Vaseghi1999_Pentose_PP_yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glucose_6_phosphate': ('C_G6P',
                             'native SBML value',
                             'Glucose 6 Phosphate. Maps to SBML symbol `C_G6P` and is emitted in '
                             'native SBML units.'),
     'source_6_phosphogluconate': ('C_6PG',
                                   'native SBML value',
                                   '6 Phosphogluconate. Maps to SBML symbol `C_6PG` and is emitted in '
                                   'native SBML units.'),
     'ribulose_5_phosphate': ('C_Ru5P',
                              'native SBML value',
                              'Ribulose 5 Phosphate. Maps to SBML symbol `C_Ru5P` and is emitted in '
                              'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_fructose_6_phosphate': ('C_F6P',
                                      0.17,
                                      'native SBML value',
                                      'Initial level of Fructose 6 Phosphate. Maps to SBML symbol '
                                      '`C_F6P`; exposed as a traceable initial-condition '
                                      'perturbation.'),
     'initial_glucose_6_phosphate': ('C_G6P',
                                     0.9,
                                     'native SBML value',
                                     'Initial level of Glucose 6 Phosphate. Maps to SBML symbol '
                                     '`C_G6P`; exposed as a traceable initial-condition perturbation.'),
     'initial_glyceraldehyde_3_phosphate': ('C_GAP',
                                            0.064,
                                            'native SBML value',
                                            'Initial level of Glyceraldehyde 3 Phosphate. Maps to SBML '
                                            'symbol `C_GAP`; exposed as a traceable initial-condition '
                                            'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C_G6P': 'Glucose 6 Phosphate',
     'C_6PG': '6 Phosphogluconate',
     'C_Ru5P': 'Ribulose 5 Phosphate',
     'C_X5P': 'Xylulose 5 Phosphate',
     'C_F6P': 'Fructose 6 Phosphate',
     'C_E4P': 'Erythrose 4 Phosphate',
     'C_GAP': 'Glyceraldehyde 3 Phosphate',
     'C_R5P': 'Ribose 5 Phosphate',
     'C_S7P': 'Sedoheptulose 7 Phosphate',
     'C_PRPP': 'Phosphoribosylpyrophosphate',
     'C_PHE': 'Phenylalanine',
     'C_TYR': 'Tyrosine',
     'C_TRP': 'Tryptophan',
     'C_NADP': 'source-defined NADP+ state',
     'C_NADPH': 'NADPH',
     'C_MgATP': 'Mg ATP'}
    _STATE_OUTPUT_ALIASES = {'C_G6P': 'glucose_6_phosphate',
     'C_6PG': 'source_6_phosphogluconate',
     'C_Ru5P': 'ribulose_5_phosphate',
     'C_X5P': 'xylulose_5_phosphate',
     'C_F6P': 'fructose_6_phosphate',
     'C_E4P': 'erythrose_4_phosphate',
     'C_GAP': 'glyceraldehyde_3_phosphate',
     'C_R5P': 'ribose_5_phosphate',
     'C_S7P': 'sedoheptulose_7_phosphate',
     'C_PRPP': 'phosphoribosylpyrophosphate',
     'C_PHE': 'phenylalanine',
     'C_TYR': 'tyrosine',
     'C_TRP': 'tryptophan',
     'C_NADP': 'source_defined_nadp_state',
     'C_NADPH': 'nadph',
     'C_MgATP': 'mg_atp'}

    def __init__(self, model_path: str = 'data/MODEL1004070001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Vaseghi1999PentosePpYeastModel1004070001Model = Vaseghi1999PentosePpYeastModel
