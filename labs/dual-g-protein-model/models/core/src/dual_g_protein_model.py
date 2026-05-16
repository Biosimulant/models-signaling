# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dual G protein Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class DualGProteinModelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2306210001'
    _TITLE = 'Dual G protein Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'inactive_ligand_receptor_complex': ('LRi',
                                          'substance',
                                          'inactive ligand-receptor complex. Maps to SBML symbol `LRi` '
                                          'and is emitted in native SBML units.'),
     'active_ligand_receptor_complex': ('LRa',
                                        'substance',
                                        'active ligand-receptor complex. Maps to SBML symbol `LRa` and '
                                        'is emitted in native SBML units.'),
     'source_defined_rig1_state': ('RiG1',
                                   'substance',
                                   'source-defined RIG1 state. Maps to SBML symbol `RiG1` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_ligand_conc_added_level': ('LigandConcAdded',
                                         1e-06,
                                         'native SBML value',
                                         'Ligand Conc Added source parameter. Maps to SBML symbol '
                                         '`LigandConcAdded` and preserves the bundled default.')}
    _SPECIES_LABELS = {'L': 'source-defined L state',
     'LRi': 'inactive ligand-receptor complex',
     'Ri': 'source-defined RI state',
     'Ra': 'source-defined RA state',
     'LRa': 'active ligand-receptor complex',
     'G1': 'source-defined G1 state',
     'RiG1': 'source-defined RIG1 state',
     'LRiG1': 'source-defined LRIG1 state',
     'RaG1': 'source-defined RAG1 state',
     'LRaG1': 'source-defined LRAG1 state',
     'G2': 'source-defined G2 state',
     'RiG2': 'source-defined RIG2 state',
     'LRiG2': 'source-defined LRIG2 state',
     'RaG2': 'source-defined RAG2 state',
     'LRaG2': 'source-defined LRAG2 state',
     'G1aGTP': 'G1a GTP',
     'Gbg': 'G beta-gamma complex',
     'G2aGTP': 'G2a GTP',
     'G1aGDP': 'G1a GDP',
     'G2aGDP': 'G2a GDP'}
    _STATE_OUTPUT_ALIASES = {'L': 'source_defined_l_state',
     'LRi': 'inactive_ligand_receptor_complex',
     'Ri': 'source_defined_ri_state',
     'Ra': 'source_defined_ra_state',
     'LRa': 'active_ligand_receptor_complex',
     'G1': 'source_defined_g1_state',
     'RiG1': 'source_defined_rig1_state',
     'LRiG1': 'source_defined_lrig1_state',
     'RaG1': 'source_defined_rag1_state',
     'LRaG1': 'source_defined_lrag1_state',
     'G2': 'source_defined_g2_state',
     'RiG2': 'source_defined_rig2_state',
     'LRiG2': 'source_defined_lrig2_state',
     'RaG2': 'source_defined_rag2_state',
     'LRaG2': 'source_defined_lrag2_state',
     'G1aGTP': 'g1a_gtp',
     'Gbg': 'g_beta_gamma_complex',
     'G2aGTP': 'g2a_gtp',
     'G1aGDP': 'g1a_gdp',
     'G2aGDP': 'g2a_gdp'}

    def __init__(self, model_path: str = 'data/MODEL2306210001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


DualGProteinModelModel2306210001Model = DualGProteinModelModel
