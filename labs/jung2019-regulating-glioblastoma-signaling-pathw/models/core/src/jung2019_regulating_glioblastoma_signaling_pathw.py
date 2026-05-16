# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jung2019 - Regulating glioblastoma signaling pathways and anti-invasion therapy - core control model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jung2019RegulatingGlioblastomaSignalingPathwModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000828'
    _TITLE = 'Jung2019 - Regulating glioblastoma signaling pathways and anti-invasion therapy - core control model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glucose_g': ('Glucose_G',
                   'substance',
                   'Glucose G. Maps to SBML symbol `Glucose_G` and is emitted in native SBML units.'),
     'drug_d': ('Drug_D',
                'substance',
                'Drug D. Maps to SBML symbol `Drug_D` and is emitted in native SBML units.'),
     'mi_r_451_m': ('miR_451_M',
                    'substance',
                    'Mi R 451 M. Maps to SBML symbol `miR_451_M` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_delta_d': ('deltaD',
                         1.0,
                         'substance',
                         'Initial level of Delta D. Maps to SBML symbol `deltaD`; exposed as a '
                         'traceable initial-condition perturbation.'),
     'initial_drug_d': ('Drug_D',
                        0.0,
                        'substance',
                        'Initial level of Drug D. Maps to SBML symbol `Drug_D`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_glucose_g': ('Glucose_G',
                           6.64215616170866e-22,
                           'substance',
                           'Initial level of Glucose G. Maps to SBML symbol `Glucose_G`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Glucose_G': 'Glucose G',
     'Drug_D': 'Drug D',
     'miR_451_M': 'Mi R 451 M',
     'AMPK_A': 'AMPK A',
     'mTOR_R': 'M TOR R',
     'deltaD': 'Delta D'}
    _STATE_OUTPUT_ALIASES = {'Glucose_G': 'glucose_g',
     'Drug_D': 'drug_d',
     'miR_451_M': 'mi_r_451_m',
     'AMPK_A': 'ampk_a',
     'mTOR_R': 'm_tor_r',
     'deltaD': 'delta_d'}

    def __init__(self, model_path: str = 'data/BIOMD0000000828.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Jung2019RegulatingGlioblastomaSignalingPathwBiomd0000000828Model = Jung2019RegulatingGlioblastomaSignalingPathwModel
