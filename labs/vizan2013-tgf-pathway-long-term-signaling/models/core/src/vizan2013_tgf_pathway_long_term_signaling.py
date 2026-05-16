# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Vizan2013 - TGF pathway long term signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vizan2013TgfPathwayLongTermSignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000499'
    _TITLE = 'Vizan2013 - TGF pathway long term signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'abstract_source_state_s22': ('species_1',
                                   'native SBML value',
                                   'Abstract source state S22. Maps to SBML symbol `species_1` and is '
                                   'emitted in native SBML units.'),
     'abstract_source_state_s24': ('species_2',
                                   'native SBML value',
                                   'Abstract source state S24. Maps to SBML symbol `species_2` and is '
                                   'emitted in native SBML units.'),
     'p_s2tot': ('species_3',
                 'native SBML value',
                 'P S2tot. Maps to SBML symbol `species_3` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_rt_state': ('species_24',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined RT state. Maps to SBML '
                                         'symbol `species_24`; exposed as a traceable '
                                         'initial-condition perturbation.'),
     'initial_source_defined_r_state': ('species_5',
                                        0.87962962962963,
                                        'native SBML value',
                                        'Initial level of source-defined R state. Maps to SBML symbol '
                                        '`species_5`; exposed as a traceable initial-condition '
                                        'perturbation.'),
     'initial_p_s2c': ('species_8',
                       0.0,
                       'native SBML value',
                       'Initial level of P S2c. Maps to SBML symbol `species_8`; exposed as a '
                       'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'Abstract source state S22',
     'species_2': 'Abstract source state S24',
     'species_3': 'P S2tot',
     'species_4': 'source-defined TGF state',
     'species_5': 'source-defined R state',
     'species_6': 'S2c',
     'species_7': 'source-defined RCOM state',
     'species_8': 'P S2c',
     'species_9': 'Rcom S',
     'species_10': 'S2n',
     'species_11': 'S22n',
     'species_12': 'S4n',
     'species_13': 'S22c',
     'species_14': 'P S2n',
     'species_15': 'P S2fn',
     'species_16': 'S24n',
     'species_17': 'S24c',
     'species_18': 'S4fc',
     'species_19': 'S4c',
     'species_20': 'P S2fc',
     'species_21': 'S4fn',
     'species_22': 'source-defined SBI state',
     'species_23': 'source-defined RTOT state',
     'species_24': 'source-defined RT state',
     'species_25': 'Rcom I',
     'species_26': 'source-defined RACT state'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'abstract_source_state_s22',
     'species_2': 'abstract_source_state_s24',
     'species_3': 'p_s2tot',
     'species_4': 'source_defined_tgf_state',
     'species_5': 'source_defined_r_state',
     'species_6': 's2c',
     'species_7': 'source_defined_rcom_state',
     'species_8': 'p_s2c',
     'species_9': 'rcom_s',
     'species_10': 's2n',
     'species_11': 's22n',
     'species_12': 's4n',
     'species_13': 's22c',
     'species_14': 'p_s2n',
     'species_15': 'p_s2fn',
     'species_16': 's24n',
     'species_17': 's24c',
     'species_18': 's4fc',
     'species_19': 's4c',
     'species_20': 'p_s2fc',
     'species_21': 's4fn',
     'species_22': 'source_defined_sbi_state',
     'species_23': 'source_defined_rtot_state',
     'species_24': 'source_defined_rt_state',
     'species_25': 'rcom_i',
     'species_26': 'source_defined_ract_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000499.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Vizan2013TgfPathwayLongTermSignalingBiomd0000000499Model = Vizan2013TgfPathwayLongTermSignalingModel
