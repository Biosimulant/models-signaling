# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Rutkis2013 - Entner-Doudoroff pathway in Z.mobilis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rutkis2013EntnerDoudoroffPathwayInZMobilisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1409050000'
    _TITLE = 'Rutkis2013 - Entner-Doudoroff pathway in Z.mobilis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ethanolex': ('species_1',
                   'native SBML value',
                   'Ethanolex. Maps to SBML symbol `species_1` and is emitted in native SBML units.'),
     'glucex': ('GLCo',
                'native SBML value',
                'Glucex. Maps to SBML symbol `GLCo` and is emitted in native SBML units.'),
     'gluccy': ('GLCi',
                'native SBML value',
                'Gluccy. Maps to SBML symbol `GLCi` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_co2_state': ('CO2',
                                          180.0,
                                          'native SBML value',
                                          'Initial level of source-defined CO2 state. Maps to SBML '
                                          'symbol `CO2`; exposed as a traceable initial-condition '
                                          'perturbation.'),
     'initial_ethanolex': ('species_1',
                           1000.0,
                           'native SBML value',
                           'Initial level of Ethanolex. Maps to SBML symbol `species_1`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_glucex': ('GLCo',
                        140000.0,
                        'native SBML value',
                        'Initial level of Glucex. Maps to SBML symbol `GLCo`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_1': 'Ethanolex',
     'GLCo': 'Glucex',
     'GLCi': 'Gluccy',
     'G6P': 'GLUC6P',
     'BPG': 'source-defined BPG state',
     'P3G': 'P3G',
     'P2G': 'P2G',
     'PEP': 'source-defined PEP state',
     'PYR': 'source-defined PYR state',
     'ACE': 'source-defined ACET state',
     'NAD': 'NAD',
     'NADH': 'source-defined NADH state',
     'CO2': 'source-defined CO2 state',
     'ETOH': 'Ethanolcy',
     'ATP': 'ATP',
     'ADP': 'ADP',
     'species_2': 'PGLACTON',
     'species_3': 'PGLUCONATE',
     'species_4': 'source-defined KDPG state',
     'species_5': 'source-defined GAP state',
     'species_6': 'AMP'}
    _STATE_OUTPUT_ALIASES = {'species_1': 'ethanolex',
     'GLCo': 'glucex',
     'GLCi': 'gluccy',
     'G6P': 'gluc6p',
     'BPG': 'source_defined_bpg_state',
     'P3G': 'p3g',
     'P2G': 'p2g',
     'PEP': 'source_defined_pep_state',
     'PYR': 'source_defined_pyr_state',
     'ACE': 'source_defined_acet_state',
     'NAD': 'nad',
     'NADH': 'source_defined_nadh_state',
     'CO2': 'source_defined_co2_state',
     'ETOH': 'ethanolcy',
     'ATP': 'atp',
     'ADP': 'adp',
     'species_2': 'pglacton',
     'species_3': 'pgluconate',
     'species_4': 'source_defined_kdpg_state',
     'species_5': 'source_defined_gap_state',
     'species_6': 'amp'}

    def __init__(self, model_path: str = 'data/MODEL1409050000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Rutkis2013EntnerDoudoroffPathwayInZMobilisModel1409050000Model = Rutkis2013EntnerDoudoroffPathwayInZMobilisModel
