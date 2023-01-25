import pandas as pd


df = pd.read_csv('../../2022/cleaning/hfi2022_cc.csv')
df.to_csv('HFI2022.csv', index=False)

# JSON
df.to_json('HFI2022.json')

# dta
df.to_stata('HFI2022.dta')
