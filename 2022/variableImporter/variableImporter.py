import pandas as pd
import numpy as np

# read csv
df = pd.read_csv('../../2022/cleaning/hfi2022_cc.csv')
no_countries = ['Armenia', 'Azerbaijan', 'Georgia', 'Kazakhstan', 'Kyrgyz Republic', 'Tajikistan']

# clean 'data' columns
for i in df.columns:
    if 'data' in i:
        df = df.drop(columns=[i])

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
                'ef_government_investment', 'ef_government_tax', 'ef_government_soa',
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

all_ef = ['ef_government', 'ef_government_consumption', 'ef_government_transfers', 'ef_government_investment',
          'ef_government_tax', 'ef_government_soa', 'ef_legal', 'ef_legal_judicial', 'ef_legal_courts',
          'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity', 'ef_legal_enforcement',
          'ef_legal_regulatory', 'ef_legal_police', 'ef_money', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
          'ef_money_currency', 'ef_trade', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
          'ef_trade_movement', 'ef_regulation', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

country_file = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Australia', 'Austria',
                'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia',
                'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina',
                'Burundi', 'CaboVerde', 'Cambodia', 'Cameroon', 'Canada',
                'CentralAfRep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                'CongoDem', 'CongoRep', 'CostaRica', 'CotedIvoire', 'Croatia',
                'Cyprus', 'Czech', 'Denmark', 'Djibouti', 'DominicanRep',
                'Ecuador', 'Egypt', 'Salvador', 'Estonia', 'Eswatini',
                'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
                'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'GuineaBissau', 'Guyana',
                'Haiti', 'Honduras', 'HongKong', 'Hungary', 'Iceland', 'India',
                'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
                'Jamaica', 'Japan', 'Jordan', 'Kenya', 'Korea', 'Kuwait',
                'Lao', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Mali',
                'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia',
                'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal',
                'Netherlands', 'NewZealand', 'Nicaragua', 'Niger', 'Nigeria',
                'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua',
                'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                'Russia', 'Rwanda', 'SaudiArabia', 'Senegal', 'Serbia',
                'Seychelles', 'SierraLeone', 'Singapore', 'Slovak', 'Slovenia',
                'Somalia', 'SouthAfrica', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden',
                'Switzerland', 'Syria', 'Taiwan', 'Tanzania',
                'Thailand', 'TimorLeste', 'Togo', 'Trinidad', 'Tunisia', 'Turkey',
                'Uganda', 'Ukraine', 'UnitedAE', 'UnitedKingdom',
                'UnitedStates', 'Uruguay', 'Venezuela', 'Vietnam', 'Yemen',
                'Zambia', 'Zimbabwe']


hf_nu = df[df['hf_score'].isnull()].index.tolist()
# print(hf_nu)
countries_nu = []
years_nu = []
for i in hf_nu:
    nu = df["countries"][i]
    ye = df["year"][i]
    countries_nu.append(nu)
    years_nu.append(ye)


for i in range(len(hf_nu)):
    for j in range(len(all_pf)):
        for k in range(len(df[all_pf[j]])):

            if df['countries'][k] == countries_nu[i] and df['year'][k] <= years_nu[i]:
                df[all_pf[j]][k] = np.nan
                df['pf_score'][k] = np.nan


country = df['countries'].unique().tolist()

for b in no_countries:
    country.remove(b)

country_name = [i.upper() for i in country]
region = [i.upper() for i in df.loc[df['year'] == 2000, 'region']]
ranking2020 = [int(i) for i in df.loc[df['year'] == 2020, 'hf_rank']]
hfscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'hf_score']]  # two decimal points
rankingpf = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2020, 'pf_rank']]
rankingef = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2020, 'ef_rank']]
pfscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'pf_score']]  # two decimal points
efscore2020 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2020, 'ef_score']]  # two decimal points


decimals = 1
df[df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_quartile', 'hf_score', 'pf_score', 'ef_score', 'ef_regulation_labor_dismissal'])]] = df[
    df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_quartile', 'hf_score', 'pf_score', 'ef_score', 'ef_regulation_labor_dismissal'])]].apply(
    lambda x: round(x, decimals))

df['hf_rank'] = pd.to_numeric(df['hf_rank'], downcast="integer")

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
        x = df.loc[(df['year'] == 2020) & (df['countries'] == i), j]
        print(x)
        pf.append(float(x))

    for k in main_ef:
        x = df.loc[(df['year'] == 2020) & (df['countries'] == i), k]
        ef.append(float(x))

    for l in other_cat_pf:
        x = df.loc[(df['year'] == 2020) & (df['countries'] == i), l]
        other_pf.append(float(x))

    for m in other_cat_ef:
        x = df.loc[(df['year'] == 2020) & (df['countries'] == i), m]
        other_ef.append(float(x))

    list_score_ef_main.append(ef)
    list_score_pf_main.append(pf)
    list_score_other_ef_main.append(other_ef)
    list_score_other_pf_main.append(other_pf)

# create list with final ef and pf values (main categories)
final_pf_main = []
for i in list_score_pf_main:
    a = str(i[0]) + '\n' * 6 + str(i[1]) + '\n' * 4 + str(i[2]) + '\n' * 4 + str(i[3]) + '\n' * 4 + str(
        i[4]) + '\n' * 6 \
        + str(i[5]) + '\n' * 7 + str(i[6])
    final_pf_main.append(a)

final_ef_main = []
for j in list_score_ef_main:
    a = str(j[0]) + '\n' * 7 + str(j[1]) + '\n' * 10 + str(j[2]) + '\n' * 6 + str(j[3]) + '\n' * 6 + str(j[4])
    final_ef_main.append(a)

# create a list with final ef and pf value (other categories)
final_other_ef_main = []
for i in list_score_other_ef_main:
    a = '\n' + str(i[0]) + '\n' + str(i[1]) + '\n' + str(i[2]) + '\n' + str(i[3]) + '\n' + str(i[4]) + '\n' * 3 + \
        str(i[5]) + '\n' + str(i[6]) + '\n' + str(i[7]) + '\n' + str(i[8]) + '\n' + str(i[9]) + '\n' + str(i[10]) + \
        '\n' + str(i[11]) + '\n' + str(i[12]) + '\n' * 3 + \
        str(i[13]) + '\n' + str(i[14]) + '\n' + str(i[15]) + '\n' + str(i[16]) + '\n' * 3 + \
        str(i[17]) + '\n' + str(i[18]) + '\n' + str(i[19]) + '\n' + str(i[20]) + '\n' * 3 + \
        str(i[21]) + '\n' + str(i[22]) + '\n' + str(i[23])
    final_other_ef_main.append(a)

final_other_pf_main = []
for i in list_score_other_pf_main:
    a = '\n' + str(i[0]) + '\n' + str(i[1]) + '\n' + str(i[2]) + '\n' + str(i[3]) + '\n' * 3 + \
        str(i[4]) + '\n' + str(i[5]) + '\n' * 3 + \
        str(i[6]) + '\n' + str(i[7]) + '\n' * 3 + \
        str(i[8]) + '\n' + str(i[9]) + '\n' * 3 + \
        str(i[10]) + '\n' + str(i[11]) + '\n' + str(i[12]) + '\n' + str(i[13]) + '\n' * 3 + \
        str(i[14]) + '\n' + str(i[15]) + '\n' + str(i[16]) + '\n' + str(i[17]) + '\n' + str(i[18]) + '\n' * 3 + \
        str(i[19]) + '\n' + str(i[20]) + '\n' + str(i[21]) + '\n' + str(i[22])
    final_other_pf_main.append(a)

# graph pf and ef
for co in range(len(country)):
    pf = []
    ef = []

    for j in all_pf:
        x = df.loc[(df['year'] == 2020) & (df['countries'] == country[co]), j]
        pf.append(float(x))

    for k in all_ef:
        x = df.loc[(df['year'] == 2020) & (df['countries'] == country[co]), k]
        ef.append(float(x))

    # personal freedom
    pos = [5, 9, 13, 17, 23, 30]
    acc = 0
    for i in range(len(pos)):
        pf.insert(pos[i], 0)
        acc += 1
    w = pd.DataFrame(pf)
    w = w.fillna(0)  # fillna with 0 for the bar chart
    w.to_csv('/Users/guillerminasutter/Dropbox/Human Freedom Index/2022/Data/GraphPF/{}.csv'.format(country_file[co]),
             index=False, header=False)

    # economic freedom
    pos = [6, 15, 20, 25]
    acc = 0
    for i in range(len(pos)):
        ef.insert(pos[i] + acc, 0)
        acc += 1
    w = pd.DataFrame(ef)
    w = w.fillna(0)  # fillna with 0 for the bar chart
    w.to_csv('/Users/guillerminasutter/Dropbox/Human Freedom Index/2022/Data/GraphEF/{}.csv'.format(country_file[co]),
             index=False, header=False)

# human freedom chart - order: country, world, region
selected = pd.read_csv('../../2022/selected_countries.csv')
selected = selected[~selected['countries'].isin(no_countries)]

# world average
world_avg = []
for i in selected['year'].unique():
    mean = selected.loc[selected['year'] == i, 'hf_score'].mean()
    world_avg.append(mean)

world_avg = world_avg[::-1]

# score countries
countries_score = []
region_score = []
for i in df['countries'].unique():

    country_hf = []

    cat_by_region = selected.groupby(['year', 'region'])['hf_score'].mean().reset_index()
    cat_pivot = cat_by_region.pivot(index='year', columns='region', values='hf_score')
    reg = df.loc[(df['year'] == 2000) & (df['countries'] == i), 'region'].values[0]

    reg_score = cat_pivot[str(reg)].to_list()
    region_score.append(reg_score)

    for j in df['year'].unique():
        hf_score = df.loc[(df['year'] == j) & (df['countries'] == i), 'hf_score']
        country_hf.append(float(hf_score))

    country_hf = country_hf[::-1]
    countries_score.append(country_hf)


for i in range(len(country)):
        hf_graph = {'hf': countries_score[i],
                    'world': world_avg,
                    'reg': region_score[i]}
        graph_df = pd.DataFrame(hf_graph)
        graph_df.to_csv('/Users/guillerminasutter/Dropbox/Human Freedom Index/2022/Data/GraphHF/{}.csv'.format(country_file[i]),
                        index=False, header=False)

# ranking graph
for i in range(len(country)):
    rank_country = []
    for j in df['year'].unique():
        ranking = df.loc[(df['year'] == j) & (df['countries'] == country[i]), 'hf_rank']
        rank_country.append(float(ranking))
    rank_country = rank_country[::-1]
    w = pd.DataFrame(rank_country)
    w.to_csv('/Users/guillerminasutter/Dropbox/Human Freedom Index/2022/Data/GraphRank/{}.csv'.format(country_file[i]),
             index=False, header=False)