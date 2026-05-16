# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Novak2022 - Mitotic kinase oscillation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Novak2022MitoticKinaseOscillationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001058'
    _TITLE = 'Novak2022 - Mitotic kinase oscillation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cln_cyclin': ('Cln',
                    'native SBML value',
                    'Cln cyclin. Maps to SBML symbol `Cln` and is emitted in native SBML units.'),
     'clb_cyclin_st': ('ClbSt',
                       'native SBML value',
                       'Clb cyclin St. Maps to SBML symbol `ClbSt` and is emitted in native SBML '
                       'units.'),
     'source_defined_mbf_state': ('MBF',
                                  'native SBML value',
                                  'source-defined MBF state. Maps to SBML symbol `MBF` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cln_cyclin': ('Cln',
                            0.0,
                            'native SBML value',
                            'Initial level of Cln cyclin. Maps to SBML symbol `Cln`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Cln': 'Cln cyclin',
     'ClbSt': 'Clb cyclin St',
     'MBF': 'source-defined MBF state',
     'Nrm1t': 'Nrm1t',
     'ClbMt': 'Clb cyclin Mt',
     'Polo': 'source-defined POLO state',
     'Sic1t': 'Sic1t',
     'SBF': 'source-defined SBF state',
     'Cdh1': 'Cdh1 cell-cycle regulator',
     'Cdc14': 'Cdc14 phosphatase'}
    _STATE_OUTPUT_ALIASES = {'Cln': 'cln_cyclin',
     'ClbSt': 'clb_cyclin_st',
     'MBF': 'source_defined_mbf_state',
     'Nrm1t': 'nrm1t',
     'ClbMt': 'clb_cyclin_mt',
     'Polo': 'source_defined_polo_state',
     'Sic1t': 'sic1t',
     'SBF': 'source_defined_sbf_state',
     'Cdh1': 'cdh1_cell_cycle_regulator',
     'Cdc14': 'cdc14_phosphatase'}

    def __init__(self, model_path: str = 'data/BIOMD0000001058.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Novak2022MitoticKinaseOscillationBiomd0000001058Model = Novak2022MitoticKinaseOscillationModel
