# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ortega2006 - bistability from double phosphorylation in signal transduction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ortega2006BistabilityFromDoublePhosphorylatiModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000258'
    _TITLE = 'Ortega2006 - bistability from double phosphorylation in signal transduction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'alpha': ('alpha',
               'native SBML value',
               'Alpha. Maps to SBML symbol `alpha` and is emitted in native SBML units.'),
     'beta_response_parameter': ('beta',
                                 'native SBML value',
                                 'beta response parameter. Maps to SBML symbol `beta` and is emitted '
                                 'in native SBML units.'),
     'gamma': ('gamma',
               'native SBML value',
               'Gamma. Maps to SBML symbol `gamma` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_alpha': ('alpha',
                       0.0,
                       'native SBML value',
                       'Initial level of Alpha. Maps to SBML symbol `alpha`; exposed as a traceable '
                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'alpha': 'Alpha', 'beta': 'beta response parameter', 'gamma': 'Gamma'}
    _STATE_OUTPUT_ALIASES = {'alpha': 'alpha', 'beta': 'beta_response_parameter', 'gamma': 'gamma'}

    def __init__(self, model_path: str = 'data/BIOMD0000000258.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Ortega2006BistabilityFromDoublePhosphorylatiBiomd0000000258Model = Ortega2006BistabilityFromDoublePhosphorylatiModel
