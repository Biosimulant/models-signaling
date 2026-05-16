# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Thomson2009 – Unlimited multistability in multisite phosphorylation systems."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Thomson2009UnlimitedMultistabilityInMultisitModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2002110001'
    _TITLE = 'Thomson2009 – Unlimited multistability in multisite phosphorylation systems'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_es0_state': ('ES0',
                                  'native SBML value',
                                  'Source Defined ES0 State. Maps to SBML symbol `ES0` and is emitted '
                                  'in native SBML units.'),
     'source_defined_es1_state': ('ES1',
                                  'native SBML value',
                                  'Source Defined ES1 State. Maps to SBML symbol `ES1` and is emitted '
                                  'in native SBML units.'),
     'source_defined_es2_state': ('ES2',
                                  'native SBML value',
                                  'Source Defined ES2 State. Maps to SBML symbol `ES2` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_e_state': ('E',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined E state. Maps to SBML symbol '
                                        '`E`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'E': 'Source Defined E State',
     'S0': 'Source Defined S0 State',
     'ES0': 'Source Defined ES0 State',
     'S1': 'Source Defined S1 State',
     'ES1': 'Source Defined ES1 State',
     'S2': 'Source Defined S2 State',
     'ES2': 'Source Defined ES2 State',
     'S3': 'Source Defined S3 State',
     'ES3': 'Source Defined ES3 State',
     'S4': 'Source Defined S4 State',
     'F': 'Source Defined F State',
     'FS4': 'Source Defined FS4 State',
     'FS3': 'Source Defined FS3 State',
     'FS2': 'Source Defined FS2 State',
     'FS1': 'Source Defined FS1 State'}
    _STATE_OUTPUT_ALIASES = {'E': 'source_defined_e_state',
     'S0': 'source_defined_s0_state',
     'ES0': 'source_defined_es0_state',
     'S1': 'source_defined_s1_state',
     'ES1': 'source_defined_es1_state',
     'S2': 'source_defined_s2_state',
     'ES2': 'source_defined_es2_state',
     'S3': 'source_defined_s3_state',
     'ES3': 'source_defined_es3_state',
     'S4': 'source_defined_s4_state',
     'F': 'source_defined_f_state',
     'FS4': 'source_defined_fs4_state',
     'FS3': 'source_defined_fs3_state',
     'FS2': 'source_defined_fs2_state',
     'FS1': 'source_defined_fs1_state'}

    def __init__(self, model_path: str = 'data/MODEL2002110001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Thomson2009UnlimitedMultistabilityInMultisitModel2002110001Model = Thomson2009UnlimitedMultistabilityInMultisitModel
