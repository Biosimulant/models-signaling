# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Smith2009 - RGS mediated GTP hydrolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2009RgsMediatedGtpHydrolysisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000439'
    _TITLE = 'Smith2009 - RGS mediated GTP hydrolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_gabg_state': ('Gabg',
                                   'nanomole',
                                   'source-defined GABG state. Maps to SBML symbol `Gabg` and is '
                                   'emitted in native SBML units.'),
     'rgabg': ('RGabg',
               'nanomole',
               'Rgabg. Maps to SBML symbol `RGabg` and is emitted in native SBML units.'),
     'rgabg_l': ('RGabgL',
                 'nanomole',
                 'Rgabg L. Maps to SBML symbol `RGabgL` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_ligand_conc_level': ('Ligand_conc',
                                   0.1,
                                   'nanoMolar',
                                   'Ligand Conc source parameter. Maps to SBML symbol `Ligand_conc` '
                                   'and preserves the bundled default.')}
    _SPECIES_LABELS = {'R': 'source-defined R state',
     'L': 'source-defined L state',
     'RL': 'source-defined RL state',
     'Gabg': 'source-defined GABG state',
     'RGabg': 'Rgabg',
     'RGabgL': 'Rgabg L',
     'GaGTP': 'Ga GTP',
     'Gbg': 'G beta-gamma complex',
     'RGS': 'source-defined RGS state',
     'RGSGaGTP': 'Rgsga GTP',
     'GaGDPP': 'Ga GDPP',
     'Effector': 'Effector',
     'GaGTPEffector': 'Ga Gtpeffector',
     'inertGaGTP': 'Inert Ga GTP',
     'RGSinertGaGTP': 'Rgsinert Ga GTP',
     'GaGDP': 'Ga GDP',
     'P': 'source-defined P state',
     'z1': 'source-defined Z1 state',
     'z2': 'source-defined Z2 state',
     'z3': 'source-defined Z3 state'}
    _STATE_OUTPUT_ALIASES = {'R': 'source_defined_r_state',
     'L': 'source_defined_l_state',
     'RL': 'source_defined_rl_state',
     'Gabg': 'source_defined_gabg_state',
     'RGabg': 'rgabg',
     'RGabgL': 'rgabg_l',
     'GaGTP': 'ga_gtp',
     'Gbg': 'g_beta_gamma_complex',
     'RGS': 'source_defined_rgs_state',
     'RGSGaGTP': 'rgsga_gtp',
     'GaGDPP': 'ga_gdpp',
     'Effector': 'effector',
     'GaGTPEffector': 'ga_gtpeffector',
     'inertGaGTP': 'inert_ga_gtp',
     'RGSinertGaGTP': 'rgsinert_ga_gtp',
     'GaGDP': 'ga_gdp',
     'P': 'source_defined_p_state',
     'z1': 'source_defined_z1_state',
     'z2': 'source_defined_z2_state',
     'z3': 'source_defined_z3_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000439.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smith2009RgsMediatedGtpHydrolysisBiomd0000000439Model = Smith2009RgsMediatedGtpHydrolysisModel
