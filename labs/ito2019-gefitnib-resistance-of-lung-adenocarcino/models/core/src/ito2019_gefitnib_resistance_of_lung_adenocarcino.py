# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ito2019 - gefitnib resistance of lung adenocarcinoma caused by MET amplification."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ito2019GefitnibResistanceOfLungAdenocarcinoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000827'
    _TITLE = 'Ito2019 - gefitnib resistance of lung adenocarcinoma caused by MET amplification'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'x_1_egfr': ('X_1_EGFR',
                  'native SBML value',
                  'X 1 EGFR. Maps to SBML symbol `X_1_EGFR` and is emitted in native SBML units.'),
     'x_4_egfr_egfr': ('X_4_EGFR_EGFR',
                       'native SBML value',
                       'X 4 EGFR EGFR. Maps to SBML symbol `X_4_EGFR_EGFR` and is emitted in native '
                       'SBML units.'),
     'x_2_erb_b3': ('X_2_ErbB3',
                    'native SBML value',
                    'X 2 Erb B3. Maps to SBML symbol `X_2_ErbB3` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_x_1_egfr': ('X_1_EGFR',
                          3.6e-12,
                          'native SBML value',
                          'Initial level of X 1 EGFR. Maps to SBML symbol `X_1_EGFR`; exposed as a '
                          'traceable initial-condition perturbation.'),
     'initial_x_4_egfr_egfr': ('X_4_EGFR_EGFR',
                               0.0,
                               'native SBML value',
                               'Initial level of X 4 EGFR EGFR. Maps to SBML symbol `X_4_EGFR_EGFR`; '
                               'exposed as a traceable initial-condition perturbation.'),
     'initial_x_5_egfr_erb_b3': ('X_5_EGFR_ErbB3',
                                 0.0,
                                 'native SBML value',
                                 'Initial level of X 5 EGFR Erb B3. Maps to SBML symbol '
                                 '`X_5_EGFR_ErbB3`; exposed as a traceable initial-condition '
                                 'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'X_1_EGFR': 'X 1 EGFR',
     'X_4_EGFR_EGFR': 'X 4 EGFR EGFR',
     'X_2_ErbB3': 'X 2 Erb B3',
     'X_6_ErbB3_ErbB3': 'X 6 Erb B3 Erb B3',
     'X_5_EGFR_ErbB3': 'X 5 EGFR Erb B3',
     'X_3_MET': 'X 3 MET',
     'X_7_MET_MET': 'X 7 MET MET',
     'X_10_p_MET_MET': 'X 10 P MET MET',
     'X_8_p_EGFR_ErbB3': 'X 8 P EGFR Erb B3',
     'X_9_p_ErbB3_ErbB3': 'X 9 P Erb B3 Erb B3'}
    _STATE_OUTPUT_ALIASES = {'X_1_EGFR': 'x_1_egfr',
     'X_4_EGFR_EGFR': 'x_4_egfr_egfr',
     'X_2_ErbB3': 'x_2_erb_b3',
     'X_6_ErbB3_ErbB3': 'x_6_erb_b3_erb_b3',
     'X_5_EGFR_ErbB3': 'x_5_egfr_erb_b3',
     'X_3_MET': 'x_3_met',
     'X_7_MET_MET': 'x_7_met_met',
     'X_10_p_MET_MET': 'x_10_p_met_met',
     'X_8_p_EGFR_ErbB3': 'x_8_p_egfr_erb_b3',
     'X_9_p_ErbB3_ErbB3': 'x_9_p_erb_b3_erb_b3'}

    def __init__(self, model_path: str = 'data/BIOMD0000000827.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Ito2019GefitnibResistanceOfLungAdenocarcinoBiomd0000000827Model = Ito2019GefitnibResistanceOfLungAdenocarcinoModel
