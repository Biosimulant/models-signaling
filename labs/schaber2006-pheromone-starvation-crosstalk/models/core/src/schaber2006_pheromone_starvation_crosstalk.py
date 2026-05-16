# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schaber2006_Pheromone_Starvation_Crosstalk."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schaber2006PheromoneStarvationCrosstalkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000237'
    _TITLE = 'Schaber2006_Pheromone_Starvation_Crosstalk'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_ste5_state': ('Ste5',
                                   'native SBML value',
                                   'source-defined STE5 state. Maps to SBML symbol `Ste5` and is '
                                   'emitted in native SBML units.'),
     'ste11': ('Ste11',
               'native SBML value',
               'Ste11. Maps to SBML symbol `Ste11` and is emitted in native SBML units.'),
     'ste5ste11': ('Ste5Ste11',
                   'native SBML value',
                   'Ste5ste11. Maps to SBML symbol `Ste5Ste11` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_p_state': ('p',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined P state. Maps to SBML symbol '
                                        '`p`; exposed as a traceable initial-condition perturbation.'),
     'initial_source_defined_s_state': ('s',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined S state. Maps to SBML symbol '
                                        '`s`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Ste5': 'source-defined STE5 state',
     'Ste11': 'Ste11',
     'Ste5Ste11': 'Ste5ste11',
     'Gbg': 'G beta-gamma complex',
     'Ste5Ste11Gbg': 'Ste5ste11gbg',
     'Fus3': 'source-defined FUS3 state',
     'Ste5Ste11GbgFus3': 'Ste5ste11gbg Fus3',
     'Ste5Ste11GbgFus3P': 'Ste5ste11gbg Fus3p',
     'Fus3PP': 'Fus3pp',
     'Ste5Ste11GbgP': 'Ste5ste11gbg P',
     'Ste11Ubi': 'Ste11ubi',
     'Kss1': 'source-defined KSS1 state',
     'Ste5Ste11GbgKss1': 'Ste5ste11gbg Kss1',
     'Ste5Ste11GbgKss1P': 'Ste5ste11gbg Kss1p',
     'Kss1PP': 'Kss1pp',
     'Ste11P': 'Ste11p',
     'Ste12Kss1': 'Ste12kss1',
     'Ste12': 'Ste12',
     'Ste12P': 'Ste12p',
     'PREP': 'source-defined PREP state',
     'Ste12TeSte5Kss1': 'Ste12te Ste5kss1',
     'Ste12TeSte5': 'Ste12te Ste5',
     'Ste12TeSte5P': 'Ste12te Ste5p',
     'FREP': 'source-defined FREP state'}
    _STATE_OUTPUT_ALIASES = {'Ste5': 'source_defined_ste5_state',
     'Ste11': 'ste11',
     'Ste5Ste11': 'ste5ste11',
     'Gbg': 'g_beta_gamma_complex',
     'Ste5Ste11Gbg': 'ste5ste11gbg',
     'Fus3': 'source_defined_fus3_state',
     'Ste5Ste11GbgFus3': 'ste5ste11gbg_fus3',
     'Ste5Ste11GbgFus3P': 'ste5ste11gbg_fus3p',
     'Fus3PP': 'fus3pp',
     'Ste5Ste11GbgP': 'ste5ste11gbg_p',
     'Ste11Ubi': 'ste11ubi',
     'Kss1': 'source_defined_kss1_state',
     'Ste5Ste11GbgKss1': 'ste5ste11gbg_kss1',
     'Ste5Ste11GbgKss1P': 'ste5ste11gbg_kss1p',
     'Kss1PP': 'kss1pp',
     'Ste11P': 'ste11p',
     'Ste12Kss1': 'ste12kss1',
     'Ste12': 'ste12',
     'Ste12P': 'ste12p',
     'PREP': 'source_defined_prep_state',
     'Ste12TeSte5Kss1': 'ste12te_ste5kss1',
     'Ste12TeSte5': 'ste12te_ste5',
     'Ste12TeSte5P': 'ste12te_ste5p',
     'FREP': 'source_defined_frep_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000237.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Schaber2006PheromoneStarvationCrosstalkBiomd0000000237Model = Schaber2006PheromoneStarvationCrosstalkModel
