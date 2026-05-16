# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Scaramellini1997 - Two-receptor:One-transducer (2R1T) model for analysis of interactions between agonists."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Scaramellini1997TwoReceptorOneTransducer2r1Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000001008'
    _TITLE = 'Scaramellini1997 - Two-receptor:One-transducer (2R1T) model for analysis of interactions between agonists'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mediator_a1': ('Mediator_A1',
                     'native SBML value',
                     'Mediator A1. Maps to SBML symbol `Mediator_A1` and is emitted in native SBML '
                     'units.'),
     'mediator_a2': ('Mediator_A2',
                     'native SBML value',
                     'Mediator A2. Maps to SBML symbol `Mediator_A2` and is emitted in native SBML '
                     'units.'),
     'agonist_1': ('Agonist_1',
                   'native SBML value',
                   'Agonist 1. Maps to SBML symbol `Agonist_1` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_effect': ('Effect',
                        9.55128864177634,
                        'native SBML value',
                        'Initial level of Effect. Maps to SBML symbol `Effect`; exposed as a traceable '
                        'initial-condition perturbation.'),
     'initial_mediator_a1': ('Mediator_A1',
                             0.000999999999,
                             'native SBML value',
                             'Initial level of Mediator A1. Maps to SBML symbol `Mediator_A1`; exposed '
                             'as a traceable initial-condition perturbation.'),
     'initial_mediator_a2': ('Mediator_A2',
                             9.999999999e-05,
                             'native SBML value',
                             'Initial level of Mediator A2. Maps to SBML symbol `Mediator_A2`; exposed '
                             'as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Mediator_A1': 'Mediator A1',
     'Mediator_A2': 'Mediator A2',
     'Agonist_1': 'Agonist 1',
     'Agonist_2': 'Agonist 2',
     'Effect': 'Effect'}
    _STATE_OUTPUT_ALIASES = {'Mediator_A1': 'mediator_a1',
     'Mediator_A2': 'mediator_a2',
     'Agonist_1': 'agonist_1',
     'Agonist_2': 'agonist_2',
     'Effect': 'effect'}

    def __init__(self, model_path: str = 'data/BIOMD0000001008.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Scaramellini1997TwoReceptorOneTransducer2r1Biomd0000001008Model = Scaramellini1997TwoReceptorOneTransducer2r1Model
