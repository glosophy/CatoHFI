import wbdata
import pandas as pd

# set up the indicator
indicators = {'NY.GDP.PCAP.PP.KD': 'gdppc'}

gdp = wbdata.get_dataframe(indicators, convert_date=False)

gdp = gdp.reset_index()
gdp = gdp.rename(columns={'date': 'year'})

gdp.to_csv('gdpPerCap.csv', index=None)

