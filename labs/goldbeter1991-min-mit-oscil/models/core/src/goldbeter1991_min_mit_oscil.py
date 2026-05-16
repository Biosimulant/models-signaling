# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Goldbeter1991 - Min Mit Oscil."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter1991MinMitOscilModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000003'
    _TITLE = 'Goldbeter1991 - Min Mit Oscil'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cyclin': ('C',
                'substance',
                'Cyclin. Maps to SBML symbol `C` and is emitted in native SBML units.'),
     'cdc_2_kinase': ('M',
                      'substance',
                      'CDC 2 Kinase. Maps to SBML symbol `M` and is emitted in native SBML units.'),
     'cyclin_protease': ('X',
                         'substance',
                         'Cyclin Protease. Maps to SBML symbol `X` and is emitted in native SBML '
                         'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cyclin': ('C',
                        0.0,
                        'native SBML value',
                        'Initial level of Cyclin. Maps to SBML symbol `C`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'C': 'Cyclin', 'M': 'CDC 2 Kinase', 'X': 'Cyclin Protease'}
    _STATE_OUTPUT_ALIASES = {'C': 'cyclin', 'M': 'cdc_2_kinase', 'X': 'cyclin_protease'}

    def __init__(self, model_path: str = 'data/BIOMD0000000003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Goldbeter1991MinMitOscilBiomd0000000003Model = Goldbeter1991MinMitOscilModel
