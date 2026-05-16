# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Huang2014 - Systematic modeling for the insulin signaling network mediated by IRS1 and IRS2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Huang2014SystematicModelingForTheInsulinSiModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1912090001'
    _TITLE = 'Huang2014 - Systematic modeling for the insulin signaling network mediated by IRS1 and IRS2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'x2_receptor': ('x2_Receptor',
                     'native SBML value',
                     'X2 Receptor. Maps to SBML symbol `x2_Receptor` and is emitted in native SBML '
                     'units.'),
     'x6_en_receptor': ('x6_EN_Receptor',
                        'native SBML value',
                        'X6 EN Receptor. Maps to SBML symbol `x6_EN_Receptor` and is emitted in native '
                        'SBML units.'),
     'x16_akt': ('x16_AKT',
                 'native SBML value',
                 'X16 AKT. Maps to SBML symbol `x16_AKT` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_x1_insulin': ('x1_Insulin',
                            0.0,
                            'native SBML value',
                            'Initial level of X1 Insulin. Maps to SBML symbol `x1_Insulin`; exposed as '
                            'a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'x2_Receptor': 'X2 Receptor',
     'x6_EN_Receptor': 'X6 EN Receptor',
     'x9_IRS_1': 'X9 IRS 1',
     'x21_IRS_2': 'X21 IRS 2',
     'x11_PI3K': 'X11 PI3K',
     'x14_PI45P2': 'X14 PI45P2',
     'x15_PI34P2': 'X15 PI34P2',
     'x13_PI345P3': 'X13 PI345P3',
     'x16_AKT': 'X16 AKT',
     'x18_PKR': 'X18 PKR',
     'x19_PKR_P': 'X19 PKR P',
     'x26_Shc': 'X26 Shc adapter protein',
     'x31_GS': 'X31 GS',
     'x33_RasGDP': 'X33 RAS GDP',
     'x35_MEK': 'X35 MEK',
     'x37_JNK': 'X37 JNK',
     'x4_I2R_P': 'X4 I2R P',
     'x20_IRS_1_SerP': 'X20 IRS 1 Ser P',
     'x22_IRS_2_TyrP': 'X22 IRS 2 tyrosine site P',
     'x23_PI3K_IRS_2_P': 'X23 PI3K IRS 2 P',
     'x38_JNK_P': 'X38 JNK P',
     'x25_ActiveFox01': 'X25 active Fox01',
     'x17_AKT_P': 'X17 AKT P',
     'x12_PI3K_IRS_1_P': 'X12 PI3K IRS 1 P',
     'x1_Insulin': 'X1 Insulin',
     'x3_IR': 'X3 insulin receptor',
     'x8_EN_IR_p': 'X8 EN insulin receptor P',
     'x7_EN_I2R_p': 'X7 EN I2R P',
     'x10_IRS_1_TyrP': 'X10 IRS 1 tyrosine site P',
     'x27_IRSh': 'X27 Irsh',
     'x5_IR_P': 'X5 insulin receptor P',
     'x28_IRSh_P': 'X28 Irsh P',
     'x29_IRShGS': 'X29 Irsh GS',
     'x32_ShGS': 'X32 Sh GS',
     'x30_Sh_P': 'X30 Sh P',
     'x34_RasGTP': 'X34 RAS GTP',
     'x36_MEK_P': 'X36 MEK P',
     'x24_Fox01': 'X24 Fox01'}
    _STATE_OUTPUT_ALIASES = {'x2_Receptor': 'x2_receptor',
     'x6_EN_Receptor': 'x6_en_receptor',
     'x9_IRS_1': 'x9_irs_1',
     'x21_IRS_2': 'x21_irs_2',
     'x11_PI3K': 'x11_pi3k',
     'x14_PI45P2': 'x14_pi45p2',
     'x15_PI34P2': 'x15_pi34p2',
     'x13_PI345P3': 'x13_pi345p3',
     'x16_AKT': 'x16_akt',
     'x18_PKR': 'x18_pkr',
     'x19_PKR_P': 'x19_pkr_p',
     'x26_Shc': 'x26_shc_adapter_protein',
     'x31_GS': 'x31_gs',
     'x33_RasGDP': 'x33_ras_gdp',
     'x35_MEK': 'x35_mek',
     'x37_JNK': 'x37_jnk',
     'x4_I2R_P': 'x4_i2r_p',
     'x20_IRS_1_SerP': 'x20_irs_1_ser_p',
     'x22_IRS_2_TyrP': 'x22_irs_2_tyrosine_site_p',
     'x23_PI3K_IRS_2_P': 'x23_pi3k_irs_2_p',
     'x38_JNK_P': 'x38_jnk_p',
     'x25_ActiveFox01': 'x25_active_fox01',
     'x17_AKT_P': 'x17_akt_p',
     'x12_PI3K_IRS_1_P': 'x12_pi3k_irs_1_p',
     'x1_Insulin': 'x1_insulin',
     'x3_IR': 'x3_insulin_receptor',
     'x8_EN_IR_p': 'x8_en_insulin_receptor_p',
     'x7_EN_I2R_p': 'x7_en_i2r_p',
     'x10_IRS_1_TyrP': 'x10_irs_1_tyrosine_site_p',
     'x27_IRSh': 'x27_irsh',
     'x5_IR_P': 'x5_insulin_receptor_p',
     'x28_IRSh_P': 'x28_irsh_p',
     'x29_IRShGS': 'x29_irsh_gs',
     'x32_ShGS': 'x32_sh_gs',
     'x30_Sh_P': 'x30_sh_p',
     'x34_RasGTP': 'x34_ras_gtp',
     'x36_MEK_P': 'x36_mek_p',
     'x24_Fox01': 'x24_fox01'}

    def __init__(self, model_path: str = 'data/MODEL1912090001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Huang2014SystematicModelingForTheInsulinSiModel1912090001Model = Huang2014SystematicModelingForTheInsulinSiModel
