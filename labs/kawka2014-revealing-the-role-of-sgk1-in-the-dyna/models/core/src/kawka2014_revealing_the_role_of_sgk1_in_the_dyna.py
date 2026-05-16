# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kawka2014 - Revealing the role of SGK1 in the dynamics of medulloblastoma using a mathematical model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kawka2014RevealingTheRoleOfSgk1InTheDynaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1912090002'
    _TITLE = 'Kawka2014 - Revealing the role of SGK1 in the dynamics of medulloblastoma using a mathematical model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'sgk1_t': ('SGK1_t',
                'native SBML value',
                'SGK1 T. Maps to SBML symbol `SGK1_t` and is emitted in native SBML units.'),
     'sgk1_p': ('SGK1_p',
                'native SBML value',
                'SGK1 P. Maps to SBML symbol `SGK1_p` and is emitted in native SBML units.'),
     'source_defined_myc_t_state': ('MYC_t',
                                    'native SBML value',
                                    'source-defined MYC_T state. Maps to SBML symbol `MYC_t` and is '
                                    'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sgk1_t': ('SGK1_t',
                        0.0,
                        'native SBML value',
                        'Initial level of SGK1 T. Maps to SBML symbol `SGK1_t`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'SGK1_t': 'SGK1 T',
     'SGK1_p': 'SGK1 P',
     'MYC_t': 'source-defined MYC_T state',
     'cMyc_pc': 'C MYC transcription factor Pc',
     'cMyc_pn': 'C MYC transcription factor Pn',
     'GSK3Beta_c': 'Gsk3beta C',
     'GSK3Beta_occ': 'Gsk3beta Occ',
     'SGK1_occ': 'SGK1 Occ',
     'GSK3Beta_n': 'Gsk3beta N'}
    _STATE_OUTPUT_ALIASES = {'SGK1_t': 'sgk1_t',
     'SGK1_p': 'sgk1_p',
     'MYC_t': 'source_defined_myc_t_state',
     'cMyc_pc': 'c_myc_transcription_factor_pc',
     'cMyc_pn': 'c_myc_transcription_factor_pn',
     'GSK3Beta_c': 'gsk3beta_c',
     'GSK3Beta_occ': 'gsk3beta_occ',
     'SGK1_occ': 'sgk1_occ',
     'GSK3Beta_n': 'gsk3beta_n'}

    def __init__(self, model_path: str = 'data/MODEL1912090002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kawka2014RevealingTheRoleOfSgk1InTheDynaModel1912090002Model = Kawka2014RevealingTheRoleOfSgk1InTheDynaModel
