# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mueller2015 - Hepatocyte proliferation, T160 phosphorylation of CDK2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mueller2015HepatocyteProliferationT160PhosphModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000568'
    _TITLE = 'Mueller2015 - Hepatocyte proliferation, T160 phosphorylation of CDK2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'inh_erk': ('inherk',
                 'native SBML value',
                 'Inh ERK. Maps to SBML symbol `inherk` and is emitted in native SBML units.'),
     'inh_akt': ('inhakt',
                 'native SBML value',
                 'Inh AKT. Maps to SBML symbol `inhakt` and is emitted in native SBML units.'),
     'cyto_c2e_t160_u_b': ('S4',
                           'native SBML value',
                           'Cyto C2E T160 U B. Maps to SBML symbol `S4` and is emitted in native SBML '
                           'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cdk2p21': ('ObsCDK2P21_obs',
                         0.0409109861876772,
                         'native SBML value',
                         'Initial level of CDK2P21. Maps to SBML symbol `ObsCDK2P21_obs`; exposed as a '
                         'traceable initial-condition perturbation.'),
     'initial_dnacontent': ('ObsDNAContent_obs',
                            1.0,
                            'native SBML value',
                            'Initial level of Dnacontent. Maps to SBML symbol `ObsDNAContent_obs`; '
                            'exposed as a traceable initial-condition perturbation.'),
     'initial_source_defined_hgf_state': ('hgf',
                                          0.0,
                                          'native SBML value',
                                          'Initial level of source-defined HGF state. Maps to SBML '
                                          'symbol `hgf`; exposed as a traceable initial-condition '
                                          'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'S4': 'Cyto C2E T160 U B',
     'S10': 'Cyto C4D1 B',
     'S12': 'Cyto P21 B',
     'S19': 'Cyto C4D1 B 1 P21 B 1',
     'S20': 'Cyto C2E T160 U B 1 P21 B 1',
     'hgf': 'source-defined HGF state',
     'inhp53': 'Inhp53',
     'inherk': 'Inh ERK',
     'inhakt': 'Inh AKT',
     'inhc4d1': 'Inhc4d1',
     'ObsTotCycECDK2_obs': 'Tot Cyc ECDK2',
     'ObsTotCDK2T160_obs': 'Tot CDK2T160',
     'ObsTotCycDCDK4_obs': 'Tot Cyc DCDK4',
     'ObsTotP21_obs': 'Tot P21',
     'ObsCDK2P21_obs': 'CDK2P21',
     'ObsTotE2F_obs': 'Tot E2F',
     'ObsTotRb_obs': 'Tot Rb',
     'ObsPhosRbS788_obs': 'Phos Rb S788',
     'ObsPhosRbS800_obs': 'Phos Rb S800',
     'ObsDNAContent_obs': 'Dnacontent',
     'S23': 'Nuc C2E T160 P B 1 P21 B 1',
     'S18': 'Nuc C2E T160 P B',
     'S3': 'Nuc C2E T160 U B 1 P21 B 1',
     'S13': 'Nuc C2E T160 U B',
     'S24': 'Nuc C4D1 B 1 P21 B 1',
     'S26': 'Nuc C4D1 B',
     'S5': 'Nuc Dnapre',
     'S17': 'Nuc Dnapre1',
     'S22': 'Nuc Dnapre2',
     'S25': 'Nuc Dnapre3',
     'S27': 'Nuc Dnapre4',
     'S16': 'Nuc E2f B 1 Rb S788 P S800 U B 1',
     'S2': 'Nuc E2f B 1 Rb S788 U S800 U B 1',
     'S14': 'Nuc E2f B',
     'S11': 'Nuc P21 B',
     'S21': 'Nuc Rb S788 P S800 P B',
     'S15': 'Nuc Rb S788 P S800 U B',
     'S1': 'Nuc Rb S788 U S800 U B',
     'S28': 'Nuc Dnapre5'}
    _STATE_OUTPUT_ALIASES = {'S4': 'cyto_c2e_t160_u_b',
     'S10': 'cyto_c4d1_b',
     'S12': 'cyto_p21_b',
     'S19': 'cyto_c4d1_b_1_p21_b_1',
     'S20': 'cyto_c2e_t160_u_b_1_p21_b_1',
     'hgf': 'source_defined_hgf_state',
     'inhp53': 'inhp53',
     'inherk': 'inh_erk',
     'inhakt': 'inh_akt',
     'inhc4d1': 'inhc4d1',
     'ObsTotCycECDK2_obs': 'tot_cyc_ecdk2',
     'ObsTotCDK2T160_obs': 'tot_cdk2t160',
     'ObsTotCycDCDK4_obs': 'tot_cyc_dcdk4',
     'ObsTotP21_obs': 'tot_p21',
     'ObsCDK2P21_obs': 'cdk2p21',
     'ObsTotE2F_obs': 'tot_e2f',
     'ObsTotRb_obs': 'tot_rb',
     'ObsPhosRbS788_obs': 'phos_rb_s788',
     'ObsPhosRbS800_obs': 'phos_rb_s800',
     'ObsDNAContent_obs': 'dnacontent',
     'S23': 'nuc_c2e_t160_p_b_1_p21_b_1',
     'S18': 'nuc_c2e_t160_p_b',
     'S3': 'nuc_c2e_t160_u_b_1_p21_b_1',
     'S13': 'nuc_c2e_t160_u_b',
     'S24': 'nuc_c4d1_b_1_p21_b_1',
     'S26': 'nuc_c4d1_b',
     'S5': 'nuc_dnapre',
     'S17': 'nuc_dnapre1',
     'S22': 'nuc_dnapre2',
     'S25': 'nuc_dnapre3',
     'S27': 'nuc_dnapre4',
     'S16': 'nuc_e2f_b_1_rb_s788_p_s800_u_b_1',
     'S2': 'nuc_e2f_b_1_rb_s788_u_s800_u_b_1',
     'S14': 'nuc_e2f_b',
     'S11': 'nuc_p21_b',
     'S21': 'nuc_rb_s788_p_s800_p_b',
     'S15': 'nuc_rb_s788_p_s800_u_b',
     'S1': 'nuc_rb_s788_u_s800_u_b',
     'S28': 'nuc_dnapre5'}

    def __init__(self, model_path: str = 'data/BIOMD0000000568.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Mueller2015HepatocyteProliferationT160PhosphBiomd0000000568Model = Mueller2015HepatocyteProliferationT160PhosphModel
