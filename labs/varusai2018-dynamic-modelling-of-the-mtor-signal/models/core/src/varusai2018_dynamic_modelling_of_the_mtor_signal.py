# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Varusai2018 - Dynamic modelling of the mTOR signalling network reveals complex emergent behaviours conferred by DEPTOR."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Varusai2018DynamicModellingOfTheMtorSignalModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000823'
    _TITLE = 'Varusai2018 - Dynamic modelling of the mTOR signalling network reveals complex emergent behaviours conferred by DEPTOR'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt': ('Akt',
             'native SBML value',
             'AKT. Maps to SBML symbol `Akt` and is emitted in native SBML units.'),
     'source_defined_pakt_state': ('pAkt',
                                   'native SBML value',
                                   'source-defined PAKT state. Maps to SBML symbol `pAkt` and is '
                                   'emitted in native SBML units.'),
     'source_defined_pir_state': ('pIR',
                                  'native SBML value',
                                  'source-defined PIR state. Maps to SBML symbol `pIR` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_insulin_receptor': ('IR',
                                  0.0,
                                  'native SBML value',
                                  'Initial level of insulin receptor. Maps to SBML symbol `IR`; '
                                  'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IR': 'insulin receptor',
     'pIR': 'source-defined PIR state',
     'IRS': 'IRS',
     'pIRS': 'source-defined PIRS state',
     'iIRS': 'source-defined IIRS state',
     'Akt': 'AKT',
     'pAkt': 'source-defined PAKT state',
     'mTORC1': 'M TORC1',
     'pmTORC1': 'Pm TORC1',
     'mTORC2': 'M TORC2',
     'pmTORC2': 'Pm TORC2',
     'imTORC2': 'Im TORC2',
     'mTORC1_DEPTOR': 'M TORC1 DEPTOR',
     'mTORC2_DEPTOR': 'M TORC2 DEPTOR',
     'DEPTOR': 'DEPTOR',
     'pDEPTOR': 'P DEPTOR'}
    _STATE_OUTPUT_ALIASES = {'IR': 'insulin_receptor',
     'pIR': 'source_defined_pir_state',
     'IRS': 'irs',
     'pIRS': 'source_defined_pirs_state',
     'iIRS': 'source_defined_iirs_state',
     'Akt': 'akt',
     'pAkt': 'source_defined_pakt_state',
     'mTORC1': 'm_torc1',
     'pmTORC1': 'pm_torc1',
     'mTORC2': 'm_torc2',
     'pmTORC2': 'pm_torc2',
     'imTORC2': 'im_torc2',
     'mTORC1_DEPTOR': 'm_torc1_deptor',
     'mTORC2_DEPTOR': 'm_torc2_deptor',
     'DEPTOR': 'deptor',
     'pDEPTOR': 'p_deptor'}

    def __init__(self, model_path: str = 'data/BIOMD0000000823.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Varusai2018DynamicModellingOfTheMtorSignalBiomd0000000823Model = Varusai2018DynamicModellingOfTheMtorSignalModel
