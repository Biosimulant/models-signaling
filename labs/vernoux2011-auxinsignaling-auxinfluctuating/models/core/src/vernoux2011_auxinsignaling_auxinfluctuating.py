# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Vernoux2011_AuxinSignaling_AuxinFluctuating."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vernoux2011AuxinsignalingAuxinfluctuatingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000352'
    _TITLE = 'Vernoux2011_AuxinSignaling_AuxinFluctuating'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'aux_indole_3_acetic_acid': ('I',
                                  'native SBML value',
                                  'Aux indole-3-acetic acid. Maps to SBML symbol `I` and is emitted in '
                                  'native SBML units.'),
     'auxin_response_factor': ('A',
                               'native SBML value',
                               'auxin response factor. Maps to SBML symbol `A` and is emitted in '
                               'native SBML units.'),
     'aux_indole_3_acetic_acid_aux_indole_3_acetic_acid': ('D_II',
                                                           'native SBML value',
                                                           'Aux indole-3-acetic acid Aux '
                                                           'indole-3-acetic acid. Maps to SBML symbol '
                                                           '`D_II` and is emitted in native SBML '
                                                           'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_auxin': ('aux',
                       1.11,
                       'native SBML value',
                       'Initial level of Auxin. Maps to SBML symbol `aux`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'I': 'Aux indole-3-acetic acid',
     'A': 'auxin response factor',
     'D_II': 'Aux indole-3-acetic acid Aux indole-3-acetic acid',
     'D_IA': 'Aux indole-3-acetic acid auxin response factor',
     'R': 'source-defined MRNA state',
     'aux': 'Auxin'}
    _STATE_OUTPUT_ALIASES = {'I': 'aux_indole_3_acetic_acid',
     'A': 'auxin_response_factor',
     'D_II': 'aux_indole_3_acetic_acid_aux_indole_3_acetic_acid',
     'D_IA': 'aux_indole_3_acetic_acid_auxin_response_factor',
     'R': 'source_defined_mrna_state',
     'aux': 'auxin'}

    def __init__(self, model_path: str = 'data/BIOMD0000000352.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Vernoux2011AuxinsignalingAuxinfluctuatingBiomd0000000352Model = Vernoux2011AuxinsignalingAuxinfluctuatingModel
