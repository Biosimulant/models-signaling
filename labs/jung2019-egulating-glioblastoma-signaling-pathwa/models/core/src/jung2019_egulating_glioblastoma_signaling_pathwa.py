# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jung2019 - egulating glioblastoma signaling pathways and anti-invasion therapy cell cycle dynamics model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jung2019EgulatingGlioblastomaSignalingPathwaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000829'
    _TITLE = 'Jung2019 - egulating glioblastoma signaling pathways and anti-invasion therapy cell cycle dynamics model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glucose_g': ('Glucose_G',
                   'native SBML value',
                   'Glucose G. Maps to SBML symbol `Glucose_G` and is emitted in native SBML units.'),
     'drug_d': ('Drug_D',
                'native SBML value',
                'Drug D. Maps to SBML symbol `Drug_D` and is emitted in native SBML units.'),
     'mi_r_451_m': ('miR_451_M',
                    'native SBML value',
                    'Mi R 451 M. Maps to SBML symbol `miR_451_M` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_delta_d': ('deltaD',
                         1.0,
                         'native SBML value',
                         'Initial level of Delta D. Maps to SBML symbol `deltaD`; exposed as a '
                         'traceable initial-condition perturbation.'),
     'initial_mass_s': ('mass_s',
                        2.95,
                        'native SBML value',
                        'Initial level of Mass S. Maps to SBML symbol `mass_s`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_drug_d': ('Drug_D',
                        0.0,
                        'native SBML value',
                        'Initial level of Drug D. Maps to SBML symbol `Drug_D`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Glucose_G': 'Glucose G',
     'Drug_D': 'Drug D',
     'miR_451_M': 'Mi R 451 M',
     'AMPK_A': 'AMPK A',
     'mTOR_R': 'M TOR R',
     'deltaD': 'Delta D',
     'Cdh1': 'Cdh1 cell-cycle regulator',
     'CycB': 'source-defined CYCB state',
     'p55cdc_T': 'P55cdc T',
     'mass': 'source-defined MASS state',
     'mass_s': 'Mass S',
     'p55cdc_A': 'P55cdc A',
     'Plk1': 'source-defined PLK1 state'}
    _STATE_OUTPUT_ALIASES = {'Glucose_G': 'glucose_g',
     'Drug_D': 'drug_d',
     'miR_451_M': 'mi_r_451_m',
     'AMPK_A': 'ampk_a',
     'mTOR_R': 'm_tor_r',
     'deltaD': 'delta_d',
     'Cdh1': 'cdh1_cell_cycle_regulator',
     'CycB': 'source_defined_cycb_state',
     'p55cdc_T': 'p55cdc_t',
     'mass': 'source_defined_mass_state',
     'mass_s': 'mass_s',
     'p55cdc_A': 'p55cdc_a',
     'Plk1': 'source_defined_plk1_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000829.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Jung2019EgulatingGlioblastomaSignalingPathwaBiomd0000000829Model = Jung2019EgulatingGlioblastomaSignalingPathwaModel
