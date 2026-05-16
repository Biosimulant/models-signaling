# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Integrated Model of DNA Damage Response and p53 Signaling in ATM/ATR-Deficient Ataxia Telangiectasia: Exploring the Therapeutic Roles of Possible repurposed drugs."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class IntegratedModelOfDnaDamageResponseAndP53Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2503190002'
    _TITLE = 'Integrated Model of DNA Damage Response and p53 Signaling in ATM/ATR-Deficient Ataxia Telangiectasia: Exploring the Therapeutic Roles of Possible repurposed drugs'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'atm_inactive': ('ATM_inactive',
                      'native SBML value',
                      'ATM Inactive. Maps to SBML symbol `ATM_inactive` and is emitted in native SBML '
                      'units.'),
     'atm_active': ('ATM_active',
                    'native SBML value',
                    'ATM active. Maps to SBML symbol `ATM_active` and is emitted in native SBML '
                    'units.'),
     'atr_inactive': ('ATR_inactive',
                      'native SBML value',
                      'ATR Inactive. Maps to SBML symbol `ATR_inactive` and is emitted in native SBML '
                      'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_ck2_state': ('CK2',
                                          50.0,
                                          'native SBML value',
                                          'Initial level of source-defined CK2 state. Maps to SBML '
                                          'symbol `CK2`; exposed as a traceable initial-condition '
                                          'perturbation.'),
     'initial_keap1': ('KEAP1',
                       100.0,
                       'native SBML value',
                       'Initial level of KEAP1. Maps to SBML symbol `KEAP1`; exposed as a traceable '
                       'initial-condition perturbation.'),
     'initial_omaveloxolone': ('Omaveloxolone',
                               0.0,
                               'native SBML value',
                               'Initial level of Omaveloxolone. Maps to SBML symbol `Omaveloxolone`; '
                               'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'ATM_inactive': 'ATM Inactive',
     'ATM_active': 'ATM active',
     'ATR_inactive': 'ATR Inactive',
     'ATR_active': 'ATR active',
     'DNA_damage': 'DNA Damage',
     'p53_inactive': 'P53 Inactive',
     'p53_active': 'P53 active',
     'HDAC4_inactive': 'HDAC4 Inactive',
     'HDAC4_active': 'HDAC4 active',
     'HDAC4_phospho': 'HDAC4 Phospho',
     'PP2A': 'PP2A',
     'I2PP2A': 'I2PP2A',
     'PP2A_I2PP2A': 'PP2A I2PP2A',
     'TOPBP1_inactive': 'TOPBP1 Inactive',
     'TOPBP1_active': 'TOPBP1 active',
     'CK2': 'source-defined CK2 state',
     'CHK1_inactive': 'CHK1 Inactive',
     'CHK1_active': 'CHK1 active',
     'CHK2_inactive': 'CHK2 Inactive',
     'CHK2_active': 'CHK2 active',
     'NRF2_inactive': 'NRF2 Inactive',
     'NRF2_active': 'NRF2 active',
     'KEAP1': 'KEAP1',
     'NRF2_degraded': 'NRF2 Degraded',
     'Omaveloxolone': 'Omaveloxolone',
     'Spermidine': 'Spermidine',
     'Autophagy_inactive': 'Autophagy Inactive',
     'Autophagy_active': 'Autophagy active',
     'p21': 'Abstract source state P21',
     'BAX': 'source-defined BAX state',
     'PUMA': 'source-defined PUMA state'}
    _STATE_OUTPUT_ALIASES = {'ATM_inactive': 'atm_inactive',
     'ATM_active': 'atm_active',
     'ATR_inactive': 'atr_inactive',
     'ATR_active': 'atr_active',
     'DNA_damage': 'dna_damage',
     'p53_inactive': 'p53_inactive',
     'p53_active': 'p53_active',
     'HDAC4_inactive': 'hdac4_inactive',
     'HDAC4_active': 'hdac4_active',
     'HDAC4_phospho': 'hdac4_phospho',
     'PP2A': 'pp2a',
     'I2PP2A': 'i2pp2a',
     'PP2A_I2PP2A': 'pp2a_i2pp2a',
     'TOPBP1_inactive': 'topbp1_inactive',
     'TOPBP1_active': 'topbp1_active',
     'CK2': 'source_defined_ck2_state',
     'CHK1_inactive': 'chk1_inactive',
     'CHK1_active': 'chk1_active',
     'CHK2_inactive': 'chk2_inactive',
     'CHK2_active': 'chk2_active',
     'NRF2_inactive': 'nrf2_inactive',
     'NRF2_active': 'nrf2_active',
     'KEAP1': 'keap1',
     'NRF2_degraded': 'nrf2_degraded',
     'Omaveloxolone': 'omaveloxolone',
     'Spermidine': 'spermidine',
     'Autophagy_inactive': 'autophagy_inactive',
     'Autophagy_active': 'autophagy_active',
     'p21': 'abstract_source_state_p21',
     'BAX': 'source_defined_bax_state',
     'PUMA': 'source_defined_puma_state'}

    def __init__(self, model_path: str = 'data/MODEL2503190002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


IntegratedModelOfDnaDamageResponseAndP53Model2503190002Model = IntegratedModelOfDnaDamageResponseAndP53Model
