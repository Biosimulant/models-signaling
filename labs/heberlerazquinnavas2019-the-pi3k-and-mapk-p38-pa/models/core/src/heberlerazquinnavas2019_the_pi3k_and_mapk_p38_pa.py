# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 3."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heberlerazquinnavas2019ThePi3kAndMapkP38PaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000907'
    _TITLE = 'HeberleRazquinNavas2019 - The PI3K and MAPK/p38 pathways control stress granuleassembly in a hierarchical manner model 3'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt_p_t308_obs': ('Akt_pT308_obs',
                        'native SBML value',
                        'AKT P T308 Obs. Maps to SBML symbol `Akt_pT308_obs` and is emitted in native '
                        'SBML units.'),
     'akt_p_s473_obs': ('Akt_pS473_obs',
                        'native SBML value',
                        'AKT P S473 Obs. Maps to SBML symbol `Akt_pS473_obs` and is emitted in native '
                        'SBML units.'),
     'pras40_p_t246_obs': ('PRAS40_pT246_obs',
                           'native SBML value',
                           'PRAS40 P T246 Obs. Maps to SBML symbol `PRAS40_pT246_obs` and is emitted '
                           'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_akt_p_s473_obs': ('Akt_pS473_obs',
                                0.0125245862006138,
                                'native SBML value',
                                'Initial level of AKT P S473 Obs. Maps to SBML symbol `Akt_pS473_obs`; '
                                'exposed as a traceable initial-condition perturbation.'),
     'initial_akt_p_t308_obs': ('Akt_pT308_obs',
                                0.241624144113638,
                                'native SBML value',
                                'Initial level of AKT P T308 Obs. Maps to SBML symbol `Akt_pT308_obs`; '
                                'exposed as a traceable initial-condition perturbation.'),
     'initial_four_ebp1_p_t37_46_obs': ('fourEBP1_pT37_46_obs',
                                        0.406274357698408,
                                        'native SBML value',
                                        'Initial level of Four EBP1 P T37 46 Obs. Maps to SBML symbol '
                                        '`fourEBP1_pT37_46_obs`; exposed as a traceable '
                                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'X1_0': 'X1 0',
     'X1_1': 'X1 1',
     'X2_0': 'X2 0',
     'X2_1': 'X2 1',
     'X2_2': 'X2 2',
     'X4_0': 'X4 0',
     'X4_1': 'X4 1',
     'X5_0': 'X5 0',
     'X5_1': 'X5 1',
     'X8_0': 'X8 0',
     'X8_1': 'X8 1',
     'X8_2': 'X8 2',
     'X8_3': 'X8 3',
     'X9_0': 'X9 0',
     'X9_2': 'X9 2',
     'X10_0': 'X10 0',
     'X10_1': 'X10 1',
     'X10_2': 'X10 2',
     'X10_3': 'X10 3',
     'X11_0': 'X11 0',
     'X11_1': 'X11 1',
     'X11_2': 'X11 2',
     'X11_3': 'X11 3',
     'X12_0': 'X12 0',
     'X12_1': 'X12 1',
     'Akt_pT308_obs': 'AKT P T308 Obs',
     'Akt_pS473_obs': 'AKT P S473 Obs',
     'TSC1_TSC2_pT1462_obs': 'TSC1 TSC2 P T1462 Obs',
     'PRAS40_pT246_obs': 'PRAS40 P T246 Obs',
     'PRAS40_pS183_obs': 'PRAS40 P S183 Obs',
     'fourEBP1_pT37_46_obs': 'Four EBP1 P T37 46 Obs',
     'p70_S6K_pT389_obs': 'P70 S6K P T389 Obs',
     'p70_S6K_pT229_obs': 'P70 S6K P T229 Obs',
     'IRS1_pS636_639_obs': 'IRS1 P S636 639 Obs'}
    _STATE_OUTPUT_ALIASES = {'X1_0': 'x1_0',
     'X1_1': 'x1_1',
     'X2_0': 'x2_0',
     'X2_1': 'x2_1',
     'X2_2': 'x2_2',
     'X4_0': 'x4_0',
     'X4_1': 'x4_1',
     'X5_0': 'x5_0',
     'X5_1': 'x5_1',
     'X8_0': 'x8_0',
     'X8_1': 'x8_1',
     'X8_2': 'x8_2',
     'X8_3': 'x8_3',
     'X9_0': 'x9_0',
     'X9_2': 'x9_2',
     'X10_0': 'x10_0',
     'X10_1': 'x10_1',
     'X10_2': 'x10_2',
     'X10_3': 'x10_3',
     'X11_0': 'x11_0',
     'X11_1': 'x11_1',
     'X11_2': 'x11_2',
     'X11_3': 'x11_3',
     'X12_0': 'x12_0',
     'X12_1': 'x12_1',
     'Akt_pT308_obs': 'akt_p_t308_obs',
     'Akt_pS473_obs': 'akt_p_s473_obs',
     'TSC1_TSC2_pT1462_obs': 'tsc1_tsc2_p_t1462_obs',
     'PRAS40_pT246_obs': 'pras40_p_t246_obs',
     'PRAS40_pS183_obs': 'pras40_p_s183_obs',
     'fourEBP1_pT37_46_obs': 'four_ebp1_p_t37_46_obs',
     'p70_S6K_pT389_obs': 'p70_s6k_p_t389_obs',
     'p70_S6K_pT229_obs': 'p70_s6k_p_t229_obs',
     'IRS1_pS636_639_obs': 'irs1_p_s636_639_obs'}

    def __init__(self, model_path: str = 'data/BIOMD0000000907.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Heberlerazquinnavas2019ThePi3kAndMapkP38PaBiomd0000000907Model = Heberlerazquinnavas2019ThePi3kAndMapkP38PaModel
