# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nakakuki2010_CellFateDecision_Core."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nakakuki2010CellfatedecisionCoreModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000251'
    _TITLE = 'Nakakuki2010_CellFateDecision_Core'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pp_erk_nucleus': ('ppERKn',
                        'native SBML value',
                        'Pp ERK Nucleus. Maps to SBML symbol `ppERKn` and is emitted in native SBML '
                        'units.'),
     'pp_erk_cytosol': ('ppERKc',
                        'native SBML value',
                        'Pp ERK Cytosol. Maps to SBML symbol `ppERKc` and is emitted in native SBML '
                        'units.'),
     'source_defined_dusp_state': ('DUSP',
                                   'native SBML value',
                                   'source-defined DUSP state. Maps to SBML symbol `DUSP` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_pp_erk_cytosol': ('ppERKc',
                                0.0,
                                'native SBML value',
                                'Initial level of Pp ERK Cytosol. Maps to SBML symbol `ppERKc`; '
                                'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x1': 'source-defined X1 state',
     'x2': 'source-defined X2 state',
     'ppERKn': 'Pp ERK Nucleus',
     'DUSP': 'source-defined DUSP state',
     'pRSKn': 'P Rskn',
     'cFOSp': 'C FOS Pre RNA',
     'cFOS': 'source-defined CFOS state',
     'pcFOS': 'Pc FOS',
     'cFOSm': 'C Fosm RNA',
     'ppERKc': 'Pp ERK Cytosol'}
    _STATE_OUTPUT_ALIASES = {'x1': 'source_defined_x1_state',
     'x2': 'source_defined_x2_state',
     'ppERKn': 'pp_erk_nucleus',
     'DUSP': 'source_defined_dusp_state',
     'pRSKn': 'p_rskn',
     'cFOSp': 'c_fos_pre_rna',
     'cFOS': 'source_defined_cfos_state',
     'pcFOS': 'pc_fos',
     'cFOSm': 'c_fosm_rna',
     'ppERKc': 'pp_erk_cytosol'}

    def __init__(self, model_path: str = 'data/BIOMD0000000251.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Nakakuki2010CellfatedecisionCoreBiomd0000000251Model = Nakakuki2010CellfatedecisionCoreModel
