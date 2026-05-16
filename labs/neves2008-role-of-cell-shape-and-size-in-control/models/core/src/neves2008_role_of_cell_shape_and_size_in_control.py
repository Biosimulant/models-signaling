# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Neves2008 - Role of cell shape and size in controlling intracellular signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Neves2008RoleOfCellShapeAndSizeInControlModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000182'
    _TITLE = 'Neves2008 - Role of cell shape and size in controlling intracellular signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ac_active_cyto_mem': ('AC_active_cyto_mem',
                            'molecules',
                            'AC active Cyto Mem. Maps to SBML symbol `AC_active_cyto_mem` and is '
                            'emitted in native SBML units.'),
     'mapk_active_cyto': ('MAPK_active_cyto',
                          'molecules',
                          'MAPK active Cyto. Maps to SBML symbol `MAPK_active_cyto` and is emitted in '
                          'native SBML units.'),
     'mek_active_cyto': ('MEK_active_cyto',
                         'molecules',
                         'MEK active Cyto. Maps to SBML symbol `MEK_active_cyto` and is emitted in '
                         'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_c_amp_cyto': ('cAMP_cyto',
                            0.0,
                            'molecules',
                            'Initial level of C AMP Cyto. Maps to SBML symbol `cAMP_cyto`; exposed as '
                            'a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'AC_active_cyto_mem': 'AC active Cyto Mem',
     'G_GDP_cyto': 'G GDP Cyto',
     'G_protein_cyto': 'G Protein Cyto',
     'G_a_s_cyto': 'G A S Cyto',
     'GRK_bg_cyto': 'GRK Bg Cyto',
     'iso_BAR_p_cyto_mem': 'Iso BAR P Cyto Mem',
     'PDE4_cyto': 'PDE4 Cyto',
     'ATP_cyto': 'ATP Cyto',
     'AC_PKA_cyto_mem': 'AC PKA Cyto Mem',
     'R2C2_cyto': 'R2C2 Cyto',
     'PP_PDE_cyto': 'PP PDE Cyto',
     'BAR_cyto_mem': 'BAR Cyto Mem',
     'BAR_G_cyto_mem': 'BAR G Cyto Mem',
     'iso_extra': 'Iso Extra',
     'iso_BAR_cyto_mem': 'Iso BAR Cyto Mem',
     'MAPK_active_cyto': 'MAPK active Cyto',
     'MEK_cyto': 'MEK Cyto',
     'MEK_active_cyto': 'MEK active Cyto',
     'B_Raf_active_cyto': 'B RAF active Cyto',
     'bg_cyto': 'Bg Cyto',
     'B_Raf_cyto': 'B RAF Cyto',
     'PKA_cyto': 'PKA Cyto',
     'AC_cyto_mem': 'AC Cyto Mem',
     'AMP_cyto': 'AMP Cyto',
     'GRK_cyto': 'GRK Cyto',
     'PP2A_cyto': 'PP2A Cyto',
     'MAPK_cyto': 'MAPK Cyto',
     'PTP_cyto': 'PTP Cyto',
     'PTP_PKA_cyto': 'PTP PKA Cyto',
     'c_R2C2_cyto': 'C R2C2 Cyto',
     'c2_R2C2_cyto': 'C2 R2C2 Cyto',
     'c3_R2C2_cyto': 'Complement Complement Complement Complement Complement complement C3 R2C2 Cyto',
     'iso_BAR_G_cyto_mem': 'Iso BAR G Cyto Mem',
     'PDE_high_km_cyto': 'PDE High Km Cyto',
     'cAMP_cyto': 'C AMP Cyto',
     'PTP_PP_cyto': 'PTP PP Cyto',
     'PDE4_P_cyto': 'PDE4 P Cyto'}
    _STATE_OUTPUT_ALIASES = {'AC_active_cyto_mem': 'ac_active_cyto_mem',
     'G_GDP_cyto': 'g_gdp_cyto',
     'G_protein_cyto': 'g_protein_cyto',
     'G_a_s_cyto': 'g_a_s_cyto',
     'GRK_bg_cyto': 'grk_bg_cyto',
     'iso_BAR_p_cyto_mem': 'iso_bar_p_cyto_mem',
     'PDE4_cyto': 'pde4_cyto',
     'ATP_cyto': 'atp_cyto',
     'AC_PKA_cyto_mem': 'ac_pka_cyto_mem',
     'R2C2_cyto': 'r2c2_cyto',
     'PP_PDE_cyto': 'pp_pde_cyto',
     'BAR_cyto_mem': 'bar_cyto_mem',
     'BAR_G_cyto_mem': 'bar_g_cyto_mem',
     'iso_extra': 'iso_extra',
     'iso_BAR_cyto_mem': 'iso_bar_cyto_mem',
     'MAPK_active_cyto': 'mapk_active_cyto',
     'MEK_cyto': 'mek_cyto',
     'MEK_active_cyto': 'mek_active_cyto',
     'B_Raf_active_cyto': 'b_raf_active_cyto',
     'bg_cyto': 'bg_cyto',
     'B_Raf_cyto': 'b_raf_cyto',
     'PKA_cyto': 'pka_cyto',
     'AC_cyto_mem': 'ac_cyto_mem',
     'AMP_cyto': 'amp_cyto',
     'GRK_cyto': 'grk_cyto',
     'PP2A_cyto': 'pp2a_cyto',
     'MAPK_cyto': 'mapk_cyto',
     'PTP_cyto': 'ptp_cyto',
     'PTP_PKA_cyto': 'ptp_pka_cyto',
     'c_R2C2_cyto': 'c_r2c2_cyto',
     'c2_R2C2_cyto': 'c2_r2c2_cyto',
     'c3_R2C2_cyto': 'complement_complement_complement_complement_complement_complement_c3_r2c2_cyto',
     'iso_BAR_G_cyto_mem': 'iso_bar_g_cyto_mem',
     'PDE_high_km_cyto': 'pde_high_km_cyto',
     'cAMP_cyto': 'c_amp_cyto',
     'PTP_PP_cyto': 'ptp_pp_cyto',
     'PDE4_P_cyto': 'pde4_p_cyto'}

    def __init__(self, model_path: str = 'data/BIOMD0000000182.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Neves2008RoleOfCellShapeAndSizeInControlBiomd0000000182Model = Neves2008RoleOfCellShapeAndSizeInControlModel
