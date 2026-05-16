# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dasgupta2020 - Reduced model of receptor clusturing and aggregation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dasgupta2020ReducedModelOfReceptorClusturinModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000973'
    _TITLE = 'Dasgupta2020 - Reduced model of receptor clusturing and aggregation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_p_state': ('P',
                                'native SBML value',
                                'source-defined P state. Maps to SBML symbol `P` and is emitted in '
                                'native SBML units.'),
     'source_defined_n_state': ('N',
                                'native SBML value',
                                'source-defined N state. Maps to SBML symbol `N` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_p_state': ('P',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined P state. Maps to SBML symbol '
                                        '`P`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'P': 'source-defined P state', 'N': 'source-defined N state'}
    _STATE_OUTPUT_ALIASES = {'P': 'source_defined_p_state', 'N': 'source_defined_n_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000973.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dasgupta2020ReducedModelOfReceptorClusturinBiomd0000000973Model = Dasgupta2020ReducedModelOfReceptorClusturinModel
