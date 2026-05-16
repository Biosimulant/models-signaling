# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bush2016 - Extended Carrousel model of GPCR-RGS."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bush2016ExtendedCarrouselModelOfGpcrRgsModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000638'
    _TITLE = 'Bush2016 - Extended Carrousel model of GPCR-RGS'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'g_beta_gamma_complex': ('Gbg',
                              'substance',
                              'G beta-gamma complex. Maps to SBML symbol `Gbg` and is emitted in '
                              'native SBML units.'),
     'source_defined_lrg_state': ('LRG',
                                  'substance',
                                  'source-defined LRG state. Maps to SBML symbol `LRG` and is emitted '
                                  'in native SBML units.'),
     'ligand_receptor_gtp_complex': ('LRGt',
                                     'substance',
                                     'ligand-receptor GTP complex. Maps to SBML symbol `LRGt` and is '
                                     'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_r_state': ('R',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined R state. Maps to SBML symbol '
                                        '`R`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'R': 'source-defined R state',
     'LR': 'source-defined LR state',
     'G': 'source-defined G state',
     'Gt': 'source-defined GT state',
     'Gd': 'source-defined GD state',
     'RG': 'source-defined RG state',
     'Gbg': 'G beta-gamma complex',
     'LRG': 'source-defined LRG state',
     'LRGt': 'ligand-receptor GTP complex',
     'RGd': 'source-defined RGD state',
     'RGt': 'source-defined RGT state',
     'LRGd': 'source-defined LRGD state',
     'LRrgs': 'Lrrgs',
     'LRrgsG': 'Lrrgs G',
     'LRrgsGd': 'Lrrgs Gd',
     'LRrgsGt': 'Lrrgs Gt',
     'Rrgs': 'source-defined RRGS state',
     'RrgsG': 'Rrgs G',
     'RrgsGd': 'Rrgs Gd',
     'RrgsGt': 'Rrgs Gt',
     'rgs': 'source-defined RGS state'}
    _STATE_OUTPUT_ALIASES = {'R': 'source_defined_r_state',
     'LR': 'source_defined_lr_state',
     'G': 'source_defined_g_state',
     'Gt': 'source_defined_gt_state',
     'Gd': 'source_defined_gd_state',
     'RG': 'source_defined_rg_state',
     'Gbg': 'g_beta_gamma_complex',
     'LRG': 'source_defined_lrg_state',
     'LRGt': 'ligand_receptor_gtp_complex',
     'RGd': 'source_defined_rgd_state',
     'RGt': 'source_defined_rgt_state',
     'LRGd': 'source_defined_lrgd_state',
     'LRrgs': 'lrrgs',
     'LRrgsG': 'lrrgs_g',
     'LRrgsGd': 'lrrgs_gd',
     'LRrgsGt': 'lrrgs_gt',
     'Rrgs': 'source_defined_rrgs_state',
     'RrgsG': 'rrgs_g',
     'RrgsGd': 'rrgs_gd',
     'RrgsGt': 'rrgs_gt',
     'rgs': 'source_defined_rgs_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000638.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bush2016ExtendedCarrouselModelOfGpcrRgsBiomd0000000638Model = Bush2016ExtendedCarrouselModelOfGpcrRgsModel
