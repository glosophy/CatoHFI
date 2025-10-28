import pandas as pd
from math import trunc
pd.set_option('display.max_columns', None)

df = pd.read_csv('../../2025/variableImporter/final.csv')

df.fillna('-', inplace=True)


str_columns = ['listscorepfmain', 'listscorepf', 'listscoreefmain', 'listscoreef',
               'main2023', 'main2022', 'main2021', 'main2019', 'main2017', 'main2015', 'main2013',
               'main2011', 'main2009', 'main2007', 'main2005', 'main2000',
               'sub2023', 'sub2022', 'sub2021', 'sub2019', 'sub2017', 'sub2015', 'sub2013',
               'sub2011', 'sub2009', 'sub2007', 'sub2005', 'sub2000',
               'dscore2023', 'dscore2022', 'dscore2021', 'dscore2019', 'dscore2017', 'dscore2015', 'dscore2013',
               'dscore2011', 'dscore2009', 'dscore2007', 'dscore2005', 'dscore2000']

ranking_cols = ['ranking2023', 'ranking2022', 'ranking2021', 'ranking2019', 'ranking2017', 'ranking2015', 'ranking2013',
                'ranking2011', 'ranking2009', 'ranking2007', 'ranking2005', 'ranking2000']

# replace 'nan' with '-'
df[str_columns] = df[str_columns].replace('nan', '-', regex=True)

# remove decimal point from rankings
for i in ranking_cols:
    for j in df[i]:
        if j == '-':
            pass
        else:
            j = str(trunc(j))


df.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2025/Data/final.csv', index=False)
