# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schoeberl2002 - EGF MAPK."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schoeberl2002EgfMapkModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000019'
    _TITLE = 'Schoeberl2002 - EGF MAPK'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp': ('x20',
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
                                                                                             '`x20` '
                                                                                             'and is '
                                                                                             'emitted '
                                                                                             'in '
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'units.'),
     'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp': ('x21',
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
                                                                                             '`x21` '
                                                                                             'and is '
                                                                                             'emitted '
                                                                                             'in '
                                                                                             'native '
                                                                                             'SBML '
                                                                                             'units.'),
     'ras_gdp': ('x26',
                 'native SBML value',
                 'RAS GDP. Maps to SBML symbol `x26` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_egf': ('x1',
                     4962.0,
                     'native SBML value',
                     'Initial level of EGF. Maps to SBML symbol `x1`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_t_egf_egfr': ('EGF_EGFR_act',
                            0.0,
                            'native SBML value',
                            'Initial level of T EGF EGFR. Maps to SBML symbol `EGF_EGFR_act`; exposed '
                            'as a traceable initial-condition perturbation.'),
     'initial_t_erk_pp': ('ERK_PP',
                          0.0,
                          'native SBML value',
                          'Initial level of T ERK PP. Maps to SBML symbol `ERK_PP`; exposed as a '
                          'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x1': 'EGF',
     'x2': 'EGFR',
     'x3': 'EGF EGFR',
     'x4': 'EGF EGFR 2',
     'x5': 'EGF EGFR 2',
     'x6': 'Egfri',
     'x7': 'EGF EGFR 2 GAP Grb2 adapter protein Prot',
     'x8': 'EGF Egfri 2',
     'x9': 'Proti',
     'x10': 'EGF Egfri',
     'x11': 'EGF Egfri 2',
     'x12': 'source-defined PROT state',
     'x13': 'Egfideg',
     'x14': 'source-defined GAP state',
     'x15': 'EGF EGFR 2 GAP',
     'x16': 'source-defined EGFI state',
     'x17': 'EGF Egfri 2 GAP',
     'x18': 'EGF Egfri 2 GAP Grb2 adapter protein',
     'x19': 'EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'x20': 'EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GDP',
     'x21': 'EGF Egfri 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GTP',
     'x22': 'Grb2 adapter protein',
     'x23': 'EGF EGFR 2 GAP Grb2 adapter protein',
     'x24': 'SOS guanine-nucleotide exchange factor',
     'x25': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'x26': 'RAS GDP',
     'x27': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GDP',
     'x28': 'RAS GTP',
     'x29': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GTP',
     'x30': 'Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'x31': 'Shc adapter protein',
     'x32': 'EGF EGFR 2 GAP Shc adapter protein',
     'x33': 'EGF EGFR 2 GAP Shc adapter protein',
     'x34': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein',
     'x35': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor',
     'x36': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GDP',
     'x37': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GTP',
     'x38': 'Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'x39': 'Shc adapter protein Grb2 adapter protein',
     'x40': 'Shc adapter protein',
     'x41': 'RAF',
     'x42': 'RAF RAS GTP',
     'x43': 'RAS GTP',
     'x44': 'Phosphotase1',
     'x45': 'RAF',
     'x46': 'RAF P Ase',
     'x47': 'MEK',
     'x48': 'MEK RAF',
     'x49': 'source-defined MEK-P state',
     'x50': 'MEK P RAF',
     'x51': 'MEK PP',
     'x52': 'MEK PP P Ase2',
     'x53': 'Phosphatase2',
     'x54': 'MEK P P Ase2',
     'x55': 'ERK',
     'x56': 'ERK MEK PP',
     'x57': 'source-defined ERK-P state',
     'x58': 'ERK P MEK PP',
     'x59': 'ERK PP',
     'x60': 'Phosphotase3',
     'x61': 'ERK PP P Ase3',
     'x62': 'ERK P P Ase3',
     'x63': 'EGF Egfri 2 GAP Shc adapter protein',
     'x64': 'EGF Egfri 2 GAP Shc adapter protein',
     'x65': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein',
     'x66': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor',
     'x67': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GDP',
     'x68': 'EGF Egfri 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GTP',
     'x69': 'Rasi GTP',
     'x70': 'Rafi Rasi GTP',
     'x71': 'Rasi GTP',
     'x72': 'source-defined RAFI* state',
     'x73': 'Rafi P Ase',
     'x74': 'Meki Rafi',
     'x75': 'Meki P',
     'x76': 'Meki P Rafi',
     'x77': 'Meki PP',
     'x78': 'Meki PP P Ase2i',
     'x79': 'Meki P P Ase2i',
     'x80': 'Erki Meki PP',
     'x81': 'Erki P',
     'x82': 'Erki P Meki PP',
     'x83': 'Erki PP',
     'x84': 'Erki PP P Ase3i',
     'x85': 'Erki P P Ase3i',
     'x86': 'Egfrideg',
     'x87': 'EGF Egfri 2deg',
     'x88': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor Prot',
     'x89': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GDP Prot',
     'x90': 'EGF EGFR 2 GAP Grb2 adapter protein SOS guanine-nucleotide exchange factor RAS GTP Prot',
     'x91': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein Prot',
     'x92': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor Prot',
     'x93': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GDP Prot',
     'x94': 'EGF EGFR 2 GAP Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
            'factor RAS GTP Prot',
     'Raf_act': 'source-defined T_RAF* state',
     'Ras_GTP': 'T RAS GTP',
     'MEK_PP': 'T MEK PP',
     'ERK_PP': 'T ERK PP',
     'SHC_P_t': 'T Shc adapter protein P T',
     'EGF_EGFR_act': 'T EGF EGFR'}
    _STATE_OUTPUT_ALIASES = {'x1': 'egf',
     'x2': 'egfr',
     'x3': 'egf_egfr',
     'x4': 'egf_egfr_2',
     'x5': 'egf_egfr_2_2',
     'x6': 'egfri',
     'x7': 'egf_egfr_2_gap_grb2_adapter_protein_prot',
     'x8': 'egf_egfri_2',
     'x9': 'proti',
     'x10': 'egf_egfri',
     'x11': 'egf_egfri_2_2',
     'x12': 'source_defined_prot_state',
     'x13': 'egfideg',
     'x14': 'source_defined_gap_state',
     'x15': 'egf_egfr_2_gap',
     'x16': 'source_defined_egfi_state',
     'x17': 'egf_egfri_2_gap',
     'x18': 'egf_egfri_2_gap_grb2_adapter_protein',
     'x19': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x20': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     'x21': 'egf_egfri_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'x22': 'grb2_adapter_protein',
     'x23': 'egf_egfr_2_gap_grb2_adapter_protein',
     'x24': 'sos_guanine_nucleotide_exchange_factor',
     'x25': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x26': 'ras_gdp',
     'x27': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     'x28': 'ras_gtp',
     'x29': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'x30': 'grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x31': 'shc_adapter_protein',
     'x32': 'egf_egfr_2_gap_shc_adapter_protein',
     'x33': 'egf_egfr_2_gap_shc_adapter_protein_2',
     'x34': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein',
     'x35': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x36': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     'x37': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'x38': 'shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x39': 'shc_adapter_protein_grb2_adapter_protein',
     'x40': 'shc_adapter_protein_2',
     'x41': 'raf',
     'x42': 'raf_ras_gtp',
     'x43': 'ras_gtp_2',
     'x44': 'phosphotase1',
     'x45': 'raf_2',
     'x46': 'raf_p_ase',
     'x47': 'mek',
     'x48': 'mek_raf',
     'x49': 'source_defined_mek_p_state',
     'x50': 'mek_p_raf',
     'x51': 'mek_pp',
     'x52': 'mek_pp_p_ase2',
     'x53': 'phosphatase2',
     'x54': 'mek_p_p_ase2',
     'x55': 'erk',
     'x56': 'erk_mek_pp',
     'x57': 'source_defined_erk_p_state',
     'x58': 'erk_p_mek_pp',
     'x59': 'erk_pp',
     'x60': 'phosphotase3',
     'x61': 'erk_pp_p_ase3',
     'x62': 'erk_p_p_ase3',
     'x63': 'egf_egfri_2_gap_shc_adapter_protein',
     'x64': 'egf_egfri_2_gap_shc_adapter_protein_2',
     'x65': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein',
     'x66': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'x67': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp',
     'x68': 'egf_egfri_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp',
     'x69': 'rasi_gtp',
     'x70': 'rafi_rasi_gtp',
     'x71': 'rasi_gtp_2',
     'x72': 'source_defined_rafi_state',
     'x73': 'rafi_p_ase',
     'x74': 'meki_rafi',
     'x75': 'meki_p',
     'x76': 'meki_p_rafi',
     'x77': 'meki_pp',
     'x78': 'meki_pp_p_ase2i',
     'x79': 'meki_p_p_ase2i',
     'x80': 'erki_meki_pp',
     'x81': 'erki_p',
     'x82': 'erki_p_meki_pp',
     'x83': 'erki_pp',
     'x84': 'erki_pp_p_ase3i',
     'x85': 'erki_p_p_ase3i',
     'x86': 'egfrideg',
     'x87': 'egf_egfri_2deg',
     'x88': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_prot',
     'x89': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp_prot',
     'x90': 'egf_egfr_2_gap_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp_prot',
     'x91': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_prot',
     'x92': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_prot',
     'x93': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gdp_prot',
     'x94': 'egf_egfr_2_gap_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor_ras_gtp_prot',
     'Raf_act': 'source_defined_t_raf_state',
     'Ras_GTP': 't_ras_gtp',
     'MEK_PP': 't_mek_pp',
     'ERK_PP': 't_erk_pp',
     'SHC_P_t': 't_shc_adapter_protein_p_t',
     'EGF_EGFR_act': 't_egf_egfr'}

    def __init__(self, model_path: str = 'data/BIOMD0000000019.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Schoeberl2002EgfMapkBiomd0000000019Model = Schoeberl2002EgfMapkModel
