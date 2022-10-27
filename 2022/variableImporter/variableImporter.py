import pandas as pd
import numpy as np

# read csv
df = pd.read_csv('../../2022/cleaning/hfi2022_cc.csv')

# categories
main_pf = ['pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression', 'pf_identity']
main_ef = ['ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation']

other_cat_pf = ['pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol_vdem',
                'pf_ss_homicide', 'pf_ss_disappearances',
                'pf_movement_vdem', 'pf_movement_cld',
                'pf_religion_freedom', 'pf_religion_suppression',
                'pf_assembly_entry', 'pf_assembly_freedom', 'pf_assembly_parties', 'pf_assembly_civil',
                'pf_expression_direct', 'pf_expression_vdem', 'pf_expression_house', 'pf_expression_bti',
                'pf_expression_cld',
                'pf_identity_same', 'pf_identity_divorce', 'pf_identity_inheritance', 'pf_identity_fgm']

other_cat_ef = ['ef_government_consumption', 'ef_government_transfers',
                'ef_government_enterprises', 'ef_government_tax', 'ef_government_soa',
                'ef_legal_judicial', 'ef_legal_courts', 'ef_legal_protection', 'ef_legal_military',
                'ef_legal_integrity', 'ef_legal_enforcement', 'ef_legal_regulatory',
                'ef_legal_police', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
                'ef_money_currency', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
                'ef_trade_movement', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

all_pf = ['pf_rol', 'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol_vdem',
          'pf_ss', 'pf_ss_homicide', 'pf_ss_disappearances',
          'pf_movement', 'pf_movement_vdem', 'pf_movement_cld',
          'pf_religion', 'pf_religion_freedom', 'pf_religion_suppression',
          'pf_assembly', 'pf_assembly_entry', 'pf_assembly_freedom', 'pf_assembly_parties', 'pf_assembly_civil',
          'pf_expression', 'pf_expression_direct', 'pf_expression_vdem', 'pf_expression_house',
          'pf_expression_bti', 'pf_expression_cld',
          'pf_identity', 'pf_identity_same', 'pf_identity_divorce', 'pf_identity_inheritance', 'pf_identity_fgm']

all_ef = ['ef_government', 'ef_government_consumption', 'ef_government_transfers', 'ef_government_enterprises',
          'ef_government_tax', 'ef_government_soa', 'ef_legal', 'ef_legal_judicial', 'ef_legal_courts',
          'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity', 'ef_legal_enforcement',
          'ef_legal_regulatory', 'ef_legal_police', 'ef_money', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
          'ef_money_currency', 'ef_trade', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
          'ef_trade_movement', 'ef_regulation', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

country_file = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria',
                'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia',
                'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina',
                'Burundi', 'CaboVerde', 'Cambodia', 'Cameroon', 'Canada',
                'CentralAfRep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                'CongoDem', 'CongoRep', 'CostaRica', 'CotedIvoire', 'Croatia',
                'Cyprus', 'Czech', 'Denmark', 'Djibouti', 'DominicanRep',
                'Ecuador', 'Egypt', 'Salvador', 'Estonia', 'Eswatini',
                'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
                'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'GuineaBissau', 'Guyana',
                'Haiti', 'Honduras', 'HongKong', 'Hungary', 'Iceland', 'India',
                'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
                'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea', 'Kuwait',
                'Kyrgyz', 'Lao', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Mali',
                'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia',
                'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal',
                'Netherlands', 'NewZealand', 'Nicaragua', 'Niger', 'Nigeria',
                'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua',
                'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                'Russia', 'Rwanda', 'SaudiArabia', 'Senegal', 'Serbia',
                'Seychelles', 'SierraLeone', 'Singapore', 'Slovak', 'Slovenia',
                'Somalia', 'SouthAfrica', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden',
                'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
                'Thailand', 'TimorLeste', 'Togo', 'Trinidad', 'Tunisia', 'Turkey',
                'Uganda', 'Ukraine', 'UnitedAE', 'UnitedKingdom',
                'UnitedStates', 'Uruguay', 'Venezuela', 'Vietnam', 'Yemen',
                'Zambia', 'Zimbabwe']

hf_nu = df[df['hf_score'].isnull()].index.tolist()
print(hf_nu)
countries_nu = []
years_nu = []
for i in hf_nu:
    nu = df["countries"][i]
    ye = df["year"][i]
    countries_nu.append(nu)
    years_nu.append(ye)

print(countries_nu)
print(years_nu)

print(len(countries_nu))
print(len(years_nu))
print(len(hf_nu))

for i in range(len(hf_nu)):
    for j in range(len(all_pf)):
        for k in range(len(df[all_pf[j]])):

            if df["countries"][k] == countries_nu[i] and df["year"][k] <= years_nu[i]:
                df[all_pf[j]][k] = np.nan
                df["pf_score"][k] = np.nan
                # print(df[all_pf[j]][k])


country = df['countries'].unique()
country_name = [i.upper() for i in country]
region = [i.upper() for i in df.loc[df['year'] == 2020, 'region']]
ranking2020 = [int(i) for i in df.loc[df['year'] == 2020, 'hf_rank']]
hfscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'hf_score']]  # two decimal points
rankingpf = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2020, 'pf_rank']]
rankingef = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2020, 'ef_rank']]
pfscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'pf_score']]  # two decimal points
efscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'ef_score']]  # two decimal points

decimals = 1
df[df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_score', 'pf_score', 'ef_score'])]] = df[
    df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_score', 'pf_score', 'ef_score'])]].apply(
    lambda x: round(x, decimals))

df['hf_rank'] = pd.to_numeric(df['hf_rank'], downcast="integer")