# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Goldbeter2007_Somitogenesis_Switch."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Goldbeter2007SomitogenesisSwitchModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000275'
    _TITLE = 'Goldbeter2007_Somitogenesis_Switch'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cyp26_m_rna': ('M_C',
                     'native SBML value',
                     'Cyp26 M RNA. Maps to SBML symbol `M_C` and is emitted in native SBML units.'),
     'cyp26': ('C',
               'native SBML value',
               'CYP26. Maps to SBML symbol `C` and is emitted in native SBML units.'),
     'source_defined_fgf_state': ('F',
                                  'native SBML value',
                                  'source-defined FGF state. Maps to SBML symbol `F` and is emitted in '
                                  'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_ra_state': ('RA',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined RA state. Maps to SBML '
                                         'symbol `RA`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'RA': 'Source Defined RA State',
     'M_C': 'Cyp26 M RNA',
     'C': 'CYP26',
     'F': 'source-defined FGF state',
     'M_F': 'FGF M RNA'}
    _STATE_OUTPUT_ALIASES = {'RA': 'source_defined_ra_state',
     'M_C': 'cyp26_m_rna',
     'C': 'cyp26',
     'F': 'source_defined_fgf_state',
     'M_F': 'fgf_m_rna'}

    def __init__(self, model_path: str = 'data/BIOMD0000000275.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Goldbeter2007SomitogenesisSwitchBiomd0000000275Model = Goldbeter2007SomitogenesisSwitchModel
