# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zymomonas ED Pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class ZymomonasEdPathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2008060001'
    _TITLE = 'Zymomonas ED Pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ethanolex': ('ETHANOLex',
                   'native SBML value',
                   'Ethanolex. Maps to SBML symbol `ETHANOLex` and is emitted in native SBML units.'),
     'glucex': ('GLUCex',
                'native SBML value',
                'Glucex. Maps to SBML symbol `GLUCex` and is emitted in native SBML units.'),
     'pyrex': ('PYRex',
               'native SBML value',
               'Pyrex. Maps to SBML symbol `PYRex` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_co2ex': ('CO2ex',
                       36183.4535976826,
                       'native SBML value',
                       'Initial level of Co2ex. Maps to SBML symbol `CO2ex`; exposed as a traceable '
                       'initial-condition perturbation.'),
     'initial_glucex': ('GLUCex',
                        140000.0,
                        'native SBML value',
                        'Initial level of Glucex. Maps to SBML symbol `GLUCex`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'ETHANOLex': 'Ethanolex',
     'GLUCex': 'Glucex',
     'PYRex': 'Pyrex',
     'ACETper': 'Acetper',
     'ACETex': 'Acetex',
     'CO2per': 'Co2per',
     'CO2ex': 'Co2ex',
     'GLCi': 'Gluccy',
     'G6P': 'GLUC6P',
     'BPG': 'source-defined BPG state',
     'P3G': 'P3G',
     'P2G': 'P2G',
     'PEP': 'source-defined PEP state',
     'PYR': 'Pyrcy',
     'ACE': 'Acetcy',
     'NAD': 'NAD',
     'NADH': 'source-defined NADH state',
     'CO2': 'Co2cy',
     'ETOH': 'Ethanolcy',
     'ATP': 'ATP',
     'ADP': 'ADP',
     'PGLACTON': 'PGLACTON',
     'PGLUCONATE': 'PGLUCONATE',
     'KDPG': 'source-defined KDPG state',
     'GAP': 'source-defined GAP state',
     'AMP': 'AMP',
     'GLCo': 'Glucper',
     'ETHANOLper': 'Ethanolper',
     'PYRper': 'Pyrper'}
    _STATE_OUTPUT_ALIASES = {'ETHANOLex': 'ethanolex',
     'GLUCex': 'glucex',
     'PYRex': 'pyrex',
     'ACETper': 'acetper',
     'ACETex': 'acetex',
     'CO2per': 'co2per',
     'CO2ex': 'co2ex',
     'GLCi': 'gluccy',
     'G6P': 'gluc6p',
     'BPG': 'source_defined_bpg_state',
     'P3G': 'p3g',
     'P2G': 'p2g',
     'PEP': 'source_defined_pep_state',
     'PYR': 'pyrcy',
     'ACE': 'acetcy',
     'NAD': 'nad',
     'NADH': 'source_defined_nadh_state',
     'CO2': 'co2cy',
     'ETOH': 'ethanolcy',
     'ATP': 'atp',
     'ADP': 'adp',
     'PGLACTON': 'pglacton',
     'PGLUCONATE': 'pgluconate',
     'KDPG': 'source_defined_kdpg_state',
     'GAP': 'source_defined_gap_state',
     'AMP': 'amp',
     'GLCo': 'glucper',
     'ETHANOLper': 'ethanolper',
     'PYRper': 'pyrper'}

    def __init__(self, model_path: str = 'data/MODEL2008060001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


ZymomonasEdPathwayModel2008060001Model = ZymomonasEdPathwayModel
