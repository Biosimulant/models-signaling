# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sible2007 - Mitotic cell cycle mecanism in Xenopus Laevis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sible2007MitoticCellCycleMecanismInXenopusModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000942'
    _TITLE = 'Sible2007 - Mitotic cell cycle mecanism in Xenopus Laevis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cdc25_phosphorylated': ('Cdc25_phosphorylated',
                              'native SBML value',
                              'Cdc25 Phosphorylated. Maps to SBML symbol `Cdc25_phosphorylated` and is '
                              'emitted in native SBML units.'),
     'wee1_phosphorylated': ('Wee1_phosphorylated',
                             'native SBML value',
                             'Wee1 Phosphorylated. Maps to SBML symbol `Wee1_phosphorylated` and is '
                             'emitted in native SBML units.'),
     'ie_phosphorylated': ('IE_phosphorylated',
                           'native SBML value',
                           'IE Phosphorylated. Maps to SBML symbol `IE_phosphorylated` and is emitted '
                           'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_apc_total': ('APC_total',
                           1.0,
                           'native SBML value',
                           'Initial level of APC Total. Maps to SBML symbol `APC_total`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_cdc25': ('Cdc25',
                       1.0,
                       'native SBML value',
                       'Initial level of Cdc25. Maps to SBML symbol `Cdc25`; exposed as a traceable '
                       'initial-condition perturbation.'),
     'initial_cdc25_total': ('Cdc25_total',
                             1.0,
                             'native SBML value',
                             'Initial level of Cdc25 Total. Maps to SBML symbol `Cdc25_total`; exposed '
                             'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Cdc25': 'Cdc25',
     'Cdc25_phosphorylated': 'Cdc25 Phosphorylated',
     'Cyclin_Cdk1_MPF': 'Cyclin Cdk1 MPF',
     'Cyclin_Cdk1_preMPF': 'Cyclin Cdk1 Pre MPF',
     'Wee1': 'source-defined WEE1 state',
     'Wee1_phosphorylated': 'Wee1 Phosphorylated',
     'Cyclin': 'Cyclin',
     'Cdk1': 'source-defined CDK1 state',
     'IE': 'source-defined IE state',
     'IE_phosphorylated': 'IE Phosphorylated',
     'APC_active': 'APC active',
     'Cdk1_total': 'Cdk1 Total',
     'Cdc25_total': 'Cdc25 Total',
     'Wee1_total': 'Wee1 Total',
     'IE_total': 'IE Total',
     'APC_total': 'APC Total',
     'ppase': 'Ppase',
     'Cyclin_total': 'Cyclin Total'}
    _STATE_OUTPUT_ALIASES = {'Cdc25': 'cdc25',
     'Cdc25_phosphorylated': 'cdc25_phosphorylated',
     'Cyclin_Cdk1_MPF': 'cyclin_cdk1_mpf',
     'Cyclin_Cdk1_preMPF': 'cyclin_cdk1_pre_mpf',
     'Wee1': 'source_defined_wee1_state',
     'Wee1_phosphorylated': 'wee1_phosphorylated',
     'Cyclin': 'cyclin',
     'Cdk1': 'source_defined_cdk1_state',
     'IE': 'source_defined_ie_state',
     'IE_phosphorylated': 'ie_phosphorylated',
     'APC_active': 'apc_active',
     'Cdk1_total': 'cdk1_total',
     'Cdc25_total': 'cdc25_total',
     'Wee1_total': 'wee1_total',
     'IE_total': 'ie_total',
     'APC_total': 'apc_total',
     'ppase': 'ppase',
     'Cyclin_total': 'cyclin_total'}

    def __init__(self, model_path: str = 'data/BIOMD0000000942.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sible2007MitoticCellCycleMecanismInXenopusBiomd0000000942Model = Sible2007MitoticCellCycleMecanismInXenopusModel
