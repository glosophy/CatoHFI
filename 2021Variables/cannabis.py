import pandas as pd
import re
desired_width = 320
pd.set_option('display.width', desired_width)

# read table with pandas
tables = pd.read_html('https://en.wikipedia.org/wiki/Legality_of_cannabis')

# print total number of tables
print(f'Total number of tables: {len(tables)}')
print('---------'*7)

# print first rows of tables in the wiki page
# for i in range(len(tables)):
#   print(tables[i].head())

# create table with selected
df = tables[0]
print(df.head())
print('---------'*7)

# print dataframe info
print(df.info())
print('---------'*7)

# print columns of dataframe
print(df.columns)
print('---------'*7)

# print unique values of 'Recreational' column
print('Unique values in Recreational column:')
print(df['Recreational'].unique())
print('---------'*7)

# print unique values of 'Recreational' column
print('Unique values in Medical column:')
print(df['Medical'].unique())
print('---------'*7)

pattern = r'\[.*?\]'
for i in df['Recreational']:
    i = re.sub(pattern, '', i)

print(df['Recreational'].unique())