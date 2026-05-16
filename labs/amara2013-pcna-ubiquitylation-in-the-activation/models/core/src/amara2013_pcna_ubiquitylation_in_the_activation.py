# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Amara2013 - PCNA ubiquitylation in the activation of PRR pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Amara2013PcnaUbiquitylationInTheActivationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000475'
    _TITLE = 'Amara2013 - PCNA ubiquitylation in the activation of PRR pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pcna': ('species_2',
              'native SBML value',
              'PCNA. Maps to SBML symbol `species_2` and is emitted in native SBML units.'),
     'active_pcna': ('species_3',
                     'native SBML value',
                     'active PCNA. Maps to SBML symbol `species_3` and is emitted in native SBML '
                     'units.'),
     'rad18_rad18': ('species_4',
                     'native SBML value',
                     'Rad18 Rad18. Maps to SBML symbol `species_4` and is emitted in native SBML '
                     'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_l_state': ('species_1',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined L state. Maps to SBML symbol '
                                        '`species_1`; exposed as a traceable initial-condition '
                                        'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'source-defined L state',
     'species_2': 'PCNA',
     'species_3': 'active PCNA',
     'species_4': 'Rad18 Rad18',
     'species_5': 'Rad18',
     'species_6': 'Rad6',
     'species_7': 'Rad6u',
     'species_8': 'source-defined U state',
     'species_9': 'Rad18 Rad18 active PCNA',
     'species_10': 'Rad18 Rad18 active PCNA Rad6u',
     'species_11': 'Rad18 Rad18 active PCNA U',
     'species_12': 'active PCNA U',
     'species_13': 'Rad5',
     'species_14': 'Rad5 active PCNA U',
     'species_15': 'Ubc13u Mms2',
     'species_16': 'Ubc13u Mms2 Rad5 active PCNA U',
     'species_17': 'Rad5 active PCNA U U',
     'species_18': 'Ubc13 Mms2',
     'species_19': 'active PCNA U U',
     'species_20': 'Ubc13u Mms2 Rad5 active PCNA U U',
     'species_21': 'Rad5 active PCNA U U U',
     'species_22': 'active PCNA U U U',
     'species_23': 'Pcnaoff'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'source_defined_l_state',
     'species_2': 'pcna',
     'species_3': 'active_pcna',
     'species_4': 'rad18_rad18',
     'species_5': 'rad18',
     'species_6': 'rad6',
     'species_7': 'rad6u',
     'species_8': 'source_defined_u_state',
     'species_9': 'rad18_rad18_active_pcna',
     'species_10': 'rad18_rad18_active_pcna_rad6u',
     'species_11': 'rad18_rad18_active_pcna_u',
     'species_12': 'active_pcna_u',
     'species_13': 'rad5',
     'species_14': 'rad5_active_pcna_u',
     'species_15': 'ubc13u_mms2',
     'species_16': 'ubc13u_mms2_rad5_active_pcna_u',
     'species_17': 'rad5_active_pcna_u_u',
     'species_18': 'ubc13_mms2',
     'species_19': 'active_pcna_u_u',
     'species_20': 'ubc13u_mms2_rad5_active_pcna_u_u',
     'species_21': 'rad5_active_pcna_u_u_u',
     'species_22': 'active_pcna_u_u_u',
     'species_23': 'pcnaoff'}

    def __init__(self, model_path: str = 'data/BIOMD0000000475.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Amara2013PcnaUbiquitylationInTheActivationBiomd0000000475Model = Amara2013PcnaUbiquitylationInTheActivationModel
