# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kolodkin2013 - Nuclear receptor-mediated cortisol signalling network."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kolodkin2013NuclearReceptorMediatedCortisolModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000576'
    _TITLE = 'Kolodkin2013 - Nuclear receptor-mediated cortisol signalling network'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_s_rna_state': ('s28',
                                    'native SBML value',
                                    'source-defined S_RNA state. Maps to SBML symbol `s28` and is '
                                    'emitted in native SBML units.'),
     's_prot': ('s36',
                'native SBML value',
                'S PROT. Maps to SBML symbol `s36` and is emitted in native SBML units.'),
     'pxr_gene': ('s46',
                  'native SBML value',
                  'PXR GENE. Maps to SBML symbol `s46` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cort_degr': ('s10',
                           0.0,
                           'native SBML value',
                           'Initial level of Cort Degr. Maps to SBML symbol `s10`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_cort_added': ('CortAdded',
                            0.0,
                            'native SBML value',
                            'Initial level of Cort Added. Maps to SBML symbol `CortAdded`; exposed as '
                            'a traceable initial-condition perturbation.'),
     'initial_cortisone': ('Cortisone',
                           24.0000071336767,
                           'native SBML value',
                           'Initial level of Cortisone. Maps to SBML symbol `Cortisone`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s28': 'source-defined S_RNA state',
     's36': 'S PROT',
     's46': 'PXR GENE',
     's32': 'PXR RNA',
     's42': 'PXR PROT',
     's30': 'Abstract source state S30',
     's40': 'GR GENE',
     's33': 'GR RNA',
     's39': 'GR PROT',
     's114': 'source-defined CORT state',
     's155': 'CYP GENE',
     's172': 'CYP PROT',
     's173': 'CYP RNA',
     's185': 'TAT RNA',
     's84': 'Grgene Grprot Cort',
     's165': 'Cypgene Pxrprot Cort',
     's109': 'Pxrgene Grprot Cort',
     's87': 'Grprot Cort',
     's119': 'Pxrprot Cort',
     's183': 'Tatgene Grprot Cort',
     's178': 'TAT GENE',
     's10': 'Cort Degr',
     'Cortisone': 'Cortisone',
     'TAT_PROT': 'TAT PROT',
     'Ligand2': 'Ligand2',
     'PXRprot_Ligand2': 'Pxrprot Ligand2',
     'CYPgene_PXRprot_Ligand2': 'Cypgene Pxrprot Ligand2',
     'DEX': 'source-defined DEX state',
     'GRprot_DEX': 'Grprot DEX',
     'PXRprot_DEX': 'Pxrprot DEX',
     'DEX_degr': 'DEX Degr',
     'CYPgene_PXRprot_DEX': 'Cypgene Pxrprot DEX',
     'PXRgene_GRprot_DEX': 'Pxrgene Grprot DEX',
     'GRgene_GRprot_DEX': 'Grgene Grprot DEX',
     'TATgene_GRprot_DEX': 'Tatgene Grprot DEX',
     's2': 'Cort OUT',
     'DEXout': 'Dexout',
     'CBG': 'source-defined CBG state',
     'CBG_CortOUT': 'CBG Cort OUT',
     'Alb': 'source-defined ALB state',
     'Alb_CortOUT': 'Alb Cort OUT',
     'CortAdded': 'Cort Added'}
    _STATE_OUTPUT_ALIASES = {'s28': 'source_defined_s_rna_state',
     's36': 's_prot',
     's46': 'pxr_gene',
     's32': 'pxr_rna',
     's42': 'pxr_prot',
     's30': 'abstract_source_state_s30',
     's40': 'gr_gene',
     's33': 'gr_rna',
     's39': 'gr_prot',
     's114': 'source_defined_cort_state',
     's155': 'cyp_gene',
     's172': 'cyp_prot',
     's173': 'cyp_rna',
     's185': 'tat_rna',
     's84': 'grgene_grprot_cort',
     's165': 'cypgene_pxrprot_cort',
     's109': 'pxrgene_grprot_cort',
     's87': 'grprot_cort',
     's119': 'pxrprot_cort',
     's183': 'tatgene_grprot_cort',
     's178': 'tat_gene',
     's10': 'cort_degr',
     'Cortisone': 'cortisone',
     'TAT_PROT': 'tat_prot',
     'Ligand2': 'ligand2',
     'PXRprot_Ligand2': 'pxrprot_ligand2',
     'CYPgene_PXRprot_Ligand2': 'cypgene_pxrprot_ligand2',
     'DEX': 'source_defined_dex_state',
     'GRprot_DEX': 'grprot_dex',
     'PXRprot_DEX': 'pxrprot_dex',
     'DEX_degr': 'dex_degr',
     'CYPgene_PXRprot_DEX': 'cypgene_pxrprot_dex',
     'PXRgene_GRprot_DEX': 'pxrgene_grprot_dex',
     'GRgene_GRprot_DEX': 'grgene_grprot_dex',
     'TATgene_GRprot_DEX': 'tatgene_grprot_dex',
     's2': 'cort_out',
     'DEXout': 'dexout',
     'CBG': 'source_defined_cbg_state',
     'CBG_CortOUT': 'cbg_cort_out',
     'Alb': 'source_defined_alb_state',
     'Alb_CortOUT': 'alb_cort_out',
     'CortAdded': 'cort_added'}

    def __init__(self, model_path: str = 'data/BIOMD0000000576.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kolodkin2013NuclearReceptorMediatedCortisolBiomd0000000576Model = Kolodkin2013NuclearReceptorMediatedCortisolModel
