import pandas as pd

df = pd.read_csv('../../2024/cleaning/hfi2024_cc.csv')
df.to_csv('HFI2024.csv', index=False)

# JSON
df.to_json('HFI2024.json')

# dta
df.to_stata('HFI2024.dta')
