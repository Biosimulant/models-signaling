# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bertram2006_Endothelin."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram2006EndothelinModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000128'
    _TITLE = 'Bertram2006_Endothelin'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytosolic_calcium_concentration': ('c',
                                         'native SBML value',
                                         'cytosolic Calcium Concentration. Maps to SBML symbol `c` and '
                                         'is emitted in native SBML units.'),
     'er_calcium_concentration': ('cer',
                                  'native SBML value',
                                  'ER Calcium Concentration. Maps to SBML symbol `cer` and is emitted '
                                  'in native SBML units.'),
     'camp': ('cAMP',
              'native SBML value',
              'cAMP. Maps to SBML symbol `cAMP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_calcium_concentration': ('c',
                                                 0.3,
                                                 'native SBML value',
                                                 'Initial level of cytosolic Calcium Concentration. '
                                                 'Maps to SBML symbol `c`; exposed as a traceable '
                                                 'initial-condition perturbation.'),
     'initial_er_calcium_concentration': ('cer',
                                          260.0,
                                          'native SBML value',
                                          'Initial level of ER Calcium Concentration. Maps to SBML '
                                          'symbol `cer`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {'initial_c_amplow_level': ('cAMPlow',
                                0.2,
                                'native SBML value',
                                'C Amplow source parameter. Maps to SBML symbol `cAMPlow` and '
                                'preserves the bundled default.')}
    _SPECIES_LABELS = {'c': 'cytosolic Calcium Concentration', 'cer': 'ER Calcium Concentration', 'cAMP': 'cAMP'}
    _STATE_OUTPUT_ALIASES = {'c': 'cytosolic_calcium_concentration', 'cer': 'er_calcium_concentration', 'cAMP': 'camp'}

    def __init__(self, model_path: str = 'data/BIOMD0000000128.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bertram2006EndothelinBiomd0000000128Model = Bertram2006EndothelinModel
