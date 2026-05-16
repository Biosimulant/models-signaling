# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Cellière2011 - Plasticity of TGF-β Signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CelliRe2011PlasticityOfTgfSignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000600'
    _TITLE = 'Cellière2011 - Plasticity of TGF-β Signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'i_smad_tgf_beta_tgf_beta_r_p': ('I_Smad_TGFb_TGFbR_P',
                                      'native SBML value',
                                      'I SMAD TGF-beta TGF-beta R P. Maps to SBML symbol '
                                      '`I_Smad_TGFb_TGFbR_P` and is emitted in native SBML units.'),
     'smad': ('Smad',
              'native SBML value',
              'SMAD. Maps to SBML symbol `Smad` and is emitted in native SBML units.'),
     'smad_p': ('Smad_P',
                'native SBML value',
                'SMAD P. Maps to SBML symbol `Smad_P` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tgf_beta': ('TGFb',
                          460.0,
                          'native SBML value',
                          'Initial level of TGF-beta. Maps to SBML symbol `TGFb`; exposed as a '
                          'traceable initial-condition perturbation.'),
     'initial_i_smad_tgf_beta_tgf_beta_r_p': ('I_Smad_TGFb_TGFbR_P',
                                              0.0,
                                              'native SBML value',
                                              'Initial level of I SMAD TGF-beta TGF-beta R P. Maps to '
                                              'SBML symbol `I_Smad_TGFb_TGFbR_P`; exposed as a '
                                              'traceable initial-condition perturbation.'),
     'initial_tgf_beta_tgf_beta_r': ('TGFb_TGFbR',
                                     0.0,
                                     'native SBML value',
                                     'Initial level of TGF-beta TGF-beta R. Maps to SBML symbol '
                                     '`TGFb_TGFbR`; exposed as a traceable initial-condition '
                                     'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'TGFbR': 'TGF-beta R',
     'TGFb_TGFbR': 'TGF-beta TGF-beta R',
     'TGFb_TGFbR_P': 'TGF-beta TGF-beta R P',
     'I_Smad_TGFb_TGFbR_P': 'I SMAD TGF-beta TGF-beta R P',
     'Smad': 'SMAD',
     'Smad_P': 'SMAD P',
     'CoSmad': 'Co SMAD',
     'Smad_P_Smad_P': 'SMAD P SMAD P',
     'Smad_P_CoSmad': 'SMAD P Co SMAD',
     'I_Smad_mRNA2': 'I SMAD M RNA2',
     'I_Smad': 'I SMAD',
     'Smad_N': 'SMAD N',
     'Smad_P_Smad_P_N': 'SMAD P SMAD P N',
     'Smad_P_N': 'SMAD P N',
     'Smad_P_CoSmad_N': 'SMAD P Co SMAD N',
     'CoSmad_N': 'Co SMAD N',
     'I_Smad_mRNA1': 'I SMAD M RNA1',
     'TGFb': 'TGF-beta'}
    _STATE_OUTPUT_ALIASES = {'TGFbR': 'tgf_beta_r',
     'TGFb_TGFbR': 'tgf_beta_tgf_beta_r',
     'TGFb_TGFbR_P': 'tgf_beta_tgf_beta_r_p',
     'I_Smad_TGFb_TGFbR_P': 'i_smad_tgf_beta_tgf_beta_r_p',
     'Smad': 'smad',
     'Smad_P': 'smad_p',
     'CoSmad': 'co_smad',
     'Smad_P_Smad_P': 'smad_p_smad_p',
     'Smad_P_CoSmad': 'smad_p_co_smad',
     'I_Smad_mRNA2': 'i_smad_m_rna2',
     'I_Smad': 'i_smad',
     'Smad_N': 'smad_n',
     'Smad_P_Smad_P_N': 'smad_p_smad_p_n',
     'Smad_P_N': 'smad_p_n',
     'Smad_P_CoSmad_N': 'smad_p_co_smad_n',
     'CoSmad_N': 'co_smad_n',
     'I_Smad_mRNA1': 'i_smad_m_rna1',
     'TGFb': 'tgf_beta'}

    def __init__(self, model_path: str = 'data/BIOMD0000000600.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


CelliRe2011PlasticityOfTgfSignallingBiomd0000000600Model = CelliRe2011PlasticityOfTgfSignallingModel
