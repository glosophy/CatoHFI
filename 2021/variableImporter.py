import pandas as pd
import numpy as np
import os

cwd = os.getcwd()

df = pd.read_csv(cwd + '/' + 'all_countries.csv')


main_pf = ['pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_association', 'pf_expression', 'pf_identity']
main_ef = ['ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation']

other_cat_pf = ['pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_ss_homicide',
                'pf_ss_disappearances', 'pf_ss_women', 'pf_movement_domestic', 'pf_movement_foreign',
                'pf_movement_women', 'pf_religion_freedom', 'pf_religion_repression',
                'pf_religion_harassment', 'pf_religion_restrictions', 'pf_association_entry',
                'pf_association_assembly', 'pf_association_estopparties', 'pf_association_opposition',
                'pf_association_civilrepression', 'pf_expression_killed', 'pf_expression_jailed',
                'pf_expression_media', 'pf_expression_cable', 'pf_expression_newspapers', 'pf_expression_control',
                'pf_identity_legal', 'pf_identity_sex', 'pf_identity_divorce']

other_cat_ef = ['ef_government_consumption', 'ef_government_transfers',
                'ef_government_enterprises', 'ef_government_tax', 'ef_government_soa',
                'ef_legal_judicial', 'ef_legal_courts', 'ef_legal_protection', 'ef_legal_military',
                'ef_legal_integrity', 'ef_legal_enforcement', 'ef_legal_regulatory',
                'ef_legal_police', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
                'ef_money_currency', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
                'ef_trade_movement', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

all_pf = ['pf_rol', 'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_ss', 'pf_ss_homicide',
          'pf_ss_disappearances', 'pf_ss_women', 'pf_movement', 'pf_movement_domestic',
          'pf_movement_foreign', 'pf_movement_women', 'pf_religion', 'pf_religion_freedom',
          'pf_religion_repression', 'pf_religion_harassment', 'pf_religion_restrictions', 'pf_association',
          'pf_association_entry', 'pf_association_assembly', 'pf_association_estopparties', 'pf_association_opposition',
          'pf_association_civilrepression', 'pf_expression', 'pf_expression_killed', 'pf_expression_jailed',
          'pf_expression_media', 'pf_expression_cable', 'pf_expression_newspapers', 'pf_expression_control',
          'pf_identity', 'pf_identity_legal', 'pf_identity_sex', 'pf_identity_divorce']

all_ef = ['ef_government', 'ef_government_consumption', 'ef_government_transfers', 'ef_government_enterprises',
          'ef_government_tax', 'ef_government_soa', 'ef_legal', 'ef_legal_judicial', 'ef_legal_courts',
          'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity', 'ef_legal_enforcement',
          'ef_legal_regulatory', 'ef_legal_police', 'ef_money', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
          'ef_money_currency', 'ef_trade', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
          'ef_trade_movement', 'ef_regulation', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

country_file = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria',
                'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia',
                'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi',
                'Cabo', 'Cambodia', 'Cameroon', 'Canada', 'Central', 'Chad', 'Chile', 'China', 'Colombia',
                'Congodem', 'Congorep', 'Costa', 'Cote', 'Croatia', 'Cyprus', 'Czech', 'Denmark',
                'Dominican', 'Ecuador', 'Egypt', 'Salvador', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji',
                'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
                'Greece', 'Guatemala', 'Guinea', 'Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong',
                'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
                'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea', 'Kuwait', 'Kyrgyz',
                'Lao', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg',
                'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
                'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal',
                'Netherlands', 'Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Macedonia', 'Norway', 'Oman',
                'Pakistan', 'Panama', 'Papua', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
                'Qatar', 'Romania', 'Russian', 'Rwanda', 'Saudi', 'Senegal', 'Serbia', 'Seychelles',
                'Leone', 'Singapore', 'Slovak', 'Slovenia', 'Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                'Sweden', 'Switzerland', 'Syrian', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor',
                'Togo', 'Trinidad', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'Emirates', 'Kingdom', 'UnitedStates',
                'Uruguay', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
