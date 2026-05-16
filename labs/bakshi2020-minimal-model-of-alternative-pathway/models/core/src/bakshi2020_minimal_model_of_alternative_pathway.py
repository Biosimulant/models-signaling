# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bakshi2020 - Minimal model of alternative pathway of complement system."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bakshi2020MinimalModelOfAlternativePathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001017'
    _TITLE = 'Bakshi2020 - Minimal model of alternative pathway of complement system'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'complement_c3b': ('C3b',
                        'native SBML value',
                        'complement C3b. Maps to SBML symbol `C3b` and is emitted in native SBML '
                        'units.'),
     'closed_complement_c3bb_complex': ('C3bB_closed',
                                        'native SBML value',
                                        'closed complement C3bB complex. Maps to SBML symbol '
                                        '`C3bB_closed` and is emitted in native SBML units.'),
     'open_complement_c3bb_complex': ('C3bB_open',
                                      'native SBML value',
                                      'open complement C3bB complex. Maps to SBML symbol `C3bB_open` '
                                      'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_complement_factor_b': ('Factor_B',
                                     2.0,
                                     'native SBML value',
                                     'Initial level of complement factor B. Maps to SBML symbol '
                                     '`Factor_B`; exposed as a traceable initial-condition '
                                     'perturbation.'),
     'initial_complement_factor_d': ('Factor_D',
                                     0.08,
                                     'native SBML value',
                                     'Initial level of complement factor D. Maps to SBML symbol '
                                     '`Factor_D`; exposed as a traceable initial-condition '
                                     'perturbation.'),
     'initial_complement_factor_h': ('Factor_H',
                                     3.0,
                                     'native SBML value',
                                     'Initial level of complement factor H. Maps to SBML symbol '
                                     '`Factor_H`; exposed as a traceable initial-condition '
                                     'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C3': 'complement C3',
     'C3b': 'complement C3b',
     'C3bB_closed': 'closed complement C3bB complex',
     'C3bB_open': 'open complement C3bB complex',
     'C3bBb': 'complement C3b complement factor Bb',
     'C3bBbH': 'complement C3b complement factor Bb H',
     'Bb': 'complement factor Bb',
     'Factor_H': 'complement factor H',
     'Factor_B': 'complement factor B',
     'C3bH': 'complement C3b H',
     'Factor_I': 'Factor I',
     'iC3b': 'inactive complement iC3b',
     'Factor_D': 'complement factor D'}
    _STATE_OUTPUT_ALIASES = {'C3': 'complement_c3',
     'C3b': 'complement_c3b',
     'C3bB_closed': 'closed_complement_c3bb_complex',
     'C3bB_open': 'open_complement_c3bb_complex',
     'C3bBb': 'complement_c3b_complement_factor_bb',
     'C3bBbH': 'complement_c3b_complement_factor_bb_h',
     'Bb': 'complement_factor_bb',
     'Factor_H': 'complement_factor_h',
     'Factor_B': 'complement_factor_b',
     'C3bH': 'complement_c3b_h',
     'Factor_I': 'factor_i',
     'iC3b': 'inactive_complement_ic3b',
     'Factor_D': 'complement_factor_d'}

    def __init__(self, model_path: str = 'data/BIOMD0000001017.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bakshi2020MinimalModelOfAlternativePathwayBiomd0000001017Model = Bakshi2020MinimalModelOfAlternativePathwayModel
