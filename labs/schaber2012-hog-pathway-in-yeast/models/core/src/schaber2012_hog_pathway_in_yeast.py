# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schaber2012 - Hog pathway in yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schaber2012HogPathwayInYeastModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000429'
    _TITLE = 'Schaber2012 - Hog pathway in yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphatase': ('species_6',
                     'native SBML value',
                     'Phosphatase. Maps to SBML symbol `species_6` and is emitted in native SBML '
                     'units.'),
     'hog1ppactive': ('species_12',
                      'native SBML value',
                      'Hog1ppactive. Maps to SBML symbol `species_12` and is emitted in native SBML '
                      'units.'),
     'glyin': ('species_1',
               'native SBML value',
               'Glyin. Maps to SBML symbol `species_1` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_hog1ppactive': ('species_12',
                              0.201092527399535,
                              'native SBML value',
                              'Initial level of Hog1ppactive. Maps to SBML symbol `species_12`; '
                              'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'Glyin',
     'species_2': 'source-defined HOG1 state',
     'species_3': 'Hog1pp',
     'species_4': 'source-defined PBS2 state',
     'species_5': 'Pbs2p',
     'species_6': 'Phosphatase',
     'species_7': 'Protein',
     'species_8': 'source-defined RNA state',
     'species_9': 'Hog1p',
     'species_10': 'source-defined SHO1 state',
     'species_11': 'Sho1pbs2p',
     'species_12': 'Hog1ppactive',
     'species_13': 'Glyex',
     'species_14': 'source-defined FPS1 state',
     'species_15': 'Fps1p'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'glyin',
     'species_2': 'source_defined_hog1_state',
     'species_3': 'hog1pp',
     'species_4': 'source_defined_pbs2_state',
     'species_5': 'pbs2p',
     'species_6': 'phosphatase',
     'species_7': 'protein',
     'species_8': 'source_defined_rna_state',
     'species_9': 'hog1p',
     'species_10': 'source_defined_sho1_state',
     'species_11': 'sho1pbs2p',
     'species_12': 'hog1ppactive',
     'species_13': 'glyex',
     'species_14': 'source_defined_fps1_state',
     'species_15': 'fps1p'}

    def __init__(self, model_path: str = 'data/BIOMD0000000429.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Schaber2012HogPathwayInYeastBiomd0000000429Model = Schaber2012HogPathwayInYeastModel
