import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('final.csv')
df.fillna('-', inplace=True)

str_columns = ['listscorepfmain', 'listscorepf', 'listscoreefmain', 'listscoreef', 'yearsmain2018', 'yearsmain2017',
               'yearsmain2016', 'yearsmain2015', 'yearsmain2014', 'yearsmain2013', 'yearsmain2012', 'yearsmain2011',
               'yearsmain2010', 'yearsmain2009', 'yearsmain2008', 'year2018', 'year2017', 'year2016', 'year2015',
               'year2014', 'year2013', 'year2012', 'year2011', 'year2010', 'year2009', 'year2008', 'dscore2018',
               'dscore2017', 'dscore2016', 'dscore2015', 'dscore2014', 'dscore2013', 'dscore2012', 'dscore2011',
               'dscore2010', 'dscore2009', 'dscore2008']

ranking_cols = ['ranking2018', 'ranking2017', 'ranking2016', 'ranking2015', 'ranking2014', 'ranking2013',
                'ranking2012', 'ranking2011', 'ranking2010', 'ranking2009', 'ranking2008']

# replace 'nan' with '-'
df[str_columns] = df[str_columns].replace('nan', '-', regex=True)

# remove decimal point from rankings
for i in ranking_cols:
    for j in df[i]:
        if j == '-':
            pass
        else:
            str('{:.0f}'.format(float(j)))


df.to_csv('/Users/glosophy/Dropbox/Human Freedom Index/2020/Data/final.csv', index=False)
