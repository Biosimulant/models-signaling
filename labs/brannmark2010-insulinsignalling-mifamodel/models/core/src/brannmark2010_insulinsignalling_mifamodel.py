# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Brannmark2010_InsulinSignalling_Mifamodel."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Brannmark2010InsulinsignallingMifamodelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000343'
    _TITLE = 'Brannmark2010_InsulinSignalling_Mifamodel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'insulin_bound_insulin_receptor': ('IRins',
                                        'native SBML value',
                                        'insulin-bound insulin receptor. Maps to SBML symbol `IRins` '
                                        'and is emitted in native SBML units.'),
     'phosphorylated_insulin_receptor': ('IRp',
                                         'native SBML value',
                                         'phosphorylated insulin receptor. Maps to SBML symbol `IRp` '
                                         'and is emitted in native SBML units.'),
     'internalized_phosphorylated_insulin_receptor': ('IRip',
                                                      'native SBML value',
                                                      'internalized phosphorylated insulin receptor. '
                                                      'Maps to SBML symbol `IRip` and is emitted in '
                                                      'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_internalized_insulin_receptor_amount': ('intamount',
                                                      0.0,
                                                      'native SBML value',
                                                      'Initial level of internalized insulin receptor '
                                                      'amount. Maps to SBML symbol `intamount`; '
                                                      'exposed as a traceable initial-condition '
                                                      'perturbation.'),
     'initial_internalized_insulin_receptor': ('IRi',
                                               0.0,
                                               'native SBML value',
                                               'Initial level of internalized insulin receptor. Maps '
                                               'to SBML symbol `IRi`; exposed as a traceable '
                                               'initial-condition perturbation.'),
     'initial_insulin_bound_insulin_receptor': ('IRins',
                                                0.0,
                                                'native SBML value',
                                                'Initial level of insulin-bound insulin receptor. Maps '
                                                'to SBML symbol `IRins`; exposed as a traceable '
                                                'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IR': 'insulin receptor',
     'IRins': 'insulin-bound insulin receptor',
     'IRp': 'phosphorylated insulin receptor',
     'IRip': 'internalized phosphorylated insulin receptor',
     'IRi': 'internalized insulin receptor',
     'IRS': 'IRS',
     'IRSip': 'Irsip',
     'X': 'response node X',
     'Xp': 'phosphorylated response node X',
     'V1a': 'V1a',
     'V1b': 'V1b',
     'V1c': 'V1c',
     'V1d': 'V1d',
     'V1e': 'V1e',
     'V1g': 'V1g',
     'V1r': 'V1r',
     'V2': 'source-defined V2 state',
     'Vm2': 'source-defined VM2 state',
     'V3': 'source-defined V3 state',
     'Vm3': 'source-defined VM3 state',
     'simXP': 'simulated phosphorylated response node X',
     'intamount': 'internalized insulin receptor amount',
     'measIRp': 'Meas phosphorylated insulin receptor',
     'measdoublestep': 'Measdoublestep',
     'measanna': 'Measanna',
     'measdosR': 'Measdos R'}
    _STATE_OUTPUT_ALIASES = {'IR': 'insulin_receptor',
     'IRins': 'insulin_bound_insulin_receptor',
     'IRp': 'phosphorylated_insulin_receptor',
     'IRip': 'internalized_phosphorylated_insulin_receptor',
     'IRi': 'internalized_insulin_receptor',
     'IRS': 'irs',
     'IRSip': 'irsip',
     'X': 'response_node_x',
     'Xp': 'phosphorylated_response_node_x',
     'V1a': 'v1a',
     'V1b': 'v1b',
     'V1c': 'v1c',
     'V1d': 'v1d',
     'V1e': 'v1e',
     'V1g': 'v1g',
     'V1r': 'v1r',
     'V2': 'source_defined_v2_state',
     'Vm2': 'source_defined_vm2_state',
     'V3': 'source_defined_v3_state',
     'Vm3': 'source_defined_vm3_state',
     'simXP': 'simulated_phosphorylated_response_node_x',
     'intamount': 'internalized_insulin_receptor_amount',
     'measIRp': 'meas_phosphorylated_insulin_receptor',
     'measdoublestep': 'measdoublestep',
     'measanna': 'measanna',
     'measdosR': 'measdos_r'}

    def __init__(self, model_path: str = 'data/BIOMD0000000343.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Brannmark2010InsulinsignallingMifamodelBiomd0000000343Model = Brannmark2010InsulinsignallingMifamodelModel
