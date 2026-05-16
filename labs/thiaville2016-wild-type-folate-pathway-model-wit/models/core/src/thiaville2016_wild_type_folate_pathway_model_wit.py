# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Thiaville2016 - Wild type folate pathway model with proposed PanB reaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Thiaville2016WildTypeFolatePathwayModelWitModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000639'
    _TITLE = 'Thiaville2016 - Wild type folate pathway model with proposed PanB reaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphate': ('Phosphate',
                   'native SBML value',
                   'Phosphate. Maps to SBML symbol `Phosphate` and is emitted in native SBML units.'),
     'h2_hmpt': ('H2_HMPt',
                 'native SBML value',
                 'H2 Hmpt. Maps to SBML symbol `H2_HMPt` and is emitted in native SBML units.'),
     'atp': ('ATP',
             'native SBML value',
             'ATP. Maps to SBML symbol `ATP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP',
                     0.00056,
                     'native SBML value',
                     'Initial level of ADP. Maps to SBML symbol `ADP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_amp': ('AMP',
                     0.00028,
                     'native SBML value',
                     'Initial level of AMP. Maps to SBML symbol `AMP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_atp': ('ATP',
                     0.0096,
                     'native SBML value',
                     'Initial level of ATP. Maps to SBML symbol `ATP`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'H2_HMPt': 'H2 Hmpt',
     'ATP': 'ATP',
     'H2_HMPterinPP': 'H2 Hmpterin PP',
     'AMP': 'AMP',
     'p_ABA': 'source-defined P-ABA state',
     'PPi': 'source-defined PPI state',
     'H2_Pteroate': 'H2 Pteroate',
     'L_Glutamate': 'L Glutamate',
     'Phosphate': 'Phosphate',
     'ADP': 'ADP',
     'DHF': 'source-defined DHF state',
     'L_serine': 'L Serine',
     'Glycine': 'Glycine',
     'NADP': 'source-defined NADP state',
     'NADPH': 'NADPH',
     'THF': 'source-defined THF state',
     'CH2_THF': 'CH2 THF'}
    _STATE_OUTPUT_ALIASES = {'H2_HMPt': 'h2_hmpt',
     'ATP': 'atp',
     'H2_HMPterinPP': 'h2_hmpterin_pp',
     'AMP': 'amp',
     'p_ABA': 'source_defined_p_aba_state',
     'PPi': 'source_defined_ppi_state',
     'H2_Pteroate': 'h2_pteroate',
     'L_Glutamate': 'l_glutamate',
     'Phosphate': 'phosphate',
     'ADP': 'adp',
     'DHF': 'source_defined_dhf_state',
     'L_serine': 'l_serine',
     'Glycine': 'glycine',
     'NADP': 'source_defined_nadp_state',
     'NADPH': 'nadph',
     'THF': 'source_defined_thf_state',
     'CH2_THF': 'ch2_thf'}

    def __init__(self, model_path: str = 'data/BIOMD0000000639.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Thiaville2016WildTypeFolatePathwayModelWitBiomd0000000639Model = Thiaville2016WildTypeFolatePathwayModelWitModel
