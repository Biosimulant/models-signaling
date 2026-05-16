# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yugi2014 - Insulin induced signalling (PFKL phosphorylation) - model 2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yugi2014InsulinInducedSignallingPfklPhosphoBiomd0000000541Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000541'
    _TITLE = 'Yugi2014 - Insulin induced signalling (PFKL phosphorylation) - model 2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'insulin_receptor_complex': ('s23',
                                  'native SBML value',
                                  'insulin receptor Complex. Maps to SBML symbol `s23` and is emitted '
                                  'in native SBML units.'),
     'pro_insulin_receptor_complex': ('s24',
                                      'native SBML value',
                                      'Pro insulin receptor Complex. Maps to SBML symbol `s24` and is '
                                      'emitted in native SBML units.'),
     'p1ir_complex': ('s25',
                      'native SBML value',
                      'P1ir Complex. Maps to SBML symbol `s25` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_akt': ('s28',
                     4.33812187331668,
                     'native SBML value',
                     'Initial level of AKT. Maps to SBML symbol `s28`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_f6p_proxy': ('s22',
                           14.0774258421,
                           'substance',
                           'Initial level of F6P Proxy. Maps to SBML symbol `s22`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_abstract_source_state_s34': ('s34',
                                           14.9913345914433,
                                           'native SBML value',
                                           'Initial level of Abstract source state S34. Maps to SBML '
                                           'symbol `s34`; exposed as a traceable initial-condition '
                                           'perturbation.')}
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
     's23': 'insulin receptor Complex',
     's24': 'Pro insulin receptor Complex',
     's25': 'P1ir Complex',
     's26': 'P2ir Complex',
     's27': 'P1p2ircomplex',
     's28': 'AKT',
     's29': 'source-defined PAKT state',
     's30': 'mTOR',
     's31': 'Pm TOR',
     's32': 'S6K',
     's33': 'P S6K',
     's34': 'Abstract source state S34',
     's35': 'source-defined PX state',
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
     's23': 'insulin_receptor_complex',
     's24': 'pro_insulin_receptor_complex',
     's25': 'p1ir_complex',
     's26': 'p2ir_complex',
     's27': 'p1p2ircomplex',
     's28': 'akt',
     's29': 'source_defined_pakt_state',
     's30': 'mtor',
     's31': 'pm_tor',
     's32': 's6k',
     's33': 'p_s6k',
     's34': 'abstract_source_state_s34',
     's35': 'source_defined_px_state',
     's22': 'f6p_proxy'}

    def __init__(self, model_path: str = 'data/BIOMD0000000541.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Yugi2014InsulinInducedSignallingPfklPhosphoBiomd0000000541Model = Yugi2014InsulinInducedSignallingPfklPhosphoBiomd0000000541Model
