import pandas as pd

vdem = pd.read_csv('V-Dem-CY-Full+Others-v10.csv')
print(vdem.head(5))

# Check dtypes
print(vdem.dtypes)


df = vdem[['year', 'country_name', 'v2clacfree', 'v2cltort', 'v2clkill', 'v2clfmove', 'v2cldmovem', 'v2cldmovew',
           'v2cldiscm', 'v2cldiscw', 'v2meharjrn', 'v2meslfcen', 'v2mecenefm', 'v2mecenefi']]

# great2008 = df['year'] >= 2008
# vdem_2008 = df[great2008]

print(df.columns)
print(len(df['country_name'].unique()))


df.to_csv('vdemFinalIndicators.csv')