# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Benson2017 - Systems Pharmacology Multidrug (cholesterol biosynthesis pathway)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Benson2017SystemsPharmacologyMultidrugCholesModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1506220000'
    _TITLE = 'Benson2017 - Systems Pharmacology Multidrug (cholesterol biosynthesis pathway)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'rosuvastatin': ('s95',
                      'native SBML value',
                      'Rosuvastatin. Maps to SBML symbol `s95` and is emitted in native SBML units.'),
     'farnesyl_thiodiphosphate': ('s96',
                                  'native SBML value',
                                  'Farnesyl Thiodiphosphate. Maps to SBML symbol `s96` and is emitted '
                                  'in native SBML units.'),
     'source_6_fluoromevalonate_5_diphosphate': ('s98',
                                                 'native SBML value',
                                                 '6 Fluoromevalonate 5 Diphosphate. Maps to SBML '
                                                 'symbol `s98` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_rosuvastatin': ('s95',
                              0.0,
                              'native SBML value',
                              'Initial level of Rosuvastatin. Maps to SBML symbol `s95`; exposed as a '
                              'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s4': '3 Hydroxy 3 Methylglutaryl Co A',
     's5': 'Presqualene PP',
     's6': 'Squalene',
     's7': 'source-defined FDFT1 state',
     's10': 'Mevalonate P',
     's11': 'source-defined MVK state',
     's16': 'Mevalonate PP',
     's17': 'source-defined PMVK state',
     's20': 'Isopentenyl PP',
     's21': 'source-defined MVD state',
     's22': 'Dimethylallyl PP',
     's23': 'Geranyl PP',
     's29': 'source-defined FDPS state',
     's31': 'source-defined GGPS1 state',
     's38': 'source-defined IDI2 state',
     's39': 'source-defined IDI1 state',
     's77': 'Geranylgeranyl PP',
     's83': 'Acetyl Co A',
     's85': 'HMGCR',
     's86': 'Acetoacetyl Co A',
     's87': 'HMGCS1',
     's88': 'Mevaldyl Co A',
     's89': 'Mevalonate',
     's90': 'Farnesyl PP',
     's94': 'L 659 699',
     's95': 'Rosuvastatin',
     's96': 'Farnesyl Thiodiphosphate',
     's97': 'Cinnamic Acid',
     's98': '6 Fluoromevalonate 5 Diphosphate',
     's99': 'Zoledronic Acid',
     's100': 'BPH 628',
     's101': 'Zaragozic Acid'}
    _STATE_OUTPUT_ALIASES = {'s4': 'source_3_hydroxy_3_methylglutaryl_co_a',
     's5': 'presqualene_pp',
     's6': 'squalene',
     's7': 'source_defined_fdft1_state',
     's10': 'mevalonate_p',
     's11': 'source_defined_mvk_state',
     's16': 'mevalonate_pp',
     's17': 'source_defined_pmvk_state',
     's20': 'isopentenyl_pp',
     's21': 'source_defined_mvd_state',
     's22': 'dimethylallyl_pp',
     's23': 'geranyl_pp',
     's29': 'source_defined_fdps_state',
     's31': 'source_defined_ggps1_state',
     's38': 'source_defined_idi2_state',
     's39': 'source_defined_idi1_state',
     's77': 'geranylgeranyl_pp',
     's83': 'acetyl_co_a',
     's85': 'hmgcr',
     's86': 'acetoacetyl_co_a',
     's87': 'hmgcs1',
     's88': 'mevaldyl_co_a',
     's89': 'mevalonate',
     's90': 'farnesyl_pp',
     's94': 'l_659_699',
     's95': 'rosuvastatin',
     's96': 'farnesyl_thiodiphosphate',
     's97': 'cinnamic_acid',
     's98': 'source_6_fluoromevalonate_5_diphosphate',
     's99': 'zoledronic_acid',
     's100': 'bph_628',
     's101': 'zaragozic_acid'}

    def __init__(self, model_path: str = 'data/MODEL1506220000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Benson2017SystemsPharmacologyMultidrugCholesModel1506220000Model = Benson2017SystemsPharmacologyMultidrugCholesModel
