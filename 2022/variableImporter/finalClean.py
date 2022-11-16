import pandas as pd
import os
pd.set_option('display.max_columns', None)

df = pd.read_csv('../../2022/variableImporter/final.csv')
df.fillna('-', inplace=True)

str_columns = ['listscorepfmain', 'listscorepf', 'listscoreefmain', 'listscoreef',
               'main2020', 'main2019', 'main2018', 'main2016', 'main2014', 'main2012', 'main2010',
               'main2008', 'main2006', 'main2004', 'main2002', 'main2000',
               'sub2020', 'sub2019', 'sub2018', 'sub2016', 'sub2014', 'sub2012', 'sub2010',
               'sub2008', 'sub2006', 'sub2004', 'sub2002', 'sub2000',
               'dscore2020', 'dscore2019', 'dscore2018', 'dscore2016', 'dscore2014', 'dscore2012', 'dscore2010',
               'dscore2008', 'dscore2006', 'dscore2004', 'dscore2002', 'dscore2000']

ranking_cols = ['ranking2020', 'ranking2019', 'ranking2018', 'ranking2016', 'ranking2014', 'ranking2012', 'ranking2010',
                'ranking2008', 'ranking2006', 'ranking2004', 'ranking2002', 'ranking2000']

# replace 'nan' with '-'
df[str_columns] = df[str_columns].replace('nan', '-', regex=True)

# remove decimal point from rankings
for i in ranking_cols:
    for j in df[i]:
        if j == '-':
            pass
        else:
            j = str(int(j))


df.to_csv('/Users/guillerminasutter/Dropbox/Human Freedom Index/2022/Data/final.csv', index=False)