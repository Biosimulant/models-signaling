# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in MAPK cascade."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kholodenko2000UltrasensitivityAndNegativeFeeModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000010'
    _TITLE = 'Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in MAPK cascade'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_erk2_state': ('MAPK',
                                   'native SBML value',
                                   'source-defined ERK2 state. Maps to SBML symbol `MAPK` and is '
                                   'emitted in native SBML units.'),
     'erk2_p': ('MAPK_P',
                'native SBML value',
                'Erk2 P. Maps to SBML symbol `MAPK_P` and is emitted in native SBML units.'),
     'erk2_pp': ('MAPK_PP',
                 'native SBML value',
                 'Erk2 PP. Maps to SBML symbol `MAPK_PP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_mos_kinase': ('MKKK',
                            0.0,
                            'native SBML value',
                            'Initial level of Mos kinase. Maps to SBML symbol `MKKK`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'MKKK': 'Mos kinase',
     'MKKK_P': 'source-defined MOS-P state',
     'MKK': 'source-defined MEK1 state',
     'MKK_P': 'Mek1 P',
     'MKK_PP': 'Mek1 PP',
     'MAPK': 'source-defined ERK2 state',
     'MAPK_P': 'Erk2 P',
     'MAPK_PP': 'Erk2 PP'}
    _STATE_OUTPUT_ALIASES = {'MKKK': 'mos_kinase',
     'MKKK_P': 'source_defined_mos_p_state',
     'MKK': 'source_defined_mek1_state',
     'MKK_P': 'mek1_p',
     'MKK_PP': 'mek1_pp',
     'MAPK': 'source_defined_erk2_state',
     'MAPK_P': 'erk2_p',
     'MAPK_PP': 'erk2_pp'}

    def __init__(self, model_path: str = 'data/BIOMD0000000010.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kholodenko2000UltrasensitivityAndNegativeFeeBiomd0000000010Model = Kholodenko2000UltrasensitivityAndNegativeFeeModel
