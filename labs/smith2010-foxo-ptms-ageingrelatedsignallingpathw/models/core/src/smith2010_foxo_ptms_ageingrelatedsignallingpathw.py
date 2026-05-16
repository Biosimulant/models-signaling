# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Smith2010_Foxo_PTMs_AgeingRelatedSignallingPathway_C."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2010FoxoPtmsAgeingrelatedsignallingpathwModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1112260002'
    _TITLE = 'Smith2010_Foxo_PTMs_AgeingRelatedSignallingPathway_C'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt': ('Akt',
             'native SBML value',
             'AKT. Maps to SBML symbol `Akt` and is emitted in native SBML units.'),
     'source_defined_null_state': ('null',
                                   'native SBML value',
                                   'Source Defined NULL State. Maps to SBML symbol `null` and is '
                                   'emitted in native SBML units.'),
     'degr_foxo1': ('degr_Foxo1',
                    'native SBML value',
                    'Degr FOXO1. Maps to SBML symbol `degr_Foxo1` and is emitted in native SBML '
                    'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_degr_foxo1': ('degr_Foxo1',
                            0.0,
                            'native SBML value',
                            'Initial level of Degr Foxo1. Maps to SBML symbol `degr_Foxo1`; exposed as '
                            'a traceable initial-condition perturbation.'),
     'initial_source_defined_null_state': ('null',
                                           0.0,
                                           'native SBML value',
                                           'Initial level of source-defined NULL state. Maps to SBML '
                                           'symbol `null`; exposed as a traceable initial-condition '
                                           'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'null': 'Source Defined NULL State',
     'degr_Foxo1': 'Degr FOXO1',
     'cytoplasm_Foxo1_Pa0_Pd0_pUb0': 'Cytoplasm FOXO1 PA0 PD0 PUB0',
     'nucleus_Foxo1_Pa0_Pd0_pUb0': 'Nucleus FOXO1 PA0 PD0 PUB0',
     'dnabound_Foxo1_Pa0_Pd0_pUb0': 'Dnabound FOXO1 PA0 PD0 PUB0',
     'cytoplasm_Foxo1_Pa0_Pd0_pUb1': 'Cytoplasm FOXO1 PA0 PD0 PUB1',
     'nucleus_Foxo1_Pa0_Pd0_pUb1': 'Nucleus FOXO1 PA0 PD0 PUB1',
     'dnabound_Foxo1_Pa0_Pd0_pUb1': 'Dnabound FOXO1 PA0 PD0 PUB1',
     'cytoplasm_Foxo1_Pa0_Pd1_pUb0': 'Cytoplasm FOXO1 PA0 PD1 PUB0',
     'nucleus_Foxo1_Pa0_Pd1_pUb0': 'Nucleus FOXO1 PA0 PD1 PUB0',
     'dnabound_Foxo1_Pa0_Pd1_pUb0': 'Dnabound FOXO1 PA0 PD1 PUB0',
     'cytoplasm_Foxo1_Pa0_Pd1_pUb1': 'Cytoplasm FOXO1 PA0 PD1 PUB1',
     'nucleus_Foxo1_Pa0_Pd1_pUb1': 'Nucleus FOXO1 PA0 PD1 PUB1',
     'dnabound_Foxo1_Pa0_Pd1_pUb1': 'Dnabound FOXO1 PA0 PD1 PUB1',
     'cytoplasm_Foxo1_Pa1_Pd0_pUb0': 'Cytoplasm FOXO1 PA1 PD0 PUB0',
     'nucleus_Foxo1_Pa1_Pd0_pUb0': 'Nucleus FOXO1 PA1 PD0 PUB0',
     'dnabound_Foxo1_Pa1_Pd0_pUb0': 'Dnabound FOXO1 PA1 PD0 PUB0',
     'cytoplasm_Foxo1_Pa1_Pd0_pUb1': 'Cytoplasm FOXO1 PA1 PD0 PUB1',
     'nucleus_Foxo1_Pa1_Pd0_pUb1': 'Nucleus FOXO1 PA1 PD0 PUB1',
     'dnabound_Foxo1_Pa1_Pd0_pUb1': 'Dnabound FOXO1 PA1 PD0 PUB1',
     'cytoplasm_Foxo1_Pa1_Pd1_pUb0': 'Cytoplasm FOXO1 PA1 PD1 PUB0',
     'nucleus_Foxo1_Pa1_Pd1_pUb0': 'Nucleus FOXO1 PA1 PD1 PUB0',
     'dnabound_Foxo1_Pa1_Pd1_pUb0': 'Dnabound FOXO1 PA1 PD1 PUB0',
     'cytoplasm_Foxo1_Pa1_Pd1_pUb1': 'Cytoplasm FOXO1 PA1 PD1 PUB1',
     'nucleus_Foxo1_Pa1_Pd1_pUb1': 'Nucleus FOXO1 PA1 PD1 PUB1',
     'dnabound_Foxo1_Pa1_Pd1_pUb1': 'Dnabound FOXO1 PA1 PD1 PUB1',
     'Foxo1_Pa0_tot': 'FOXO1 PA0 Tot',
     'Foxo1_Pa1_tot': 'FOXO1 PA1 Tot',
     'Foxo1_Pd0_tot': 'FOXO1 PD0 Tot',
     'Foxo1_Pd1_tot': 'FOXO1 PD1 Tot',
     'Foxo1_pUb0_tot': 'FOXO1 PUB0 Tot',
     'Foxo1_pUb1_tot': 'FOXO1 PUB1 Tot',
     'cytoplasm_Foxo1_tot': 'Cytoplasm FOXO1 Tot',
     'nucleus_Foxo1_tot': 'Nucleus FOXO1 Tot',
     'dnabound_Foxo1_tot': 'Dnabound FOXO1 Tot',
     'Foxo1_all': 'FOXO1 All',
     'nucleus_RNA_Inr': 'Nucleus RNA Inr',
     'cytoplasm_RNA_Inr': 'Cytoplasm RNA Inr',
     'cytoplasm_Inr': 'Cytoplasm Inr',
     'nucleus_RNA_Sod2': 'Nucleus RNA SOD2',
     'cytoplasm_RNA_Sod2': 'Cytoplasm RNA SOD2',
     'cytoplasm_Sod2': 'Cytoplasm SOD2',
     'E2F1': 'E2F1',
     'Akt': 'AKT',
     'SGK': 'Source Defined SGK State',
     'CDK2': 'Source Defined CDK2 State',
     'AMPK': 'Source Defined AMPK State',
     'IKKb': 'Source Defined IKKB State',
     'JNK': 'Source Defined JNK State',
     'PP2A': 'PP2A',
     'CBPP300': 'CBPP300',
     'SIRT1': 'Source Defined SIRT1 State',
     'E3': 'Source Defined E3 State',
     'USP7': 'Source Defined USP7 State',
     'SCF': 'Source Defined SCF State',
     'Proteasome': 'Proteasome'}
    _STATE_OUTPUT_ALIASES = {'null': 'source_defined_null_state',
     'degr_Foxo1': 'degr_foxo1',
     'cytoplasm_Foxo1_Pa0_Pd0_pUb0': 'cytoplasm_foxo1_pa0_pd0_pub0',
     'nucleus_Foxo1_Pa0_Pd0_pUb0': 'nucleus_foxo1_pa0_pd0_pub0',
     'dnabound_Foxo1_Pa0_Pd0_pUb0': 'dnabound_foxo1_pa0_pd0_pub0',
     'cytoplasm_Foxo1_Pa0_Pd0_pUb1': 'cytoplasm_foxo1_pa0_pd0_pub1',
     'nucleus_Foxo1_Pa0_Pd0_pUb1': 'nucleus_foxo1_pa0_pd0_pub1',
     'dnabound_Foxo1_Pa0_Pd0_pUb1': 'dnabound_foxo1_pa0_pd0_pub1',
     'cytoplasm_Foxo1_Pa0_Pd1_pUb0': 'cytoplasm_foxo1_pa0_pd1_pub0',
     'nucleus_Foxo1_Pa0_Pd1_pUb0': 'nucleus_foxo1_pa0_pd1_pub0',
     'dnabound_Foxo1_Pa0_Pd1_pUb0': 'dnabound_foxo1_pa0_pd1_pub0',
     'cytoplasm_Foxo1_Pa0_Pd1_pUb1': 'cytoplasm_foxo1_pa0_pd1_pub1',
     'nucleus_Foxo1_Pa0_Pd1_pUb1': 'nucleus_foxo1_pa0_pd1_pub1',
     'dnabound_Foxo1_Pa0_Pd1_pUb1': 'dnabound_foxo1_pa0_pd1_pub1',
     'cytoplasm_Foxo1_Pa1_Pd0_pUb0': 'cytoplasm_foxo1_pa1_pd0_pub0',
     'nucleus_Foxo1_Pa1_Pd0_pUb0': 'nucleus_foxo1_pa1_pd0_pub0',
     'dnabound_Foxo1_Pa1_Pd0_pUb0': 'dnabound_foxo1_pa1_pd0_pub0',
     'cytoplasm_Foxo1_Pa1_Pd0_pUb1': 'cytoplasm_foxo1_pa1_pd0_pub1',
     'nucleus_Foxo1_Pa1_Pd0_pUb1': 'nucleus_foxo1_pa1_pd0_pub1',
     'dnabound_Foxo1_Pa1_Pd0_pUb1': 'dnabound_foxo1_pa1_pd0_pub1',
     'cytoplasm_Foxo1_Pa1_Pd1_pUb0': 'cytoplasm_foxo1_pa1_pd1_pub0',
     'nucleus_Foxo1_Pa1_Pd1_pUb0': 'nucleus_foxo1_pa1_pd1_pub0',
     'dnabound_Foxo1_Pa1_Pd1_pUb0': 'dnabound_foxo1_pa1_pd1_pub0',
     'cytoplasm_Foxo1_Pa1_Pd1_pUb1': 'cytoplasm_foxo1_pa1_pd1_pub1',
     'nucleus_Foxo1_Pa1_Pd1_pUb1': 'nucleus_foxo1_pa1_pd1_pub1',
     'dnabound_Foxo1_Pa1_Pd1_pUb1': 'dnabound_foxo1_pa1_pd1_pub1',
     'Foxo1_Pa0_tot': 'foxo1_pa0_tot',
     'Foxo1_Pa1_tot': 'foxo1_pa1_tot',
     'Foxo1_Pd0_tot': 'foxo1_pd0_tot',
     'Foxo1_Pd1_tot': 'foxo1_pd1_tot',
     'Foxo1_pUb0_tot': 'foxo1_pub0_tot',
     'Foxo1_pUb1_tot': 'foxo1_pub1_tot',
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
     'Proteasome': 'proteasome'}

    def __init__(self, model_path: str = 'data/MODEL1112260002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smith2010FoxoPtmsAgeingrelatedsignallingpathwModel1112260002Model = Smith2010FoxoPtmsAgeingrelatedsignallingpathwModel
