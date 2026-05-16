# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sasagawa2005_MAPK."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sasagawa2005MapkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000049'
    _TITLE = 'Sasagawa2005_MAPK'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ras_gap': ('RasGAP',
                 'native SBML value',
                 'RAS GAP. Maps to SBML symbol `RasGAP` and is emitted in native SBML units.'),
     'erk': ('ERK',
             'native SBML value',
             'ERK. Maps to SBML symbol `ERK` and is emitted in native SBML units.'),
     'ras_gdp': ('Ras_GDP',
                 'native SBML value',
                 'RAS GDP. Maps to SBML symbol `Ras_GDP` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_degradation': ('degradation',
                             0.0,
                             'native SBML value',
                             'Initial level of Degradation. Maps to SBML symbol `degradation`; exposed '
                             'as a traceable initial-condition perturbation.'),
     'initial_egf': ('EGF',
                     0.001613,
                     'native SBML value',
                     'Initial level of EGF. Maps to SBML symbol `EGF`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_nerve_growth_factor': ('NGF',
                                     0.0,
                                     'native SBML value',
                                     'Initial level of nerve growth factor. Maps to SBML symbol `NGF`; '
                                     'exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EGFR': 'EGFR',
     'L_EGFR': 'L EGFR',
     'L_EGFR_dimer': 'L EGFR Dimer',
     'SOS': 'Source Defined SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
            'Exchange Factor State',
     'L_dpEGFR': 'L Dp EGFR',
     'pSOS': 'Phospho SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
             'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
             'Exchange Factor',
     'SOS_Grb2': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor Guanine '
                 'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                 'Exchange Factor Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein '
                 'Adapter Protein Adapter Protein',
     'Grb2': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter Protein '
             'Adapter Protein',
     'Dok': 'Source Defined DOK State',
     'pDok': 'Phospho Dok',
     'Crk': 'Source Defined CRK State',
     'FRS2': 'Source Defined FRS2 State',
     'Shc': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter Protein '
            'Adapter Protein',
     'pSOS_Grb2': 'Phospho SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
                  'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                  'Nucleotide Exchange Factor Grb2 adapter protein Adapter Protein Adapter Protein '
                  'Adapter Protein Adapter Protein Adapter Protein',
     'Rap1_GDP': 'RAP1 GDP',
     'MEK': 'MEK',
     'MKP3': 'Source Defined MKP3 State',
     'pShc_dpEGFR': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                    'Adapter Protein Adapter Protein Dp EGFR',
     'dpEGFR_c_Cbl': 'Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                     'Ligase Ubiquitin Ligase Ubiquitin Ligase',
     'B_Raf_Rap1_GTP': 'B RAF RAP1 GTP',
     'pShc_dpEGFR_c_Cbl': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                          'Adapter Protein Adapter Protein Dp EGFR C Cbl ubiquitin ligase Ubiquitin '
                          'Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase',
     'pFRS2_dpEGFR_c_Cbl': 'PFRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase '
                           'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase',
     'Shc_dpEGFR': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter '
                   'Protein Adapter Protein Dp EGFR',
     'c_Cbl': 'Source Defined C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
              'Ligase Ubiquitin Ligase State',
     'RasGAP': 'RAS GAP',
     'c_Raf': 'Source Defined C RAF State',
     'B_Raf': 'Source Defined B RAF State',
     'ERK': 'ERK',
     'PP2A': 'PP2A',
     'Ras_GDP': 'RAS GDP',
     'Rap1GAP': 'Rap1gap',
     'C3G': 'C3G',
     'NGFR': 'Source Defined NGFR State',
     'pShc': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter '
             'Protein Adapter Protein',
     'pFRS2_dpEGFR': 'PFRS2 Dp EGFR',
     'pTrkA_endo': 'Phospho Trk A Endo',
     'MEK_ERK': 'MEK ERK',
     'pMEK_ERK': 'Phospho MEK ERK',
     'FRS2_dpEGFR_c_Cbl_ubiq': 'FRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase '
                               'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiq',
     'Crk_C3G_pFRS2_dpEGFR_c_Cbl': 'Crk C3G PFRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase '
                                   'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                                   'Ligase',
     'pShc_dpEGFR_c_Cbl_ubiq': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter '
                               'Protein Adapter Protein Adapter Protein Dp EGFR C Cbl ubiquitin ligase '
                               'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase '
                               'Ubiquitin Ligase Ubiq',
     'Crk_C3G_pFRS2_dpEGFR': 'Crk C3G PFRS2 Dp EGFR',
     'Grb2_SOS_pShc_dpEGFR_c_Cbl_ubiq': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter '
                                        'Protein Adapter Protein Adapter Protein SOS '
                                        'guanine-nucleotide exchange factor Guanine Nucleotide '
                                        'Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                                        'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                                        'Phospho Shc adapter protein Adapter Protein Adapter Protein '
                                        'Adapter Protein Adapter Protein Adapter Protein Dp EGFR C Cbl '
                                        'ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                                        'Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiq',
     'Grb2_SOS_pShc_dpEGFR_c_Cbl': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter '
                                   'Protein Adapter Protein Adapter Protein SOS guanine-nucleotide '
                                   'exchange factor Guanine Nucleotide Exchange Factor Guanine '
                                   'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                                   'Guanine Nucleotide Exchange Factor Phospho Shc adapter protein '
                                   'Adapter Protein Adapter Protein Adapter Protein Adapter Protein '
                                   'Adapter Protein Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase '
                                   'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                                   'Ligase',
     'Shc_dpEGFR_c_Cbl_ubiq': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                              'Adapter Protein Adapter Protein Dp EGFR C Cbl ubiquitin ligase '
                              'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase '
                              'Ubiquitin Ligase Ubiq',
     'dpEGFR_c_Cbl_ubiq': 'Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                          'Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiq',
     'proteosome': 'Proteasome',
     'Grb2_SOS_pShc': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter '
                      'Protein Adapter Protein SOS guanine-nucleotide exchange factor Guanine '
                      'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                      'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Phospho Shc '
                      'adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter Protein '
                      'Adapter Protein',
     'Shc_dpEGFR_c_Cbl': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter '
                         'Protein Adapter Protein Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase '
                         'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase',
     'Grb2_SOS_pShc_dpEGFR': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein '
                             'Adapter Protein Adapter Protein SOS guanine-nucleotide exchange factor '
                             'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                             'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                             'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter '
                             'Protein Adapter Protein Adapter Protein Dp EGFR',
     'pFRS2': 'Source Defined PFRS2 State',
     'FRS2_dpEGFR': 'FRS2 Dp EGFR',
     'pDok_RasGAP': 'Phospho Dok RAS GAP',
     'pMEK': 'Phospho MEK',
     'FRS2_dpEGFR_c_Cbl': 'FRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin Ligase '
                          'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase',
     'pFRS2_dpEGFR_c_Cbl_ubiq': 'PFRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase Ubiquitin '
                                'Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiq',
     'Ras_GTP': 'RAS GTP',
     'Crk_C3G_pFRS2_dpEGFR_c_Cbl_ubiq': 'Crk C3G PFRS2 Dp EGFR C Cbl ubiquitin ligase Ubiquitin Ligase '
                                        'Ubiquitin Ligase Ubiquitin Ligase Ubiquitin Ligase Ubiquitin '
                                        'Ligase Ubiq',
     'c_Raf_Ras_GTP': 'C RAF RAS GTP',
     'B_Raf_Ras_GTP': 'B RAF RAS GTP',
     'ppMEK': 'Pp MEK',
     'ppERK': 'Pp ERK',
     'pTrkA': 'Phospho Trk A',
     'Crk_C3G': 'Crk C3G',
     'Rap1_GTP': 'RAP1 GTP',
     'L_NGFR': 'L NGFR',
     'ppMEK_ERK': 'Pp MEK ERK',
     'dppERK': 'Dpp ERK',
     'Shc_pTrkA': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter Protein '
                  'Adapter Protein Phospho Trk A',
     'Shc_pTrkA_endo': 'Shc adapter protein Adapter Protein Adapter Protein Adapter Protein Adapter '
                       'Protein Adapter Protein Phospho Trk A Endo',
     'pShc_pTrkA': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                   'Adapter Protein Adapter Protein Phospho Trk A',
     'pFRS2_pTrkA': 'PFRS2 Phospho Trk A',
     'FRS2_pTrkA': 'FRS2 Phospho Trk A',
     'pShc_pTrkA_endo': 'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter Protein '
                        'Adapter Protein Adapter Protein Phospho Trk A Endo',
     'FRS2_pTrkA_endo': 'FRS2 Phospho Trk A Endo',
     'pFRS2_pTrkA_endo': 'PFRS2 Phospho Trk A Endo',
     'Crk_C3G_pFRS2_pTrkA_endo': 'Crk C3G PFRS2 Phospho Trk A Endo',
     'Grb2_SOS_pShc_pTrkA': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein '
                            'Adapter Protein Adapter Protein SOS guanine-nucleotide exchange factor '
                            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor '
                            'Phospho Shc adapter protein Adapter Protein Adapter Protein Adapter '
                            'Protein Adapter Protein Adapter Protein Phospho Trk A',
     'Crk_C3G_pFRS2_pTrkA': 'Crk C3G PFRS2 Phospho Trk A',
     'Grb2_SOS_pShc_pTrkA_endo': 'Grb2 adapter protein Adapter Protein Adapter Protein Adapter Protein '
                                 'Adapter Protein Adapter Protein SOS guanine-nucleotide exchange '
                                 'factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                                 'Exchange Factor Guanine Nucleotide Exchange Factor Guanine '
                                 'Nucleotide Exchange Factor Phospho Shc adapter protein Adapter '
                                 'Protein Adapter Protein Adapter Protein Adapter Protein Adapter '
                                 'Protein Phospho Trk A Endo',
     'c_Raf_Ras_GTP_MEK': 'C RAF RAS GTP MEK',
     'c_Raf_Ras_GTP_pMEK': 'C RAF RAS GTP Phospho MEK',
     'c_Raf_Ras_GTP_MEK_ERK': 'C RAF RAS GTP MEK ERK',
     'c_Raf_Ras_GTP_pMEK_ERK': 'C RAF RAS GTP Phospho MEK ERK',
     'B_Raf_Ras_GTP_MEK': 'B RAF RAS GTP MEK',
     'B_Raf_Ras_GTP_pMEK': 'B RAF RAS GTP Phospho MEK',
     'B_Raf_Ras_GTP_MEK_ERK': 'B RAF RAS GTP MEK ERK',
     'B_Raf_Ras_GTP_pMEK_ERK': 'B RAF RAS GTP Phospho MEK ERK',
     'B_Raf_Rap1_GTP_MEK': 'B RAF RAP1 GTP MEK',
     'B_Raf_Rap1_GTP_pMEK': 'B RAF RAP1 GTP Phospho MEK',
     'B_Raf_Rap1_GTP_MEK_ERK': 'B RAF RAP1 GTP MEK ERK',
     'B_Raf_Rap1_GTP_pMEK_ERK': 'B RAF RAP1 GTP Phospho MEK ERK',
     'ppERK_MKP3': 'Pp ERK MKP3',
     'dppERK_MKP3': 'Dpp ERK MKP3',
     'pro_TrkA': 'Pro Trk A',
     'NGF': 'Source Defined Nerve Growth Factor State',
     'EGF': 'EGF',
     'pro_EGFR': 'Pro EGFR',
     'degradation': 'Degradation'}
    _STATE_OUTPUT_ALIASES = {'EGFR': 'egfr',
     'L_EGFR': 'l_egfr',
     'L_EGFR_dimer': 'l_egfr_dimer',
     'SOS': 'source_defined_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_state',
     'L_dpEGFR': 'l_dp_egfr',
     'pSOS': 'phospho_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor',
     'SOS_Grb2': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Grb2': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Dok': 'source_defined_dok_state',
     'pDok': 'phospho_dok',
     'Crk': 'source_defined_crk_state',
     'FRS2': 'source_defined_frs2_state',
     'Shc': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'pSOS_Grb2': 'phospho_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Rap1_GDP': 'rap1_gdp',
     'MEK': 'mek',
     'MKP3': 'source_defined_mkp3_state',
     'pShc_dpEGFR': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr',
     'dpEGFR_c_Cbl': 'dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'B_Raf_Rap1_GTP': 'b_raf_rap1_gtp',
     'pShc_dpEGFR_c_Cbl': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'pFRS2_dpEGFR_c_Cbl': 'pfrs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'Shc_dpEGFR': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr',
     'c_Cbl': 'source_defined_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_state',
     'RasGAP': 'ras_gap',
     'c_Raf': 'source_defined_c_raf_state',
     'B_Raf': 'source_defined_b_raf_state',
     'ERK': 'erk',
     'PP2A': 'pp2a',
     'Ras_GDP': 'ras_gdp',
     'Rap1GAP': 'rap1gap',
     'C3G': 'c3g',
     'NGFR': 'source_defined_ngfr_state',
     'pShc': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'pFRS2_dpEGFR': 'pfrs2_dp_egfr',
     'pTrkA_endo': 'phospho_trk_a_endo',
     'MEK_ERK': 'mek_erk',
     'pMEK_ERK': 'phospho_mek_erk',
     'FRS2_dpEGFR_c_Cbl_ubiq': 'frs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'Crk_C3G_pFRS2_dpEGFR_c_Cbl': 'crk_c3g_pfrs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'pShc_dpEGFR_c_Cbl_ubiq': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'Crk_C3G_pFRS2_dpEGFR': 'crk_c3g_pfrs2_dp_egfr',
     'Grb2_SOS_pShc_dpEGFR_c_Cbl_ubiq': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'Grb2_SOS_pShc_dpEGFR_c_Cbl': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'Shc_dpEGFR_c_Cbl_ubiq': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'dpEGFR_c_Cbl_ubiq': 'dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'proteosome': 'proteasome',
     'Grb2_SOS_pShc': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein',
     'Shc_dpEGFR_c_Cbl': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'Grb2_SOS_pShc_dpEGFR': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_dp_egfr',
     'pFRS2': 'source_defined_pfrs2_state',
     'FRS2_dpEGFR': 'frs2_dp_egfr',
     'pDok_RasGAP': 'phospho_dok_ras_gap',
     'pMEK': 'phospho_mek',
     'FRS2_dpEGFR_c_Cbl': 'frs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase',
     'pFRS2_dpEGFR_c_Cbl_ubiq': 'pfrs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'Ras_GTP': 'ras_gtp',
     'Crk_C3G_pFRS2_dpEGFR_c_Cbl_ubiq': 'crk_c3g_pfrs2_dp_egfr_c_cbl_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiquitin_ligase_ubiq',
     'c_Raf_Ras_GTP': 'c_raf_ras_gtp',
     'B_Raf_Ras_GTP': 'b_raf_ras_gtp',
     'ppMEK': 'pp_mek',
     'ppERK': 'pp_erk',
     'pTrkA': 'phospho_trk_a',
     'Crk_C3G': 'crk_c3g',
     'Rap1_GTP': 'rap1_gtp',
     'L_NGFR': 'l_ngfr',
     'ppMEK_ERK': 'pp_mek_erk',
     'dppERK': 'dpp_erk',
     'Shc_pTrkA': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a',
     'Shc_pTrkA_endo': 'shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a_endo',
     'pShc_pTrkA': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a',
     'pFRS2_pTrkA': 'pfrs2_phospho_trk_a',
     'FRS2_pTrkA': 'frs2_phospho_trk_a',
     'pShc_pTrkA_endo': 'phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a_endo',
     'FRS2_pTrkA_endo': 'frs2_phospho_trk_a_endo',
     'pFRS2_pTrkA_endo': 'pfrs2_phospho_trk_a_endo',
     'Crk_C3G_pFRS2_pTrkA_endo': 'crk_c3g_pfrs2_phospho_trk_a_endo',
     'Grb2_SOS_pShc_pTrkA': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a',
     'Crk_C3G_pFRS2_pTrkA': 'crk_c3g_pfrs2_phospho_trk_a',
     'Grb2_SOS_pShc_pTrkA_endo': 'grb2_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_phospho_shc_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_adapter_protein_phospho_trk_a_endo',
     'c_Raf_Ras_GTP_MEK': 'c_raf_ras_gtp_mek',
     'c_Raf_Ras_GTP_pMEK': 'c_raf_ras_gtp_phospho_mek',
     'c_Raf_Ras_GTP_MEK_ERK': 'c_raf_ras_gtp_mek_erk',
     'c_Raf_Ras_GTP_pMEK_ERK': 'c_raf_ras_gtp_phospho_mek_erk',
     'B_Raf_Ras_GTP_MEK': 'b_raf_ras_gtp_mek',
     'B_Raf_Ras_GTP_pMEK': 'b_raf_ras_gtp_phospho_mek',
     'B_Raf_Ras_GTP_MEK_ERK': 'b_raf_ras_gtp_mek_erk',
     'B_Raf_Ras_GTP_pMEK_ERK': 'b_raf_ras_gtp_phospho_mek_erk',
     'B_Raf_Rap1_GTP_MEK': 'b_raf_rap1_gtp_mek',
     'B_Raf_Rap1_GTP_pMEK': 'b_raf_rap1_gtp_phospho_mek',
     'B_Raf_Rap1_GTP_MEK_ERK': 'b_raf_rap1_gtp_mek_erk',
     'B_Raf_Rap1_GTP_pMEK_ERK': 'b_raf_rap1_gtp_phospho_mek_erk',
     'ppERK_MKP3': 'pp_erk_mkp3',
     'dppERK_MKP3': 'dpp_erk_mkp3',
     'pro_TrkA': 'pro_trk_a',
     'NGF': 'source_defined_nerve_growth_factor_state',
     'EGF': 'egf',
     'pro_EGFR': 'pro_egfr',
     'degradation': 'degradation'}

    def __init__(self, model_path: str = 'data/BIOMD0000000049.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sasagawa2005MapkBiomd0000000049Model = Sasagawa2005MapkModel
