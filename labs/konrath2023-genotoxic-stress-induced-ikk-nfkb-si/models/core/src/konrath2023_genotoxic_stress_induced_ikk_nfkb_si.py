# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Konrath2023_genotoxic_stress_induced_IKK_NFkB_signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Konrath2023GenotoxicStressInducedIkkNfkbSiModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2307130001'
    _TITLE = 'Konrath2023_genotoxic_stress_induced_IKK_NFkB_signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_bs_p_state': ('BS_P',
                                   'native SBML value',
                                   'Source Defined BS P State. Maps to SBML symbol `BS_P` and is '
                                   'emitted in native SBML units.'),
     'source_defined_parp1_state': ('PARP1',
                                    'native SBML value',
                                    'Source Defined PARP1 State. Maps to SBML symbol `PARP1` and is '
                                    'emitted in native SBML units.'),
     'parp1dsb_b': ('PARP1DSB_b',
                    'native SBML value',
                    'PARP1DSB B. Maps to SBML symbol `PARP1DSB_b` and is emitted in native SBML '
                    'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_bs_p_state': ('BS_P',
                                           0.0,
                                           'native SBML value',
                                           'Initial level of source-defined BS_P state. Maps to SBML '
                                           'symbol `BS_P`; exposed as a traceable initial-condition '
                                           'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'BS_P': 'Source Defined BS P State',
     'PARP1': 'Source Defined PARP1 State',
     'PARP1DSB_b': 'PARP1DSB B',
     'PARP1_b': 'PARP1 B',
     'parPARP1_b': 'PARPARP1 B',
     'parPARP1': 'PARPARP1',
     'BS_M': 'Source Defined BS M State',
     'MRN': 'Source Defined MRN State',
     'MRN_b': 'Source Defined MRN B State',
     'AMRN_b': 'AMRN B',
     'ATM_n': 'Source Defined ATM N State',
     'pATM_n': 'Phospho ATM N',
     'IKKg': 'Source Defined IKKG State',
     'sig': 'Source Defined SIG State',
     'spIKKg_n': 'Sp Ikkg N',
     'TRAF6': 'Source Defined TRAF6 State',
     'AT': 'Source Defined AT State',
     'ATT': 'Source Defined ATT State',
     'TAK1': 'Source Defined TAK1 State',
     'pIKK': 'Phospho IKK'}
    _STATE_OUTPUT_ALIASES = {'BS_P': 'source_defined_bs_p_state',
     'PARP1': 'source_defined_parp1_state',
     'PARP1DSB_b': 'parp1dsb_b',
     'PARP1_b': 'parp1_b',
     'parPARP1_b': 'parparp1_b',
     'parPARP1': 'parparp1',
     'BS_M': 'source_defined_bs_m_state',
     'MRN': 'source_defined_mrn_state',
     'MRN_b': 'source_defined_mrn_b_state',
     'AMRN_b': 'amrn_b',
     'ATM_n': 'source_defined_atm_n_state',
     'pATM_n': 'phospho_atm_n',
     'IKKg': 'source_defined_ikkg_state',
     'sig': 'source_defined_sig_state',
     'spIKKg_n': 'sp_ikkg_n',
     'TRAF6': 'source_defined_traf6_state',
     'AT': 'source_defined_at_state',
     'ATT': 'source_defined_att_state',
     'TAK1': 'source_defined_tak1_state',
     'pIKK': 'phospho_ikk'}

    def __init__(self, model_path: str = 'data/MODEL2307130001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Konrath2023GenotoxicStressInducedIkkNfkbSiModel2307130001Model = Konrath2023GenotoxicStressInducedIkkNfkbSiModel
