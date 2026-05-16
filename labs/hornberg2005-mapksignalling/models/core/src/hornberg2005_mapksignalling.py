# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hornberg2005 - MAPKsignalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hornberg2005MapksignallingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000667'
    _TITLE = 'Hornberg2005 - MAPKsignalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp': ('_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GDP',
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'value',
                                                                                             'EGF '
                                                                                             'Egfri 2 '
                                                                                             'GAP Grb2 '
                                                                                             'adapter '
                                                                                             'protein '
                                                                                             'SOS '
                                                                                             'guanine-nucleotide '
                                                                                             'exchange '
                                                                                             'factor '
                                                                                             'RAS GDP. '
                                                                                             'Maps to '
                                                                                             'SBML '
                                                                                             'symbol '
                                                                                             '`_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GDP` '
                                                                                             'and is '
                                                                                             'emitted '
                                                                                             'in '
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'units.'),
     'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp': ('_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GTP',
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'value',
                                                                                             'EGF '
                                                                                             'Egfri 2 '
                                                                                             'GAP Grb2 '
                                                                                             'adapter '
                                                                                             'protein '
                                                                                             'SOS '
                                                                                             'guanine-nucleotide '
                                                                                             'exchange '
                                                                                             'factor '
                                                                                             'RAS GTP. '
                                                                                             'Maps to '
                                                                                             'SBML '
                                                                                             'symbol '
                                                                                             '`_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GTP` '
                                                                                             'and is '
                                                                                             'emitted '
                                                                                             'in '
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'units.'),
     'ras_gdp': ('Ras_GDP',
                 'native SBML value',
                 'RAS GDP. Maps to SBML symbol `Ras_GDP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_egf': ('EGF',
                     4.99999999999939e-08,
                     'native SBML value',
                     'Initial level of EGF. Maps to SBML symbol `EGF`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_egf_egfr': ('EGF_EGFR',
                          0.0,
                          'native SBML value',
                          'Initial level of EGF EGFR. Maps to SBML symbol `EGF_EGFR`; exposed as a '
                          'traceable initial-condition perturbation.'),
     'initial_egf_egfr_2': ('_EGF_EGFR_2',
                            0.0,
                            'native SBML value',
                            'Initial level of EGF EGFR 2. Maps to SBML symbol `_EGF_EGFR_2`; exposed '
                            'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EGF': 'EGF',
     'EGFR': 'EGFR',
     'EGF_EGFR': 'EGF EGFR',
     '_EGF_EGFR_2': 'EGF EGFR 2',
     '_EGF_EGFR__2': 'EGF EGFR 2',
     'EGFRi': 'Egfri',
     '_EGF_EGFR__2_GAP_Grb2_Prot': 'EGF EGFR 2 GAP Grb2 adapter protein Prot',
     '_EGF_EGFRi__2': 'EGF Egfri 2',
     'Proti': 'Proti',
     'EGF_EGFRi': 'EGF Egfri',
     '_EGF_EGFRi_2': 'EGF Egfri 2',
     'Prot': 'source-defined PROT state',
     'EGFideg': 'Egfideg',
     'GAP': 'source-defined GAP state',
     '_EGF_EGFR__2_GAP': 'EGF EGFR 2 GAP',
     'EGFi': 'source-defined EGFI state',
     '_EGF_EGFRi__2_GAP': 'EGF Egfri 2 GAP',
     '_EGF_EGFRi__2_GAP_Grb2': 'EGF Egfri 2 GAP Grb2 adapter protein',
     '_EGF_EGFRi__2_GAP_Grb2_Sos': 'EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                   'exchange factor',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GDP': 'EGF Egfri 2 GAP Grb2 adapter protein SOS '
                                           'guanine-nucleotide exchange factor RAS GDP',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GTP': 'EGF Egfri 2 GAP Grb2 adapter protein SOS '
                                           'guanine-nucleotide exchange factor RAS GTP',
     'Grb2': 'Grb2 adapter protein',
     '_EGF_EGFR__2_GAP_Grb2': 'EGF EGFR 2 GAP Grb2 adapter protein',
     'Sos': 'SOS guanine-nucleotide exchange factor',
     '_EGF_EGFR__2_GAP_Grb2_Sos': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange '
                                  'factor',
     'Ras_GDP': 'RAS GDP',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GDP': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                          'exchange factor RAS GDP',
     'Ras_GTP': 'RAS GTP',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GTP': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                          'exchange factor RAS GTP',
     'Grb2_Sos': 'Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'Shc': 'Shc adapter protein',
     '_EGF_EGFR__2_GAP_SHC': 'EGF EGFR 2 GAP Shc adapter protein',
     '_EGF_EGFR__2_GAP_SHC_0': 'EGF EGFR 2 GAP Shc adapter protein',
     '_EGF_EGFR__2_GAP_SHC__Grb2': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS '
                                       'guanine-nucleotide exchange factor',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GDP': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter '
                                               'protein SOS guanine-nucleotide exchange factor RAS GDP',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GTP': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter '
                                               'protein SOS guanine-nucleotide exchange factor RAS GTP',
     'Shc__Grb2_Sos': 'Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'Shc__Grb2': 'Shc adapter protein Grb2 adapter protein',
     'Shc_0': 'Shc adapter protein',
     'Raf': 'RAF',
     'Raf_Ras_GTP': 'RAF RAS GTP',
     'Ras_GTP_': 'RAS GTP',
     'Phosphatase1': 'Phosphatase1',
     'Raf_0': 'RAF',
     'Raf__phosphatase1': 'RAF Phosphatase1',
     'MEK': 'MEK',
     'MEK_Raf': 'MEK RAF',
     'MEK_P': 'source-defined MEK_P state',
     'MEK_P_Raf': 'MEK P RAF',
     'MEK_PP': 'MEK PP',
     'MEK_PP_phosphatase2': 'MEK PP Phosphatase2',
     'phosphatse2': 'Phosphatse2',
     'MEK_P_phosphatase2': 'MEK P Phosphatase2',
     'ERK': 'ERK',
     'ERK_MEK_PP': 'ERK MEK PP',
     'ERK_P': 'source-defined ERK_P state',
     'ERK_P_MEKPP': 'ERK P MEKPP',
     'ERK_PP': 'ERK PP',
     'phosphatase3': 'Phosphatase3',
     'ERK_PP_phosphatase3': 'ERK PP Phosphatase3',
     'ERK_P_phosphatase3': 'ERK P Phosphatase3',
     '_EGF_EGFRi__2_GAP_SHC': 'EGF Egfri 2 GAP Shc adapter protein',
     '_EGF_EGFRi__2_GAP_SHC_0': 'EGF Egfri 2 GAP Shc adapter protein',
     '_EGF_EGFRi__2_GAP_SHC__Grb2': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein SOS '
                                        'guanine-nucleotide exchange factor',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_Ras_GDP': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter '
                                                'protein SOS guanine-nucleotide exchange factor RAS '
                                                'GDP',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_Ras_GTP': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter '
                                                'protein SOS guanine-nucleotide exchange factor RAS '
                                                'GTP',
     'Ras_GTPi': 'RAS Gtpi',
     'Raf_Ras_GTPi': 'RAF RAS Gtpi',
     'Ras_GTPi_0': 'RAS Gtpi',
     'Rafi': 'source-defined RAFI* state',
     'Rafi__phosphatase1': 'Rafi Phosphatase1',
     'MEK_Rafi': 'MEK Rafi',
     'MEKi_P': 'Meki P',
     'MEK_P_Rafi': 'MEK P Rafi',
     'MEKi_PP': 'Meki PP',
     'MEKi_PP_phosphatase2': 'Meki PP Phosphatase2',
     'MEKi_P_phosphatase2': 'Meki P Phosphatase2',
     'ERKi_P': 'Erki P',
     'ERKi_P_MEKi_PP': 'Erki P Meki PP',
     'ERKi_PP': 'Erki PP',
     'ERKi_PP_phosphatase3': 'Erki PP Phosphatase3',
     'ERKi_P_phosphatase3': 'Erki P Phosphatase3',
     'EGFRidag': 'Egfridag',
     '_EGF_EGFRi___2deg': 'EGF Egfri 2deg',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Prot': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                       'exchange factor Prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GDP_Prot': 'EGF EGFR 2 GAP Grb2 adapter protein SOS '
                                               'guanine-nucleotide exchange factor RAS GDP Prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GTP_Prot': 'EGF EGFR 2 GAP Grb2 adapter protein SOS '
                                               'guanine-nucleotide exchange factor RAS GTP Prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_ERK_PP': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                         'exchange factor ERK PP',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_ERKi_PP': 'EGF Egfri 2 GAP Grb2 adapter protein SOS '
                                           'guanine-nucleotide exchange factor Erki PP',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_ERK_PP': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein '
                                              'SOS guanine-nucleotide exchange factor ERK PP',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_ERKi_PP': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter '
                                                'protein SOS guanine-nucleotide exchange factor Erki '
                                                'PP',
     '_EGF_EGFR__2_GAP_Grb2_Sos_deg': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                      'exchange factor Deg',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_deg': 'EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide '
                                       'exchange factor Deg',
     'Sos_ERK_PP': 'SOS guanine-nucleotide exchange factor ERK PP',
     'Sos_ERKi_PP': 'SOS guanine-nucleotide exchange factor Erki PP',
     'Sosi': 'source-defined SOSI state',
     'ERKi_MEKi_PP_0': 'Erki Meki PP',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Prot_0': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein '
                                          'Prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Prot_0': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein '
                                              'SOS guanine-nucleotide exchange factor Prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GDP_Prot_0': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter '
                                                      'protein SOS guanine-nucleotide exchange factor '
                                                      'RAS GDP Prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GTP_Prot_0': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter '
                                                      'protein SOS guanine-nucleotide exchange factor '
                                                      'RAS GTP Prot'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'egf',
     'EGFR': 'egfr',
     'EGF_EGFR': 'egf_egfr',
     '_EGF_EGFR_2': 'egf_egfr_2',
     '_EGF_EGFR__2': 'egf_egfr_2_2',
     'EGFRi': 'egfri',
     '_EGF_EGFR__2_GAP_Grb2_Prot': 'egf_egfr_2_gap_grb2_adapter_protein_prot',
     '_EGF_EGFRi__2': 'egf_egfri_2',
     'Proti': 'proti',
     'EGF_EGFRi': 'egf_egfri',
     '_EGF_EGFRi_2': 'egf_egfri_2_2',
     'Prot': 'source_defined_prot_state',
     'EGFideg': 'egfideg',
     'GAP': 'source_defined_gap_state',
     '_EGF_EGFR__2_GAP': 'egf_egfr_2_gap',
     'EGFi': 'source_defined_egfi_state',
     '_EGF_EGFRi__2_GAP': 'egf_egfri_2_gap',
     '_EGF_EGFRi__2_GAP_Grb2': 'egf_egfri_2_gap_grb2_adapter_protein',
     '_EGF_EGFRi__2_GAP_Grb2_Sos': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GDP': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GTP': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'Grb2': 'grb2_adapter_protein',
     '_EGF_EGFR__2_GAP_Grb2': 'egf_egfr_2_gap_grb2_adapter_protein',
     'Sos': 'sos_guanine_nucleotide_exchange_factor',
     '_EGF_EGFR__2_GAP_Grb2_Sos': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'Ras_GDP': 'ras_gdp',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GDP': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     'Ras_GTP': 'ras_gtp',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GTP': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'Grb2_Sos': 'grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'Shc': 'shc_adapter_protein',
     '_EGF_EGFR__2_GAP_SHC': 'egf_egfr_2_gap_shc_adapter_protein',
     '_EGF_EGFR__2_GAP_SHC_0': 'egf_egfr_2_gap_shc_adapter_protein_2',
     '_EGF_EGFR__2_GAP_SHC__Grb2': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GDP': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GTP': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'Shc__Grb2_Sos': 'shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'Shc__Grb2': 'shc_adapter_protein_grb2_adapter_protein',
     'Shc_0': 'shc_adapter_protein_2',
     'Raf': 'raf',
     'Raf_Ras_GTP': 'raf_ras_gtp',
     'Ras_GTP_': 'ras_gtp_2',
     'Phosphatase1': 'phosphatase1',
     'Raf_0': 'raf_2',
     'Raf__phosphatase1': 'raf_phosphatase1',
     'MEK': 'mek',
     'MEK_Raf': 'mek_raf',
     'MEK_P': 'source_defined_mek_p_state',
     'MEK_P_Raf': 'mek_p_raf',
     'MEK_PP': 'mek_pp',
     'MEK_PP_phosphatase2': 'mek_pp_phosphatase2',
     'phosphatse2': 'phosphatse2',
     'MEK_P_phosphatase2': 'mek_p_phosphatase2',
     'ERK': 'erk',
     'ERK_MEK_PP': 'erk_mek_pp',
     'ERK_P': 'source_defined_erk_p_state',
     'ERK_P_MEKPP': 'erk_p_mekpp',
     'ERK_PP': 'erk_pp',
     'phosphatase3': 'phosphatase3',
     'ERK_PP_phosphatase3': 'erk_pp_phosphatase3',
     'ERK_P_phosphatase3': 'erk_p_phosphatase3',
     '_EGF_EGFRi__2_GAP_SHC': 'egf_egfri_2_gap_shc_adapter_protein',
     '_EGF_EGFRi__2_GAP_SHC_0': 'egf_egfri_2_gap_shc_adapter_protein_2',
     '_EGF_EGFRi__2_GAP_SHC__Grb2': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_Ras_GDP': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_Ras_GTP': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'Ras_GTPi': 'ras_gtpi',
     'Raf_Ras_GTPi': 'raf_ras_gtpi',
     'Ras_GTPi_0': 'ras_gtpi_2',
     'Rafi': 'source_defined_rafi_state',
     'Rafi__phosphatase1': 'rafi_phosphatase1',
     'MEK_Rafi': 'mek_rafi',
     'MEKi_P': 'meki_p',
     'MEK_P_Rafi': 'mek_p_rafi',
     'MEKi_PP': 'meki_pp',
     'MEKi_PP_phosphatase2': 'meki_pp_phosphatase2',
     'MEKi_P_phosphatase2': 'meki_p_phosphatase2',
     'ERKi_P': 'erki_p',
     'ERKi_P_MEKi_PP': 'erki_p_meki_pp',
     'ERKi_PP': 'erki_pp',
     'ERKi_PP_phosphatase3': 'erki_pp_phosphatase3',
     'ERKi_P_phosphatase3': 'erki_p_phosphatase3',
     'EGFRidag': 'egfridag',
     '_EGF_EGFRi___2deg': 'egf_egfri_2deg',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Prot': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GDP_Prot': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp_prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_Ras_GTP_Prot': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp_prot',
     '_EGF_EGFR__2_GAP_Grb2_Sos_ERK_PP': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_erk_pp',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_ERKi_PP': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_erki_pp',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_ERK_PP': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_erk_pp',
     '_EGF_EGFRi__2_GAP_SHC__Grb2_Sos_ERKi_PP': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_erki_pp',
     '_EGF_EGFR__2_GAP_Grb2_Sos_deg': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_deg',
     '_EGF_EGFRi__2_GAP_Grb2_Sos_deg': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_deg',
     'Sos_ERK_PP': 'sos_guanine_nucleotide_exchange_factor_erk_pp',
     'Sos_ERKi_PP': 'sos_guanine_nucleotide_exchange_factor_erki_pp',
     'Sosi': 'source_defined_sosi_state',
     'ERKi_MEKi_PP_0': 'erki_meki_pp',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Prot_0': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Prot_0': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GDP_Prot_0': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp_prot',
     '_EGF_EGFR__2_GAP_SHC__Grb2_Sos_Ras_GTP_Prot_0': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp_prot'}

    def __init__(self, model_path: str = 'data/BIOMD0000000667.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hornberg2005MapksignallingBiomd0000000667Model = Hornberg2005MapksignallingModel
