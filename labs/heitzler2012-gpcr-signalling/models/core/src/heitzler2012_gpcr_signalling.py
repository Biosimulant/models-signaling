# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Heitzler2012 - GPCR signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heitzler2012GpcrSignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000842'
    _TITLE = 'Heitzler2012 - GPCR signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'erk': ('ERK',
             'native SBML value',
             'ERK. Maps to SBML symbol `ERK` and is emitted in native SBML units.'),
     'gp_p_erk': ('GpERK',
                  'native SBML value',
                  'Gp P ERK. Maps to SBML symbol `GpERK` and is emitted in native SBML units.'),
     'b_p_erk': ('bpERK',
                 'native SBML value',
                 'B P ERK. Maps to SBML symbol `bpERK` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_perk_kinase': ('pERK',
                             0.03,
                             'native SBML value',
                             'Initial level of PERK kinase. Maps to SBML symbol `pERK`; exposed as a '
                             'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'HR': 'source-defined HR state',
     'G': 'source-defined GP state',
     'ERK': 'ERK',
     'PIP2': 'source-defined PIP2 state',
     'DAG': 'DAG',
     'PKC': 'PKC',
     'PKC_a': 'source-defined PKC_A state',
     'GpERK': 'Gp P ERK',
     'bpERK': 'B P ERK',
     'barr1': 'B Arrestin1',
     'barr2': 'B Arrestin2',
     'G_a': 'source-defined GP_A state',
     'HRP1': 'source-defined HR-P1 state',
     'Hbarr1RP1': 'HR P1 B Arrestin1',
     'Hbarr2RP1': 'HR P1 B Arrestin2',
     'HRP2': 'source-defined HR-P2 state',
     'HRbarr2': 'HR B Arrestin2',
     'Hbarr2RP2': 'HR P2 B Arrestin2',
     'GRK2_3': 'GRK2 3',
     'GRK5_6': 'GRK5 6',
     'pERK': 'PERK kinase'}
    _STATE_OUTPUT_ALIASES = {'HR': 'source_defined_hr_state',
     'G': 'source_defined_gp_state',
     'ERK': 'erk',
     'PIP2': 'source_defined_pip2_state',
     'DAG': 'dag',
     'PKC': 'pkc',
     'PKC_a': 'source_defined_pkc_a_state',
     'GpERK': 'gp_p_erk',
     'bpERK': 'b_p_erk',
     'barr1': 'b_arrestin1',
     'barr2': 'b_arrestin2',
     'G_a': 'source_defined_gp_a_state',
     'HRP1': 'source_defined_hr_p1_state',
     'Hbarr1RP1': 'hr_p1_b_arrestin1',
     'Hbarr2RP1': 'hr_p1_b_arrestin2',
     'HRP2': 'source_defined_hr_p2_state',
     'HRbarr2': 'hr_b_arrestin2',
     'Hbarr2RP2': 'hr_p2_b_arrestin2',
     'GRK2_3': 'grk2_3',
     'GRK5_6': 'grk5_6',
     'pERK': 'perk_kinase'}

    def __init__(self, model_path: str = 'data/BIOMD0000000842.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Heitzler2012GpcrSignallingBiomd0000000842Model = Heitzler2012GpcrSignallingModel
