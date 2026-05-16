# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Goldbeter2013-Oscillatory activity of cyclin-dependent kinases in the cell cycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter2013OscillatoryActivityOfCyclinDepModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000944'
    _TITLE = 'Goldbeter2013-Oscillatory activity of cyclin-dependent kinases in the cell cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'active_cdc2_kinase': ('Active_Cdc2_kinase',
                            'native SBML value',
                            'active Cdc2 Kinase. Maps to SBML symbol `Active_Cdc2_kinase` and is '
                            'emitted in native SBML units.'),
     'active_apc': ('Active_APC',
                    'native SBML value',
                    'active APC. Maps to SBML symbol `Active_APC` and is emitted in native SBML '
                    'units.'),
     'cyclin': ('Cyclin',
                'native SBML value',
                'Cyclin. Maps to SBML symbol `Cyclin` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cyclin': ('Cyclin',
                        0.0,
                        'native SBML value',
                        'Initial level of Cyclin. Maps to SBML symbol `Cyclin`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Cyclin': 'Cyclin', 'Active_Cdc2_kinase': 'active Cdc2 Kinase', 'Active_APC': 'active APC'}
    _STATE_OUTPUT_ALIASES = {'Cyclin': 'cyclin', 'Active_Cdc2_kinase': 'active_cdc2_kinase', 'Active_APC': 'active_apc'}

    def __init__(self, model_path: str = 'data/BIOMD0000000944.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Goldbeter2013OscillatoryActivityOfCyclinDepBiomd0000000944Model = Goldbeter2013OscillatoryActivityOfCyclinDepModel
