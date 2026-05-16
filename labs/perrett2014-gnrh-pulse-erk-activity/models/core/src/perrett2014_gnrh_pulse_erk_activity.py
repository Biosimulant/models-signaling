# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Perrett2014 - GnRH pulse, ERK activity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Perrett2014GnrhPulseErkActivityModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1509050002'
    _TITLE = 'Perrett2014 - GnRH pulse, ERK activity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nuclear_phosphorylated_erk': ('species_1',
                                    'native SBML value',
                                    'nuclear phosphorylated ERK. Maps to SBML symbol `species_1` and '
                                    'is emitted in native SBML units.'),
     'pp_erk_n': ('species_2',
                  'native SBML value',
                  'Pp ERK N. Maps to SBML symbol `species_2` and is emitted in native SBML units.'),
     'cytosolic_phosphorylated_erk': ('species_6',
                                      'native SBML value',
                                      'cytosolic phosphorylated ERK. Maps to SBML symbol `species_6` '
                                      'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_hr_inact': ('species_11',
                          0.0,
                          'native SBML value',
                          'Initial level of HR Inact. Maps to SBML symbol `species_11`; exposed as a '
                          'traceable initial-condition perturbation.'),
     'initial_mek_act': ('species_14',
                         5.71428571428571,
                         'native SBML value',
                         'Initial level of MEK Act. Maps to SBML symbol `species_14`; exposed as a '
                         'traceable initial-condition perturbation.'),
     'initial_p_erk_c': ('species_13',
                         0.3,
                         'native SBML value',
                         'Initial level of P ERK C. Maps to SBML symbol `species_13`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'nuclear phosphorylated ERK',
     'species_2': 'Pp ERK N',
     'species_3': 'source-defined TF1 state',
     'species_4': 'TF1DT',
     'species_5': 'source-defined E state',
     'species_6': 'cytosolic phosphorylated ERK',
     'species_7': 'source-defined GNRH state',
     'species_8': 'source-defined GQ state',
     'species_9': 'E Inact',
     'species_10': 'Pp ERK C',
     'species_11': 'HR Inact',
     'species_12': 'source-defined HR state',
     'species_13': 'P ERK C',
     'species_14': 'MEK Act'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'nuclear_phosphorylated_erk',
     'species_2': 'pp_erk_n',
     'species_3': 'source_defined_tf1_state',
     'species_4': 'tf1dt',
     'species_5': 'source_defined_e_state',
     'species_6': 'cytosolic_phosphorylated_erk',
     'species_7': 'source_defined_gnrh_state',
     'species_8': 'source_defined_gq_state',
     'species_9': 'e_inact',
     'species_10': 'pp_erk_c',
     'species_11': 'hr_inact',
     'species_12': 'source_defined_hr_state',
     'species_13': 'p_erk_c',
     'species_14': 'mek_act'}

    def __init__(self, model_path: str = 'data/MODEL1509050002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Perrett2014GnrhPulseErkActivityModel1509050002Model = Perrett2014GnrhPulseErkActivityModel
