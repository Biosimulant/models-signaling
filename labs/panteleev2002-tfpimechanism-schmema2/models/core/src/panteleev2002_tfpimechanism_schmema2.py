# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Panteleev2002_TFPImechanism_schmema2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Panteleev2002TfpimechanismSchmema2Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000360'
    _TITLE = 'Panteleev2002_TFPImechanism_schmema2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'viia_tf': ('VIIa_TF',
                 'native SBML value',
                 'Viia TF. Maps to SBML symbol `VIIa_TF` and is emitted in native SBML units.'),
     'viia_tf_x': ('VIIa_TF_X',
                   'native SBML value',
                   'Viia TF X. Maps to SBML symbol `VIIa_TF_X` and is emitted in native SBML units.'),
     'viia_tf_xa': ('VIIa_TF_Xa',
                    'native SBML value',
                    'Viia TF Xa. Maps to SBML symbol `VIIa_TF_Xa` and is emitted in native SBML '
                    'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_viia_tf': ('VIIa_TF',
                         0.0,
                         'native SBML value',
                         'Initial level of Viia TF. Maps to SBML symbol `VIIa_TF`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'VIIa_TF': 'Viia TF',
     'X': 'response node X',
     'VIIa_TF_X': 'Viia TF X',
     'VIIa_TF_Xa': 'Viia TF Xa',
     'Xa': 'source-defined XA state',
     'TFPI': 'source-defined TFPI state',
     'Xa_TFPI': 'Xa TFPI',
     'Xa_TFPI_VIIa_TF': 'Xa TFPI Viia TF',
     'VIIa_TF_Xa_TFPI': 'Viia TF Xa TFPI'}
    _STATE_OUTPUT_ALIASES = {'VIIa_TF': 'viia_tf',
     'X': 'response_node_x',
     'VIIa_TF_X': 'viia_tf_x',
     'VIIa_TF_Xa': 'viia_tf_xa',
     'Xa': 'source_defined_xa_state',
     'TFPI': 'source_defined_tfpi_state',
     'Xa_TFPI': 'xa_tfpi',
     'Xa_TFPI_VIIa_TF': 'xa_tfpi_viia_tf',
     'VIIa_TF_Xa_TFPI': 'viia_tf_xa_tfpi'}

    def __init__(self, model_path: str = 'data/BIOMD0000000360.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Panteleev2002TfpimechanismSchmema2Biomd0000000360Model = Panteleev2002TfpimechanismSchmema2Model
