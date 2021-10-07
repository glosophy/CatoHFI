import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/' + 'HFI2021.csv')
print('Raw shape:', df.shape)

# clean 'data' columns
for i in df.columns:
    if 'data' in i:
        df = df.drop(columns=[i])
print('Clean shape:', df.shape)

columns = ['year', 'countries', 'region', 'hf_score', 'hf_rank', 'hf_quartile',
           'pf_rol_procedural', 'pf_rol_civil', 'pf_rol_criminal', 'pf_rol_wgi', 'pf_rol',
           'pf_ss_homicide', 'pf_ss_disappearances_disap', 'pf_ss_disappearances_violent', 'pf_ss_disappearances_organized',
           'pf_ss_disappearances_fatalities', 'pf_ss_disappearances_injuries', 'pf_ss_disappearances_torture',
           'pf_ss_killings', 'pf_ss_disappearances', 'pf_ss',
           'pf_movement_vdem_foreign', 'pf_movement_vdem_men', 'pf_movement_vdem_women', 'pf_movement_vdem',
           'pf_movement_cld', 'pf_movement',
           'pf_religion_suppression', 'pf_religion_freedom_vdem', 'pf_religion_freedom_cld', 'pf_religion_freedom',
           'pr_religion',
           'pf_assembly_entry', 'pf_assembly_freedom_house', 'pf_assembly_freedom_bti',
           'pf_assembly_freedom_cld', 'pf_assembly_freedom', 'pf_assembly_parties_barriers', 'pf_assembly_parties_bans',
           'pf_assembly_parties_auton', 'pf_assembly_parties', 'pf_assembly_civil', 'pf_assembly', 'pf_assembly_rank',
           'pf_expression_killed', 'pf_expression_jailed', 'pf_expression_media', 'pf_expression_cultural',
           'pf_expression_gov', 'pf_expression_internet', 'pf_expression_harass', 'pf_expression_selfcens',
           'pf_expression_freedom_bti', 'pf_expression_freedom_cld', 'pf_expression_freedom', 'pf_expression',
           'pf_expression_rank',
           'pf_identity_same_m', 'pf_identity_same_f', 'pf_identity_same', 'pf_identity_divorce', 'pf_identity_fgm',
           'pf_identity_inheritance_widows', 'pf_identity_inheritance_daughters', 'pf_identity_inheritance',
           'pf_identity',
           'pf_score', 'pf_rank', 'pf_womens',
           'ef_size', 'ef_property', 'ef_money', 'ef_trade', 'ef_regulation', 'ef_score', 'ef_rank']

# assign columns to df
df.columns = columns

# clean up the '-' and turn into numeric
df = df.replace(to_replace='-',value='')
cols = df.columns.drop(['year', 'countries', 'region'])
df[cols] = df[cols].apply(pd.to_numeric)

countries = ['Belarus', 'Bhutan', 'Brunei Darussalam', 'Cabo Verde', 'Cambodia', 'Comoros', 'Djibouti', 'Eswatini',
             'Gambia, The', 'Guinea', 'Iraq', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Qatar',
             'Saudi Arabia', 'Seychelles', 'Somalia','Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste', 'Yemen, Rep.']

regions = ['Latin America & the Caribbean', 'Sub-Saharan Africa', 'Middle East & North Africa',
           'Caucasus & Central Asia', 'Eastern Europe', 'South Asia', 'Western Europe', 'East Asia',
           'Oceania', 'North America']

# selecting rows based on condition | ~ is not in
selected_df = df[~df['countries'].isin(countries)]
selected_df.to_csv('selected_countries.csv', index=False)
df.to_csv('all_countries.csv', index=False)

hfi2008 = selected_df.loc[selected_df['year'] == 2008, 'hf_score']
hfi2019 = selected_df.loc[selected_df['year'] == 2019, 'hf_score']
sns.distplot(hfi2008, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2008')
sns.distplot(hfi2019, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2019')
plt.legend(prop={'size': 16}, title = 'Human Freedom Scores')
plt.title('Density Plot | Human Freedom Scores')
plt.xlabel('Human Freedom')
plt.ylabel('Density')
plt.show()

