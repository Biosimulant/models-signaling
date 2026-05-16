# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Thomsen1988_AdenylateCyclase_Inhibition."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Thomsen1988AdenylatecyclaseInhibitionModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000082'
    _TITLE = 'Thomsen1988_AdenylateCyclase_Inhibition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'drg_gdp': ('DRG_GDP',
                 'native SBML value',
                 'DRG GDP. Maps to SBML symbol `DRG_GDP` and is emitted in native SBML units.'),
     'source_defined_drg_state': ('DRG',
                                  'native SBML value',
                                  'source-defined DRG state. Maps to SBML symbol `DRG` and is emitted '
                                  'in native SBML units.'),
     'gdp': ('GDP',
             'native SBML value',
             'GDP. Maps to SBML symbol `GDP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_agonist': ('agonist',
                         1e-08,
                         'native SBML value',
                         'Initial level of Agonist. Maps to SBML symbol `agonist`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'agonist': 'Agonist',
     'DR': 'source-defined DR state',
     'DRG_GDP': 'DRG GDP',
     'DRG': 'source-defined DRG state',
     'GDP': 'GDP',
     'DRG_GTP': 'DRG GTP',
     'GTP': 'GTP',
     'Recptor': 'Recptor',
     'G_GDP': 'source-defined G_GDP state',
     'G_GTP': 'source-defined G_GTP state'}
    _STATE_OUTPUT_ALIASES = {'agonist': 'agonist',
     'DR': 'source_defined_dr_state',
     'DRG_GDP': 'drg_gdp',
     'DRG': 'source_defined_drg_state',
     'GDP': 'gdp',
     'DRG_GTP': 'drg_gtp',
     'GTP': 'gtp',
     'Recptor': 'recptor',
     'G_GDP': 'source_defined_g_gdp_state',
     'G_GTP': 'source_defined_g_gtp_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000082.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Thomsen1988AdenylatecyclaseInhibitionBiomd0000000082Model = Thomsen1988AdenylatecyclaseInhibitionModel
