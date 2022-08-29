import pandas as pd
import numpy as np

# read csv
df = pd.read_csv('../cleaning/hfi2022_cc.csv')

# 141 countries
countries = ['Belarus', 'Bhutan', 'Brunei Darussalam', 'Cabo Verde', 'Cambodia', 'Comoros', 'Djibouti', 'Eswatini',
             'Gambia, The', 'Guinea', 'Iraq', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Qatar',
             'Saudi Arabia', 'Seychelles', 'Somalia', 'Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste', 'Yemen, Rep.']

regions = df['region'].unique()

