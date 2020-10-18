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
region = [i.upper() for i in df.loc[df['year'] == 2018, 'region']]
ranking2018 = [int(i) for i in df.loc[df['year'] == 2018, 'hf_rank']]
hfscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year'] == 2018, 'hf_score']] # two decimal points
rankingpf = [(str(int(i))+'/162') for i in df.loc[df['year'] == 2018, 'pf_rank']]
rankingef = [(str(int(i))+'/162') for i in df.loc[df['year'] == 2018, 'ef_rank']]
pfscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year'] == 2018, 'pf_score']] # two decimal points
efscore2018 = ['{:.2f}'.format(i) for i in df.loc[df['year'] == 2018, 'ef_score']] # two decimal points


# personal and economic freedom categories
list_score_pf_main = []
list_score_ef_main = []
list_score_other_pf_main = []
list_score_other_ef_main = []
for i in country:
    pf = []
    ef = []
    other_pf = []
    other_ef = []

    for j in main_pf:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), j]
        pf.append(float(x))

    for k in main_ef:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), k]
        ef.append(float(x))

    for l in other_cat_pf:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), l]
        other_pf.append(float(x))

    for m in other_cat_ef:
        x = df.loc[(df['year'] == 2018) & (df['countries'] == i), m]
        other_ef.append(float(x))

    list_score_ef_main.append(ef)
    list_score_pf_main.append(pf)
    list_score_other_ef_main.append(other_ef)
    list_score_other_pf_main.append(other_pf)


# create list with final ef and pf values (main categories)
final_pf_main = []
for i in list_score_pf_main:
    a = str(i[0]) + '\n'*4 + str(i[1]) + '\n'*4 + str(i[2]) + '\n'*4 + str(i[3]) + '\n'*5 + str(i[4]) + '\n'*6 \
        + str(i[5]) + '\n'*7 + str(i[6])
    final_pf_main.append(a)

final_ef_main = []
for j in list_score_ef_main:
    a = str(j[0]) + '\n'*6 + str(j[1]) + '\n'*9 + str(j[2]) + '\n'*5 + str(j[3]) + '\n'*3 + str(j[4])
    final_ef_main.append(a)

# create a list with final ef and pf value (other categories)
final_other_ef_main = []
for i in list_score_other_ef_main:
    a = '\n'*2 + str(i[0]) + '\n' + str(i[1]) + '\n' + str(i[2]) + '\n' + str(i[3]) + '\n' + str(i[4]) + '\n'*3 + \
        str(i[5]) + '\n' + str(i[6]) + '\n' + str(i[7]) + '\n' + str(i[8]) + '\n' + str(i[9]) + '\n' + str(i[10]) + \
        '\n' + str(i[11]) + '\n' + str(i[12]) + '\n'*3 + \
        str(i[13]) + '\n' + str(i[14]) + '\n' + str(i[15]) + '\n' + str(i[16]) + '\n'*3 + \
        str(i[17]) + '\n' + str(i[18]) + '\n' + str(i[19]) + '\n' + str(i[20]) + '\n'*3 + \
        str(i[21]) + '\n' + str(i[22]) + '\n' + str(i[23])
final_other_ef_main.append(a)

final_other_pf_main = []
for i in list_score_other_pf_main:
    a = '\n'*2 + str(i[0]) + '\n' + str(i[1]) + '\n' + str(i[2]) + '\n'*3 + \
        str(i[3]) + '\n' + str(i[4]) + '\n' + str(i[5]) + '\n'*3 + \
        str(i[6]) + '\n' + str(i[7]) + '\n' + str(i[8]) + '\n'*3 + \
        str(i[9]) + '\n' + str(i[10]) + '\n' + str(i[11]) + '\n' + str(i[12]) + '\n'*3 + \
        str(i[13]) + '\n' + str(i[14]) + '\n' + str(i[15]) + '\n' + str(i[16]) + '\n' + str(i[17]) + '\n'*3 + \
        str(i[18]) + '\n' + str(i[19]) + '\n' + str(i[20]) + '\n' + str(i[21]) + '\n' + str(i[22]) + '\n' + str(i[23]) + '\n'*3 + \
        str(i[24]) + '\n' + str(i[25]) + '\n' + str(i[26])
    final_other_pf_main.append(a)


