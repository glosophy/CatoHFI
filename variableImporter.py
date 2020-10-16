import pandas as pd
import numpy as np

df = pd.read_csv('all_countries.csv')

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



country = df['countries'].unique()
country_name = [i.upper() for i in country]
region = [i.upper() for i in df.loc[df['year']==2018, 'region']]
ranking2018 = [int(i) for i in df.loc[df['year']==2018, 'hf_rank']]
hfscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year']==2018, 'hf_score']] # two decimal points
rankingpf = [(str(int(i))+'/162') for i in df.loc[df['year']==2018, 'pf_rank']]
rankingef = [(str(int(i))+'/162') for i in df.loc[df['year']==2018, 'ef_rank']]
pfscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year']==2018, 'pf_score']] # two decimal points
efscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year']==2018, 'ef_score']] # two decimal points

# personal freedom main categories
pf_main = []
for i in country:
    pf = []
    for j in main_pf:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), j]
        pf.append(float(x))
    pf_main.append(pf)

for i in pf_main:
    a = str(i[0]) + '\n'*4 + str(i[1]) + '\n'*4 + str(i[2]) + '\n'*4 + str(i[3]) + '\n'*5 + str(i[4]) + '\n'*6 + str(i[5]) + '\n'*7 + str(i[6])
    print(str(a))


# personal freedom main categories
list_score_pf_main = []
for i in country:
    pf = []
    for j in main_pf:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), j]
        pf.append(float(x))
    list_score_pf_main.append(pf)

for i in list_score_pf_main:
    a = str(i[0]) + '\n'*4 + str(i[1]) + '\n'*4 + str(i[2]) + '\n'*4 + str(i[3]) + '\n'*5 + str(i[4]) + '\n'*6 + str(i[5]) + '\n'*7 + str(i[6])
    print(str(a))

PF = 4, 4, 4, 5, 6, 7
EF = 6, 9, 5, 3
PF_rest = 1, 2, 2, 2, 2, 2
EF_rest = 1, 2, 2, 2, 2, 2

# print(list_score_pf_main[0])