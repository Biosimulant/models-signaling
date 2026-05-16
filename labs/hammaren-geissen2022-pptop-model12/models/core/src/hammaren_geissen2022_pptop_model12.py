# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hammaren-Geissen2022_PPToP_Model12."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class HammarenGeissen2022PptopModel12Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001078'
    _TITLE = 'Hammaren-Geissen2022_PPToP_Model12'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pu_old': ('Pu',
                'native SBML value',
                'Pu Old. Maps to SBML symbol `Pu` and is emitted in native SBML units.'),
     'pp_old': ('Pp',
                'native SBML value',
                'Pp Old. Maps to SBML symbol `Pp` and is emitted in native SBML units.'),
     'pu_new': ('Pu_new',
                'native SBML value',
                'Pu New. Maps to SBML symbol `Pu_new` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_pp_new': ('Pp_new',
                        0.0,
                        'native SBML value',
                        'Initial level of Pp New. Maps to SBML symbol `Pp_new`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_pu_new': ('Pu_new',
                        0.0,
                        'native SBML value',
                        'Initial level of Pu New. Maps to SBML symbol `Pu_new`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Pu': 'Pu Old', 'Pp': 'Pp Old', 'Pu_new': 'Pu New', 'Pp_new': 'Pp New'}
    _STATE_OUTPUT_ALIASES = {'Pu': 'pu_old', 'Pp': 'pp_old', 'Pu_new': 'pu_new', 'Pp_new': 'pp_new'}

    def __init__(self, model_path: str = 'data/BIOMD0000001078.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


HammarenGeissen2022PptopModel12Biomd0000001078Model = HammarenGeissen2022PptopModel12Model
