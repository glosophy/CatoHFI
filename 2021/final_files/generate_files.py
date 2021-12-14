import pandas as pd
import os

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/' + 'all_countries.csv')
df = df.drop(['pf_rol_wgi'], axis=1)
df.to_csv(cwd + '/final_files/HFI2021.csv', index=False)

# JSON
df.to_json(cwd + '/final_files/' + 'HFI2021.json')

# dta
df.to_stata(cwd + '/final_files/' + 'HFI2021.dta')
