# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Goldbeter1991 - Min Mit Oscil, Expl Inact."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter1991MinMitOscilExplInactModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000004'
    _TITLE = 'Goldbeter1991 - Min Mit Oscil, Expl Inact'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'active_cdc_2_kinase': ('M',
                             'substance',
                             'active CDC 2 Kinase. Maps to SBML symbol `M` and is emitted in native '
                             'SBML units.'),
     'active_cyclin_protease': ('X',
                                'substance',
                                'active Cyclin Protease. Maps to SBML symbol `X` and is emitted in '
                                'native SBML units.'),
     'inactive_cdc_2_kinase': ('MI',
                               'substance',
                               'Inactive CDC 2 Kinase. Maps to SBML symbol `MI` and is emitted in '
                               'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cyclin': ('C',
                        0.0,
                        'native SBML value',
                        'Initial level of Cyclin. Maps to SBML symbol `C`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C': 'Cyclin',
     'M': 'active CDC 2 Kinase',
     'X': 'active Cyclin Protease',
     'MI': 'Inactive CDC 2 Kinase',
     'XI': 'Inactive Cyclin Protease'}
    _STATE_OUTPUT_ALIASES = {'C': 'cyclin',
     'M': 'active_cdc_2_kinase',
     'X': 'active_cyclin_protease',
     'MI': 'inactive_cdc_2_kinase',
     'XI': 'inactive_cyclin_protease'}

    def __init__(self, model_path: str = 'data/BIOMD0000000004.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Goldbeter1991MinMitOscilExplInactBiomd0000000004Model = Goldbeter1991MinMitOscilExplInactModel
