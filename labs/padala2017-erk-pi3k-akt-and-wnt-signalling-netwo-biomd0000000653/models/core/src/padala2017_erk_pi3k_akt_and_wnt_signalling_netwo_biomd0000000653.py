# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Padala2017- ERK, PI3K/Akt and Wnt signalling network (bRaf mutated)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Padala2017ErkPi3kAktAndWntSignallingNetwoBiomd0000000653Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000653'
    _TITLE = 'Padala2017- ERK, PI3K/Akt and Wnt signalling network (bRaf mutated)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'apc_axin': ('APCAxin',
                  'native SBML value',
                  'APC Axin. Maps to SBML symbol `APCAxin` and is emitted in native SBML units.'),
     'apc_axin_gsk3b': ('APCAxinGSK3B',
                        'native SBML value',
                        'APC Axin Gsk3b. Maps to SBML symbol `APCAxinGSK3B` and is emitted in native '
                        'SBML units.'),
     'apc_b_catenin': ('APCBCatenin',
                       'native SBML value',
                       'APC B Catenin. Maps to SBML symbol `APCBCatenin` and is emitted in native SBML '
                       'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_p_egfr': ('pEGFR',
                        0.05,
                        'native SBML value',
                        'Initial level of P EGFR. Maps to SBML symbol `pEGFR`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_bound_egfr': ('bEGFR',
                            0.0,
                            'native SBML value',
                            'Initial level of bound EGFR. Maps to SBML symbol `bEGFR`; exposed as a '
                            'traceable initial-condition perturbation.'),
     'initial_egf': ('EGF',
                     600.0,
                     'native SBML value',
                     'Initial level of EGF. Maps to SBML symbol `EGF`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'APC': 'source-defined APC state',
     'APCAxin': 'APC Axin',
     'APCAxinGSK3B': 'APC Axin Gsk3b',
     'APCBCatenin': 'APC B Catenin',
     'Akt': 'AKT',
     'Axin': 'source-defined AXIN state',
     'BCatenin': 'B Catenin',
     'BRaf': 'source-defined BRAF state',
     'C3G': 'C3G',
     'Dsha': 'source-defined DSHA state',
     'Dshi': 'source-defined DSHI state',
     'EGF': 'EGF',
     'ERK': 'ERK',
     'GSK3B': 'Gsk3b',
     'MEK': 'MEK',
     'P90Rsk': 'P90rsk',
     'PI3K': 'PI3K',
     'PIP2': 'source-defined PIP2 state',
     'PIP3': 'source-defined PIP3 state',
     'PKCD': 'source-defined PKCD state',
     'PP2A': 'PP2A',
     'PTEN': 'source-defined PTEN state',
     'RKIP': 'source-defined RKIP state',
     'Raf1': 'RAF1',
     'RafPPtase': 'RAF Pptase',
     'Rap1': 'source-defined RAP1 state',
     'Rap1Gap': 'Rap1 Gap',
     'Ras': 'RAS',
     'RasGap': 'RAS Gap',
     'SOS': 'SOS guanine-nucleotide exchange factor',
     'TCF': 'source-defined TCF state',
     'TCFBCatenin': 'B Catenin TCF',
     'X': 'response node X',
     'bEGFR': 'bound EGFR',
     'fEGFR': 'free EGFR',
     'pAPCpAxinGSK3B': 'P APC P Axin Gsk3b',
     'pAPCpAxinGSK3BBCatenin': 'P APC P Axin Gsk3b B Catenin',
     'pAPCpAxinGSK3BpBCatenin': 'P APC P Axin Gsk3b Pb Catenin',
     'pAkt': 'source-defined PAKT state',
     'pBCatenin': 'Pb Catenin',
     'pBRaf': 'Pb RAF',
     'pC3G': 'P C3G',
     'pEGFR': 'P EGFR',
     'pERK': 'PERK kinase',
     'pGSK3B': 'P Gsk3b',
     'pMEK': 'source-defined PMEK state',
     'pP90Rsk': 'P P90rsk',
     'pPI3K': 'P PI3K',
     'pRKIP': 'P RKIP',
     'pRaf1': 'source-defined PRAF1 state',
     'pRap1': 'source-defined PRAP1 state',
     'pRas': 'source-defined PRAS state',
     'pSOS': 'source-defined PSOS state',
     'null': 'source-defined NULL state'}
    _STATE_OUTPUT_ALIASES = {'APC': 'source_defined_apc_state',
     'APCAxin': 'apc_axin',
     'APCAxinGSK3B': 'apc_axin_gsk3b',
     'APCBCatenin': 'apc_b_catenin',
     'Akt': 'akt',
     'Axin': 'source_defined_axin_state',
     'BCatenin': 'b_catenin',
     'BRaf': 'source_defined_braf_state',
     'C3G': 'c3g',
     'Dsha': 'source_defined_dsha_state',
     'Dshi': 'source_defined_dshi_state',
     'EGF': 'egf',
     'ERK': 'erk',
     'GSK3B': 'gsk3b',
     'MEK': 'mek',
     'P90Rsk': 'p90rsk',
     'PI3K': 'pi3k',
     'PIP2': 'source_defined_pip2_state',
     'PIP3': 'source_defined_pip3_state',
     'PKCD': 'source_defined_pkcd_state',
     'PP2A': 'pp2a',
     'PTEN': 'source_defined_pten_state',
     'RKIP': 'source_defined_rkip_state',
     'Raf1': 'raf1',
     'RafPPtase': 'raf_pptase',
     'Rap1': 'source_defined_rap1_state',
     'Rap1Gap': 'rap1_gap',
     'Ras': 'ras',
     'RasGap': 'ras_gap',
     'SOS': 'sos_guanine_nucleotide_exchange_factor',
     'TCF': 'source_defined_tcf_state',
     'TCFBCatenin': 'b_catenin_tcf',
     'X': 'response_node_x',
     'bEGFR': 'bound_egfr',
     'fEGFR': 'free_egfr',
     'pAPCpAxinGSK3B': 'p_apc_p_axin_gsk3b',
     'pAPCpAxinGSK3BBCatenin': 'p_apc_p_axin_gsk3b_b_catenin',
     'pAPCpAxinGSK3BpBCatenin': 'p_apc_p_axin_gsk3b_pb_catenin',
     'pAkt': 'source_defined_pakt_state',
     'pBCatenin': 'pb_catenin',
     'pBRaf': 'pb_raf',
     'pC3G': 'p_c3g',
     'pEGFR': 'p_egfr',
     'pERK': 'perk_kinase',
     'pGSK3B': 'p_gsk3b',
     'pMEK': 'source_defined_pmek_state',
     'pP90Rsk': 'p_p90rsk',
     'pPI3K': 'p_pi3k',
     'pRKIP': 'p_rkip',
     'pRaf1': 'source_defined_praf1_state',
     'pRap1': 'source_defined_prap1_state',
     'pRas': 'source_defined_pras_state',
     'pSOS': 'source_defined_psos_state',
     'null': 'source_defined_null_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000653.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Padala2017ErkPi3kAktAndWntSignallingNetwoBiomd0000000653Model = Padala2017ErkPi3kAktAndWntSignallingNetwoBiomd0000000653Model
