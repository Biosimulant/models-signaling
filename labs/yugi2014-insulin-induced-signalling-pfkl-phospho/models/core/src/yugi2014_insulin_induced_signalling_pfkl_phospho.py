# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yugi2014 - Insulin induced signalling (PFKL phosphorylation) - model 1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yugi2014InsulinInducedSignallingPfklPhosphoModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000540'
    _TITLE = 'Yugi2014 - Insulin induced signalling (PFKL phosphorylation) - model 1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_pfkl_state': ('s1',
                                   'native SBML value',
                                   'source-defined PFKL state. Maps to SBML symbol `s1` and is emitted '
                                   'in native SBML units.'),
     'fbpase': ('s2',
                'native SBML value',
                'Fbpase. Maps to SBML symbol `s2` and is emitted in native SBML units.'),
     'f6p': ('s3',
             'native SBML value',
             'F6P. Maps to SBML symbol `s3` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_f6p_proxy': ('s22',
                           14.0774258421,
                           'substance',
                           'Initial level of F6P Proxy. Maps to SBML symbol `s22`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s1': 'source-defined PFKL state',
     's2': 'Fbpase',
     's3': 'F6P',
     's4': 'F1 6BP',
     's5': 'source-defined PEP state',
     's6': 'Isocitrate',
     's7': '2 Oxoglutarate',
     's8': 'Malate',
     's9': 'F2 6BP',
     's10': 'Citrate',
     's12': 'source-defined ALDO state',
     's13': 'P PFKL',
     's22': 'F6P Proxy'}
    _STATE_OUTPUT_ALIASES = {'s1': 'source_defined_pfkl_state',
     's2': 'fbpase',
     's3': 'f6p',
     's4': 'f1_6bp',
     's5': 'source_defined_pep_state',
     's6': 'isocitrate',
     's7': 'source_2_oxoglutarate',
     's8': 'malate',
     's9': 'f2_6bp',
     's10': 'citrate',
     's12': 'source_defined_aldo_state',
     's13': 'p_pfkl',
     's22': 'f6p_proxy'}

    def __init__(self, model_path: str = 'data/BIOMD0000000540.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Yugi2014InsulinInducedSignallingPfklPhosphoBiomd0000000540Model = Yugi2014InsulinInducedSignallingPfklPhosphoModel
