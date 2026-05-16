# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kholodenko1999 - EGFR signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kholodenko1999EgfrSignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000048'
    _TITLE = 'Kholodenko1999 - EGFR signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'epidermal_growth_factor': ('EGF',
                                 'native SBML value',
                                 'Epidermal Growth Factor. Maps to SBML symbol `EGF` and is emitted in '
                                 'native SBML units.'),
     'egfr': ('R',
              'native SBML value',
              'EGFR. Maps to SBML symbol `R` and is emitted in native SBML units.'),
     'egf_egfr': ('Ra',
                  'native SBML value',
                  'EGF EGFR. Maps to SBML symbol `Ra` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_egf_egfr': ('Ra',
                          0.0,
                          'native SBML value',
                          'Initial level of EGF EGFR. Maps to SBML symbol `Ra`; exposed as a traceable '
                          'initial-condition perturbation.'),
     'initial_egf_egfr_2': ('R2',
                            0.0,
                            'native SBML value',
                            'Initial level of EGF EGFR 2. Maps to SBML symbol `R2`; exposed as a '
                            'traceable initial-condition perturbation.'),
     'initial_egf_egfr_2_grb2_adapter_protein': ('RG',
                                                 0.0,
                                                 'native SBML value',
                                                 'Initial level of EGF EGFR 2 Grb2 adapter protein. '
                                                 'Maps to SBML symbol `RG`; exposed as a traceable '
                                                 'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EGF': 'Epidermal Growth Factor',
     'R': 'EGFR',
     'Ra': 'EGF EGFR',
     'R2': 'EGF EGFR 2',
     'RP': 'EGF EGFR 2 P',
     'PLCg': 'source-defined PLCG state',
     'RPLCg': 'EGF EGFR 2 Plcg',
     'RPLCgP': 'EGF EGFR 2 Plcg P',
     'PLCgP': 'Plcg P',
     'Grb': 'Grb2 adapter protein',
     'RG': 'EGF EGFR 2 Grb2 adapter protein',
     'SOS': 'SOS guanine-nucleotide exchange factor',
     'RGS': 'EGF EGFR 2 Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'GS': 'Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'Shc': 'Shc adapter protein',
     'RSh': 'EGF EGFR 2 Shc adapter protein',
     'RShP': 'EGF EGFR Shc adapter protein P',
     'ShP': 'source-defined SHC-P state',
     'RShG': 'EGF EGFR 2 Shc adapter protein Grb2 adapter protein',
     'ShG': 'Shc adapter protein Grb2 adapter protein',
     'RShGS': 'EGF EGFR 2 Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange '
              'factor',
     'ShGS': 'Shc adapter protein Grb2 adapter protein SOS guanine-nucleotide exchange factor',
     'PLCgl': 'Plcg P I'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'epidermal_growth_factor',
     'R': 'egfr',
     'Ra': 'egf_egfr',
     'R2': 'egf_egfr_2',
     'RP': 'egf_egfr_2_p',
     'PLCg': 'source_defined_plcg_state',
     'RPLCg': 'egf_egfr_2_plcg',
     'RPLCgP': 'egf_egfr_2_plcg_p',
     'PLCgP': 'plcg_p',
     'Grb': 'grb2_adapter_protein',
     'RG': 'egf_egfr_2_grb2_adapter_protein',
     'SOS': 'sos_guanine_nucleotide_exchange_factor',
     'RGS': 'egf_egfr_2_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'GS': 'grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'Shc': 'shc_adapter_protein',
     'RSh': 'egf_egfr_2_shc_adapter_protein',
     'RShP': 'egf_egfr_shc_adapter_protein_p',
     'ShP': 'source_defined_shc_p_state',
     'RShG': 'egf_egfr_2_shc_adapter_protein_grb2_adapter_protein',
     'ShG': 'shc_adapter_protein_grb2_adapter_protein',
     'RShGS': 'egf_egfr_2_shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'ShGS': 'shc_adapter_protein_grb2_adapter_protein_sos_guanine_nucleotide_exchange_factor',
     'PLCgl': 'plcg_p_i'}

    def __init__(self, model_path: str = 'data/BIOMD0000000048.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kholodenko1999EgfrSignalingBiomd0000000048Model = Kholodenko1999EgfrSignalingModel
