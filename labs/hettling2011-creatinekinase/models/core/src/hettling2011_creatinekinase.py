# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hettling2011_CreatineKinase."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hettling2011CreatinekinaseModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000408'
    _TITLE = 'Hettling2011_CreatineKinase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'intracellular_adp': ('ADPi',
                           'micromole',
                           'intracellular ADP. Maps to SBML symbol `ADPi` and is emitted in native '
                           'SBML units.'),
     'intracellular_atp': ('ATPi',
                           'micromole',
                           'intracellular ATP. Maps to SBML symbol `ATPi` and is emitted in native '
                           'SBML units.'),
     'intracellular_creatine': ('Cri',
                                'micromole',
                                'intracellular creatine. Maps to SBML symbol `Cri` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_ck_factor_ia_level': ('ck_factor_ia',
                                    0.0286,
                                    'native SBML value',
                                    'Ck Factor Ia source parameter. Maps to SBML symbol `ck_factor_ia` '
                                    'and preserves the bundled default.'),
     'initial_ck_factor_indole_3_acetic_acid_level': ('ck_factor_iaa',
                                                      1.0,
                                                      'native SBML value',
                                                      'Ck Factor indole-3-acetic acid source '
                                                      'parameter. Maps to SBML symbol `ck_factor_iaa` '
                                                      'and preserves the bundled default.'),
     'initial_tmito_factor_level': ('tmito_factor',
                                    0.0,
                                    'native SBML value',
                                    'Tmito Factor source parameter. Maps to SBML symbol `tmito_factor` '
                                    'and preserves the bundled default.')}
    _SPECIES_LABELS = {'ADPi': 'intracellular ADP',
     'ATPi': 'intracellular ATP',
     'Cri': 'intracellular creatine',
     'PCri': 'source-defined PCRI state',
     'PCr': 'source-defined PCR state',
     'ADP': 'ADP',
     'ATP': 'ATP',
     'Cr': 'source-defined CR state',
     'P_ii': 'source-defined P_II state',
     'P_i': 'source-defined P_I state'}
    _STATE_OUTPUT_ALIASES = {'ADPi': 'intracellular_adp',
     'ATPi': 'intracellular_atp',
     'Cri': 'intracellular_creatine',
     'PCri': 'source_defined_pcri_state',
     'PCr': 'source_defined_pcr_state',
     'ADP': 'adp',
     'ATP': 'atp',
     'Cr': 'source_defined_cr_state',
     'P_ii': 'source_defined_p_ii_state',
     'P_i': 'source_defined_p_i_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000408.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hettling2011CreatinekinaseBiomd0000000408Model = Hettling2011CreatinekinaseModel
