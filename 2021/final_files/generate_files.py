import pandas as pd
import os

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/' + 'all_countries.csv')

# JSON
df.to_json(cwd + '/final_files/' + 'HFI2021.json')

# dta
df.to_stata(cwd + '/final_files/' + 'HFI2021.dta')

