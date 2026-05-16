# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kok2020 - IFNalpha-induced signaling in Huh7.5 cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kok2020IfnalphaInducedSignalingInHuh75CelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000959'
    _TITLE = 'Kok2020 - IFNalpha-induced signaling in Huh7.5 cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'stat1c': ('STAT1c',
                'native SBML value',
                'Stat1c. Maps to SBML symbol `STAT1c` and is emitted in native SBML units.'),
     'stat2c': ('STAT2c',
                'native SBML value',
                'Stat2c. Maps to SBML symbol `STAT2c` and is emitted in native SBML units.'),
     'p_stat1p_stat2c': ('pSTAT1pSTAT2c',
                         'native SBML value',
                         'P Stat1p Stat2c. Maps to SBML symbol `pSTAT1pSTAT2c` and is emitted in '
                         'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_a_rec_ifna': ('aRecIFN',
                            0.0,
                            'native SBML value',
                            'Initial level of A Rec Ifna. Maps to SBML symbol `aRecIFN`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_bind_ifn_level': ('BindIFN',
                                0.0593,
                                'native SBML value',
                                'Bind IFN source parameter. Maps to SBML symbol `BindIFN` and '
                                'preserves the bundled default.'),
     'initial_dega_rec_ifnby_socs_level': ('degaRecIFNBySOCS',
                                           0.8837,
                                           'native SBML value',
                                           'Dega Rec Ifnby SOCS source parameter. Maps to SBML symbol '
                                           '`degaRecIFNBySOCS` and preserves the bundled default.')}
    _SPECIES_LABELS = {'Rec': 'source-defined REC state',
     'SOCS1': 'source-defined SOCS1 state',
     'IFN': 'source-defined IFNA state',
     'aRecIFN': 'A Rec Ifna',
     'USP18': 'USP18',
     'STAT1c': 'Stat1c',
     'STAT2c': 'Stat2c',
     'pSTAT1pSTAT2c': 'P Stat1p Stat2c',
     'pSTAT1pSTAT2n': 'P Stat1p Stat2n',
     'STAT1n': 'Stat1n',
     'STAT2n': 'Stat2n',
     'ISGF3c': 'Isgf3c',
     'ISGF3n': 'Isgf3n',
     'IRF9n': 'Irf9n',
     'pSTAT1dimc': 'P Stat1dimc',
     'pSTAT1dimn': 'P Stat1dimn',
     'OccGAS_ISREbs': 'Occ GAS Isrebs',
     'OccGASbs': 'Occ Gasbs',
     'IRF9c': 'Irf9c',
     'SOCS3': 'SOCS3',
     'STAT1mRNA': 'Stat1m RNA',
     'STAT2mRNA': 'Stat2m RNA',
     'IRF9mRNA': 'Irf9m RNA',
     'IRF2mRNA': 'Irf2m RNA',
     'IRF2': 'source-defined IRF2 state',
     'USP18mRNA': 'Usp18m RNA',
     'SOCS1mRNA': 'Socs1m RNA',
     'SOCS3mRNA': 'Socs3m RNA',
     'STAT1_LC_1': 'STAT1 LC 1',
     'STAT1_LC_2': 'STAT1 LC 2',
     'STAT1_LC_3': 'STAT1 LC 3',
     'STAT2_LC_1': 'STAT2 LC 1',
     'STAT2_LC_2': 'STAT2 LC 2',
     'STAT2_LC_3': 'STAT2 LC 3',
     'STAT2_LC_4': 'STAT2 LC 4',
     'STAT2_LC_5': 'STAT2 LC 5',
     'IRF9_LC_1': 'IRF9 LC 1',
     'IRF9_LC_2': 'IRF9 LC 2',
     'USP18_LC_1': 'USP18 LC 1',
     'USP18_LC_2': 'USP18 LC 2',
     'SOCS1_LC_1': 'SOCS1 LC 1'}
    _STATE_OUTPUT_ALIASES = {'Rec': 'source_defined_rec_state',
     'SOCS1': 'source_defined_socs1_state',
     'IFN': 'source_defined_ifna_state',
     'aRecIFN': 'a_rec_ifna',
     'USP18': 'usp18',
     'STAT1c': 'stat1c',
     'STAT2c': 'stat2c',
     'pSTAT1pSTAT2c': 'p_stat1p_stat2c',
     'pSTAT1pSTAT2n': 'p_stat1p_stat2n',
     'STAT1n': 'stat1n',
     'STAT2n': 'stat2n',
     'ISGF3c': 'isgf3c',
     'ISGF3n': 'isgf3n',
     'IRF9n': 'irf9n',
     'pSTAT1dimc': 'p_stat1dimc',
     'pSTAT1dimn': 'p_stat1dimn',
     'OccGAS_ISREbs': 'occ_gas_isrebs',
     'OccGASbs': 'occ_gasbs',
     'IRF9c': 'irf9c',
     'SOCS3': 'socs3',
     'STAT1mRNA': 'stat1m_rna',
     'STAT2mRNA': 'stat2m_rna',
     'IRF9mRNA': 'irf9m_rna',
     'IRF2mRNA': 'irf2m_rna',
     'IRF2': 'source_defined_irf2_state',
     'USP18mRNA': 'usp18m_rna',
     'SOCS1mRNA': 'socs1m_rna',
     'SOCS3mRNA': 'socs3m_rna',
     'STAT1_LC_1': 'stat1_lc_1',
     'STAT1_LC_2': 'stat1_lc_2',
     'STAT1_LC_3': 'stat1_lc_3',
     'STAT2_LC_1': 'stat2_lc_1',
     'STAT2_LC_2': 'stat2_lc_2',
     'STAT2_LC_3': 'stat2_lc_3',
     'STAT2_LC_4': 'stat2_lc_4',
     'STAT2_LC_5': 'stat2_lc_5',
     'IRF9_LC_1': 'irf9_lc_1',
     'IRF9_LC_2': 'irf9_lc_2',
     'USP18_LC_1': 'usp18_lc_1',
     'USP18_LC_2': 'usp18_lc_2',
     'SOCS1_LC_1': 'socs1_lc_1'}

    def __init__(self, model_path: str = 'data/BIOMD0000000959.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kok2020IfnalphaInducedSignalingInHuh75CelBiomd0000000959Model = Kok2020IfnalphaInducedSignalingInHuh75CelModel
