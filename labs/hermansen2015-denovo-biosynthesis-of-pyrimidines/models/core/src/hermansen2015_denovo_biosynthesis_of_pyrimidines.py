# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hermansen2015 - denovo biosynthesis of pyrimidines in yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hermansen2015DenovoBiosynthesisOfPyrimidinesModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000590'
    _TITLE = 'Hermansen2015 - denovo biosynthesis of pyrimidines in yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'calcium': ('ca',
                 'native SBML value',
                 'calcium. Maps to SBML symbol `ca` and is emitted in native SBML units.'),
     'dihydroorotate': ('dho',
                        'native SBML value',
                        'dihydroorotate. Maps to SBML symbol `dho` and is emitted in native SBML '
                        'units.'),
     'orotate': ('oro',
                 'native SBML value',
                 'orotate. Maps to SBML symbol `oro` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_cp_state': ('cp',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined CP state. Maps to SBML '
                                         'symbol `cp`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'cp': 'source-defined CP state',
     'ca': 'calcium',
     'dho': 'dihydroorotate',
     'oro': 'orotate',
     'omp': 'source-defined OMP state',
     'ump': 'source-defined UMP state',
     'udp': 'source-defined UDP state',
     'utp': 'source-defined UTP state',
     'ctp': 'source-defined CTP state'}
    _STATE_OUTPUT_ALIASES = {'cp': 'source_defined_cp_state',
     'ca': 'calcium',
     'dho': 'dihydroorotate',
     'oro': 'orotate',
     'omp': 'source_defined_omp_state',
     'ump': 'source_defined_ump_state',
     'udp': 'source_defined_udp_state',
     'utp': 'source_defined_utp_state',
     'ctp': 'source_defined_ctp_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000590.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hermansen2015DenovoBiosynthesisOfPyrimidinesBiomd0000000590Model = Hermansen2015DenovoBiosynthesisOfPyrimidinesModel
