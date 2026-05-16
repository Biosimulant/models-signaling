# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Pinto2022 - Hybrid SBML/ANN model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pinto2022HybridSbmlAnnModelModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2207280001'
    _TITLE = 'Pinto2022 - Hybrid SBML/ANN model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'adp': ('adp',
             'native SBML value',
             'ADP. Maps to SBML symbol `adp` and is emitted in native SBML units.'),
     'source_defined_asa_state': ('asa',
                                  'native SBML value',
                                  'Source Defined ASA State. Maps to SBML symbol `asa` and is emitted '
                                  'in native SBML units.'),
     'aspartate_ligand': ('asp',
                          'native SBML value',
                          'Aspartate Ligand. Maps to SBML symbol `asp` and is emitted in native SBML '
                          'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('adp',
                     0.0,
                     'native SBML value',
                     'Initial level of ADP. Maps to SBML symbol `adp`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'adp': 'ADP',
     'asa': 'Source Defined ASA State',
     'asp': 'Aspartate Ligand',
     'aspp': 'Source Defined ASPP State',
     'atp': 'ATP',
     'hs': 'Source Defined HS State',
     'hsp': 'Source Defined HSP State',
     'nadp': 'Source Defined nuclear ADP State',
     'nadph': 'Nadph',
     'phos': 'Source Defined PHOS State',
     'thr': 'Source Defined THR State'}
    _STATE_OUTPUT_ALIASES = {'adp': 'adp',
     'asa': 'source_defined_asa_state',
     'asp': 'aspartate_ligand',
     'aspp': 'source_defined_aspp_state',
     'atp': 'atp',
     'hs': 'source_defined_hs_state',
     'hsp': 'source_defined_hsp_state',
     'nadp': 'source_defined_nuclear_adp_state',
     'nadph': 'nadph',
     'phos': 'source_defined_phos_state',
     'thr': 'source_defined_thr_state'}

    def __init__(self, model_path: str = 'data/MODEL2207280001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Pinto2022HybridSbmlAnnModelModel2207280001Model = Pinto2022HybridSbmlAnnModelModel
