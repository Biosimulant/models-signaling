# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Strasen2018 - TGFb SMAD Signalling - DRB treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Strasen2018TgfbSmadSignallingDrbTreatmentModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000997'
    _TITLE = 'Strasen2018 - TGFb SMAD Signalling - DRB treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'active_tgfr2': ('Active_R2',
                      'native SBML value',
                      'active TGFR2. Maps to SBML symbol `Active_R2` and is emitted in native SBML '
                      'units.'),
     'active_tgf_beta_tgfr1_tgfr2': ('Active_Rec',
                                     'native SBML value',
                                     'active TGF-beta TGFR1 TGFR2. Maps to SBML symbol `Active_Rec` '
                                     'and is emitted in native SBML units.'),
     'active_tgf_beta_tgfr1_tgfr2_endo': ('Active_Rec_endo',
                                          'native SBML value',
                                          'active TGF-beta TGFR1 TGFR2 Endo. Maps to SBML symbol '
                                          '`Active_Rec_endo` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_index_induced_ligand_deg_level': ('index_induced_ligand_deg',
                                                2.7210717377255,
                                                'native SBML value',
                                                'Index Induced Ligand Deg source parameter. Maps to '
                                                'SBML symbol `index_induced_ligand_deg` and preserves '
                                                'the bundled default.'),
     'initial_kin_deg_ligand_level': ('kin_deg_Ligand',
                                      0.720198437381795,
                                      'native SBML value',
                                      'Kin Deg Ligand source parameter. Maps to SBML symbol '
                                      '`kin_deg_Ligand` and preserves the bundled default.'),
     'initial_tgf_beta_ligand_dose': ('TGFb_LIGAND_Dose',
                                      100.0,
                                      'native SBML value',
                                      'TGF-beta LIGAND Dose source parameter. Maps to SBML symbol '
                                      '`TGFb_LIGAND_Dose` and preserves the bundled default.')}
    _SPECIES_LABELS = {'TGFb_R1_surface': 'TGF-beta TGFR1 Surface',
     'TGFb_R2_surface': 'TGF-beta TGFR2 Surface',
     'TGFb_R1_endo': 'TGF-beta TGFR1 Endo',
     'TGFb_R2_endo': 'TGF-beta TGFR2 Endo',
     'TGFb': 'TGF-beta',
     'TGFb_In': 'TGF-beta In',
     'Active_R2': 'active TGFR2',
     'Active_Rec': 'active TGF-beta TGFR1 TGFR2',
     'Active_Rec_endo': 'active TGF-beta TGFR1 TGFR2 Endo',
     'Inactive_Rec': 'Inactive TGF-beta TGFR1 TGFR2',
     'pS2_c': 'P SMAD2 C',
     'S2_c': 'SMAD2 C',
     'S4_c': 'SMAD4 C',
     'pS2_pS2_S4_c': 'P SMAD2 P SMAD2 SMAD4 C',
     'pS2_pS2_pS2_c': 'P SMAD2 Trimer C',
     'Smad7mRNA': 'SMAD7 M RNA',
     'S7': 'SMAD7',
     'Smad7mRNA1': 'SMAD7 M RNA1',
     'pS2_n': 'P SMAD2 N',
     'pS2_pS2_S4_n': 'P SMAD2 P SMAD2 SMAD4 N',
     'pS2_pS2_pS2_n': 'P SMAD2 Trimer N',
     'S2_n': 'SMAD2 N',
     'S4_n': 'SMAD4 N'}
    _STATE_OUTPUT_ALIASES = {'TGFb_R1_surface': 'tgf_beta_tgfr1_surface',
     'TGFb_R2_surface': 'tgf_beta_tgfr2_surface',
     'TGFb_R1_endo': 'tgf_beta_tgfr1_endo',
     'TGFb_R2_endo': 'tgf_beta_tgfr2_endo',
     'TGFb': 'tgf_beta',
     'TGFb_In': 'tgf_beta_in',
     'Active_R2': 'active_tgfr2',
     'Active_Rec': 'active_tgf_beta_tgfr1_tgfr2',
     'Active_Rec_endo': 'active_tgf_beta_tgfr1_tgfr2_endo',
     'Inactive_Rec': 'inactive_tgf_beta_tgfr1_tgfr2',
     'pS2_c': 'p_smad2_c',
     'S2_c': 'smad2_c',
     'S4_c': 'smad4_c',
     'pS2_pS2_S4_c': 'p_smad2_p_smad2_smad4_c',
     'pS2_pS2_pS2_c': 'p_smad2_trimer_c',
     'Smad7mRNA': 'smad7_m_rna',
     'S7': 'smad7',
     'Smad7mRNA1': 'smad7_m_rna1',
     'pS2_n': 'p_smad2_n',
     'pS2_pS2_S4_n': 'p_smad2_p_smad2_smad4_n',
     'pS2_pS2_pS2_n': 'p_smad2_trimer_n',
     'S2_n': 'smad2_n',
     'S4_n': 'smad4_n'}

    def __init__(self, model_path: str = 'data/BIOMD0000000997.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Strasen2018TgfbSmadSignallingDrbTreatmentBiomd0000000997Model = Strasen2018TgfbSmadSignallingDrbTreatmentModel
