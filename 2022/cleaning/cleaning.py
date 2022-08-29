import pandas as pd
import os

# get cwd
cwd = os.getcwd()

# read csv
df = pd.read_csv('../../2021/all_countries.csv')

print(df.columns)

# reorder columns
df = df[['year', 'countries', 'ISO', 'region', 'hf_score', 'hf_rank', 'hf_quartile',
         # rol
         'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol_wgi', 'pf_rol',
         # ss
         'pf_ss_homicide', 'pf_ss_disappearances_disap', 'pf_ss_disappearances_violent',
         'pf_ss_disappearances_organized', 'pf_ss_disappearances_fatalities', 'pf_ss_disappearances_injuries',
         'pf_ss_disappearances_torture', 'pf_ss_killings', 'pf_ss_disappearances', 'pf_ss',
         # movement
         'pf_movement_vdem_foreign', 'pf_movement_vdem_men', 'pf_movement_vdem_women', 'pf_movement_vdem',
         'pf_movement_cld', 'pf_movement',
         # religion
         'pf_religion_freedom_vdem', 'pf_religion_freedom_cld', 'pf_religion_freedom', 'pf_religion_suppression',
         'pf_religion',
         # assembly
         'pf_assembly_entry', 'pf_assembly_freedom_house', 'pf_assembly_freedom_bti',
         'pf_assembly_freedom_cld', 'pf_assembly_freedom', 'pf_assembly_parties_barriers', 'pf_assembly_parties_bans',
         'pf_assembly_parties_auton', 'pf_assembly_parties', 'pf_assembly_civil', 'pf_assembly', 'pf_assembly_rank',
         # expression
         'pf_expression_killed', 'pf_expression_jailed', 'pf_expression_cultural', 'pf_expression_harass',
         'pf_expression_gov', 'pf_expression_internet', 'pf_expression_selfcens', 'pf_expression_media',
         'pf_expression_freedom_bti', 'pf_expression_freedom_cld', 'pf_expression_freedom', 'pf_expression',
         'pf_expression_rank',
         # identity
         'pf_identity_same_m', 'pf_identity_same_f', 'pf_identity_same', 'pf_identity_divorce',
         'pf_identity_inheritance_widows', 'pf_identity_inheritance_daughters', 'pf_identity_inheritance',
         'pf_identity_fgm', 'pf_identity',
         # personal freedom
         'pf_score', 'pf_rank', 'pf_womens',
         'ef_government_consumption', 'ef_government_transfers', 'ef_government_enterprises',
         'ef_government_tax_income', 'ef_government_tax_payroll', 'ef_government_tax', 'ef_government_soa',
         'ef_government',
         'ef_legal_judicial', 'ef_legal_courts', 'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity',
         'ef_legal_enforcement', 'ef_legal_regulatory', 'ef_legal_police', 'ef_legal',
         'ef_money_growth', 'ef_money_sd', 'ef_money_inflation', 'ef_money_currency', 'ef_money',
         'ef_trade_tariffs_revenue', 'ef_trade_tariffs_mean', 'ef_trade_tariffs_sd', 'ef_trade_tariffs',
         'ef_trade_regulatory_nontariff', 'ef_trade_regulatory_compliance', 'ef_trade_regulatory',
         'ef_trade_black', 'ef_trade_movement_foreign', 'ef_trade_movement_capital', 'ef_trade_movement_visit',
         'ef_trade_movement', 'ef_trade',
         'ef_regulation_credit_ownership', 'ef_regulation_credit_private',
         'ef_regulation_credit_interest', 'ef_regulation_credit', 'ef_regulation_labor_minwage',
         'ef_regulation_labor_firing', 'ef_regulation_labor_bargain', 'ef_regulation_labor_hours',
         'ef_regulation_labor_dismissal', 'ef_regulation_labor_conscription', 'ef_regulation_labor',
         'ef_regulation_business_adm', 'ef_regulation_business_bureaucracy', 'ef_regulation_business_start',
         'ef_regulation_business_bribes', 'ef_regulation_business_licensing', 'ef_regulation_business_compliance',
         'ef_regulation_business', 'ef_regulation', 'ef_score', 'ef_rank']]

df.to_csv('hfi2022_cc.csv')
