# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Besozzi2012 - Oscillatory regimes in the Ras/cAMP/PKA pathway in S.cerevisiae."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Besozzi2012OscillatoryRegimesInTheRasCampModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000478'
    _TITLE = 'Besozzi2012 - Oscillatory regimes in the Ras/cAMP/PKA pathway in S.cerevisiae'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ras2_gdp': ('Ras2_GDP',
                  'native SBML value',
                  'RAS2 GDP. Maps to SBML symbol `Ras2_GDP` and is emitted in native SBML units.'),
     'ras2_gdp_cdc25': ('Ras2_GDP_Cdc25',
                        'native SBML value',
                        'RAS2 GDP CDC25. Maps to SBML symbol `Ras2_GDP_Cdc25` and is emitted in native '
                        'SBML units.'),
     'ras2_cdc25': ('Ras2_Cdc25',
                    'native SBML value',
                    'RAS2 CDC25. Maps to SBML symbol `Ras2_Cdc25` and is emitted in native SBML '
                    'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_atp': ('ATP',
                     24000000.0,
                     'native SBML value',
                     'Initial level of ATP. Maps to SBML symbol `ATP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_gdp': ('GDP',
                     1500000.0,
                     'native SBML value',
                     'Initial level of GDP. Maps to SBML symbol `GDP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_gtp': ('GTP',
                     5000000.0,
                     'native SBML value',
                     'Initial level of GTP. Maps to SBML symbol `GTP`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Ras2_GDP': 'RAS2 GDP',
     'Cdc25': 'CDC25',
     'Ras2_GDP_Cdc25': 'RAS2 GDP CDC25',
     'Ras2_Cdc25': 'RAS2 CDC25',
     'GDP': 'Source Defined GDP State',
     'GTP': 'Source Defined GTP State',
     'Ras2_GTP_Cdc25': 'RAS2 GTP CDC25',
     'Ras2_GTP': 'RAS2 GTP',
     'Ira2': 'Source Defined IRA2 State',
     'Ras2_GTP_Ira2': 'RAS2 GTP IRA2',
     'CYR1': 'Source Defined CYR1 State',
     'Ras2_GTP_CYR1': 'RAS2 GTP CYR1',
     'ATP': 'ATP',
     'cAMP': 'cAMP',
     'PKA': 'Source Defined PKA State',
     'cAMP_PKA': 'C AMP PKA',
     'IIcAMP_PKA': 'Iic AMP PKA',
     'IIIcAMP_PKA': 'Iiic AMP PKA',
     'IVcAMP_PKA': 'Ivc AMP PKA',
     'C': 'Source Defined C State',
     'R_2cAMP': 'R 2c AMP',
     'R': 'Source Defined R State',
     'R_C': 'Source Defined R C State',
     'Pde1': 'Source Defined PDE1 State',
     'Pde1f': 'Pde1f',
     'cAMP_Pde1f': 'C AMP Pde1f',
     'AMP': 'AMP',
     'PPA2': 'Source Defined PPA2 State',
     'Pde2': 'Source Defined PDE2 State',
     'cAMP_Pde2': 'C AMP PDE2',
     'Cdc25f': 'Cdc25f',
     'Ira2P': 'Ira2p',
     'Ras2_GTP_Ira2P': 'RAS2 GTP Ira2p'}
    _STATE_OUTPUT_ALIASES = {'Ras2_GDP': 'ras2_gdp',
     'Cdc25': 'cdc25',
     'Ras2_GDP_Cdc25': 'ras2_gdp_cdc25',
     'Ras2_Cdc25': 'ras2_cdc25',
     'GDP': 'source_defined_gdp_state',
     'GTP': 'source_defined_gtp_state',
     'Ras2_GTP_Cdc25': 'ras2_gtp_cdc25',
     'Ras2_GTP': 'ras2_gtp',
     'Ira2': 'source_defined_ira2_state',
     'Ras2_GTP_Ira2': 'ras2_gtp_ira2',
     'CYR1': 'source_defined_cyr1_state',
     'Ras2_GTP_CYR1': 'ras2_gtp_cyr1',
     'ATP': 'atp',
     'cAMP': 'camp',
     'PKA': 'source_defined_pka_state',
     'cAMP_PKA': 'c_amp_pka',
     'IIcAMP_PKA': 'iic_amp_pka',
     'IIIcAMP_PKA': 'iiic_amp_pka',
     'IVcAMP_PKA': 'ivc_amp_pka',
     'C': 'source_defined_c_state',
     'R_2cAMP': 'r_2c_amp',
     'R': 'source_defined_r_state',
     'R_C': 'source_defined_r_c_state',
     'Pde1': 'source_defined_pde1_state',
     'Pde1f': 'pde1f',
     'cAMP_Pde1f': 'c_amp_pde1f',
     'AMP': 'amp',
     'PPA2': 'source_defined_ppa2_state',
     'Pde2': 'source_defined_pde2_state',
     'cAMP_Pde2': 'c_amp_pde2',
     'Cdc25f': 'cdc25f',
     'Ira2P': 'ira2p',
     'Ras2_GTP_Ira2P': 'ras2_gtp_ira2p'}

    def __init__(self, model_path: str = 'data/BIOMD0000000478.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Besozzi2012OscillatoryRegimesInTheRasCampBiomd0000000478Model = Besozzi2012OscillatoryRegimesInTheRasCampModel
