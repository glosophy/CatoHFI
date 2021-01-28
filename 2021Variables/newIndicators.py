import pandas as pd
pd.set_option('display.max_rows', 500)
import os

# get cwd
cwd = os.getcwd()

WB_indicators = ['A woman can apply for a passport in the same way as a man (1=yes; 0=no)',
                 'A woman can be head of household in the same way as a man (1=yes; 0=no)',
                 'A woman can choose where to live in the same way as a man (1=yes; 0=no)',
                 'A woman can get a job in the same way as a man (1=yes; 0=no)',
                 'A woman can obtain a judgment of divorce in the same way as a man (1=yes; 0=no)',
                 'A woman can open a bank account in the same way as a man (1=yes; 0=no)',
                 'A woman can register a business in the same way as a man (1=yes; 0=no)',
                 'A woman can sign a contract in the same way as a man (1=yes; 0=no)',
                 'A woman can travel outside her home in the same way as a man (1=yes; 0=no)',
                 'A woman can travel outside the country in the same way as a man (1=yes; 0=no)',
                 'A woman has the same rights to remarry as a man (1=yes; 0=no)',
                 "Decision maker about a woman's own health care: mainly husband (% of women age 15-49)",
                 "Decision maker about a woman's own health care: mainly wife (% of women age 15-49)",
                 "Decision maker about a woman's own health care: other (% of women age 15-49)",
                 "Decision maker about a woman's own health care: someone else (% of women age 15-49)",
                 "Decision maker about a woman's own health care: wife and husband jointly (% of women age 15-49)",
                 "Decision maker about a woman's visits to her family or relatives: mainly husband (% of women age 15-49)",
                 "Decision maker about a woman's visits to her family or relatives: mainly wife (% of women age 15-49)",
                 "Decision maker about a woman's visits to her family or relatives: other (% of women age 15-49)",
                 "Decision maker about a woman's visits to her family or relatives: someone else (% of women age 15-49)",
                 'Female genital mutilation prevalence (%)',
                 'Female genital mutilation prevalence (%): Q1 (lowest)',
                 'Female genital mutilation prevalence (%): Q2',
                 'Female genital mutilation prevalence (%): Q3',
                 'Female genital mutilation prevalence (%): Q4',
                 'Female genital mutilation prevalence (%): Q5 (highest)',
                 'The government administers 100% of maternity leave benefits (1=yes; 0=no)',
                 'The law grants spouses equal administrative authority over assets during marriage (1=yes; 0=no)',
                 'There is no legal provision that requires a married woman to obey her husband (1=yes; 0=no)',
                 'Time required to start a business, female (days)',
                 'Time required to start a business, male (days)',
                 'Women are able to work in the same industries as men (1=yes; 0=no)',
                 'Women can work in jobs deemed dangerous in the same way as men (1=yes; 0=no)',
                 'Women can work the same night hours as men (1=yes; 0=no)',
                 'Women making their own informed decisions regarding sexual relations, contraceptive use and reproductive health care  (% of women age 15-49)',
                 'Women participating in decision of visits to family, relatives, friends (% of women age 15-49)',
                 'Women participating in decision of what food to cook daily (% of women age 15-49)',
                 'Women participating in making daily purchase decisions (% of women age 15-49)',
                 'Women participating in making major household purchase decisions (% of women age 15-49)',
                 'Women participating in none of the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)',
                 'Women participating in own health care decisions (% of women age 15-49)',
                 'Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)']

WB = pd.read_csv('Gender_StatsEXCEL.csv')

# print columns
print('WB Columns:')
print(WB.columns)
print('-------' * 10)

print(len(WB_indicators))

# see countries covered
countries = WB['Country Name'].unique()

# filter by selected WB indicators
WB = WB[WB['Indicator Name'].isin(WB_indicators)]

# filter out regions
regions = ['Arab World', 'Caribbean small states', 'Central Europe and the Baltics',
           'Early-demographic dividend', 'East Asia & Pacific',
           'East Asia & Pacific (excluding high income)',
           'East Asia & Pacific (IDA & IBRD)', 'Euro area', 'Europe & Central Asia',
           'Europe & Central Asia (excluding high income)',
           'Europe & Central Asia (IDA & IBRD)', 'European Union',
           'Fragile and conflict affected situations',
           'Heavily indebted poor countries (HIPC)', 'High income', 'IBRD only',
           'IDA & IBRD total', 'IDA blend', 'IDA only', 'IDA total',
           'Late-demographic dividend', 'Latin America & Caribbean',
           'Latin America & Caribbean (excluding high income)',
           'Latin America & Caribbean (IDA & IBRD)',
           'Least developed countries: UN classification', 'Low & middle income',
           'Low income', 'Lower middle income', 'Middle East & North Africa',
           'Middle East & North Africa (excluding high income)',
           'Middle East & North Africa (IDA & IBRD)', 'Middle income', 'North America',
           'OECD members', 'Other small states', 'Pacific island small states',
           'Post-demographic dividend', 'Pre-demographic dividend', 'Small states',
           'South Asia', 'South Asia (IDA & IBRD)', 'Sub-Saharan Africa',
           'Sub-Saharan Africa (excluding high income)',
           'Sub-Saharan Africa (IDA & IBRD)', 'Upper middle income', 'World']

print(regions)

WB = WB[~WB['Country Name'].isin(regions)]

# check countries and data points for each year for each indicator
for i in WB_indicators:
    a = WB.loc[WB['Indicator Name'] == i]
    print('-------' * 10)
    print(i)
    print(a.count())
