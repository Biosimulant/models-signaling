# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bakshi2020 - Properdin model of alternative pathway of complement system."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bakshi2020ProperdinModelOfAlternativePathwaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001018'
    _TITLE = 'Bakshi2020 - Properdin model of alternative pathway of complement system'
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
    _INITIAL_CONDITION_INPUTS = {'initial_complement_c3b_total': ('C3b_total',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of complement C3b Total. Maps to SBML symbol '
                                      '`C3b_total`; exposed as a traceable initial-condition '
                                      'perturbation.'),
     'initial_complement_c3b_b_closed_total': ('C3bB_closed_total',
                                               0.0,
                                               'native SBML value',
                                               'Initial level of complement C3b B closed Total. Maps '
                                               'to SBML symbol `C3bB_closed_total`; exposed as a '
                                               'traceable initial-condition perturbation.'),
     'initial_complement_c3b_b_open_total': ('C3bB_open_total',
                                             0.0,
                                             'native SBML value',
                                             'Initial level of complement C3b B open Total. Maps to '
                                             'SBML symbol `C3bB_open_total`; exposed as a traceable '
                                             'initial-condition perturbation.')}
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
     'Factor_D': 'complement factor D',
     'Properdin': 'Properdin',
     'C3bBP_closed': 'complement C3b BP closed',
     'C3bBP_open': 'complement C3b BP open',
     'C3bBbP': 'complement C3b complement factor Bb P',
     'C3bP': 'complement C3b P',
     'C3b_total': 'complement C3b Total',
     'C3bB_closed_total': 'complement C3b B closed Total',
     'C3bB_open_total': 'complement C3b B open Total',
     'C3bBb_total': 'complement C3b complement factor Bb Total'}
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
     'Factor_D': 'complement_factor_d',
     'Properdin': 'properdin',
     'C3bBP_closed': 'complement_c3b_bp_closed',
     'C3bBP_open': 'complement_c3b_bp_open',
     'C3bBbP': 'complement_c3b_complement_factor_bb_p',
     'C3bP': 'complement_c3b_p',
     'C3b_total': 'complement_c3b_total',
     'C3bB_closed_total': 'complement_c3b_b_closed_total',
     'C3bB_open_total': 'complement_c3b_b_open_total',
     'C3bBb_total': 'complement_c3b_complement_factor_bb_total'}

    def __init__(self, model_path: str = 'data/BIOMD0000001018.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bakshi2020ProperdinModelOfAlternativePathwaBiomd0000001018Model = Bakshi2020ProperdinModelOfAlternativePathwaModel
