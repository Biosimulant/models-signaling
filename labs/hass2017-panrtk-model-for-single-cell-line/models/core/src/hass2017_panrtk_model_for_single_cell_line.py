# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for PanRTK model for single cell line."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hass2017PanrtkModelForSingleCellLineModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1708210000'
    _TITLE = 'PanRTK model for single cell line'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'erk': ('ERK', 'substance', 'ERK. Maps to SBML symbol `ERK` and is emitted in native SBML units.'),
     'perk_kinase': ('pERK',
                     'substance',
                     'PERK kinase. Maps to SBML symbol `pERK` and is emitted in native SBML units.'),
     'akt': ('AKT', 'substance', 'AKT. Maps to SBML symbol `AKT` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_akt_activation_p_egfr_level': ('AKT_activation_pEGFR',
                                             1.00000000000008e-05,
                                             'native SBML value',
                                             'AKT Activation P EGFR source parameter. Maps to SBML '
                                             'symbol `AKT_activation_pEGFR` and preserves the bundled '
                                             'default.'),
     'initial_akt_activation_p_met_egfr_level': ('AKT_activation_pMetEGFR',
                                                 1.00000000000016e-05,
                                                 'native SBML value',
                                                 'AKT Activation P Met EGFR source parameter. Maps to '
                                                 'SBML symbol `AKT_activation_pMetEGFR` and preserves '
                                                 'the bundled default.'),
     'initial_egf_k_d_level': ('EGF_kD',
                               1.0,
                               'native SBML value',
                               'EGF K D source parameter. Maps to SBML symbol `EGF_kD` and preserves '
                               'the bundled default.')}
    _SPECIES_LABELS = {'dose_EGF': 'Dose EGF',
     'dose_HGF': 'Dose HGF',
     'RTKph': 'Rtkph',
     'dose_IGF1': 'Dose IGF1',
     'dose_HRG': 'Dose heregulin',
     'EGFR': 'EGFR',
     'EGFR_EGF': 'EGFR EGF',
     'pEGFRd': 'P Egfrd',
     'pEGFRi': 'P Egfri',
     'pEGFRi_ph': 'P Egfri Ph',
     'EGFRi': 'Egfri',
     'ErbB2': 'source-defined ERBB2 state',
     'pErbB2': 'P Erb B2',
     'pErbB2i': 'P Erb B2i',
     'ErbB2i': 'Erb B2i',
     'pErbB2i_ph': 'P Erb B2i Ph',
     'pErbB12': 'P Erb B12',
     'pErbB12i': 'P Erb B12i',
     'pErbB12i_ph': 'P Erb B12i Ph',
     'ErbB3': 'source-defined ERBB3 state',
     'ErbB3_HRG': 'Erb B3 heregulin',
     'pErbB3d': 'P Erb B3d',
     'pErbB3i': 'P Erb B3i',
     'pErbB3i_ph': 'P Erb B3i Ph',
     'ErbB3i': 'Erb B3i',
     'pErbB13': 'P Erb B13',
     'pErbB13i': 'P Erb B13i',
     'pErbB13i_ph': 'P Erb B13i Ph',
     'pErbB32': 'P Erb B32',
     'pErbB32i': 'P Erb B32i',
     'pErbB32i_ph': 'P Erb B32i Ph',
     'IGF1R': 'IGF1R',
     'IGF1R_IGF1': 'IGF1R IGF1',
     'pIGF1Rd': 'P Igf1rd',
     'pIGF1Ri': 'P Igf1ri',
     'pIGF1Ri_ph': 'P Igf1ri Ph',
     'IGF1Ri': 'Igf1ri',
     'Met': 'source-defined MET state',
     'Met_HGF': 'Met HGF',
     'pMetd': 'P Metd',
     'pMeti': 'P Meti',
     'pMeti_ph': 'P Meti Ph',
     'Meti': 'source-defined METI state',
     'pMetErbB3': 'P Met Erb B3',
     'pMetErbB3i': 'P Met Erb B3i',
     'pMetErbB3i_ph': 'P Met Erb B3i Ph',
     'pMetEGFR': 'P Met EGFR',
     'pMetEGFRi': 'P Met Egfri',
     'pMetEGFRi_ph': 'P Met Egfri Ph',
     'MEK': 'MEK',
     'pMEK': 'source-defined PMEK state',
     'ERK': 'ERK',
     'pERK': 'PERK kinase',
     'AKT': 'AKT',
     'pAKT': 'source-defined PAKT state',
     'S6K1': 'S6K1',
     'pS6K1': 'P S6K1',
     'S6': 'source-defined S6 state',
     'pS6': 'source-defined PS6 state'}
    _STATE_OUTPUT_ALIASES = {'dose_EGF': 'dose_egf',
     'dose_HGF': 'dose_hgf',
     'RTKph': 'rtkph',
     'dose_IGF1': 'dose_igf1',
     'dose_HRG': 'dose_heregulin',
     'EGFR': 'egfr',
     'EGFR_EGF': 'egfr_egf',
     'pEGFRd': 'p_egfrd',
     'pEGFRi': 'p_egfri',
     'pEGFRi_ph': 'p_egfri_ph',
     'EGFRi': 'egfri',
     'ErbB2': 'source_defined_erbb2_state',
     'pErbB2': 'p_erb_b2',
     'pErbB2i': 'p_erb_b2i',
     'ErbB2i': 'erb_b2i',
     'pErbB2i_ph': 'p_erb_b2i_ph',
     'pErbB12': 'p_erb_b12',
     'pErbB12i': 'p_erb_b12i',
     'pErbB12i_ph': 'p_erb_b12i_ph',
     'ErbB3': 'source_defined_erbb3_state',
     'ErbB3_HRG': 'erb_b3_heregulin',
     'pErbB3d': 'p_erb_b3d',
     'pErbB3i': 'p_erb_b3i',
     'pErbB3i_ph': 'p_erb_b3i_ph',
     'ErbB3i': 'erb_b3i',
     'pErbB13': 'p_erb_b13',
     'pErbB13i': 'p_erb_b13i',
     'pErbB13i_ph': 'p_erb_b13i_ph',
     'pErbB32': 'p_erb_b32',
     'pErbB32i': 'p_erb_b32i',
     'pErbB32i_ph': 'p_erb_b32i_ph',
     'IGF1R': 'igf1r',
     'IGF1R_IGF1': 'igf1r_igf1',
     'pIGF1Rd': 'p_igf1rd',
     'pIGF1Ri': 'p_igf1ri',
     'pIGF1Ri_ph': 'p_igf1ri_ph',
     'IGF1Ri': 'igf1ri',
     'Met': 'source_defined_met_state',
     'Met_HGF': 'met_hgf',
     'pMetd': 'p_metd',
     'pMeti': 'p_meti',
     'pMeti_ph': 'p_meti_ph',
     'Meti': 'source_defined_meti_state',
     'pMetErbB3': 'p_met_erb_b3',
     'pMetErbB3i': 'p_met_erb_b3i',
     'pMetErbB3i_ph': 'p_met_erb_b3i_ph',
     'pMetEGFR': 'p_met_egfr',
     'pMetEGFRi': 'p_met_egfri',
     'pMetEGFRi_ph': 'p_met_egfri_ph',
     'MEK': 'mek',
     'pMEK': 'source_defined_pmek_state',
     'ERK': 'erk',
     'pERK': 'perk_kinase',
     'AKT': 'akt',
     'pAKT': 'source_defined_pakt_state',
     'S6K1': 's6k1',
     'pS6K1': 'p_s6k1',
     'S6': 'source_defined_s6_state',
     'pS6': 'source_defined_ps6_state'}

    def __init__(self, model_path: str = 'data/MODEL1708210000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


PanrtkModelForSingleCellLineModel1708210000Model = Hass2017PanrtkModelForSingleCellLineModel
