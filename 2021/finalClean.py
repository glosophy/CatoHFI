import pandas as pd
import os
pd.set_option('display.max_columns', None)

cwd = os.getcwd()

df = pd.read_csv(cwd + '/' + 'final.csv')
df.fillna('-', inplace=True)

str_columns = ['listscorepfmain', 'listscorepf', 'listscoreefmain', 'listscoreef', 
               'main2019', 'main2018', 'main2017', 'main2016', 'main2015', 'main2014', 
               'main2013', 'main2012', 'main2011', 'main2010', 'main2009', 'main2008', 
               'sub2019', 'sub2018', 'sub2017', 'sub2016', 'sub2015', 'sub2014', 'sub2013', 'sub2012', 
               'sub2011', 'sub2010', 'sub2009', 'sub2008', 
               'dscore2019', 'dscore2018', 'dscore2017', 'dscore2016', 'dscore2015', 'dscore2014', 
               'dscore2013', 'dscore2012', 'dscore2011', 'dscore2010', 'dscore2009', 'dscore2008']

ranking_cols = ['ranking2019', 'ranking2018', 'ranking2017', 'ranking2016', 'ranking2015', 'ranking2014', 
                'ranking2013', 'ranking2012', 'ranking2011', 'ranking2010', 'ranking2009', 'ranking2008']

# replace 'nan' with '-'
df[str_columns] = df[str_columns].replace('nan', '-', regex=True)

# remove decimal point from rankings
for i in ranking_cols:
    for j in df[i]:
        if j == '-':
            pass
        else:
            j = str(int(j))


df.to_csv('/Users/guillermina/Dropbox/Human Freedom Index/2021/Data/final.csv', index=False)