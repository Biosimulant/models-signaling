# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Muller2008 - Simplified MAPK activation Dynamics (Model B)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Muller2008SimplifiedMapkActivationDynamicsMModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000664'
    _TITLE = 'Muller2008 - Simplified MAPK activation Dynamics (Model B)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapk': ('MAPK',
              'native SBML value',
              'MAPK. Maps to SBML symbol `MAPK` and is emitted in native SBML units.'),
     'c_raf_inactive': ('C_Raf_inactive',
                        'native SBML value',
                        'C RAF Inactive. Maps to SBML symbol `C_Raf_inactive` and is emitted in native '
                        'SBML units.'),
     'source_defined_fgfr_state': ('FGFR',
                                   'native SBML value',
                                   'source-defined FGFR state. Maps to SBML symbol `FGFR` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_g1_state': ('g1_0',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined G1 state. Maps to SBML '
                                         'symbol `g1_0`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_source_defined_g2_state': ('g2_0',
                                         1.0,
                                         'native SBML value',
                                         'Initial level of source-defined G2 state. Maps to SBML '
                                         'symbol `g2_0`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'FGFR': 'source-defined FGFR state',
     'MSH': 'source-defined MSH state',
     'B_Raf': 'source-defined B-RAF state',
     'MAPK': 'MAPK',
     'C_Raf_inactive': 'C RAF Inactive',
     'g2_0': 'source-defined G2 state',
     'C_Raf': 'source-defined C-RAF state',
     'g1_0': 'source-defined G1 state'}
    _STATE_OUTPUT_ALIASES = {'FGFR': 'source_defined_fgfr_state',
     'MSH': 'source_defined_msh_state',
     'B_Raf': 'source_defined_b_raf_state',
     'MAPK': 'mapk',
     'C_Raf_inactive': 'c_raf_inactive',
     'g2_0': 'source_defined_g2_state',
     'C_Raf': 'source_defined_c_raf_state',
     'g1_0': 'source_defined_g1_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000664.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Muller2008SimplifiedMapkActivationDynamicsMBiomd0000000664Model = Muller2008SimplifiedMapkActivationDynamicsMModel
