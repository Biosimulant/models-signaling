# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Proctor2016 - Circadian rhythm of PTH and the dynamics of signaling molecules on bone remodeling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2016CircadianRhythmOfPthAndTheDynaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000612'
    _TITLE = 'Proctor2016 - Circadian rhythm of PTH and the dynamics of signaling molecules on bone remodeling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_bone_state': ('Bone',
                                   'native SBML value',
                                   'Source Defined BONE State. Maps to SBML symbol `Bone` and is '
                                   'emitted in native SBML units.'),
     'source_defined_hsc_state': ('HSC',
                                  'native SBML value',
                                  'Source Defined HSC State. Maps to SBML symbol `HSC` and is emitted '
                                  'in native SBML units.'),
     'source_defined_ob_m_state': ('Ob_m',
                                   'native SBML value',
                                   'Source Defined OB M State. Maps to SBML symbol `Ob_m` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sink_species': ('Sink',
                              1.0,
                              'native SBML value',
                              'Initial level of sink species. Maps to SBML symbol `Sink`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_source': ('Source',
                        1.0,
                        'native SBML value',
                        'Initial level of Source. Maps to SBML symbol `Source`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_kact_tgf_beta_level': ('kactTgfb',
                                     2e-07,
                                     'native SBML value',
                                     'Kact TGF-beta source parameter. Maps to SBML symbol `kactTgfb` '
                                     'and preserves the bundled default.')}
    _SPECIES_LABELS = {'Bone': 'Source Defined BONE State',
     'HSC': 'Source Defined HSC State',
     'Ob_m': 'Source Defined OB M State',
     'Ob_p': 'Source Defined OB P State',
     'Ob_p_Tgfb_A': 'Ob P TGF beta response parameter Response Parameter Response Parameter Response '
                    'Parameter Response Parameter A',
     'Ob_pro': 'Ob Pro',
     'Ocl_m': 'Source Defined OCL M State',
     'Ocl_p': 'Source Defined OCL P State',
     'Ocl_p_RANKL': 'Ocl P RANKL',
     'Ocy_A': 'Source Defined OCY A State',
     'Ocy_I': 'Source Defined OCY I State',
     'Ocy_I_PTH': 'Ocy I PTH',
     'MSC': 'Source Defined MSC State',
     'LOAD': 'Source Defined LOAD State',
     'MCSF': 'Source Defined MCSF State',
     'Ob_m_PTH': 'Ob M PTH',
     'Ob_p_PTH': 'Ob P PTH',
     'OPG': 'Source Defined OPG State',
     'OPG_RANKL': 'OPG RANKL',
     'PTH': 'Source Defined PTH State',
     'RANKL': 'RANKL',
     'Sost': 'Source Defined SOST State',
     'Tgfb_A': 'TGF beta response parameter Response Parameter Response Parameter Response Parameter '
               'Response Parameter A',
     'Tgfb_I': 'TGF beta response parameter Response Parameter Response Parameter Response Parameter '
               'Response Parameter I',
     'Wnt_A': 'Source Defined WNT A State',
     'Wnt_I': 'Source Defined WNT I State',
     'Source': 'Source',
     'Sink': 'sink species Species Species Species Species Species',
     'X': 'Response Node X',
     'newbone': 'Newbone',
     'Bax': 'Source Defined BAX State',
     'Bax_Bcl2': 'Bax BCL2',
     'Bcl2': 'Source Defined BCL2 State',
     'CREB': 'Source Defined CREB State',
     'CREB_P': 'CREB P',
     'CREB_Runx2': 'CREB RUNX2',
     'Runx2': 'Source Defined RUNX2 State'}
    _STATE_OUTPUT_ALIASES = {'Bone': 'source_defined_bone_state',
     'HSC': 'source_defined_hsc_state',
     'Ob_m': 'source_defined_ob_m_state',
     'Ob_p': 'source_defined_ob_p_state',
     'Ob_p_Tgfb_A': 'ob_p_tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_a',
     'Ob_pro': 'ob_pro',
     'Ocl_m': 'source_defined_ocl_m_state',
     'Ocl_p': 'source_defined_ocl_p_state',
     'Ocl_p_RANKL': 'ocl_p_rankl',
     'Ocy_A': 'source_defined_ocy_a_state',
     'Ocy_I': 'source_defined_ocy_i_state',
     'Ocy_I_PTH': 'ocy_i_pth',
     'MSC': 'source_defined_msc_state',
     'LOAD': 'source_defined_load_state',
     'MCSF': 'source_defined_mcsf_state',
     'Ob_m_PTH': 'ob_m_pth',
     'Ob_p_PTH': 'ob_p_pth',
     'OPG': 'source_defined_opg_state',
     'OPG_RANKL': 'opg_rankl',
     'PTH': 'source_defined_pth_state',
     'RANKL': 'rankl',
     'Sost': 'source_defined_sost_state',
     'Tgfb_A': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_a',
     'Tgfb_I': 'tgf_beta_response_parameter_response_parameter_response_parameter_response_parameter_response_parameter_i',
     'Wnt_A': 'source_defined_wnt_a_state',
     'Wnt_I': 'source_defined_wnt_i_state',
     'Source': 'source',
     'Sink': 'sink_species_species_species_species_species_species',
     'X': 'response_node_x',
     'newbone': 'newbone',
     'Bax': 'source_defined_bax_state',
     'Bax_Bcl2': 'bax_bcl2',
     'Bcl2': 'source_defined_bcl2_state',
     'CREB': 'source_defined_creb_state',
     'CREB_P': 'creb_p',
     'CREB_Runx2': 'creb_runx2',
     'Runx2': 'source_defined_runx2_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000612.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Proctor2016CircadianRhythmOfPthAndTheDynaBiomd0000000612Model = Proctor2016CircadianRhythmOfPthAndTheDynaModel
