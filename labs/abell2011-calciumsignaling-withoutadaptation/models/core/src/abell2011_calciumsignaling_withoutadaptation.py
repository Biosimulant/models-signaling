# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Abell2011_CalciumSignaling_WithoutAdaptation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Abell2011CalciumsignalingWithoutadaptationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000354'
    _TITLE = 'Abell2011_CalciumSignaling_WithoutAdaptation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'intracellular_calcium': ('CaI',
                               'native SBML value',
                               'intracellular calcium. Maps to SBML symbol `CaI` and is emitted in '
                               'native SBML units.'),
     'extracellular_calcium': ('CaO',
                               'native SBML value',
                               'extracellular calcium. Maps to SBML symbol `CaO` and is emitted in '
                               'native SBML units.'),
     'stored_calcium': ('CaS',
                        'native SBML value',
                        'stored calcium. Maps to SBML symbol `CaS` and is emitted in native SBML '
                        'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_calcium': ('CaI',
                                       0.0,
                                       'native SBML value',
                                       'Initial level of intracellular calcium. Maps to SBML symbol '
                                       '`CaI`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'CaI': 'intracellular calcium',
     'IP3': 'IP3',
     'g': 'source-defined G state',
     'CaO': 'extracellular calcium',
     'CaS': 'stored calcium',
     'CaM': 'calmodulin'}
    _STATE_OUTPUT_ALIASES = {'CaI': 'intracellular_calcium',
     'IP3': 'ip3',
     'g': 'source_defined_g_state',
     'CaO': 'extracellular_calcium',
     'CaS': 'stored_calcium',
     'CaM': 'calmodulin'}

    def __init__(self, model_path: str = 'data/BIOMD0000000354.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Abell2011CalciumsignalingWithoutadaptationBiomd0000000354Model = Abell2011CalciumsignalingWithoutadaptationModel
