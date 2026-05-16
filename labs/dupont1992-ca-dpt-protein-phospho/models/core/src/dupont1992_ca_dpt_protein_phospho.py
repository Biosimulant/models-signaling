# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dupont1992_Ca_dpt_protein_phospho."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dupont1992CaDptProteinPhosphoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000113'
    _TITLE = 'Dupont1992_Ca_dpt_protein_phospho'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphorylated_protein': ('W_star',
                                'native SBML value',
                                'Phosphorylated Protein. Maps to SBML symbol `W_star` and is emitted '
                                'in native SBML units.'),
     'total_protein': ('Wt',
                       'native SBML value',
                       'Total Protein. Maps to SBML symbol `Wt` and is emitted in native SBML units.'),
     'source_defined_z_state': ('Z',
                                'native SBML value',
                                'Source Defined Z State. Maps to SBML symbol `Z` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_z_state': ('Z',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined Z state. Maps to SBML symbol '
                                        '`Z`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Z': 'Source Defined Z State',
     'Y': 'Source Defined Y State',
     'Wt': 'Total Protein',
     'W_star': 'Phosphorylated Protein'}
    _STATE_OUTPUT_ALIASES = {'Z': 'source_defined_z_state',
     'Y': 'source_defined_y_state',
     'Wt': 'total_protein',
     'W_star': 'phosphorylated_protein'}

    def __init__(self, model_path: str = 'data/BIOMD0000000113.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dupont1992CaDptProteinPhosphoBiomd0000000113Model = Dupont1992CaDptProteinPhosphoModel
