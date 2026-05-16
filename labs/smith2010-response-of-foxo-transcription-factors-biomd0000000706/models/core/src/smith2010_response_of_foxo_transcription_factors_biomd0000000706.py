# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Smith2010 - Response of FOXO Transcription Factors to Post-Translational Modifications (with acetylation pathway)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2010ResponseOfFoxoTranscriptionFactorsBiomd0000000706Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000706'
    _TITLE = 'Smith2010 - Response of FOXO Transcription Factors to Post-Translational Modifications (with acetylation pathway)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytoplasm_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated': ('cytoplasm_Foxo1_Pa0_Ac0_pUb0',
                                                                            'native SBML value',
                                                                            'Cytoplasm Foxo1 '
                                                                            'Unphosphorylated '
                                                                            'Unacetylated '
                                                                            'Notpolyubiquitinated. '
                                                                            'Maps to SBML symbol '
                                                                            '`cytoplasm_Foxo1_Pa0_Ac0_pUb0` '
                                                                            'and is emitted in native '
                                                                            'SBML units.'),
     'nucleus_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated': ('nucleus_Foxo1_Pa0_Ac0_pUb0',
                                                                          'native SBML value',
                                                                          'Nucleus Foxo1 '
                                                                          'Unphosphorylated '
                                                                          'Unacetylated '
                                                                          'Notpolyubiquitinated. Maps '
                                                                          'to SBML symbol '
                                                                          '`nucleus_Foxo1_Pa0_Ac0_pUb0` '
                                                                          'and is emitted in native '
                                                                          'SBML units.'),
     'dnabound_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated': ('dnabound_Foxo1_Pa0_Ac0_pUb0',
                                                                           'native SBML value',
                                                                           'Dnabound Foxo1 '
                                                                           'Unphosphorylated '
                                                                           'Unacetylated '
                                                                           'Notpolyubiquitinated. Maps '
                                                                           'to SBML symbol '
                                                                           '`dnabound_Foxo1_Pa0_Ac0_pUb0` '
                                                                           'and is emitted in native '
                                                                           'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cytoplasm_foxo1_tot': ('cytoplasm_Foxo1_tot',
                                     120481927710843.0,
                                     'native SBML value',
                                     'Initial level of Cytoplasm Foxo1 Tot. Maps to SBML symbol '
                                     '`cytoplasm_Foxo1_tot`; exposed as a traceable initial-condition '
                                     'perturbation.'),
     'initial_dnabound_foxo1_tot': ('dnabound_Foxo1_tot',
                                    0.0,
                                    'native SBML value',
                                    'Initial level of Dnabound Foxo1 Tot. Maps to SBML symbol '
                                    '`dnabound_Foxo1_tot`; exposed as a traceable initial-condition '
                                    'perturbation.'),
     'initial_foxo1_acetylated_tot': ('Foxo1_Ac1_tot',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of Foxo1 Acetylated Tot. Maps to SBML symbol '
                                      '`Foxo1_Ac1_tot`; exposed as a traceable initial-condition '
                                      'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'null': 'source-defined NULL state',
     'degr_Foxo1': 'Degr Foxo1',
     'cytoplasm_Foxo1_Pa0_Ac0_pUb0': 'Cytoplasm Foxo1 Unphosphorylated Unacetylated '
                                     'Notpolyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac0_pUb0': 'Nucleus Foxo1 Unphosphorylated Unacetylated Notpolyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac0_pUb0': 'Dnabound Foxo1 Unphosphorylated Unacetylated Notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac0_pUb1': 'Cytoplasm Foxo1 Unphosphorylated Unacetylated Polyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac0_pUb1': 'Nucleus Foxo1 Unphosphorylated Unacetylated Polyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac0_pUb1': 'Dnabound Foxo1 Unphosphorylated Unacetylated Polyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac1_pUb0': 'Cytoplasm Foxo1 Unphosphorylated Acetylated Notpolyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac1_pUb0': 'Nucleus Foxo1 Unphosphorylated Acetylated Notpolyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac1_pUb0': 'Dnabound Foxo1 Unphosphorylated Acetylated Notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac1_pUb1': 'Cytoplasm Foxo1 Unphosphorylated Acetylated Polyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac1_pUb1': 'Nucleus Foxo1 Unphosphorylated Acetylated Polyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac1_pUb1': 'Dnabound Foxo1 Unphosphorylated Acetylated Polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac0_pUb0': 'Cytoplasm Foxo1 Phosphorylated Unacetylated Notpolyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac0_pUb0': 'Nucleus Foxo1 Phosphorylated Unacetylated Notpolyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac0_pUb0': 'Dnabound Foxo1 Phosphorylated Unacetylated Notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac0_pUb1': 'Cytoplasm Foxo1 Phosphorylated Unacetylated Polyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac0_pUb1': 'Nucleus Foxo1 Phosphorylated Unacetylated Polyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac0_pUb1': 'Dnabound Foxo1 Phosphorylated Unacetylated Polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac1_pUb0': 'Cytoplasm Foxo1 Phosphorylated Acetylated Notpolyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac1_pUb0': 'Nucleus Foxo1 Phosphorylated Acetylated Notpolyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac1_pUb0': 'Dnabound Foxo1 Phosphorylated Acetylated Notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac1_pUb1': 'Cytoplasm Foxo1 Phosphorylated Acetylated Polyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac1_pUb1': 'Nucleus Foxo1 Phosphorylated Acetylated Polyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac1_pUb1': 'Dnabound Foxo1 Phosphorylated Acetylated Polyubiquitinated',
     'Foxo1_Pa0_tot': 'Foxo1 Unphosphorylated Tot',
     'Foxo1_Pa1_tot': 'Foxo1 Phosphorylated Tot',
     'Foxo1_Ac0_tot': 'Foxo1 Unacetylated Tot',
     'Foxo1_Ac1_tot': 'Foxo1 Acetylated Tot',
     'Foxo1_pUb0_tot': 'Foxo1 Unpolyubiquitinated Tot',
     'Foxo1_pUb1_tot': 'Foxo1 Polyubiquitinated Tot',
     'cytoplasm_Foxo1_tot': 'Cytoplasm Foxo1 Tot',
     'nucleus_Foxo1_tot': 'Nucleus Foxo1 Tot',
     'dnabound_Foxo1_tot': 'Dnabound Foxo1 Tot',
     'Foxo1_all': 'Foxo1 All',
     'nucleus_RNA_Inr': 'Nucleus RNA Inr',
     'cytoplasm_RNA_Inr': 'Cytoplasm RNA Inr',
     'cytoplasm_Inr': 'Cytoplasm Inr',
     'nucleus_RNA_Sod2': 'Nucleus RNA Sod2',
     'cytoplasm_RNA_Sod2': 'Cytoplasm RNA Sod2',
     'cytoplasm_Sod2': 'Cytoplasm Sod2',
     'E2F1': 'E2F1',
     'Akt': 'AKT',
     'SGK': 'source-defined SGK state',
     'CDK2': 'source-defined CDK2 state',
     'AMPK': 'source-defined AMPK state',
     'IKKb': 'source-defined IKKB state',
     'JNK': 'source-defined JNK state',
     'PP2A': 'PP2A',
     'CBPP300': 'CBPP300',
     'SIRT1': 'source-defined SIRT1 state',
     'E3': 'source-defined E3 state',
     'USP7': 'source-defined USP7 state',
     'SCF': 'source-defined SCF state',
     'Proteasome': 'Proteasome',
     'Foxo1_all_rate': 'Foxo1 All Rate'}
    _STATE_OUTPUT_ALIASES = {'null': 'source_defined_null_state',
     'degr_Foxo1': 'degr_foxo1',
     'cytoplasm_Foxo1_Pa0_Ac0_pUb0': 'cytoplasm_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac0_pUb0': 'nucleus_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac0_pUb0': 'dnabound_foxo1_unphosphorylated_unacetylated_notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac0_pUb1': 'cytoplasm_foxo1_unphosphorylated_unacetylated_polyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac0_pUb1': 'nucleus_foxo1_unphosphorylated_unacetylated_polyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac0_pUb1': 'dnabound_foxo1_unphosphorylated_unacetylated_polyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac1_pUb0': 'cytoplasm_foxo1_unphosphorylated_acetylated_notpolyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac1_pUb0': 'nucleus_foxo1_unphosphorylated_acetylated_notpolyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac1_pUb0': 'dnabound_foxo1_unphosphorylated_acetylated_notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa0_Ac1_pUb1': 'cytoplasm_foxo1_unphosphorylated_acetylated_polyubiquitinated',
     'nucleus_Foxo1_Pa0_Ac1_pUb1': 'nucleus_foxo1_unphosphorylated_acetylated_polyubiquitinated',
     'dnabound_Foxo1_Pa0_Ac1_pUb1': 'dnabound_foxo1_unphosphorylated_acetylated_polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac0_pUb0': 'cytoplasm_foxo1_phosphorylated_unacetylated_notpolyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac0_pUb0': 'nucleus_foxo1_phosphorylated_unacetylated_notpolyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac0_pUb0': 'dnabound_foxo1_phosphorylated_unacetylated_notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac0_pUb1': 'cytoplasm_foxo1_phosphorylated_unacetylated_polyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac0_pUb1': 'nucleus_foxo1_phosphorylated_unacetylated_polyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac0_pUb1': 'dnabound_foxo1_phosphorylated_unacetylated_polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac1_pUb0': 'cytoplasm_foxo1_phosphorylated_acetylated_notpolyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac1_pUb0': 'nucleus_foxo1_phosphorylated_acetylated_notpolyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac1_pUb0': 'dnabound_foxo1_phosphorylated_acetylated_notpolyubiquitinated',
     'cytoplasm_Foxo1_Pa1_Ac1_pUb1': 'cytoplasm_foxo1_phosphorylated_acetylated_polyubiquitinated',
     'nucleus_Foxo1_Pa1_Ac1_pUb1': 'nucleus_foxo1_phosphorylated_acetylated_polyubiquitinated',
     'dnabound_Foxo1_Pa1_Ac1_pUb1': 'dnabound_foxo1_phosphorylated_acetylated_polyubiquitinated',
     'Foxo1_Pa0_tot': 'foxo1_unphosphorylated_tot',
     'Foxo1_Pa1_tot': 'foxo1_phosphorylated_tot',
     'Foxo1_Ac0_tot': 'foxo1_unacetylated_tot',
     'Foxo1_Ac1_tot': 'foxo1_acetylated_tot',
     'Foxo1_pUb0_tot': 'foxo1_unpolyubiquitinated_tot',
     'Foxo1_pUb1_tot': 'foxo1_polyubiquitinated_tot',
     'cytoplasm_Foxo1_tot': 'cytoplasm_foxo1_tot',
     'nucleus_Foxo1_tot': 'nucleus_foxo1_tot',
     'dnabound_Foxo1_tot': 'dnabound_foxo1_tot',
     'Foxo1_all': 'foxo1_all',
     'nucleus_RNA_Inr': 'nucleus_rna_inr',
     'cytoplasm_RNA_Inr': 'cytoplasm_rna_inr',
     'cytoplasm_Inr': 'cytoplasm_inr',
     'nucleus_RNA_Sod2': 'nucleus_rna_sod2',
     'cytoplasm_RNA_Sod2': 'cytoplasm_rna_sod2',
     'cytoplasm_Sod2': 'cytoplasm_sod2',
     'E2F1': 'e2f1',
     'Akt': 'akt',
     'SGK': 'source_defined_sgk_state',
     'CDK2': 'source_defined_cdk2_state',
     'AMPK': 'source_defined_ampk_state',
     'IKKb': 'source_defined_ikkb_state',
     'JNK': 'source_defined_jnk_state',
     'PP2A': 'pp2a',
     'CBPP300': 'cbpp300',
     'SIRT1': 'source_defined_sirt1_state',
     'E3': 'source_defined_e3_state',
     'USP7': 'source_defined_usp7_state',
     'SCF': 'source_defined_scf_state',
     'Proteasome': 'proteasome',
     'Foxo1_all_rate': 'foxo1_all_rate'}

    def __init__(self, model_path: str = 'data/BIOMD0000000706.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smith2010ResponseOfFoxoTranscriptionFactorsBiomd0000000706Model = Smith2010ResponseOfFoxoTranscriptionFactorsBiomd0000000706Model
