# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bhalla2004_PKA_2003."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhalla2004Pka2003Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9079740062'
    _TITLE = 'Bhalla2004_PKA_2003'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'pka_c_amp_dot_r2c2': ('PKA_slash_cAMP_dot_R2C2',
                            'native SBML value',
                            'PKA C AMP Dot R2C2. Maps to SBML symbol `PKA_slash_cAMP_dot_R2C2` and is '
                            'emitted in native SBML units.'),
     'pka_camp2_dot_r2c2': ('PKA_slash_cAMP2_dot_R2C2',
                            'native SBML value',
                            'PKA CAMP2 Dot R2C2. Maps to SBML symbol `PKA_slash_cAMP2_dot_R2C2` and is '
                            'emitted in native SBML units.'),
     'pka_camp3_dot_r2c2': ('PKA_slash_cAMP3_dot_R2C2',
                            'native SBML value',
                            'PKA CAMP3 Dot R2C2. Maps to SBML symbol `PKA_slash_cAMP3_dot_R2C2` and is '
                            'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_ac_amp': ('AC_slash_AMP',
                        1000.0,
                        'native SBML value',
                        'Initial level of AC AMP. Maps to SBML symbol `AC_slash_AMP`; exposed as a '
                        'traceable initial-condition perturbation.'),
     'initial_ac_atp': ('AC_slash_ATP',
                        5000.0,
                        'native SBML value',
                        'Initial level of AC ATP. Maps to SBML symbol `AC_slash_ATP`; exposed as a '
                        'traceable initial-condition perturbation.'),
     'initial_gs_ligand': ('Gs_slash_L',
                           0.0,
                           'native SBML value',
                           'Initial level of Gs ligand. Maps to SBML symbol `Gs_slash_L`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'PKA_slash_R2C2': 'PKA R2C2',
     'PKA_slash_PKA_minus_inhibitor': 'PKA PKA Inhibitor',
     'PKA_slash_inhibited_minus_PKA': 'PKA Inhibited PKA',
     'PKA_slash_cAMP_dot_R2C2': 'PKA C AMP Dot R2C2',
     'PKA_slash_cAMP2_dot_R2C2': 'PKA CAMP2 Dot R2C2',
     'PKA_slash_cAMP3_dot_R2C2': 'PKA CAMP3 Dot R2C2',
     'PKA_slash_cAMP4_dot_R2C2': 'PKA CAMP4 Dot R2C2',
     'PKA_slash_cAMP4_dot_R2C': 'PKA CAMP4 Dot R2C',
     'PKA_slash_cAMP4_dot_R2': 'PKA CAMP4 Dot R2',
     'cAMP': 'cAMP',
     'PKA_minus_active': 'PKA active',
     'PKA_minus_active_slash_phosph_minus_PDE_slash_phosph_minus_PDE_cplx': 'PKA active Phosph PDE '
                                                                            'Phosph PDE Cplx',
     'AC_slash_cAMP_minus_PDE': 'AC C AMP PDE',
     'AC_slash_cAMP_minus_PDE_slash_PDE_slash_PDE_cplx': 'AC C AMP PDE PDE PDE Cplx',
     'AC_slash_cAMP_minus_PDE_star_': 'AC C AMP PDE active',
     'AC_slash_cAMP_minus_PDE_star__slash_PDE_star__slash_PDE_star__cplx': 'AC C AMP PDE active PDE '
                                                                           'active PDE active Cplx',
     'AC_slash_Gs_dot_AC': 'AC Gs Dot AC',
     'AC_slash_AC': 'Source Defined AC AC State',
     'GTP_dot_Ga': 'GTP Dot Ga',
     'Gs_slash_R': 'Source Defined GS R State',
     'Gs_slash_L_dot_R': 'Gs L Dot R',
     'Gs_slash_GDP_dot_Gabc': 'Gs GDP Dot Gabc',
     'Gs_slash_L_dot_R_dot_GDP_dot_Gabc': 'Gs L Dot R Dot GDP Dot Gabc',
     'Gs_slash_GDP_dot_Ga': 'Gs GDP Dot Ga',
     'Gs_slash_Gbg': 'Gs G beta response parameter Response Parameter Response Parameter Response '
                     'Parameter Response Parameter Gamma Complex',
     'Gs_slash_R_dot_GDP_dot_Gabc': 'Gs R Dot GDP Dot Gabc',
     'AC_slash_ATP': 'AC ATP',
     'AC_slash_AMP': 'AC AMP',
     'Gs_slash_L': 'Source Defined GS L State'}
    _STATE_OUTPUT_ALIASES = {'PKA_slash_R2C2': 'pka_r2c2',
     'PKA_slash_PKA_minus_inhibitor': 'pka_pka_inhibitor',
     'PKA_slash_inhibited_minus_PKA': 'pka_inhibited_pka',
     'PKA_slash_cAMP_dot_R2C2': 'pka_c_amp_dot_r2c2',
     'PKA_slash_cAMP2_dot_R2C2': 'pka_camp2_dot_r2c2',
     'PKA_slash_cAMP3_dot_R2C2': 'pka_camp3_dot_r2c2',
     'PKA_slash_cAMP4_dot_R2C2': 'pka_camp4_dot_r2c2',
     'PKA_slash_cAMP4_dot_R2C': 'pka_camp4_dot_r2c',
     'PKA_slash_cAMP4_dot_R2': 'pka_camp4_dot_r2',
     'cAMP': 'camp',
     'PKA_minus_active': 'pka_active',
     'PKA_minus_active_slash_phosph_minus_PDE_slash_phosph_minus_PDE_cplx': 'pka_active_phosph_pde_phosph_pde_cplx',
     'AC_slash_cAMP_minus_PDE': 'ac_c_amp_pde',
     'AC_slash_cAMP_minus_PDE_slash_PDE_slash_PDE_cplx': 'ac_c_amp_pde_pde_pde_cplx',
     'AC_slash_cAMP_minus_PDE_star_': 'ac_c_amp_pde_active',
     'AC_slash_cAMP_minus_PDE_star__slash_PDE_star__slash_PDE_star__cplx': 'ac_c_amp_pde_active_pde_active_pde_active_cplx',
     'AC_slash_Gs_dot_AC': 'ac_gs_dot_ac',
     'AC_slash_AC': 'source_defined_ac_ac_state',
     'GTP_dot_Ga': 'gtp_dot_ga',
     'Gs_slash_R': 'source_defined_gs_r_state',
     'Gs_slash_L_dot_R': 'gs_l_dot_r',
     'Gs_slash_GDP_dot_Gabc': 'gs_gdp_dot_gabc',
     'Gs_slash_L_dot_R_dot_GDP_dot_Gabc': 'gs_l_dot_r_dot_gdp_dot_gabc',
     'Gs_slash_GDP_dot_Ga': 'gs_gdp_dot_ga',
     'Gs_slash_Gbg': 'gs_g_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_gamma_complex',
     'Gs_slash_R_dot_GDP_dot_Gabc': 'gs_r_dot_gdp_dot_gabc',
     'AC_slash_ATP': 'ac_atp',
     'AC_slash_AMP': 'ac_amp',
     'Gs_slash_L': 'source_defined_gs_l_state'}

    def __init__(self, model_path: str = 'data/MODEL9079740062.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bhalla2004Pka2003Model9079740062Model = Bhalla2004Pka2003Model
