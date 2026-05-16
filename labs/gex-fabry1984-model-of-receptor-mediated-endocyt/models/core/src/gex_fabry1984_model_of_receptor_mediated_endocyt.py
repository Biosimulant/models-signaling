# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gex-Fabry1984 - model of receptor-mediated endocytosis of EGF in BALB/c 3T3 cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GexFabry1984ModelOfReceptorMediatedEndocytModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000985'
    _TITLE = 'Gex-Fabry1984 - model of receptor-mediated endocytosis of EGF in BALB/c 3T3 cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'surface_receptor_external': ('Surface_Receptor_External',
                                   'substance',
                                   'Surface Receptor External. Maps to SBML symbol '
                                   '`Surface_Receptor_External` and is emitted in native SBML units.'),
     'receptor_ligand_complex': ('Receptor_Ligand_Complex',
                                 'substance',
                                 'Receptor Ligand Complex. Maps to SBML symbol '
                                 '`Receptor_Ligand_Complex` and is emitted in native SBML units.'),
     'internalised_receptors': ('Internalised_receptors',
                                'substance',
                                'Internalised Receptors. Maps to SBML symbol `Internalised_receptors` '
                                'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_internalised_ligand': ('Internalised_Ligand',
                                     0.0,
                                     'substance',
                                     'Initial level of Internalised Ligand. Maps to SBML symbol '
                                     '`Internalised_Ligand`; exposed as a traceable initial-condition '
                                     'perturbation.'),
     'initial_ligand_egf': ('Ligand_EGF',
                            198730648281000.0,
                            'substance',
                            'Initial level of Ligand EGF. Maps to SBML symbol `Ligand_EGF`; exposed as '
                            'a traceable initial-condition perturbation.'),
     'initial_receptor_ligand_complex': ('Receptor_Ligand_Complex',
                                         0.0,
                                         'substance',
                                         'Initial level of Receptor Ligand Complex. Maps to SBML '
                                         'symbol `Receptor_Ligand_Complex`; exposed as a traceable '
                                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Ligand_EGF': 'Ligand EGF',
     'Surface_Receptor_External': 'Surface Receptor External',
     'Receptor_Ligand_Complex': 'Receptor Ligand Complex',
     'Internalised_receptors': 'Internalised Receptors',
     'Receptor_Ligand_Pit_Protein_complex': 'Receptor Ligand Pit Protein Complex',
     'Free_pit_proteins': 'free Pit Proteins',
     'Internalised_Ligand': 'Internalised Ligand'}
    _STATE_OUTPUT_ALIASES = {'Ligand_EGF': 'ligand_egf',
     'Surface_Receptor_External': 'surface_receptor_external',
     'Receptor_Ligand_Complex': 'receptor_ligand_complex',
     'Internalised_receptors': 'internalised_receptors',
     'Receptor_Ligand_Pit_Protein_complex': 'receptor_ligand_pit_protein_complex',
     'Free_pit_proteins': 'free_pit_proteins',
     'Internalised_Ligand': 'internalised_ligand'}

    def __init__(self, model_path: str = 'data/BIOMD0000000985.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


GexFabry1984ModelOfReceptorMediatedEndocytBiomd0000000985Model = GexFabry1984ModelOfReceptorMediatedEndocytModel
