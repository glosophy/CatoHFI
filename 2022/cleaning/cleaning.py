import pandas as pd
import os

# get cwd
cwd = os.getcwd()

# read csv
df = pd.read_excel('../../2022/HFI2022.xlsx')

print(df.columns)

# rename columns
df.columns = ['year', 'countries', 'region', 'hf_score', 'hf_rank', 'hf_quartile',
              # rol
              'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol_vdem', 'pf_rol',
              # ss
              'pf_ss_homicide', 'pf_ss_homicide_data', 'pf_ss_disappearances_disap', 'pf_ss_disappearances_violent',
              'pf_ss_disappearances_violent_data', 'pf_ss_disappearances_organized', 'pf_ss_disappearances_fatalities',
              'pf_ss_disappearances_fatalities_data', 'pf_ss_disappearances_injuries',
              'pf_ss_disappearances_injuries_data', 'pf_ss_disappearances_torture', 'pf_ss_killings',
              'pf_ss_disappearances', 'pf_ss',
              # movement
              'pf_movement_vdem_foreign', 'pf_movement_vdem_men', 'pf_movement_vdem_women', 'pf_movement_vdem',
              'pf_movement_cld', 'pf_movement',
              # religion
              'pf_religion_freedom_vdem', 'pf_religion_freedom_cld', 'pf_religion_freedom', 'pf_religion_suppression',
              'pf_religion',
              # assembly
              'pf_assembly_entry', 'pf_assembly_freedom_house', 'pf_assembly_freedom_bti',
              'pf_assembly_freedom_cld', 'pf_assembly_freedom', 'pf_assembly_parties_barriers',
              'pf_assembly_parties_bans',
              'pf_assembly_parties_auton', 'pf_assembly_parties', 'pf_assembly_civil', 'pf_assembly',
              # expression
              'pf_expression_direct_killed', 'pf_expression_direct_killed_data', 'pf_expression_direct_jailed',
              'pf_expression_direct_jailed_data', 'pf_expression_direct', 'pf_expression_vdem_cultural',
              'pf_expression_vdem_harass', 'pf_expression_vdem_gov', 'pf_expression_vdem_internet',
              'pf_expression_vdem_selfcens', 'pf_expression_vdem', 'pf_expression_house', 'pf_expression_bti',
              'pf_expression_cld', 'pf_expression',
              # identity
              'pf_identity_same_m', 'pf_identity_same_f', 'pf_identity_same', 'pf_identity_divorce',
              'pf_identity_inheritance_widows', 'pf_identity_inheritance_daughters', 'pf_identity_inheritance',
              'pf_identity_fgm', 'pf_identity',
              # personal freedom
              'pf_score', 'pf_rank',
              # government
              'ef_government_consumption', 'ef_government_consumption_data', 'ef_government_transfers',
              'ef_government_transfers_data', 'ef_government_investment', 'ef_government_investment_data',
              'ef_government_tax_income', 'ef_government_tax_income_data', 'ef_government_tax_payroll',
              'ef_government_tax_payroll_data', 'ef_government_tax', 'ef_government_soa', 'ef_government',
              # legal
              'ef_legal_judicial', 'ef_legal_courts', 'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity',
              'ef_legal_enforcement', 'ef_legal_regulatory', 'ef_legal_police', 'ef_gender', 'ef_legal',
              # money
              'ef_money_growth', 'ef_money_growth_data', 'ef_money_sd', 'ef_money_sd_data', 'ef_money_inflation',
              'ef_money_inflation_data', 'ef_money_currency', 'ef_money',
              # trade
              'ef_trade_tariffs_revenue', 'ef_trade_tariffs_revenue_data', 'ef_trade_tariffs_mean',
              'ef_trade_tariffs_mean_data', 'ef_trade_tariffs_sd', 'ef_trade_tariffs_sd_data', 'ef_trade_tariffs',
              'ef_trade_regulatory_nontariff', 'ef_trade_regulatory_compliance', 'ef_trade_regulatory',
              'ef_trade_black', 'ef_trade_movement_open', 'ef_trade_movement_capital', 'ef_trade_movement_visit',
              'ef_trade_movement', 'ef_trade',
              # regulation
              'ef_regulation_credit_ownership', 'ef_regulation_credit_private',
              'ef_regulation_credit_interest', 'ef_regulation_credit', 'ef_regulation_labor_minwage',
              'ef_regulation_labor_firing', 'ef_regulation_labor_bargain', 'ef_regulation_labor_hours',
              'ef_regulation_labor_dismissal', 'ef_regulation_labor_conscription', 'ef_regulation_labor',
              'ef_regulation_business_adm', 'ef_regulation_business_burden', 'ef_regulation_business_start',
              'ef_regulation_business_impartial', 'ef_regulation_business_licensing',
              'ef_regulation_business_compliance',
              'ef_regulation_business', 'ef_regulation',
              # economic freedom
              'ef_score', 'ef_rank']

df.to_csv('hfi2022_cc.csv', index=False)

no_countries = ['Armenia', 'Azerbaijan', 'Georgia', 'Kazakhstan', 'Kyrgyz Republic', 'Tajikistan']
df = df[~df['countries'].isin(no_countries)]

df.to_csv('hfi2022_ccopy.csv', index=False)
