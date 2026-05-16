# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lipniacki2004 - Mathematical model of NFKB regulatory module."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lipniacki2004MathematicalModelOfNfkbRegulatModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000786'
    _TITLE = 'Lipniacki2004 - Mathematical model of NFKB regulatory module'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ikk_active': ('IKK_active',
                    'native SBML value',
                    'IKK active. Maps to SBML symbol `IKK_active` and is emitted in native SBML '
                    'units.'),
     'ikkactive_ik_b': ('IKKactive_IkB',
                        'native SBML value',
                        'Ikkactive Ik B. Maps to SBML symbol `IKKactive_IkB` and is emitted in native '
                        'SBML units.'),
     'ikkactive_ik_b_nfkb': ('IKKactive_IkB_NFKB',
                             'native SBML value',
                             'Ikkactive Ik B NF-kB. Maps to SBML symbol `IKKactive_IkB_NFKB` and is '
                             'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tnf': ('TNF',
                     0.0,
                     'native SBML value',
                     'Initial level of TNF. Maps to SBML symbol `TNF`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_tnf_receptor_level': ('TNF_R',
                                    0.0,
                                    'native SBML value',
                                    'TNF receptor source parameter. Maps to SBML symbol `TNF_R` and '
                                    'preserves the bundled default.')}
    _SPECIES_LABELS = {'IKK_neutral': 'IKK Neutral',
     'IKK_active': 'IKK active',
     'IKK_inact': 'IKK Inact',
     'IKKactive_IkB': 'Ikkactive Ik B',
     'IkB': 'IkB',
     'IKKactive_IkB_NFKB': 'Ikkactive Ik B NF-kB',
     'IkB_NFKB': 'Ik B NF-kB',
     'NFKB': 'NF-kB',
     'NFKB_nuc': 'NF-kB Nuc',
     'IkB_nuc': 'Ik B Nuc',
     'IkB_NFKB_nuc': 'Ik B NF-kB Nuc',
     'IkB_mRNA': 'Ik B M RNA',
     'A20_mRNA': 'A20 M RNA',
     'A20': 'Abstract source state A20',
     'TNF': 'TNF',
     'cgen_mRNA': 'Cgen M RNA'}
    _STATE_OUTPUT_ALIASES = {'IKK_neutral': 'ikk_neutral',
     'IKK_active': 'ikk_active',
     'IKK_inact': 'ikk_inact',
     'IKKactive_IkB': 'ikkactive_ik_b',
     'IkB': 'ikb',
     'IKKactive_IkB_NFKB': 'ikkactive_ik_b_nfkb',
     'IkB_NFKB': 'ik_b_nfkb',
     'NFKB': 'nfkb',
     'NFKB_nuc': 'nfkb_nuc',
     'IkB_nuc': 'ik_b_nuc',
     'IkB_NFKB_nuc': 'ik_b_nfkb_nuc',
     'IkB_mRNA': 'ik_b_m_rna',
     'A20_mRNA': 'a20_m_rna',
     'A20': 'abstract_source_state_a20',
     'TNF': 'tnf',
     'cgen_mRNA': 'cgen_m_rna'}

    def __init__(self, model_path: str = 'data/BIOMD0000000786.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Lipniacki2004MathematicalModelOfNfkbRegulatBiomd0000000786Model = Lipniacki2004MathematicalModelOfNfkbRegulatModel
