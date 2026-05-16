# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Asthagiri2001_MAPK_Asthagiri_adapt_fb."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Asthagiri2001MapkAsthagiriAdaptFbModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9147975215'
    _TITLE = 'Asthagiri2001_MAPK_Asthagiri_adapt_fb'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'c_active': ('C_star_',
                  'native SBML value',
                  'C active. Maps to SBML symbol `C_star_` and is emitted in native SBML units.'),
     'c_active_a1': ('C_star_A1',
                     'native SBML value',
                     'C active A1. Maps to SBML symbol `C_star_A1` and is emitted in native SBML '
                     'units.'),
     'a1a2': ('A1A2',
              'native SBML value',
              'A1A2. Maps to SBML symbol `A1A2` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_l_state': ('L',
                                        0.03,
                                        'native SBML value',
                                        'Initial level of source-defined L state. Maps to SBML symbol '
                                        '`L`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'R': 'Source Defined R State',
     'C': 'Source Defined C State',
     'C_star_': 'C active',
     'C2': 'Source Defined C2 State',
     'A1': 'Source Defined A1 State',
     'A2': 'Source Defined A2 State',
     'C_star_A1': 'C active A1',
     'A1A2': 'A1A2',
     'E0_star_': 'E0 active',
     'E0_star__slash_E1_activ_slash_E1_activ_cplx': 'E0 active E1 Activ E1 Activ Cplx',
     'E1': 'Source Defined E1 State',
     'E1_star_': 'E1 active',
     'E1_star__slash_E2_activ_slash_E2_activ_cplx': 'E1 active E2 Activ E2 Activ Cplx',
     'P1': 'Source Defined P1 State',
     'P1_slash_E1_star__deactiv_slash_E1_star__deactiv_cplx': 'P1 E1 active Deactiv E1 active Deactiv '
                                                              'Cplx',
     'E2': 'Source Defined E2 State',
     'E2_star_': 'E2 active',
     'E2_star__slash_E3_activ_slash_E3_activ_cplx': 'E2 active E3 Activ E3 Activ Cplx',
     'P2': 'Source Defined P2 State',
     'P2_slash_E2_star__deactiv_slash_E2_star__deactiv_cplx': 'P2 E2 active Deactiv E2 active Deactiv '
                                                              'Cplx',
     'E3': 'Source Defined E3 State',
     'E3_star_': 'E3 active',
     'E3_star__slash_E4_activ_slash_E4_activ_cplx': 'E3 active E4 Activ E4 Activ Cplx',
     'P3': 'Source Defined P3 State',
     'P3_slash_E3_star__deactiv_slash_E3_star__deactiv_cplx': 'P3 E3 active Deactiv E3 active Deactiv '
                                                              'Cplx',
     'E4': 'Source Defined E4 State',
     'E4_star_': 'E4 active',
     'E4_star__slash_E5_activ_slash_E5_activ_cplx': 'E4 active E5 Activ E5 Activ Cplx',
     'E4_star__slash_E4_star__adpt_fb_slash_E4_star__adpt_fb_cplx': 'E4 active E4 active Adpt Fb E4 '
                                                                    'active Adpt Fb Cplx',
     'P4': 'Source Defined P4 State',
     'P4_slash_E4_star__deactiv_slash_E4_star__deactiv_cplx': 'P4 E4 active Deactiv E4 active Deactiv '
                                                              'Cplx',
     'E5': 'Source Defined E5 State',
     'P5': 'Source Defined P5 State',
     'P5_slash_E5_star__deactiv_slash_E5_star__deactiv_cplx': 'P5 E5 active Deactiv E5 active Deactiv '
                                                              'Cplx',
     'E5_star_': 'E5 active',
     'A2_minus_': 'Source Defined A2 State',
     'L': 'Source Defined L State'}
    _STATE_OUTPUT_ALIASES = {'R': 'source_defined_r_state',
     'C': 'source_defined_c_state',
     'C_star_': 'c_active',
     'C2': 'source_defined_c2_state',
     'A1': 'source_defined_a1_state',
     'A2': 'source_defined_a2_state',
     'C_star_A1': 'c_active_a1',
     'A1A2': 'a1a2',
     'E0_star_': 'e0_active',
     'E0_star__slash_E1_activ_slash_E1_activ_cplx': 'e0_active_e1_activ_e1_activ_cplx',
     'E1': 'source_defined_e1_state',
     'E1_star_': 'e1_active',
     'E1_star__slash_E2_activ_slash_E2_activ_cplx': 'e1_active_e2_activ_e2_activ_cplx',
     'P1': 'source_defined_p1_state',
     'P1_slash_E1_star__deactiv_slash_E1_star__deactiv_cplx': 'p1_e1_active_deactiv_e1_active_deactiv_cplx',
     'E2': 'source_defined_e2_state',
     'E2_star_': 'e2_active',
     'E2_star__slash_E3_activ_slash_E3_activ_cplx': 'e2_active_e3_activ_e3_activ_cplx',
     'P2': 'source_defined_p2_state',
     'P2_slash_E2_star__deactiv_slash_E2_star__deactiv_cplx': 'p2_e2_active_deactiv_e2_active_deactiv_cplx',
     'E3': 'source_defined_e3_state',
     'E3_star_': 'e3_active',
     'E3_star__slash_E4_activ_slash_E4_activ_cplx': 'e3_active_e4_activ_e4_activ_cplx',
     'P3': 'source_defined_p3_state',
     'P3_slash_E3_star__deactiv_slash_E3_star__deactiv_cplx': 'p3_e3_active_deactiv_e3_active_deactiv_cplx',
     'E4': 'source_defined_e4_state',
     'E4_star_': 'e4_active',
     'E4_star__slash_E5_activ_slash_E5_activ_cplx': 'e4_active_e5_activ_e5_activ_cplx',
     'E4_star__slash_E4_star__adpt_fb_slash_E4_star__adpt_fb_cplx': 'e4_active_e4_active_adpt_fb_e4_active_adpt_fb_cplx',
     'P4': 'source_defined_p4_state',
     'P4_slash_E4_star__deactiv_slash_E4_star__deactiv_cplx': 'p4_e4_active_deactiv_e4_active_deactiv_cplx',
     'E5': 'source_defined_e5_state',
     'P5': 'source_defined_p5_state',
     'P5_slash_E5_star__deactiv_slash_E5_star__deactiv_cplx': 'p5_e5_active_deactiv_e5_active_deactiv_cplx',
     'E5_star_': 'e5_active',
     'A2_minus_': 'source_defined_a2_state_2',
     'L': 'source_defined_l_state'}

    def __init__(self, model_path: str = 'data/MODEL9147975215.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Asthagiri2001MapkAsthagiriAdaptFbModel9147975215Model = Asthagiri2001MapkAsthagiriAdaptFbModel
