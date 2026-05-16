# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chan2004_TCell_receptor_activation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chan2004TcellReceptorActivationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000120'
    _TITLE = 'Chan2004_TCell_receptor_activation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'inactive_lck': ('lck_inactive',
                      'native SBML value',
                      'Inactive Lck. Maps to SBML symbol `lck_inactive` and is emitted in native SBML '
                      'units.'),
     'active_lck': ('lck_active',
                    'native SBML value',
                    'active Lck. Maps to SBML symbol `lck_active` and is emitted in native SBML '
                    'units.'),
     'inactive_phosphatase': ('phosphatase_inactive',
                              'native SBML value',
                              'Inactive Phosphatase. Maps to SBML symbol `phosphatase_inactive` and is '
                              'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_inactive_lck': ('lck_inactive',
                              0.0,
                              'native SBML value',
                              'Initial level of Inactive Lck. Maps to SBML symbol `lck_inactive`; '
                              'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'lck_inactive': 'Inactive Lck',
     'lck_active': 'active Lck',
     'phosphatase_inactive': 'Inactive Phosphatase',
     'phosphatase_active': 'active Phosphatase',
     'lck_total': 'Total Kinase'}
    _STATE_OUTPUT_ALIASES = {'lck_inactive': 'inactive_lck',
     'lck_active': 'active_lck',
     'phosphatase_inactive': 'inactive_phosphatase',
     'phosphatase_active': 'active_phosphatase',
     'lck_total': 'total_kinase'}

    def __init__(self, model_path: str = 'data/BIOMD0000000120.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Chan2004TcellReceptorActivationBiomd0000000120Model = Chan2004TcellReceptorActivationModel
