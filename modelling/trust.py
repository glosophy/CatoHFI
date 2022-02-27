import pandas as pd

trust = pd.read_csv('WVS_TimeSeries_1981_2020_ascii_v2_0.csv')

trust = trust[['COUNTRY_ALPHA', 'S020', 'A165', 'A170', 'A169']]

trust = trust.rename(columns={'COUNTRY_ALPHA': 'ISO'})

trust.to_csv('trust.csv', index=None)