# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bray1993_chemotaxis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bray1993ChemotaxisModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000404'
    _TITLE = 'Bray1993_chemotaxis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'aspartate_ligand': ('asp',
                          'native SBML value',
                          'aspartate ligand. Maps to SBML symbol `asp` and is emitted in native SBML '
                          'units.'),
     'total_aspartate_bound_receptor': ('Tasp',
                                        'native SBML value',
                                        'total aspartate-bound receptor. Maps to SBML symbol `Tasp` '
                                        'and is emitted in native SBML units.'),
     'total_inactive_receptor_state_ni': ('Tni',
                                          'native SBML value',
                                          'total inactive receptor state Ni. Maps to SBML symbol `Tni` '
                                          'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_aspartate_ligand': ('asp',
                                  0.0,
                                  'native SBML value',
                                  'Initial level of aspartate ligand. Maps to SBML symbol `asp`; '
                                  'exposed as a traceable initial-condition perturbation.'),
     'initial_atp': ('species_1',
                     0.1,
                     'native SBML value',
                     'Initial level of ATP. Maps to SBML symbol `species_1`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_source_defined_ni_state': ('ni',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined NI state. Maps to SBML '
                                         'symbol `ni`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'asp': 'aspartate ligand',
     'ni': 'source-defined NI state',
     'T': 'source-defined T state',
     'Tasp': 'total aspartate-bound receptor',
     'Tni': 'total inactive receptor state Ni',
     'W': 'source-defined W state',
     'TW': 'source-defined TW state',
     'Tasp_W': 'total aspartate-bound receptor W',
     'Tni_W': 'source-defined TNI_W state',
     'TA': 'source-defined TA state',
     'Tasp_A': 'total aspartate-bound receptor A',
     'Tni_A': 'source-defined TNI_A state',
     'WA': 'source-defined WA state',
     'TWA': 'source-defined TWA state',
     'Tasp_WA': 'total aspartate-bound receptor WA',
     'Tni_WA': 'total inactive receptor state Ni WA',
     'A': 'source-defined A state',
     'Ap': 'source-defined AP state',
     'B': 'source-defined B state',
     'Bp': 'source-defined BP state',
     'Z': 'source-defined Z state',
     'Y': 'source-defined Y state',
     'Yp': 'source-defined YP state',
     'M': 'source-defined M state',
     'MYp': 'source-defined MYP state',
     'MYpYp': 'Myp Yp',
     'MYpYpYp': 'Myp Yp Yp',
     'MYpYpYpYp': 'Myp Yp Yp Yp',
     'species_1': 'ATP'}
    _STATE_OUTPUT_ALIASES = {'asp': 'aspartate_ligand',
     'ni': 'source_defined_ni_state',
     'T': 'source_defined_t_state',
     'Tasp': 'total_aspartate_bound_receptor',
     'Tni': 'total_inactive_receptor_state_ni',
     'W': 'source_defined_w_state',
     'TW': 'source_defined_tw_state',
     'Tasp_W': 'total_aspartate_bound_receptor_w',
     'Tni_W': 'source_defined_tni_w_state',
     'TA': 'source_defined_ta_state',
     'Tasp_A': 'total_aspartate_bound_receptor_a',
     'Tni_A': 'source_defined_tni_a_state',
     'WA': 'source_defined_wa_state',
     'TWA': 'source_defined_twa_state',
     'Tasp_WA': 'total_aspartate_bound_receptor_wa',
     'Tni_WA': 'total_inactive_receptor_state_ni_wa',
     'A': 'source_defined_a_state',
     'Ap': 'source_defined_ap_state',
     'B': 'source_defined_b_state',
     'Bp': 'source_defined_bp_state',
     'Z': 'source_defined_z_state',
     'Y': 'source_defined_y_state',
     'Yp': 'source_defined_yp_state',
     'M': 'source_defined_m_state',
     'MYp': 'source_defined_myp_state',
     'MYpYp': 'myp_yp',
     'MYpYpYp': 'myp_yp_yp',
     'MYpYpYpYp': 'myp_yp_yp_yp',
     'species_1': 'atp'}

    def __init__(self, model_path: str = 'data/BIOMD0000000404.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bray1993ChemotaxisBiomd0000000404Model = Bray1993ChemotaxisModel
