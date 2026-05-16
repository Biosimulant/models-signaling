# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Cursons2015 - Regulation of ERK-MAPK signaling in human epidermis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cursons2015RegulationOfErkMapkSignalingInModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000659'
    _TITLE = 'Cursons2015 - Regulation of ERK-MAPK signaling in human epidermis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytosolic_phosphorylated_erk': ('pERK_cyto',
                                      'native SBML value',
                                      'cytosolic phosphorylated ERK. Maps to SBML symbol `pERK_cyto` '
                                      'and is emitted in native SBML units.'),
     'nuclear_phosphorylated_erk': ('pERK_nuc',
                                    'native SBML value',
                                    'nuclear phosphorylated ERK. Maps to SBML symbol `pERK_nuc` and is '
                                    'emitted in native SBML units.'),
     'calmodulin': ('CaM_memb',
                    'native SBML value',
                    'calmodulin. Maps to SBML symbol `CaM_memb` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_calcium_amp_level': ('numCaInputAmp',
                                   0.092,
                                   'unit_0',
                                   'calcium AMP source parameter. Maps to SBML symbol `numCaInputAmp` '
                                   'and preserves the bundled default.'),
     'initial_calcium_baseline_level': ('numCaInputBaseline',
                                        0.754,
                                        'unit_0',
                                        'calcium Baseline source parameter. Maps to SBML symbol '
                                        '`numCaInputBaseline` and preserves the bundled default.'),
     'initial_calcium_m_amp_level': ('numCaMInputAmp',
                                     0.485,
                                     'unit_0',
                                     'calcium M AMP source parameter. Maps to SBML symbol '
                                     '`numCaMInputAmp` and preserves the bundled default.')}
    _SPECIES_LABELS = {'pRaf_cyto': 'source-defined RAFC state',
     'pMEK_cyto': 'source-defined MEKC state',
     'pERK_cyto': 'cytosolic phosphorylated ERK',
     'pMEK_nuc': 'source-defined MEKN state',
     'pERK_nuc': 'nuclear phosphorylated ERK',
     'Ca': 'calcium',
     'CaM_memb': 'calmodulin'}
    _STATE_OUTPUT_ALIASES = {'pRaf_cyto': 'source_defined_rafc_state',
     'pMEK_cyto': 'source_defined_mekc_state',
     'pERK_cyto': 'cytosolic_phosphorylated_erk',
     'pMEK_nuc': 'source_defined_mekn_state',
     'pERK_nuc': 'nuclear_phosphorylated_erk',
     'Ca': 'calcium',
     'CaM_memb': 'calmodulin'}

    def __init__(self, model_path: str = 'data/BIOMD0000000659.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cursons2015RegulationOfErkMapkSignalingInBiomd0000000659Model = Cursons2015RegulationOfErkMapkSignalingInModel
