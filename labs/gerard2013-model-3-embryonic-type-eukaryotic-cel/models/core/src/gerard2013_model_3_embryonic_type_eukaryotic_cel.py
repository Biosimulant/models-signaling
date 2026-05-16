# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gerard2013 - Model 3 - Embryonic-type eukaryotic Cell Cycle regulation based on negative feedback between Cdk/cyclin and APC and competitive inhibition between Cdk/cyclin and securin for polyubiquitylation_1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gerard2013Model3EmbryonicTypeEukaryoticCelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000938'
    _TITLE = 'Gerard2013 - Model 3 - Embryonic-type eukaryotic Cell Cycle regulation based on negative feedback between Cdk/cyclin and APC and competitive inhibition between Cdk/cyclin and securin for polyubiquitylation_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'anaphase_promoting_complex_phosphorylated': ('Anaphase_promoting_complex_Phosphorylated',
                                                   'native SBML value',
                                                   'Anaphase Promoting Complex Phosphorylated. Maps to '
                                                   'SBML symbol '
                                                   '`Anaphase_promoting_complex_Phosphorylated` and is '
                                                   'emitted in native SBML units.'),
     'anaphase_promoting_complex': ('Anaphase_promoting_complex',
                                    'native SBML value',
                                    'Anaphase Promoting Complex. Maps to SBML symbol '
                                    '`Anaphase_promoting_complex` and is emitted in native SBML '
                                    'units.'),
     'anaphase_promoting_complex_total': ('Anaphase_promoting_complex_total',
                                          'native SBML value',
                                          'Anaphase Promoting Complex Total. Maps to SBML symbol '
                                          '`Anaphase_promoting_complex_total` and is emitted in native '
                                          'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_anaphase_promoting_complex': ('Anaphase_promoting_complex',
                                            1.0,
                                            'native SBML value',
                                            'Initial level of Anaphase Promoting Complex. Maps to SBML '
                                            'symbol `Anaphase_promoting_complex`; exposed as a '
                                            'traceable initial-condition perturbation.'),
     'initial_anaphase_promoting_complex_total': ('Anaphase_promoting_complex_total',
                                                  1.0,
                                                  'native SBML value',
                                                  'Initial level of Anaphase Promoting Complex Total. '
                                                  'Maps to SBML symbol '
                                                  '`Anaphase_promoting_complex_total`; exposed as a '
                                                  'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Cdk': 'source-defined CDK state',
     'Anaphase_promoting_complex_Phosphorylated': 'Anaphase Promoting Complex Phosphorylated',
     'Securin': 'Securin',
     'Anaphase_promoting_complex': 'Anaphase Promoting Complex',
     'Anaphase_promoting_complex_total': 'Anaphase Promoting Complex Total'}
    _STATE_OUTPUT_ALIASES = {'Cdk': 'source_defined_cdk_state',
     'Anaphase_promoting_complex_Phosphorylated': 'anaphase_promoting_complex_phosphorylated',
     'Securin': 'securin',
     'Anaphase_promoting_complex': 'anaphase_promoting_complex',
     'Anaphase_promoting_complex_total': 'anaphase_promoting_complex_total'}

    def __init__(self, model_path: str = 'data/BIOMD0000000938.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gerard2013Model3EmbryonicTypeEukaryoticCelBiomd0000000938Model = Gerard2013Model3EmbryonicTypeEukaryoticCelModel
