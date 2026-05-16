# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Capuani2015 - Binding of Cbl and Gbr2 to EGFR (Multisite Phosphorylation Model - MPM)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Capuani2015BindingOfCblAndGbr2ToEgfrMultModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000594'
    _TITLE = 'Capuani2015 - Binding of Cbl and Gbr2 to EGFR (Multisite Phosphorylation Model - MPM)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cbl_ubiquitin_ligase': ('Cbl',
                              'native SBML value',
                              'Cbl ubiquitin ligase. Maps to SBML symbol `Cbl` and is emitted in '
                              'native SBML units.'),
     'grb2_adapter_protein': ('Grb2',
                              'native SBML value',
                              'Grb2 adapter protein. Maps to SBML symbol `Grb2` and is emitted in '
                              'native SBML units.'),
     'tyrosine_site': ('Tyr',
                       'native SBML value',
                       'tyrosine site. Maps to SBML symbol `Tyr` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_egfr_00uu': ('EGFR_00UU',
                           0.833,
                           'native SBML value',
                           'Initial level of EGFR 00UU. Maps to SBML symbol `EGFR_00UU`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_egfr_01ug': ('EGFR_01UG',
                           0.0,
                           'native SBML value',
                           'Initial level of EGFR 01UG. Maps to SBML symbol `EGFR_01UG`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_cbl_ubiquitin_ligase_factor_level': ('CblFactor',
                                                   1.0,
                                                   'native SBML value',
                                                   'Cbl ubiquitin ligase Factor source parameter. Maps '
                                                   'to SBML symbol `CblFactor` and preserves the '
                                                   'bundled default.')}
    _SPECIES_LABELS = {'Cbl': 'Cbl ubiquitin ligase',
     'Grb2': 'Grb2 adapter protein',
     'CG': 'source-defined CG state',
     'Tyr': 'tyrosine site',
     'Ub': 'source-defined UB state',
     'TyrNorm': 'tyrosine site Norm',
     'UbNorm': 'Ub Norm',
     'EGFR_00UU': 'EGFR 00UU',
     'EGFR_10UU': 'EGFR 10UU',
     'EGFR_10CU': 'EGFR 10CU',
     'EGFR_10LU': 'EGFR 10LU',
     'EGFR_01UU': 'EGFR 01UU',
     'EGFR_01UG': 'EGFR 01UG',
     'EGFR_01UL': 'EGFR 01UL',
     'EGFR_11UU': 'EGFR 11UU',
     'EGFR_11CU': 'EGFR 11CU',
     'EGFR_11LU': 'EGFR 11LU',
     'EGFR_11UG': 'EGFR 11UG',
     'EGFR_11UL': 'EGFR 11UL',
     'EGFR_11CG': 'EGFR 11CG',
     'EGFR_11CC': 'EGFR 11CC',
     'EGFR_11LG': 'EGFR 11LG',
     'EGFR_02UU': 'EGFR 02UU',
     'EGFR_02UG': 'EGFR 02UG',
     'EGFR_02UL': 'EGFR 02UL',
     'EGFR_12UU': 'EGFR 12UU',
     'EGFR_12CU': 'EGFR 12CU',
     'EGFR_12LU': 'EGFR 12LU',
     'EGFR_12UG': 'EGFR 12UG',
     'EGFR_12UL': 'EGFR 12UL',
     'EGFR_12CG': 'EGFR 12CG',
     'EGFR_12CC': 'EGFR 12CC',
     'EGFR_12LG': 'EGFR 12LG'}
    _STATE_OUTPUT_ALIASES = {'Cbl': 'cbl_ubiquitin_ligase',
     'Grb2': 'grb2_adapter_protein',
     'CG': 'source_defined_cg_state',
     'Tyr': 'tyrosine_site',
     'Ub': 'source_defined_ub_state',
     'TyrNorm': 'tyrosine_site_norm',
     'UbNorm': 'ub_norm',
     'EGFR_00UU': 'egfr_00uu',
     'EGFR_10UU': 'egfr_10uu',
     'EGFR_10CU': 'egfr_10cu',
     'EGFR_10LU': 'egfr_10lu',
     'EGFR_01UU': 'egfr_01uu',
     'EGFR_01UG': 'egfr_01ug',
     'EGFR_01UL': 'egfr_01ul',
     'EGFR_11UU': 'egfr_11uu',
     'EGFR_11CU': 'egfr_11cu',
     'EGFR_11LU': 'egfr_11lu',
     'EGFR_11UG': 'egfr_11ug',
     'EGFR_11UL': 'egfr_11ul',
     'EGFR_11CG': 'egfr_11cg',
     'EGFR_11CC': 'egfr_11cc',
     'EGFR_11LG': 'egfr_11lg',
     'EGFR_02UU': 'egfr_02uu',
     'EGFR_02UG': 'egfr_02ug',
     'EGFR_02UL': 'egfr_02ul',
     'EGFR_12UU': 'egfr_12uu',
     'EGFR_12CU': 'egfr_12cu',
     'EGFR_12LU': 'egfr_12lu',
     'EGFR_12UG': 'egfr_12ug',
     'EGFR_12UL': 'egfr_12ul',
     'EGFR_12CG': 'egfr_12cg',
     'EGFR_12CC': 'egfr_12cc',
     'EGFR_12LG': 'egfr_12lg'}

    def __init__(self, model_path: str = 'data/BIOMD0000000594.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Capuani2015BindingOfCblAndGbr2ToEgfrMultBiomd0000000594Model = Capuani2015BindingOfCblAndGbr2ToEgfrMultModel
