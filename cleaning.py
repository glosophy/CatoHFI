import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('HFI 2020.csv')

columns = ['year', 'ISO_code', 'countries', 'region', 'hf_score', 'hf_score_NO_GENDER', 'hf_rank', 'hf_quartile',
           'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol', 'pf_ss_homicide',
           'pf_ss_disappearances_disap', 'pf_ss_disappearances_violent', 'pf_ss_disappearances_organized',
           'pf_ss_disappearances_fatalities', 'pf_ss_disappearances_injuries', 'pf_ss_disappearances',
           'pf_ss_women_fgm', 'pf_ss_women_inheritance_widows', 'pf_ss_women_inheritance_daughters',
           'pf_ss_women_inheritance', 'pf_ss_women', 'pf_ss', 'pf_movement_domestic', 'pf_movement_foreign',
           'pf_movement_women', 'pf_movement', 'pf_religion_estop_establish', 'pf_religion_estop_operate',
           'pf_religion_estop', 'pf_religion_freedom', 'pf_religion_repression', 'pf_religion_harassment', 'pf_religion_restrictions',
           'pf_religion', 'pf_association_entry', 'pf_association_assembly', 'pf_association_barries',
           'pf_association_bans', 'pf_association_estopparties', 'pf_association_opposition',
           'pf_association_civilrepression', 'pf_association', 'pf_expression_killed',
           'pf_expression_jailed', 'pf_expression_media', 'pf_expression_cable', 'pf_expression_newspapers',
           'pf_expression_control', 'pf_expression', 'pf_identity_legal',
           'pf_identity_sex_male', 'pf_identity_sex_female', 'pf_identity_sex', 'pf_identity_divorce',
           'pf_identity', 'pf_identity_NO_GENDER', 'pf_score', 'pf_score_NO_GENDER', 'pf_rank', 'ef_government_consumption', 'ef_government_transfers',
           'ef_government_enterprises', 'ef_government_tax_income', 'ef_government_tax_payroll',
           'ef_government_tax', 'ef_government_soa', 'ef_government', 'ef_legal_judicial', 'ef_legal_courts',
           'ef_legal_protection', 'ef_legal_military', 'ef_legal_integrity', 'ef_legal_enforcement',
           'ef_legal_regulatory', 'ef_legal_police', 'ef_legal_gender', 'ef_legal',
           'ef_money_growth', 'ef_money_sd', 'ef_money_inflation', 'ef_money_currency', 'ef_money',
           'ef_trade_tariffs_revenue', 'ef_trade_tariffs_mean', 'ef_trade_tariffs_sd', 'ef_trade_tariffs',
           'ef_trade_regulatory_nontariff', 'ef_trade_regulatory_compliance', 'ef_trade_regulatory',
           'ef_trade_black', 'ef_trade_movement_foreign', 'ef_trade_movement_capital', 'ef_trade_movement_visit',
           'ef_trade_movement', 'ef_trade', 'ef_regulation_credit_ownership', 'ef_regulation_credit_private',
           'ef_regulation_credit_interest', 'ef_regulation_credit', 'ef_regulation_labor_minwage',
           'ef_regulation_labor_firing', 'ef_regulation_labor_bargain', 'ef_regulation_labor_hours',
           'ef_regulation_labor_dismissal', 'ef_regulation_labor_conscription', 'ef_regulation_labor',
           'ef_regulation_business_adm', 'ef_regulation_business_bureaucracy', 'ef_regulation_business_start',
           'ef_regulation_business_bribes', 'ef_regulation_business_licensing', 'ef_regulation_business_compliance',
           'ef_regulation_business', 'ef_regulation', 'ef_score', 'ef_rank']

drop = []
for i in df.columns:
    if 'DATA' in i:
        df = df.drop(columns=[i])

# assign columns to df
df.columns = columns

# drop association and inheritance columns
df = df.drop(columns=['pf_religion_estop_establish', 'pf_religion_estop_operate', 'pf_religion_estop',
                      'pf_ss_women_inheritance_widows', 'pf_ss_women_inheritance_daughters'])

# clean up the '-' and turn into numeric
df = df.replace(to_replace='-',value='')
cols = df.columns.drop(['year', 'ISO_code', 'countries', 'region'])
df[cols] = df[cols].apply(pd.to_numeric)

# calculate the rest of the columns
df['womens_freedom'] = df[['pf_ss_women_inheritance', 'pf_ss_women', 'pf_ss_women_fgm',
                            'pf_movement_women', 'pf_identity_sex_female']].mean(axis=1)

countries = ['Belarus', 'Bhutan', 'Brunei Darussalam', 'Cabo Verde', 'Cambodia', 'Eswatini',
             'Gambia, The', 'Guinea', 'Iraq', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Qatar',
             'Saudi Arabia', 'Seychelles', 'Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste', 'Yemen, Rep.']

regions = ['Latin America & the Caribbean', 'Sub-Saharan Africa', 'Middle East & North Africa',
           'Caucasus & Central Asia', 'Eastern Europe', 'South Asia', 'Western Europe', 'East Asia',
           'Oceania', 'North America']

# selecting rows based on condition | ~ is not in
selected_df = df[~df['countries'].isin(countries)]
selected_df.to_csv('selected_countries.csv', index=False)
df.to_csv('all_countries.csv', index=False)

hfi2008 = selected_df.loc[selected_df['year'] == 2008, 'hf_score_NO_GENDER']
hfi2018 = selected_df.loc[selected_df['year'] == 2018, 'hf_score_NO_GENDER']
sns.distplot(hfi2008, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2008')
sns.distplot(hfi2018, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2018')
plt.legend(prop={'size': 16}, title = 'Human Freedom Scores')
plt.title('Density Plot | Human Freedom Scores (w/o Gender)')
plt.xlabel('Human Freedom')
plt.ylabel('Density')
plt.show()

pf2008 = selected_df.loc[selected_df['year'] == 2008, 'pf_score_NO_GENDER']
pf2018 = selected_df.loc[selected_df['year'] == 2018, 'pf_score_NO_GENDER']
sns.distplot(pf2008, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2008')
sns.distplot(pf2018, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2018')
plt.legend(prop={'size': 16}, title = 'Personal Freedom Scores')
plt.title('Density Plot | Personal Freedom Scores (w/o Gender)')
plt.xlabel('Personal Freedom')
plt.ylabel('Density')
plt.show()

# countries that improved and deteriorated
selected2018 = selected_df.loc[selected_df['year'] == 2018, 'hf_score_NO_GENDER']
selected2008 = selected_df.loc[selected_df['year'] == 2008, 'hf_score_NO_GENDER']
diff_selected = np.array(selected2018) - np.array(selected2008)

all2018 = df.loc[df['year'] == 2018, 'hf_score']
all2017 = df.loc[df['year'] == 2017, 'hf_score']
all_diff = np.array(all2018) - np.array(all2017)
all_change_hf = np.mean(np.array(all2018)) - np.mean(np.array(all2017))
print('-'*25)
print('Change in HFI score (2017-2018):', round(all_change_hf, 3))
print('HFI 2017:', round(np.mean(np.array(all2017)), 3))
print('HFI 2018:', round(np.mean(np.array(all2018)), 3))
print('-'*25)

selected_decreased = 0
selected_improved = 0
selected_same = 0
for i in diff_selected:
    if i > 0:
        selected_improved += 1
    if i < 0:
        selected_decreased += 1
    if i == 0:
        selected_same += 1

print('Countries that improved/decreased (2008-2018):')
print('Improved countries:', selected_improved)
print('Decreased countries:', selected_decreased)
print('No changes in score:', selected_same)
print('-'*25)

decreased = 0
improved = 0
same = 0
for i in all_diff:
    if i > 0:
        improved += 1
    if i < 0:
        decreased += 1
    if i == 0:
        same += 1

print('Countries that improved/decreased (2017-2018):')
print('Improved countries:', improved)
print('Decreased countries:', decreased)
print('No changes in score:', same)
print('-'*25)

# top 10% countries lost or gained freedom between 2008 and 2018?
hfi2008 = np.sort(hfi2008)
hfi2018 = np.sort(hfi2018)
mean2008 = hfi2008[-14:].mean()
mean2018 = hfi2018[-14:].mean()

print('Mean 2008:', round(mean2008, 2))
print('Mean 2018:', round(mean2018, 2))
print('-'*25)

# gap between the lowest and highest score
by_quartile = selected_df.groupby(['year', 'hf_quartile'])['hf_score_NO_GENDER'].mean().reset_index()

quartile = list(range(1, 5))
def plot_quartiles(quartile):
    for i in quartile:
        a = by_quartile.loc[by_quartile['hf_quartile'] == i, 'hf_score_NO_GENDER']
        plt.plot((list(range(2008,2019))), a, label=i)
        plt.legend(title='Quartiles', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.title('HFI Score w/o Gender by Quartile Over Time')
        plt.xlabel('Year')
        plt.ylabel('Score')
    return plt.show()

plot_quartiles(quartile)

# highest and lowest HFI score over time
low = []
high = []
for i in range(2008, 2019):
    a = selected_df.loc[selected_df['year'] == i, 'hf_score_NO_GENDER']
    minValue = a.min()
    maxValue = a.max()
    low.append(minValue)
    high.append(maxValue)

plt.plot(list(range(2008,2019)), high, label='Highest Score')
plt.plot(list(range(2008,2019)), low, label='Lowest Score')
plt.legend(title='Score', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Highest and Lowest HFI Score w/o Gender Over Time')
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()


diff2008 = high[0] - low[0]
diff2018 = high[-1] - low[-1]
print('Gap between highest and lowest score:')
print('Gap 2008:', round(diff2008, 2))
print('Gap 2018:', round(diff2018, 2))
print('-'*25)

# top 10% countries
lowest10 = []
highest10 = []
for i in range(2008, 2019):
    a = selected_df.loc[selected_df['year'] == i, 'hf_score_NO_GENDER']
    a = np.sort(a)
    highest = a[-14:].mean()
    lowest = a[:14].mean()
    lowest10.append(lowest)
    highest10.append(highest)

plt.plot(list(range(2008,2019)), highest10, label='Highest 10%')
plt.plot(list(range(2008,2019)), lowest10, label='Lowest 10%')
plt.legend(title='Score', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Highest and Lowest 10% HFI Score w/o Gender Over Time')
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()

diff2008_10 = highest10[0] - lowest10[0]
diff2018_10 = highest10[-1] - lowest10[-1]
print('Gap between highest and lowest 10%:')
print('Gap 2008:', round(diff2008_10, 2))
print('Gap 2018:', round(diff2018_10, 2))
print('-'*25)


# highest improvements and deteriorations across categories 2008-2018
by_quartile = by_quartile.pivot(index='year', columns='hf_quartile', values='hf_score_NO_GENDER')
by_quartile['diff_quartile'] = by_quartile.iloc[:,0] - by_quartile.iloc[:,-1]
print(by_quartile)
print('-'*25)

# changes en categories for quartiles
print('Gap between Q1 and Q4:')
print('Gap 2008:', round(by_quartile.iloc[0, -1], 2))
print('Gap 2018:', round(by_quartile.iloc[-1, -1], 2))
print('-'*25)

# changes in women's freedoms by region:
print("Women's Freedoms (2008-2018):")
for i in range(len(regions)):
    a2008 = selected_df.loc[(selected_df['year'] == 2008) & (selected_df['region'] == regions[i]), 'womens_freedom']
    a2018 = selected_df.loc[(selected_df['year'] == 2018) & (selected_df['region'] == regions[i]), 'womens_freedom']
    a2008 = round(np.mean(np.array(a2008)), 2)
    a2018 = round(np.mean(np.array(a2018)), 2)
    diff_score = a2018 - a2008
    print(regions[i], round(diff_score, 2))
print('-'*25)


# regions
by_region = selected_df.groupby(['year', 'region'])['hf_score_NO_GENDER'].mean().reset_index()
region_pivot = by_region.pivot(index='year', columns='region', values='hf_score_NO_GENDER')
region_pivot.to_csv('regions.csv', index=False)

main_categories = ['hf_score_NO_GENDER', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_association', 'pf_expression',
                   'pf_identity_NO_GENDER', 'pf_score_NO_GENDER', 'ef_government',
                   'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'ef_score']

cat_df = []
for i in main_categories:
  cat_by_region = selected_df.groupby(['year', 'region'])[i].mean().reset_index()
  cat_pivot = cat_by_region.pivot(index='year', columns='region', values=i)
  cat_df.append(cat_pivot)
  cat_pivot = cat_pivot.reset_index()
  cat_pivot.to_csv('CAT_{}.csv'.format(i), index=False)

for i in range(len(cat_df)):
    df = cat_df[i]
    col = df.columns
    df = df.reset_index()
    cat_diff = []
    for j in col:
        year2008 = df[j][0]
        year2018 = df[j][10]
        diff = year2018 - year2008
        cat_diff.append(diff)
    cat_diff = np.array(cat_diff)
    minValue = cat_diff.min()
    maxValue = cat_diff.max()
    minIndex = np.where(cat_diff == minValue)
    maxIndex = np.where(cat_diff == maxValue)
    print('Category:', main_categories[i])
    stringMax = str(col[maxIndex])
    stringMax = stringMax.split('[')[1]
    stringMax = stringMax.split(']')[0]

    stringMin = str(col[minIndex])
    stringMin = stringMin.split('[')[1]
    stringMin = stringMin.split(']')[0]

    print('Most improved region (2008-2018):', stringMax, round(maxValue, 2))
    print('Most deteriorated region (2008-2018):', stringMin, round(minValue, 2))
    print('-' * 25)


# see distribution over time of major regions: MENA, Sub-Saharan Africa, Caucasus, LatAm

for i in range(len(regions)):
    a2008 = selected_df.loc[(selected_df['year'] == 2008) & (selected_df['region'] == regions[i]), 'hf_score_NO_GENDER']
    a2018 = selected_df.loc[(selected_df['year'] == 2018) & (selected_df['region'] == regions[i]), 'hf_score_NO_GENDER']
    sns.distplot(a2008, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2008')
    sns.distplot(a2018, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2018')
    plt.legend(title='Human Freedom Score')
    plt.title('Density Plot | Human Freedom in {0}'.format(regions[i]))
    plt.xlabel('Human Freedom')
    plt.ylabel('Density')
    plt.show()


# Overall religion + Regions: North America, South Asia, and MENA
religion_region =  ['Middle East & North Africa', 'North America', 'South Asia']

religion = selected_df.groupby(['year'])['pf_religion'].mean()
cat_by_region = selected_df.groupby(['year', 'region'])['pf_religion'].mean().reset_index()
cat_pivot = cat_by_region.pivot(index='year', columns='region', values='pf_religion')

for i in religion_region:
  a = np.array(cat_pivot[i])
  plt.plot(range(2008,2019), a, label = i)
religion.plot(label = 'Overall Religion')
plt.legend(title='Religion Score', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Religion in MENA, North America, and South Asia')
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()


