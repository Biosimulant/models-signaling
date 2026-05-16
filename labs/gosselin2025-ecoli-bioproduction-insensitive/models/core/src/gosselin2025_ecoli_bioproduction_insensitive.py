# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gosselin2025 - Ecoli_bioproduction_insensitive."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gosselin2025EcoliBioproductionInsensitiveModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2506160001'
    _TITLE = 'Gosselin2025 - Ecoli_bioproduction_insensitive'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glucose': ('Glc',
                 'native SBML value',
                 'glucose. Maps to SBML symbol `Glc` and is emitted in native SBML units.'),
     'source_defined_acp_state': ('AcP',
                                  'native SBML value',
                                  'source-defined ACP state. Maps to SBML symbol `AcP` and is emitted '
                                  'in native SBML units.'),
     'acetate': ('Ace',
                 'native SBML value',
                 'acetate. Maps to SBML symbol `Ace` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_acetate_out': ('Ace_out',
                             10.0,
                             'native SBML value',
                             'Initial level of acetate Out. Maps to SBML symbol `Ace_out`; exposed as '
                             'a traceable initial-condition perturbation.'),
     'initial_glucose': ('Glc',
                         20.0,
                         'native SBML value',
                         'Initial level of glucose. Maps to SBML symbol `Glc`; exposed as a traceable '
                         'initial-condition perturbation.'),
     'initial_response_node_x': ('X',
                                 0.1,
                                 'native SBML value',
                                 'Initial level of response node X. Maps to SBML symbol `X`; exposed '
                                 'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Glc': 'glucose',
     'AcP': 'source-defined ACP state',
     'Ace': 'acetate',
     'AcCoA': 'Ac Co A',
     'X': 'response node X',
     'Ace_out': 'acetate Out',
     'product': 'Product'}
    _STATE_OUTPUT_ALIASES = {'Glc': 'glucose',
     'AcP': 'source_defined_acp_state',
     'Ace': 'acetate',
     'AcCoA': 'ac_co_a',
     'X': 'response_node_x',
     'Ace_out': 'acetate_out',
     'product': 'product'}

    def __init__(self, model_path: str = 'data/MODEL2506160001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gosselin2025EcoliBioproductionInsensitiveModel2506160001Model = Gosselin2025EcoliBioproductionInsensitiveModel
