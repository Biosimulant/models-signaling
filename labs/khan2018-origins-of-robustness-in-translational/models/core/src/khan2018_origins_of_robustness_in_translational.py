# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Khan2018 - Origins of robustness in translational control via eukaryotic translation initiation factor (eIF) 2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khan2018OriginsOfRobustnessInTranslationalModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1911120001'
    _TITLE = 'Khan2018 - Origins of robustness in translational control via eukaryotic translation initiation factor (eIF) 2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'e_if2_gdp': ('eIF2_GDP',
                   'native SBML value',
                   'E IF2 GDP. Maps to SBML symbol `eIF2_GDP` and is emitted in native SBML units.'),
     'e_if2b': ('eIF2B',
                'native SBML value',
                'E IF2B. Maps to SBML symbol `eIF2B` and is emitted in native SBML units.'),
     'e_if2_gtp': ('eIF2_GTP',
                   'native SBML value',
                   'E IF2 GTP. Maps to SBML symbol `eIF2_GTP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_e_if2_gdp': ('eIF2_GDP',
                           0.0,
                           'native SBML value',
                           'Initial level of E IF2 GDP. Maps to SBML symbol `eIF2_GDP`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'eIF2_GDP': 'E IF2 GDP',
     'eIF2B': 'E IF2B',
     'eIF2_GTP': 'E IF2 GTP',
     'eIF5': 'source-defined EIF5 state',
     'eIF5_eIF2_GDP': 'E IF5 E IF2 GDP',
     'eIF5_eIF2B_eIF2_GDP': 'E IF5 E IF2B E IF2 GDP',
     'eIF2B_eIF2_GDP': 'E IF2B E IF2 GDP',
     'translation': 'Translation',
     'KA': 'source-defined KA state',
     'K': 'source-defined K state',
     'KA_K': 'source-defined KA_K state',
     'eIF2_P': 'E IF2 P',
     'KA_K_eIF2': 'KA K E IF2',
     'eIF2_P_eIF2B': 'E IF2 P E IF2B'}
    _STATE_OUTPUT_ALIASES = {'eIF2_GDP': 'e_if2_gdp',
     'eIF2B': 'e_if2b',
     'eIF2_GTP': 'e_if2_gtp',
     'eIF5': 'source_defined_eif5_state',
     'eIF5_eIF2_GDP': 'e_if5_e_if2_gdp',
     'eIF5_eIF2B_eIF2_GDP': 'e_if5_e_if2b_e_if2_gdp',
     'eIF2B_eIF2_GDP': 'e_if2b_e_if2_gdp',
     'translation': 'translation',
     'KA': 'source_defined_ka_state',
     'K': 'source_defined_k_state',
     'KA_K': 'source_defined_ka_k_state',
     'eIF2_P': 'e_if2_p',
     'KA_K_eIF2': 'ka_k_e_if2',
     'eIF2_P_eIF2B': 'e_if2_p_e_if2b'}

    def __init__(self, model_path: str = 'data/MODEL1911120001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Khan2018OriginsOfRobustnessInTranslationalModel1911120001Model = Khan2018OriginsOfRobustnessInTranslationalModel
