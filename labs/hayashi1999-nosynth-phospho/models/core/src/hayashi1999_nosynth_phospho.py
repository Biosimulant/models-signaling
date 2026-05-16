# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hayashi1999_NOSynth_Phospho."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hayashi1999NosynthPhosphoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL4780784080'
    _TITLE = 'Hayashi1999_NOSynth_Phospho'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nos_calcium_calcium_mn_nos': ('NOS_slash_Ca_minus_CaMnNOS',
                                    'native SBML value',
                                    'NOS Calcium Calcium Mn NOS. Maps to SBML symbol '
                                    '`NOS_slash_Ca_minus_CaMnNOS` and is emitted in native SBML '
                                    'units.'),
     'nos_calcium_calcium_mn_nos_kenz_kenz_cplx': ('NOS_slash_Ca_minus_CaMnNOS_slash_kenz_slash_kenz_cplx',
                                                   'native SBML value',
                                                   'NOS Calcium Calcium Mn NOS Kenz Kenz Cplx. Maps to '
                                                   'SBML symbol '
                                                   '`NOS_slash_Ca_minus_CaMnNOS_slash_kenz_slash_kenz_cplx` '
                                                   'and is emitted in native SBML units.'),
     'nos_calcium_mkiv_kenz_kenz_cplx': ('NOS_slash_CaMKIV_slash_kenz_slash_kenz_cplx',
                                         'native SBML value',
                                         'NOS Calcium MKIV Kenz Kenz Cplx. Maps to SBML symbol '
                                         '`NOS_slash_CaMKIV_slash_kenz_slash_kenz_cplx` and is emitted '
                                         'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_nos_calcium_m_ca4': ('NOS_slash_CaM_minus_Ca4',
                                   20.0,
                                   'native SBML value',
                                   'Initial level of NOS calcium M Ca4. Maps to SBML symbol '
                                   '`NOS_slash_CaM_minus_Ca4`; exposed as a traceable '
                                   'initial-condition perturbation.'),
     'initial_nos_calcium_mkialpha': ('NOS_slash_CaMKIalpha',
                                      1.0,
                                      'native SBML value',
                                      'Initial level of NOS calcium Mkialpha. Maps to SBML symbol '
                                      '`NOS_slash_CaMKIalpha`; exposed as a traceable '
                                      'initial-condition perturbation.'),
     'initial_nos_calcium_mkiialpha': ('NOS_slash_CaMKIIalpha',
                                       1.0,
                                       'native SBML value',
                                       'Initial level of NOS calcium Mkiialpha. Maps to SBML symbol '
                                       '`NOS_slash_CaMKIIalpha`; exposed as a traceable '
                                       'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'NOS_slash_nNOS': 'NOS NNOS',
     'NOS_slash_NOS_star_': 'NOS NOS active',
     'NOS_slash_Ca_minus_CaMnNOS': 'NOS Calcium Calcium Mn NOS',
     'NOS_slash_Ca_minus_CaMnNOS_slash_kenz_slash_kenz_cplx': 'NOS Calcium Calcium Mn NOS Kenz Kenz '
                                                              'Cplx',
     'NOS_slash_NO': 'NOS NO',
     'NOS_slash_cit': 'NOS Cit',
     'NOS_slash_Larg': 'NOS Larg',
     'NOS_slash_CaMKIV_slash_kenz_slash_kenz_cplx': 'NOS Calcium MKIV Kenz Kenz Cplx',
     'NOS_slash_CaMKIIalpha_slash_kenz_slash_kenz_cplx': 'NOS Calcium Mkiialpha Kenz Kenz Cplx',
     'NOS_slash_CaMKIalpha_slash_kenz_slash_kenz_cplx': 'NOS Calcium Mkialpha Kenz Kenz Cplx',
     'NOS_slash_CaMKIV': 'NOS Calcium MKIV',
     'NOS_slash_CaMKIIalpha': 'NOS Calcium Mkiialpha',
     'NOS_slash_CaMKIalpha': 'NOS Calcium Mkialpha',
     'NOS_slash_CaM_minus_Ca4': 'NOS Calcium M CA4'}
    _STATE_OUTPUT_ALIASES = {'NOS_slash_nNOS': 'nos_nnos',
     'NOS_slash_NOS_star_': 'nos_nos_active',
     'NOS_slash_Ca_minus_CaMnNOS': 'nos_calcium_calcium_mn_nos',
     'NOS_slash_Ca_minus_CaMnNOS_slash_kenz_slash_kenz_cplx': 'nos_calcium_calcium_mn_nos_kenz_kenz_cplx',
     'NOS_slash_NO': 'nos_no',
     'NOS_slash_cit': 'nos_cit',
     'NOS_slash_Larg': 'nos_larg',
     'NOS_slash_CaMKIV_slash_kenz_slash_kenz_cplx': 'nos_calcium_mkiv_kenz_kenz_cplx',
     'NOS_slash_CaMKIIalpha_slash_kenz_slash_kenz_cplx': 'nos_calcium_mkiialpha_kenz_kenz_cplx',
     'NOS_slash_CaMKIalpha_slash_kenz_slash_kenz_cplx': 'nos_calcium_mkialpha_kenz_kenz_cplx',
     'NOS_slash_CaMKIV': 'nos_calcium_mkiv',
     'NOS_slash_CaMKIIalpha': 'nos_calcium_mkiialpha',
     'NOS_slash_CaMKIalpha': 'nos_calcium_mkialpha',
     'NOS_slash_CaM_minus_Ca4': 'nos_calcium_m_ca4'}

    def __init__(self, model_path: str = 'data/MODEL4780784080.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hayashi1999NosynthPhosphoModel4780784080Model = Hayashi1999NosynthPhosphoModel
