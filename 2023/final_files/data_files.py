import pandas as pd

df = pd.read_csv('../../2023/cleaning/hfi2023_cc.csv')
df.to_csv('HFI2023.csv', index=False)

# JSON
df.to_json('HFI2023.json')

# dta
df.to_stata('HFI2023.dta')
