import pandas as pd
import pycountry

pca = pd.read_csv('PCA.csv')
kMeans = pd.read_csv('kmeans.csv')
factor = pd.read_csv('factors.csv')

# Merge dfs
result = pd.merge(pca, kMeans, how='outer', on=['ISO', 'year', 'countries', 'hf_score', 'hf_quartile'])
final = pd.merge(result, factor, how='outer', on=['ISO', 'year', 'countries', 'hf_score', 'hf_quartile'])


def find_country(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_2
    except:
        return 'not found'


def findalpha2(alpha_3):
    try:
        return pycountry.countries.get(alpha_3=alpha_3).alpha_2
    except:
        return 'not found'


final['ISO2'] = final.apply(lambda row: findalpha2(row.ISO), axis=1)

# Merge other dataframes
latLong = pd.read_csv('latLong.csv')
final = pd.merge(final, latLong, how='left', on=['ISO2'])

# Fix Namibia
latNA = -22.95764
longNA = 18.49041

final.loc[final['ISO2'] == 'NA', 'latitude'] = latNA
final.loc[final['ISO2'] == 'NA', 'longitude'] = longNA

# Merge polity
polity = pd.read_excel('p5v2018.xls')
polity = polity.drop(['change', 'cyear', 'ccode', 'country', 'flag', 'fragment', 'polity2', 'durable', 'xrreg',
                      'xrcomp', 'xropen', 'xconst', 'parreg', 'parcomp', 'exrec', 'exconst',
                      'polcomp', 'prior', 'emonth', 'eday', 'eyear', 'eprec', 'interim',
                      'bmonth', 'bday', 'byear', 'bprec', 'post', 'd5', 'sf',
                      'regtrans'], axis=1)

polity = polity.rename(columns={'scode': 'ISO', 'oldName2': 'newName2'})

final = pd.merge(final, polity, how='left', on=['ISO', 'year'])

# Merge Happiness
happiness = pd.read_excel('happiness.xls')
happiness = happiness.rename(columns={'Country name': 'countries'})

happiness['ISO2'] = happiness.apply(lambda row: find_country(row.countries), axis=1)

list_NF = happiness.loc[happiness.ISO2 == 'not found', 'countries']

unique_listNF = list_NF.unique()
keysNF = ['BO', 'CG', 'CD', 'CZ', 'HK', 'IR', 'CI', 'nan', 'LA', 'MD', 'CY', 'nan', 'RU', 'SO', 'KR',
          'SZ', 'SY', 'TW', 'TZ', 'VE', 'VN']

for i in range(len(unique_listNF)):
    happiness.loc[happiness['countries'] == unique_listNF[i], 'ISO2'] = keysNF[i]

final = pd.merge(final, happiness, how='left', on=['ISO2', 'year'])

# Legal origin
legal = pd.read_csv('legalOrigin.csv')

legal['ISO2'] = legal.apply(lambda row: find_country(row.Country), axis=1)

legal_NF = legal.loc[legal.ISO2 == 'not found', 'Country']
unique_legalNF = legal_NF.unique()

legal_keysNF = ['BO', 'CN', 'CD', 'CG', 'CV', 'CZ', 'nan', 'CI', 'nan', 'TW', 'RU', 'nan', 'KR', 'SY', 'nan',
                'VN', 'VE', 'nan', 'GB', 'nan', 'nan', 'IR', 'nan', 'nan', 'nan', 'nan', 'BN', 'GM', 'nan']

for i in range(len(unique_legalNF)):
    legal.loc[legal['Country'] == unique_legalNF[i], 'ISO2'] = legal_keysNF[i]

final = pd.merge(final, legal, how='left', on=['ISO2'])

# Reorder columns
final = final[['year', 'countries_x', 'country', 'countries_y', 'Country', 'ISO', 'ISO2', 'latitude', 'longitude',
               'hf_score', 'hf_quartile', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion',
               'pf_assembly', 'pf_expression', 'pf_identity', 'ef_government',
               'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'legalOrigin',
               'Cluster', 'PC1', 'PC2', 'PC3', 'F1', 'F2', 'F3', 'p5', 'democ',
               'autoc', 'polity', 'Life Ladder', 'Log GDP per capita',
               'Social support', 'Healthy life expectancy at birth',
               'Freedom to make life choices', 'Generosity',
               'Perceptions of corruption', 'Positive affect', 'Negative affect']]

# Export final file
final.to_csv('modellingFile.csv', index=False)

# Export only columns we need for analysis
excel = final[['year', 'countries_x', 'ISO', 'latitude', 'longitude',
               'hf_score', 'hf_quartile', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion',
               'pf_assembly', 'pf_expression', 'pf_identity', 'ef_government',
               'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'legalOrigin',
               'Cluster', 'PC1', 'PC2', 'PC3', 'F1', 'F2', 'F3', 'p5', 'democ',
               'autoc', 'polity', 'Life Ladder', 'Log GDP per capita',
               'Social support', 'Healthy life expectancy at birth',
               'Freedom to make life choices', 'Generosity',
               'Perceptions of corruption', 'Positive affect', 'Negative affect']]

excel.to_csv('allData.csv', index=False)