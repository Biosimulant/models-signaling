# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zi2011_TGF-beta_Pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zi2011TgfBetaPathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000342'
    _TITLE = 'Zi2011_TGF-beta_Pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'smad2c': ('Smad2c',
                'nM',
                'Smad2c. Maps to SBML symbol `Smad2c` and is emitted in native SBML units.'),
     'smad2n': ('Smad2n',
                'nM',
                'Smad2n. Maps to SBML symbol `Smad2n` and is emitted in native SBML units.'),
     'smad4c': ('Smad4c',
                'nM',
                'Smad4c. Maps to SBML symbol `Smad4c` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_empty_degraded': ('empty_degraded',
                                0.0,
                                'nM',
                                'Initial level of Empty Degraded. Maps to SBML symbol '
                                '`empty_degraded`; exposed as a traceable initial-condition '
                                'perturbation.'),
     'initial_source_defined_aa_state': ('AA',
                                         0.0,
                                         'nM',
                                         'Initial level of source-defined AA state. Maps to SBML '
                                         'symbol `AA`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {'initial_kdeg_tgf_beta_response_parameter_level': ('kdeg_TGF_beta',
                                                        0.347,
                                                        'per_min',
                                                        'Kdeg TGF beta response parameter source '
                                                        'parameter. Maps to SBML symbol '
                                                        '`kdeg_TGF_beta` and preserves the bundled '
                                                        'default.')}
    _SPECIES_LABELS = {'TGF_beta_ex': 'TGF beta response parameter Ex',
     'T1R_surf': 'T1R Surf',
     'T1R_endo': 'T1R Endo',
     'T2R_surf': 'T2R Surf',
     'T2R_endo': 'T2R Endo',
     'LRC_surf': 'LRC Surf',
     'LRC_endo': 'LRC Endo',
     'Smad2c': 'Smad2c',
     'Smad2n': 'Smad2n',
     'Smad4c': 'Smad4c',
     'Smad4n': 'Smad4n',
     'PSmad2c': 'Psmad2c',
     'PSmad2_PSmad2_c': 'Psmad2 Psmad2 C',
     'PSmad2_Smad4_c': 'Psmad2 Smad4 C',
     'PSmad2n': 'Psmad2n',
     'PSmad2_PSmad2_n': 'Psmad2 Psmad2 N',
     'PSmad2_Smad4_n': 'Psmad2 Smad4 N',
     'TGF_beta_endo': 'TGF beta response parameter Endo',
     'TGF_beta_ns': 'TGF beta response parameter Ns'}
    _STATE_OUTPUT_ALIASES = {'TGF_beta_ex': 'tgf_beta_response_parameter_ex',
     'T1R_surf': 't1r_surf',
     'T1R_endo': 't1r_endo',
     'T2R_surf': 't2r_surf',
     'T2R_endo': 't2r_endo',
     'LRC_surf': 'lrc_surf',
     'LRC_endo': 'lrc_endo',
     'Smad2c': 'smad2c',
     'Smad2n': 'smad2n',
     'Smad4c': 'smad4c',
     'Smad4n': 'smad4n',
     'PSmad2c': 'psmad2c',
     'PSmad2_PSmad2_c': 'psmad2_psmad2_c',
     'PSmad2_Smad4_c': 'psmad2_smad4_c',
     'PSmad2n': 'psmad2n',
     'PSmad2_PSmad2_n': 'psmad2_psmad2_n',
     'PSmad2_Smad4_n': 'psmad2_smad4_n',
     'TGF_beta_endo': 'tgf_beta_response_parameter_endo',
     'TGF_beta_ns': 'tgf_beta_response_parameter_ns'}

    def __init__(self, model_path: str = 'data/BIOMD0000000342.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Zi2011TgfBetaPathwayBiomd0000000342Model = Zi2011TgfBetaPathwayModel
