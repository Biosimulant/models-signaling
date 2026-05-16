# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Park2019 - IL7 receptor signaling in T cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Park2019Il7ReceptorSignalingInTCellsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000803'
    _TITLE = 'Park2019 - IL7 receptor signaling in T cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'il7ra': ('IL7Ra',
               'native SBML value',
               'Il7ra. Maps to SBML symbol `IL7Ra` and is emitted in native SBML units.'),
     'il15rbeta': ('IL15Rbeta',
                   'native SBML value',
                   'Il15rbeta. Maps to SBML symbol `IL15Rbeta` and is emitted in native SBML units.'),
     'gamma_c': ('gamma_c',
                 'native SBML value',
                 'Gamma C. Maps to SBML symbol `gamma_c` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_il7ra': ('IL7Ra',
                       0.0,
                       'native SBML value',
                       'Initial level of Il7ra. Maps to SBML symbol `IL7Ra`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IL7Ra': 'Il7ra',
     'IL15Rbeta': 'Il15rbeta',
     'gamma_c': 'Gamma C',
     'IL7Ru': 'Il7ru',
     'IL15Ru': 'Il15ru',
     'IL7Rb': 'Il7rb',
     'IL15Rb': 'Il15rb',
     'IL7': 'source-defined IL7 state',
     'IL15': 'IL15'}
    _STATE_OUTPUT_ALIASES = {'IL7Ra': 'il7ra',
     'IL15Rbeta': 'il15rbeta',
     'gamma_c': 'gamma_c',
     'IL7Ru': 'il7ru',
     'IL15Ru': 'il15ru',
     'IL7Rb': 'il7rb',
     'IL15Rb': 'il15rb',
     'IL7': 'source_defined_il7_state',
     'IL15': 'il15'}

    def __init__(self, model_path: str = 'data/BIOMD0000000803.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Park2019Il7ReceptorSignalingInTCellsBiomd0000000803Model = Park2019Il7ReceptorSignalingInTCellsModel
