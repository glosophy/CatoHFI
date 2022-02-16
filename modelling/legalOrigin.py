import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)

# Leer las tablas en pandas
religion_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_national_legal_systems')

# Imprimir el número total de tablas
print(f'Número total de tablas: {len(religion_tables)}')

# Civil Law
dfCivilLaw = religion_tables[0]
dfCivilLaw = dfCivilLaw.drop(['Description'], axis=1)
dfCivilLaw['legalOrigin'] = 'Civil Law'

# Common Law
dfCommonLaw = religion_tables[1]
dfCommonLaw = dfCommonLaw.drop(['Description'], axis=1)
dfCommonLaw['legalOrigin'] = 'Common Law'

# Religious Law
dfReligiousLaw = religion_tables[2]
dfReligiousLaw = dfReligiousLaw.drop(['Description'], axis=1)
dfReligiousLaw['legalOrigin'] = 'Religious Law'

# Civil law + common law
dfCivComLaw = religion_tables[4]
dfCivComLaw = dfCivComLaw.drop(['Description'], axis=1)
dfCivComLaw['legalOrigin'] = 'Civil and Common Law'

# Civil + Sharia law
dfCivShariaLaw = religion_tables[5]
dfCivShariaLaw = dfCivShariaLaw.drop(['Description'], axis=1)
dfCivShariaLaw['legalOrigin'] = 'Civil and Sharia Law'

# Common + Sharia law
dfCommonShariaLaw = religion_tables[6]
dfCommonShariaLaw = dfCommonShariaLaw.drop(['Description'], axis=1)
dfCommonShariaLaw['legalOrigin'] = 'Common and Sharia Law'

# Concat and export as csv
legalOrigin = pd.concat([dfCivilLaw, dfCommonLaw, dfReligiousLaw, dfCivComLaw, dfCivShariaLaw, dfCommonShariaLaw],
                        axis=0)

legalOrigin.to_csv('legalOrigin.csv', index=False)