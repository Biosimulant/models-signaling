# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Koo2013 - Shear stress induced AKT and eNOS phosphorylation - Model 2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koo2013ShearStressInducedAktAndEnosPhosphModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000465'
    _TITLE = 'Koo2013 - Shear stress induced AKT and eNOS phosphorylation - Model 2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt': ('s16', 'substance', 'AKT. Maps to SBML symbol `s16` and is emitted in native SBML units.'),
     'p_akt_pi3p': ('s26',
                    'substance',
                    'P AKT PI3P. Maps to SBML symbol `s26` and is emitted in native SBML units.'),
     'pp_akt_pi3p': ('s27',
                     'substance',
                     'Pp AKT PI3P. Maps to SBML symbol `s27` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_shear_stress': ('s119',
                              0.0,
                              'substance',
                              'Initial level of Shear Stress. Maps to SBML symbol `s119`; exposed as a '
                              'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s14': 'source-defined PDK1 state',
     's15': 'PP2A',
     's16': 'AKT',
     's17': 'PI3P',
     's18': 'source-defined PTEN state',
     's19': 'source-defined PIP2 state',
     's20': 'P PI3K',
     's22': 'PI3K',
     's23': 'source-defined TIME state',
     's24': 'source-defined PDK2 state',
     's25': 'PDK1 Cyto',
     's26': 'P AKT PI3P',
     's27': 'Pp AKT PI3P',
     's28': 'AKT PI3P',
     's119': 'Shear Stress'}
    _STATE_OUTPUT_ALIASES = {'s14': 'source_defined_pdk1_state',
     's15': 'pp2a',
     's16': 'akt',
     's17': 'pi3p',
     's18': 'source_defined_pten_state',
     's19': 'source_defined_pip2_state',
     's20': 'p_pi3k',
     's22': 'pi3k',
     's23': 'source_defined_time_state',
     's24': 'source_defined_pdk2_state',
     's25': 'pdk1_cyto',
     's26': 'p_akt_pi3p',
     's27': 'pp_akt_pi3p',
     's28': 'akt_pi3p',
     's119': 'shear_stress'}

    def __init__(self, model_path: str = 'data/BIOMD0000000465.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Koo2013ShearStressInducedAktAndEnosPhosphBiomd0000000465Model = Koo2013ShearStressInducedAktAndEnosPhosphModel
