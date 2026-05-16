# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lemaire2004 - Role of RANK/RANKL/OPG pathway in bone remodelling process."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lemaire2004RoleOfRankRanklOpgPathwayInBoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000278'
    _TITLE = 'Lemaire2004 - Role of RANK/RANKL/OPG pathway in bone remodelling process'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'active_osteoblasts': ('B',
                            'native SBML value',
                            'active Osteoblasts. Maps to SBML symbol `B` and is emitted in native SBML '
                            'units.'),
     'active_osteoclasts': ('C',
                            'native SBML value',
                            'active Osteoclasts. Maps to SBML symbol `C` and is emitted in native SBML '
                            'units.'),
     'responding_osteoblasts': ('R',
                                'native SBML value',
                                'Responding Osteoblasts. Maps to SBML symbol `R` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_responding_osteoblasts': ('R',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of Responding Osteoblasts. Maps to SBML symbol '
                                        '`R`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'R': 'Responding Osteoblasts', 'B': 'active Osteoblasts', 'C': 'active Osteoclasts'}
    _STATE_OUTPUT_ALIASES = {'R': 'responding_osteoblasts', 'B': 'active_osteoblasts', 'C': 'active_osteoclasts'}

    def __init__(self, model_path: str = 'data/BIOMD0000000278.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Lemaire2004RoleOfRankRanklOpgPathwayInBoBiomd0000000278Model = Lemaire2004RoleOfRankRanklOpgPathwayInBoModel
