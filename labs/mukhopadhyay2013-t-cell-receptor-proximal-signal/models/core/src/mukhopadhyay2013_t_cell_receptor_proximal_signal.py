# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mukhopadhyay2013 - T cell receptor proximal signaling reveals emergent ultrasensitivity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mukhopadhyay2013TCellReceptorProximalSignalModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1604100000'
    _TITLE = 'Mukhopadhyay2013 - T cell receptor proximal signaling reveals emergent ultrasensitivity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'s_y1_u_y2_u_y3_u_b_0': ('S1',
                              'native SBML value',
                              'S Y1 U Y2 U Y3 U B 0. Maps to SBML symbol `S1` and is emitted in native '
                              'SBML units.'),
     'source_defined_e_b_state': ('S2',
                                  'native SBML value',
                                  'source-defined E(B) state. Maps to SBML symbol `S2` and is emitted '
                                  'in native SBML units.'),
     'source_defined_f_b_state': ('S3',
                                  'native SBML value',
                                  'source-defined F(B) state. Maps to SBML symbol `S3` and is emitted '
                                  'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_s_y1_u_y2_u_y3_u_b_0': ('S1',
                                      0.0,
                                      'native SBML value',
                                      'Initial level of S Y1 U Y2 U Y3 U B 0. Maps to SBML symbol '
                                      '`S1`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'S1': 'S Y1 U Y2 U Y3 U B 0',
     'S2': 'source-defined E(B) state',
     'S3': 'source-defined F(B) state',
     'S4': 'source-defined Z(B) state',
     'S5': 'E B 1 S Y1 U 1 Y2 U Y3 U B 1',
     'S6': 'S Y1 P Y2 U Y3 U B 0',
     'S7': 'F B 1 S Y1 P 1 Y2 U Y3 U B 1',
     'S8': 'E B 1 S Y1 P 1 Y2 U Y3 U B 1',
     'S9': 'S Y1 2P Y2 U Y3 U B 0',
     'S10': 'F B 1 S Y1 2P 1 Y2 U Y3 U B 1',
     'S11': 'E B 1 S Y1 2P Y2 U 1 Y3 U B 1',
     'S12': 'S Y1 2P 1 Y2 U Y3 U B 0 Z B 1',
     'S13': 'E B 1 S Y1 2P 2 Y2 U 1 Y3 U B 1 Z B 2',
     'S14': 'S Y1 2P Y2 P Y3 U B 0',
     'S15': 'S Y1 2P 1 Y2 P Y3 U B 0 Z B 1',
     'S16': 'F B 1 S Y1 2P Y2 P 1 Y3 U B 1',
     'S17': 'E B 1 S Y1 2P Y2 P 1 Y3 U B 1',
     'S18': 'F B 1 S Y1 2P 2 Y2 P 1 Y3 U B 1 Z B 2',
     'S19': 'E B 1 S Y1 2P 2 Y2 P 1 Y3 U B 1 Z B 2',
     'S20': 'S Y1 2P Y2 2P Y3 U B 0',
     'S21': 'S Y1 2P 1 Y2 2P Y3 U B 0 Z B 1',
     'S22': 'F B 1 S Y1 2P Y2 2P 1 Y3 U B 1',
     'S23': 'E B 1 S Y1 2P Y2 2P Y3 U 1 B 1',
     'S24': 'S Y1 2P Y2 2P 1 Y3 U B 0 Z B 1',
     'S25': 'F B 1 S Y1 2P 2 Y2 2P 1 Y3 U B 1 Z B 2',
     'S26': 'E B 1 S Y1 2P 2 Y2 2P Y3 U 1 B 1 Z B 2',
     'S27': 'E B 1 S Y1 2P Y2 2P 2 Y3 U 1 B 1 Z B 2',
     'S28': 'S Y1 2P Y2 2P Y3 P B 0',
     'S29': 'S Y1 2P 1 Y2 2P 2 Y3 U B 0 Z B 1 Z B 2',
     'S30': 'E B 1 S Y1 2P 2 Y2 2P 3 Y3 U 1 B 1 Z B 2 Z B 3',
     'S31': 'S Y1 2P 1 Y2 2P Y3 P B 0 Z B 1',
     'S32': 'S Y1 2P Y2 2P 1 Y3 P B 0 Z B 1',
     'S33': 'F B 1 S Y1 2P Y2 2P Y3 P 1 B 1',
     'S34': 'E B 1 S Y1 2P Y2 2P Y3 P 1 B 1',
     'S35': 'S Y1 2P 1 Y2 2P 2 Y3 P B 0 Z B 1 Z B 2',
     'S36': 'F B 1 S Y1 2P 2 Y2 2P Y3 P 1 B 1 Z B 2',
     'S37': 'F B 1 S Y1 2P Y2 2P 2 Y3 P 1 B 1 Z B 2',
     'S38': 'E B 1 S Y1 2P 2 Y2 2P Y3 P 1 B 1 Z B 2',
     'S39': 'E B 1 S Y1 2P Y2 2P 2 Y3 P 1 B 1 Z B 2',
     'S40': 'S Y1 2P Y2 2P Y3 2P B 0',
     'S41': 'F B 1 S Y1 2P 2 Y2 2P 3 Y3 P 1 B 1 Z B 2 Z B 3',
     'S42': 'E B 1 S Y1 2P 2 Y2 2P 3 Y3 P 1 B 1 Z B 2 Z B 3',
     'S43': 'S Y1 2P 1 Y2 2P Y3 2P B 0 Z B 1',
     'S44': 'S Y1 2P Y2 2P 1 Y3 2P B 0 Z B 1',
     'S45': 'F B 1 S Y1 2P Y2 2P Y3 2P 1 B 1',
     'S46': 'S Y1 2P Y2 2P Y3 2P 1 B 0 Z B 1',
     'S47': 'S Y1 2P 1 Y2 2P 2 Y3 2P B 0 Z B 1 Z B 2',
     'S48': 'F B 1 S Y1 2P 2 Y2 2P Y3 2P 1 B 1 Z B 2',
     'S49': 'F B 1 S Y1 2P Y2 2P 2 Y3 2P 1 B 1 Z B 2',
     'S50': 'S Y1 2P 1 Y2 2P Y3 2P 2 B 0 Z B 1 Z B 2',
     'S51': 'S Y1 2P Y2 2P 1 Y3 2P 2 B 0 Z B 1 Z B 2',
     'S52': 'F B 1 S Y1 2P 2 Y2 2P 3 Y3 2P 1 B 1 Z B 2 Z B 3',
     'S53': 'S Y1 2P 1 Y2 2P 2 Y3 2P 3 B 0 Z B 1 Z B 2 Z B 3'}
    _STATE_OUTPUT_ALIASES = {'S1': 's_y1_u_y2_u_y3_u_b_0',
     'S2': 'source_defined_e_b_state',
     'S3': 'source_defined_f_b_state',
     'S4': 'source_defined_z_b_state',
     'S5': 'e_b_1_s_y1_u_1_y2_u_y3_u_b_1',
     'S6': 's_y1_p_y2_u_y3_u_b_0',
     'S7': 'f_b_1_s_y1_p_1_y2_u_y3_u_b_1',
     'S8': 'e_b_1_s_y1_p_1_y2_u_y3_u_b_1',
     'S9': 's_y1_2p_y2_u_y3_u_b_0',
     'S10': 'f_b_1_s_y1_2p_1_y2_u_y3_u_b_1',
     'S11': 'e_b_1_s_y1_2p_y2_u_1_y3_u_b_1',
     'S12': 's_y1_2p_1_y2_u_y3_u_b_0_z_b_1',
     'S13': 'e_b_1_s_y1_2p_2_y2_u_1_y3_u_b_1_z_b_2',
     'S14': 's_y1_2p_y2_p_y3_u_b_0',
     'S15': 's_y1_2p_1_y2_p_y3_u_b_0_z_b_1',
     'S16': 'f_b_1_s_y1_2p_y2_p_1_y3_u_b_1',
     'S17': 'e_b_1_s_y1_2p_y2_p_1_y3_u_b_1',
     'S18': 'f_b_1_s_y1_2p_2_y2_p_1_y3_u_b_1_z_b_2',
     'S19': 'e_b_1_s_y1_2p_2_y2_p_1_y3_u_b_1_z_b_2',
     'S20': 's_y1_2p_y2_2p_y3_u_b_0',
     'S21': 's_y1_2p_1_y2_2p_y3_u_b_0_z_b_1',
     'S22': 'f_b_1_s_y1_2p_y2_2p_1_y3_u_b_1',
     'S23': 'e_b_1_s_y1_2p_y2_2p_y3_u_1_b_1',
     'S24': 's_y1_2p_y2_2p_1_y3_u_b_0_z_b_1',
     'S25': 'f_b_1_s_y1_2p_2_y2_2p_1_y3_u_b_1_z_b_2',
     'S26': 'e_b_1_s_y1_2p_2_y2_2p_y3_u_1_b_1_z_b_2',
     'S27': 'e_b_1_s_y1_2p_y2_2p_2_y3_u_1_b_1_z_b_2',
     'S28': 's_y1_2p_y2_2p_y3_p_b_0',
     'S29': 's_y1_2p_1_y2_2p_2_y3_u_b_0_z_b_1_z_b_2',
     'S30': 'e_b_1_s_y1_2p_2_y2_2p_3_y3_u_1_b_1_z_b_2_z_b_3',
     'S31': 's_y1_2p_1_y2_2p_y3_p_b_0_z_b_1',
     'S32': 's_y1_2p_y2_2p_1_y3_p_b_0_z_b_1',
     'S33': 'f_b_1_s_y1_2p_y2_2p_y3_p_1_b_1',
     'S34': 'e_b_1_s_y1_2p_y2_2p_y3_p_1_b_1',
     'S35': 's_y1_2p_1_y2_2p_2_y3_p_b_0_z_b_1_z_b_2',
     'S36': 'f_b_1_s_y1_2p_2_y2_2p_y3_p_1_b_1_z_b_2',
     'S37': 'f_b_1_s_y1_2p_y2_2p_2_y3_p_1_b_1_z_b_2',
     'S38': 'e_b_1_s_y1_2p_2_y2_2p_y3_p_1_b_1_z_b_2',
     'S39': 'e_b_1_s_y1_2p_y2_2p_2_y3_p_1_b_1_z_b_2',
     'S40': 's_y1_2p_y2_2p_y3_2p_b_0',
     'S41': 'f_b_1_s_y1_2p_2_y2_2p_3_y3_p_1_b_1_z_b_2_z_b_3',
     'S42': 'e_b_1_s_y1_2p_2_y2_2p_3_y3_p_1_b_1_z_b_2_z_b_3',
     'S43': 's_y1_2p_1_y2_2p_y3_2p_b_0_z_b_1',
     'S44': 's_y1_2p_y2_2p_1_y3_2p_b_0_z_b_1',
     'S45': 'f_b_1_s_y1_2p_y2_2p_y3_2p_1_b_1',
     'S46': 's_y1_2p_y2_2p_y3_2p_1_b_0_z_b_1',
     'S47': 's_y1_2p_1_y2_2p_2_y3_2p_b_0_z_b_1_z_b_2',
     'S48': 'f_b_1_s_y1_2p_2_y2_2p_y3_2p_1_b_1_z_b_2',
     'S49': 'f_b_1_s_y1_2p_y2_2p_2_y3_2p_1_b_1_z_b_2',
     'S50': 's_y1_2p_1_y2_2p_y3_2p_2_b_0_z_b_1_z_b_2',
     'S51': 's_y1_2p_y2_2p_1_y3_2p_2_b_0_z_b_1_z_b_2',
     'S52': 'f_b_1_s_y1_2p_2_y2_2p_3_y3_2p_1_b_1_z_b_2_z_b_3',
     'S53': 's_y1_2p_1_y2_2p_2_y3_2p_3_b_0_z_b_1_z_b_2_z_b_3'}

    def __init__(self, model_path: str = 'data/MODEL1604100000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Mukhopadhyay2013TCellReceptorProximalSignalModel1604100000Model = Mukhopadhyay2013TCellReceptorProximalSignalModel
