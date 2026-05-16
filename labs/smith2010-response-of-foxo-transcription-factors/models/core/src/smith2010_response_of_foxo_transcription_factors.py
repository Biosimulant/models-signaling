# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Smith2010 - Response of FOXO Transcription Factors to Post-Translational Modifications Made by Ageing-Related Signalling Pathways."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2010ResponseOfFoxoTranscriptionFactorsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000705'
    _TITLE = 'Smith2010 - Response of FOXO Transcription Factors to Post-Translational Modifications Made by Ageing-Related Signalling Pathways'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'cytoplasm_foxo1_unpolyubiquitinated_unphosphorylated': ('cytoplasm_Foxo1_Pa0_pUb0',
                                                              'native SBML value',
                                                              'Cytoplasm Foxo1 Unpolyubiquitinated '
                                                              'Unphosphorylated. Maps to SBML symbol '
                                                              '`cytoplasm_Foxo1_Pa0_pUb0` and is '
                                                              'emitted in native SBML units.'),
     'nucleus_foxo1_unpolyubiquitinated_unphosphorylated': ('nucleus_Foxo1_Pa0_pUb0',
                                                            'native SBML value',
                                                            'Nucleus Foxo1 Unpolyubiquitinated '
                                                            'Unphosphorylated. Maps to SBML symbol '
                                                            '`nucleus_Foxo1_Pa0_pUb0` and is emitted '
                                                            'in native SBML units.'),
     'dnabound_foxo1_unpolyubiquitinated_unphosphorylated': ('dnabound_Foxo1_Pa0_pUb0',
                                                             'native SBML value',
                                                             'Dnabound Foxo1 Unpolyubiquitinated '
                                                             'Unphosphorylated. Maps to SBML symbol '
                                                             '`dnabound_Foxo1_Pa0_pUb0` and is emitted '
                                                             'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cytoplasm_foxo1_total': ('cytoplasm_Foxo1_tot',
                                       120481927710843.0,
                                       'native SBML value',
                                       'Initial level of Cytoplasm Foxo1 Total. Maps to SBML symbol '
                                       '`cytoplasm_Foxo1_tot`; exposed as a traceable '
                                       'initial-condition perturbation.'),
     'initial_degr_foxo1': ('degr_Foxo1',
                            0.0,
                            'native SBML value',
                            'Initial level of Degr Foxo1. Maps to SBML symbol `degr_Foxo1`; exposed as '
                            'a traceable initial-condition perturbation.'),
     'initial_dnabound_foxo1_total': ('dnabound_Foxo1_tot',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of Dnabound Foxo1 Total. Maps to SBML symbol '
                                      '`dnabound_Foxo1_tot`; exposed as a traceable initial-condition '
                                      'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'null': 'source-defined NULL state',
     'degr_Foxo1': 'Degr Foxo1',
     'cytoplasm_Foxo1_Pa0_pUb0': 'Cytoplasm Foxo1 Unpolyubiquitinated Unphosphorylated',
     'nucleus_Foxo1_Pa0_pUb0': 'Nucleus Foxo1 Unpolyubiquitinated Unphosphorylated',
     'dnabound_Foxo1_Pa0_pUb0': 'Dnabound Foxo1 Unpolyubiquitinated Unphosphorylated',
     'cytoplasm_Foxo1_Pa0_pUb1': 'Cytoplasm Foxo1 Polyubiquitinated',
     'nucleus_Foxo1_Pa0_pUb1': 'Nucleus Foxo1 Polyubiquitinated',
     'dnabound_Foxo1_Pa0_pUb1': 'Dnabound Foxo1 Polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_pUb0': 'Cytoplasm Foxo1 Phosphorylated',
     'nucleus_Foxo1_Pa1_pUb0': 'Nucleus Foxo1 Phosphorylated',
     'dnabound_Foxo1_Pa1_pUb0': 'Dnabound Foxo1 Phosphorylated',
     'cytoplasm_Foxo1_Pa1_pUb1': 'Cytoplasm Foxo1 Polyubiquitinated Phosphorylated',
     'nucleus_Foxo1_Pa1_pUb1': 'Nucleus Foxo1 Polyubiquitinated Phosphorylated',
     'dnabound_Foxo1_Pa1_pUb1': 'Dnabound Foxo1 Polyubiquitinated Phosphorylated',
     'Foxo1_Pa0_tot': 'Foxo1 Unphosphorylated Total',
     'Foxo1_Pa1_tot': 'Foxo1 Phosphorylated Total',
     'Foxo1_pUb0_tot': 'Foxo1 Unpolyubiquitinated Total',
     'Foxo1_pUb1_tot': 'Foxo1 Polyubiquitinated Total',
     'cytoplasm_Foxo1_tot': 'Cytoplasm Foxo1 Total',
     'nucleus_Foxo1_tot': 'Nucleus Foxo1 Total',
     'dnabound_Foxo1_tot': 'Dnabound Foxo1 Total',
     'Foxo1_all': 'Foxo1 Total',
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
     'IKKb': 'source-defined IKK state',
     'JNK': 'source-defined JNK state',
     'PP2A': 'PP2A',
     'CBPP300': 'CBPP300',
     'SIRT1': 'source-defined SIRT1 state',
     'E3': 'source-defined E3 state',
     'USP7': 'source-defined USP7 state',
     'SCF': 'source-defined SCF state',
     'Proteasome': 'Proteasome',
     'Foxo1_total_rate': 'Foxo1 Total Rate'}
    _STATE_OUTPUT_ALIASES = {'null': 'source_defined_null_state',
     'degr_Foxo1': 'degr_foxo1',
     'cytoplasm_Foxo1_Pa0_pUb0': 'cytoplasm_foxo1_unpolyubiquitinated_unphosphorylated',
     'nucleus_Foxo1_Pa0_pUb0': 'nucleus_foxo1_unpolyubiquitinated_unphosphorylated',
     'dnabound_Foxo1_Pa0_pUb0': 'dnabound_foxo1_unpolyubiquitinated_unphosphorylated',
     'cytoplasm_Foxo1_Pa0_pUb1': 'cytoplasm_foxo1_polyubiquitinated',
     'nucleus_Foxo1_Pa0_pUb1': 'nucleus_foxo1_polyubiquitinated',
     'dnabound_Foxo1_Pa0_pUb1': 'dnabound_foxo1_polyubiquitinated',
     'cytoplasm_Foxo1_Pa1_pUb0': 'cytoplasm_foxo1_phosphorylated',
     'nucleus_Foxo1_Pa1_pUb0': 'nucleus_foxo1_phosphorylated',
     'dnabound_Foxo1_Pa1_pUb0': 'dnabound_foxo1_phosphorylated',
     'cytoplasm_Foxo1_Pa1_pUb1': 'cytoplasm_foxo1_polyubiquitinated_phosphorylated',
     'nucleus_Foxo1_Pa1_pUb1': 'nucleus_foxo1_polyubiquitinated_phosphorylated',
     'dnabound_Foxo1_Pa1_pUb1': 'dnabound_foxo1_polyubiquitinated_phosphorylated',
     'Foxo1_Pa0_tot': 'foxo1_unphosphorylated_total',
     'Foxo1_Pa1_tot': 'foxo1_phosphorylated_total',
     'Foxo1_pUb0_tot': 'foxo1_unpolyubiquitinated_total',
     'Foxo1_pUb1_tot': 'foxo1_polyubiquitinated_total',
     'cytoplasm_Foxo1_tot': 'cytoplasm_foxo1_total',
     'nucleus_Foxo1_tot': 'nucleus_foxo1_total',
     'dnabound_Foxo1_tot': 'dnabound_foxo1_total',
     'Foxo1_all': 'foxo1_total',
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
     'IKKb': 'source_defined_ikk_state',
     'JNK': 'source_defined_jnk_state',
     'PP2A': 'pp2a',
     'CBPP300': 'cbpp300',
     'SIRT1': 'source_defined_sirt1_state',
     'E3': 'source_defined_e3_state',
     'USP7': 'source_defined_usp7_state',
     'SCF': 'source_defined_scf_state',
     'Proteasome': 'proteasome',
     'Foxo1_total_rate': 'foxo1_total_rate'}

    def __init__(self, model_path: str = 'data/BIOMD0000000705.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smith2010ResponseOfFoxoTranscriptionFactorsBiomd0000000705Model = Smith2010ResponseOfFoxoTranscriptionFactorsModel
