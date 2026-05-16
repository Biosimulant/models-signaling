# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Keizer1996_Ryanodine_receptor_adaptation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Keizer1996RyanodineReceptorAdaptationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000060'
    _TITLE = 'Keizer1996_Ryanodine_receptor_adaptation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_pc1_state': ('Pc1',
                                  'native SBML value',
                                  'Source Defined PC1 State. Maps to SBML symbol `Pc1` and is emitted '
                                  'in native SBML units.'),
     'source_defined_po2_state': ('Po2',
                                  'native SBML value',
                                  'Source Defined PO2 State. Maps to SBML symbol `Po2` and is emitted '
                                  'in native SBML units.'),
     'source_defined_po1_state': ('Po1',
                                  'native SBML value',
                                  'source-defined PO1 state. Maps to SBML symbol `Po1` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_pc1_state': ('Pc1',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined PC1 state. Maps to SBML '
                                          'symbol `Pc1`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Pc1': 'Source Defined PC1 State',
     'Po2': 'Source Defined PO2 State',
     'Po1': 'source-defined PO1 state',
     'Pc2': 'source-defined PC2 state'}
    _STATE_OUTPUT_ALIASES = {'Pc1': 'source_defined_pc1_state',
     'Po2': 'source_defined_po2_state',
     'Po1': 'source_defined_po1_state',
     'Pc2': 'source_defined_pc2_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000060.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Keizer1996RyanodineReceptorAdaptationBiomd0000000060Model = Keizer1996RyanodineReceptorAdaptationModel
