import pandas as pd
import numpy as np
import os

cwd = os.getcwd()

df = pd.read_csv(cwd + '/' + 'all_countries.csv')

main_pf = ['pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression', 'pf_identity']
main_ef = ['ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation']

other_cat_pf = ['pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal',
                'pf_ss_homicide', 'pf_ss_disappearances',
                'pf_movement_vdem', 'pf_movement_cld',
                'pf_religion_freedom', 'pf_religion_suppression',
                'pf_assembly_entry', 'pf_assembly_freedom', 'pf_assembly_parties', 'pf_assembly_civil',
                'pf_expression_killed', 'pf_expression_jailed', 'pf_expression_media', 'pf_expression_cultural',
                'pf_expression_gov', 'pf_expression_internet', 'pf_expression_harass', 'pf_expression_selfcens',
                'pf_expression_freedom',
                'pf_identity_same', 'pf_identity_divorce', 'pf_identity_inheritance', 'pf_identity_fgm']

other_cat_ef = ['ef_government_consumption', 'ef_government_transfers',
                'ef_government_enterprises', 'ef_government_tax', 'ef_government_soa',
                'ef_legal_judicial', 'ef_legal_courts', 'ef_legal_protection', 'ef_legal_military',
                'ef_legal_integrity', 'ef_legal_enforcement', 'ef_legal_regulatory',
                'ef_legal_police', 'ef_money_growth', 'ef_money_sd', 'ef_money_inflation',
                'ef_money_currency', 'ef_trade_tariffs', 'ef_trade_regulatory', 'ef_trade_black',
                'ef_trade_movement', 'ef_regulation_credit', 'ef_regulation_labor', 'ef_regulation_business']

all_pf = ['pf_rol', 'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal',
          'pf_ss', 'pf_ss_homicide', 'pf_ss_disappearances',
          'pf_movement', 'pf_movement_vdem', 'pf_movement_cld',
          'pf_religion', 'pf_religion_freedom', 'pf_religion_suppression',
          'pf_assembly', 'pf_assembly_entry', 'pf_assembly_freedom', 'pf_assembly_parties', 'pf_assembly_civil',
          'pf_expression', 'pf_expression_killed', 'pf_expression_jailed', 'pf_expression_media',
          'pf_expression_cultural', 'pf_expression_gov', 'pf_expression_internet', 'pf_expression_harass',
          'pf_expression_selfcens', 'pf_expression_freedom',
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

#
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

            # print("before", df[all_pf[j]][k])
            # print(df["countries"][k])
            # print(countries_nu[i])
            # print(df["year"][k])
            # print(years_nu[i])
            #
            # print("---------")

            if df["countries"][k] == countries_nu[i] and df["year"][k] <= years_nu[i]:
                df[all_pf[j]][k] = np.nan
                df["pf_score"][k] = np.nan
                # print(df[all_pf[j]][k])

print(df["pf_rol"])

country = df['countries'].unique()
country_name = [i.upper() for i in country]
region = [i.upper() for i in df.loc[df['year'] == 2019, 'region']]
ranking2019 = [int(i) for i in df.loc[df['year'] == 2019, 'hf_rank']]
hfscore2019 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2019, 'hf_score']]  # two decimal points
rankingpf = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2019, 'pf_rank']]
rankingef = [(str(int(i)) + '/165') for i in df.loc[df['year'] == 2019, 'ef_rank']]
pfscore2019 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2019, 'pf_score']]  # two decimal points
efscore2019 = [str('{:.2f}'.format(i)) for i in df.loc[df['year'] == 2019, 'ef_score']]  # two decimal points

decimals = 1
df[df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_score', 'pf_score', 'ef_score'])]] = df[
    df.columns[~df.columns.isin(['countries', 'region', 'year', 'hf_score', 'pf_score', 'ef_score'])]].apply(
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
        x = df.loc[(df['year'] == 2019) & (df['countries'] == i), j]
        pf.append(float(x))

    for k in main_ef:
        x = df.loc[(df['year'] == 2019) & (df['countries'] == i), k]
        ef.append(float(x))

    for l in other_cat_pf:
        x = df.loc[(df['year'] == 2019) & (df['countries'] == i), l]
        other_pf.append(float(x))

    for m in other_cat_ef:
        x = df.loc[(df['year'] == 2019) & (df['countries'] == i), m]
        other_ef.append(float(x))

    list_score_ef_main.append(ef)
    list_score_pf_main.append(pf)
    list_score_other_ef_main.append(other_ef)
    list_score_other_pf_main.append(other_pf)

# create list with final ef and pf values (main categories)
final_pf_main = []
for i in list_score_pf_main:
    a = str(i[0]) + '\n' * 5 + str(i[1]) + '\n' * 4 + str(i[2]) + '\n' * 4 + str(i[3]) + '\n' * 4 + str(
        i[4]) + '\n' * 6 \
        + str(i[5]) + '\n' * 11 + str(i[6])
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
    a = '\n' + str(i[0]) + '\n' + str(i[1]) + '\n' + str(i[2]) + '\n' * 3 + \
        str(i[3]) + '\n' + str(i[4]) + '\n' * 3 + \
        str(i[5]) + '\n' + str(i[6]) + '\n' * 3 + \
        str(i[7]) + '\n' + str(i[8]) + '\n' * 3 + \
        str(i[9]) + '\n' + str(i[10]) + '\n' + str(i[11]) + '\n' + str(i[12]) + '\n' * 3 + \
        str(i[13]) + '\n' + str(i[14]) + '\n' + str(i[15]) + '\n' + str(i[16]) + '\n' + str(i[17]) + '\n' + str(
        i[18]) + '\n' + str(i[19]) + '\n' + str(i[20]) + '\n' + str(i[21]) + '\n' * 3 + \
        str(i[22]) + '\n' + str(i[23]) + '\n' + str(i[24]) + '\n' + str(i[25])
    final_other_pf_main.append(a)

# graph pf and ef
for co in range(len(country)):
    pf = []
    ef = []

    for j in all_pf:
        x = df.loc[(df['year'] == 2019) & (df['countries'] == country[co]), j]
        pf.append(float(x))

    for k in all_ef:
        x = df.loc[(df['year'] == 2019) & (df['countries'] == country[co]), k]
        ef.append(float(x))

    # personal freedom
    pos = [4, 8, 12, 16, 22, 33]
    acc = 0
    for i in range(len(pos)):
        pf.insert(pos[i], 0)
        acc += 1
    w = pd.DataFrame(pf)
    w = w.fillna(0)  # fillna with 0 for the bar chart
    w.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphPF/{}.csv'.format(country_file[co]),
             index=False, header=False)

    # economic freedom
    pos = [6, 15, 20, 25]
    acc = 0
    for i in range(len(pos)):
        ef.insert(pos[i] + acc, 0)
        acc += 1
    w = pd.DataFrame(ef)
    w = w.fillna(0)  # fillna with 0 for the bar chart
    w.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphEF/{}.csv'.format(country_file[co]),
             index=False, header=False)

# human freedom chart - order: country, world, region
selected = pd.read_csv('selected_countries.csv')

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
    reg = df.loc[(df['year'] == 2019) & (df['countries'] == i), 'region'].values[0]
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
    graph_df.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphHF/{}.csv'.format(country_file[i]),
                    index=False, header=False)

# ranking graph
for i in range(len(country)):
    rank_country = []
    for j in df['year'].unique():
        ranking = df.loc[(df['year'] == j) & (df['countries'] == country[i]), 'hf_rank']
        rank_country.append(float(ranking))
    rank_country = rank_country[::-1]
    w = pd.DataFrame(rank_country)
    w.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphRank/{}.csv'.format(country_file[i]),
             index=False, header=False)

# main years second page
list_score_pf_main_page2 = []
list_score_other_pf_main_page2 = []
for k in df['year'].unique():
    pf = []
    other_pf = []

    for i in country:
        years_main = []
        years_other = []
        for j in main_pf:
            x = df.loc[(df['year'] == k) & (df['countries'] == i), j]
            years_main.append(float(x))

        for l in other_cat_pf:
            x = df.loc[(df['year'] == k) & (df['countries'] == i), l]
            years_other.append(float(x))

        pf.append(years_main)
        other_pf.append(years_other)

    years_pf_pf = []
    for m in pf:
        a = str(m[0]) + '\n' * 5 + str(m[1]) + '\n' * 4 + str(m[2]) + '\n' * 4 + str(m[3]) + '\n' * 4 + str(
            m[4]) + '\n' * 6 \
            + str(m[5]) + '\n' * 11 + str(m[6])
        years_pf_pf.append(a)

    years_other_other = []
    for n in other_pf:
        b = str(n[0]) + '\n' + str(n[1]) + '\n' + str(n[2]) + '\n' * 3 + \
            str(n[3]) + '\n' + str(n[4]) + '\n' * 3 + \
            str(n[5]) + '\n' + str(n[6]) + '\n' * 3 + \
            str(n[7]) + '\n' + str(n[8]) + '\n' * 3 + \
            str(n[9]) + '\n' + str(n[10]) + '\n' + str(n[11]) + '\n' + str(n[12]) + '\n' * 3 + \
            str(n[13]) + '\n' + str(n[14]) + '\n' + str(n[15]) + '\n' + str(n[16]) + '\n' + str(n[17]) + '\n' + str(
            n[18]) + '\n' + str(n[19]) + '\n' + str(n[20]) + '\n' + str(n[21]) + '\n' * 3 + \
            str(n[22]) + '\n' + str(n[23]) + '\n' + str(n[24]) + '\n' + str(n[25])
        years_other_other.append(b)

    list_score_pf_main_page2.append(years_pf_pf)
    list_score_other_pf_main_page2.append(years_other_other)

# score country by year
score_year = []
for k in df['year'].unique():
    score = []
    for i in country:
        x = df.loc[(df['year'] == k) & (df['countries'] == i), 'hf_score']
        x = float(x)
        score.append('{:.2f}'.format(x))
    score_year.append(score)

# ranking by year
rank_year = []
for k in df['year'].unique():
    rank = []
    for i in country:
        x = df.loc[(df['year'] == k) & (df['countries'] == i), 'hf_rank']
        x = float(x)
        rank.append('{:.2f}'.format(x))
    rank_year.append(rank)

# dscores:
dscore = []
for k in df['year'].unique():
    midstep = []
    for i in country:
        x = df.loc[(df['year'] == k) & (df['countries'] == i), 'pf_score'].values[0]
        y = df.loc[(df['year'] == k) & (df['countries'] == i), 'ef_score'].values[0]
        # x = float(x)
        # y = float(y)
        a = str('{:.2f}'.format(y)) + '\n' + str('{:.2f}'.format(x))
        midstep.append(a)
    dscore.append(midstep)

scores = []
for i in df['year'].unique():
    midstep = []
    for k in country:
        x = df.loc[(df['year'] == i) & (df['countries'] == k), 'hf_score'].values[0]
        midstep.append(str('{:.2f}'.format(float(x))))
    scores.append(midstep)

rank_years = []
for i in df['year'].unique():
    midstep2 = []
    for k in country:
        x = df.loc[(df['year'] == i) & (df['countries'] == k), 'hf_rank'].values[0]
        midstep2.append(str('{:.0f}'.format(float(x))))
    rank_years.append(midstep2)

# create dictionary with all variables
d = {'countryname': country_name,
     'country': country,
     'region': region,
     'ranking': ranking2019,
     'score': hfscore2019,
     'rankingpf': rankingpf,
     'scorepf': pfscore2019,
     'rankingef': rankingef,
     'scoreef': efscore2019,
     'listscorepfmain': final_pf_main,
     'listscorepf': final_other_pf_main,
     '%graphpf': ['/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphPF/{}.csv'.format(co) for co in
                  country_file],
     'listscoreefmain': final_ef_main,
     'listscoreef': final_other_ef_main,
     '%graphef': ['/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphEF/{}.csv'.format(co) for co in
                  country_file],
     '%graphscorehf': ['/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphHF/{}.csv'.format(co) for co in
                       country_file],
     '%graphrankinghf': ['/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/GraphRank/{}.csv'.format(co) for co in
                         country_file],
     'main2019': list_score_pf_main_page2[0],
     'main2018': list_score_pf_main_page2[1],
     'main2017': list_score_pf_main_page2[2],
     'main2016': list_score_pf_main_page2[3],
     'main2015': list_score_pf_main_page2[4],
     'main2014': list_score_pf_main_page2[5],
     'main2013': list_score_pf_main_page2[6],
     'main2012': list_score_pf_main_page2[7],
     'main2011': list_score_pf_main_page2[8],
     'main2010': list_score_pf_main_page2[9],
     'main2009': list_score_pf_main_page2[10],
     'main2008': list_score_pf_main_page2[11],
     'sub2019': list_score_other_pf_main_page2[0],
     'sub2018': list_score_other_pf_main_page2[1],
     'sub2017': list_score_other_pf_main_page2[2],
     'sub2016': list_score_other_pf_main_page2[3],
     'sub2015': list_score_other_pf_main_page2[4],
     'sub2014': list_score_other_pf_main_page2[5],
     'sub2013': list_score_other_pf_main_page2[6],
     'sub2012': list_score_other_pf_main_page2[7],
     'sub2011': list_score_other_pf_main_page2[8],
     'sub2010': list_score_other_pf_main_page2[9],
     'sub2009': list_score_other_pf_main_page2[10],
     'sub2008': list_score_other_pf_main_page2[11],
     'dscore2019': dscore[0],
     'dscore2018': dscore[1],
     'dscore2017': dscore[2],
     'dscore2016': dscore[3],
     'dscore2015': dscore[4],
     'dscore2014': dscore[5],
     'dscore2013': dscore[6],
     'dscore2012': dscore[7],
     'dscore2011': dscore[8],
     'dscore2010': dscore[9],
     'dscore2009': dscore[10],
     'dscore2008': dscore[11],
     'score2019': scores[0],
     'score2018': scores[1],
     'score2017': scores[2],
     'score2016': scores[3],
     'score2015': scores[4],
     'score2014': scores[5],
     'score2013': scores[6],
     'score2012': scores[7],
     'score2011': scores[8],
     'score2010': scores[9],
     'score2009': scores[10],
     'score2008': scores[11],
     'ranking2019': rank_years[0],
     'ranking2018': rank_years[1],
     'ranking2017': rank_years[2],
     'ranking2016': rank_years[3],
     'ranking2015': rank_years[4],
     'ranking2014': rank_years[5],
     'ranking2013': rank_years[6],
     'ranking2012': rank_years[7],
     'ranking2011': rank_years[8],
     'ranking2010': rank_years[9],
     'ranking2009': rank_years[10],
     'ranking2008': rank_years[11]}

# create Dataframe
df_final = pd.DataFrame(d)
df_final.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/final.csv', index=False)
df_final.to_csv('final.csv', index=False)

print('csv FILE CREATED! :)')