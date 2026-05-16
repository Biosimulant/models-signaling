# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kervizic2008_Cholesterol_SREBP."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kervizic2008CholesterolSrebpModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL0568648427'
    _TITLE = 'Kervizic2008_Cholesterol_SREBP'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'srebp_scap': ('s0',
                    'native SBML value',
                    'SREBP SCAP. Maps to SBML symbol `s0` and is emitted in native SBML units.'),
     'acetyl_co_a_c_acetyltransferase_gene': ('s12',
                                              'native SBML value',
                                              'Acetyl Co A C Acetyltransferase Gene. Maps to SBML '
                                              'symbol `s12` and is emitted in native SBML units.'),
     'acetyl_co_a_c_acetyltransferase_rna': ('s13',
                                             'native SBML value',
                                             'Acetyl Co A C Acetyltransferase RNA. Maps to SBML symbol '
                                             '`s13` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_srebp_scap': ('s0',
                            0.0,
                            'native SBML value',
                            'Initial level of SREBP SCAP. Maps to SBML symbol `s0`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s0': 'SREBP SCAP',
     's1': 'P SREBP',
     's2': 'M SREBP',
     's3': 'HMG Co A Synthase Gene',
     's4': 'HMG Co A Synthase RNA',
     's5': 'HMG Co A Synthase',
     's6': 'HMG Co A Reductase Gene',
     's7': 'HMG Co A Reductase RNA',
     's8': 'HMG Co A Reductase',
     's9': 'FPP Synthase Gene',
     's10': 'FPP Synthase RNA',
     's11': 'FPP Synthase',
     's12': 'Acetyl Co A C Acetyltransferase Gene',
     's13': 'Acetyl Co A C Acetyltransferase RNA',
     's14': 'Acetyl Co A C Acetyltransferase',
     's15': 'Cyp51 Gene',
     's16': 'Cyp51 RNA',
     's17': 'Cyp51',
     's18': 'Acetyl Co A',
     's19': 'Acetoacetyl Co A',
     's20': 'HMG Co A',
     's21': 'Mevalonic Acid',
     's22': 'Mevalonyl Pyrophosphate',
     's23': 'Isopentenyl Pyrophosphate',
     's24': 'Dimethyl Allyl Pyrophosphate',
     's25': 'Geranyl Pyrophosphate',
     's26': 'Farnesyl Pyrophosphate',
     's27': 'Squalene',
     's28': 'Lanosterol',
     's29': 'Desmosterol',
     's30': 'Septdehydrocholesterol',
     's31': 'Cholesterol',
     's32': 'Statins'}
    _STATE_OUTPUT_ALIASES = {'s0': 'srebp_scap',
     's1': 'p_srebp',
     's2': 'm_srebp',
     's3': 'hmg_co_a_synthase_gene',
     's4': 'hmg_co_a_synthase_rna',
     's5': 'hmg_co_a_synthase',
     's6': 'hmg_co_a_reductase_gene',
     's7': 'hmg_co_a_reductase_rna',
     's8': 'hmg_co_a_reductase',
     's9': 'fpp_synthase_gene',
     's10': 'fpp_synthase_rna',
     's11': 'fpp_synthase',
     's12': 'acetyl_co_a_c_acetyltransferase_gene',
     's13': 'acetyl_co_a_c_acetyltransferase_rna',
     's14': 'acetyl_co_a_c_acetyltransferase',
     's15': 'cyp51_gene',
     's16': 'cyp51_rna',
     's17': 'cyp51',
     's18': 'acetyl_co_a',
     's19': 'acetoacetyl_co_a',
     's20': 'hmg_co_a',
     's21': 'mevalonic_acid',
     's22': 'mevalonyl_pyrophosphate',
     's23': 'isopentenyl_pyrophosphate',
     's24': 'dimethyl_allyl_pyrophosphate',
     's25': 'geranyl_pyrophosphate',
     's26': 'farnesyl_pyrophosphate',
     's27': 'squalene',
     's28': 'lanosterol',
     's29': 'desmosterol',
     's30': 'septdehydrocholesterol',
     's31': 'cholesterol',
     's32': 'statins'}

    def __init__(self, model_path: str = 'data/MODEL0568648427.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kervizic2008CholesterolSrebpModel0568648427Model = Kervizic2008CholesterolSrebpModel
