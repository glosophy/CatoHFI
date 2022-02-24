import pandas as pd

xls = pd.ExcelFile('pwt100.xls')
penn = pd.read_excel(xls, 'Data')

cols = penn.columns

penn = penn.drop(['currency_unit', 'rgdpe', 'rgdpo',
                  'pop', 'emp', 'avh', 'ccon', 'cda', 'cgdpe', 'cgdpo', 'cn', 'ck',
                  'ctfp', 'cwtfp', 'rgdpna', 'rconna', 'rdana', 'rnna', 'rkna', 'rtfpna',
                  'rwtfpna', 'labsh', 'irr', 'delta', 'xr', 'pl_con', 'pl_da', 'pl_gdpo',
                  'i_cig', 'i_xm', 'i_xr', 'i_outlier', 'i_irr', 'cor_exp', 'statcap',
                  'csh_c', 'csh_i', 'csh_g', 'csh_x', 'csh_m', 'csh_r', 'pl_c', 'pl_i',
                  'pl_g', 'pl_x', 'pl_m', 'pl_n', 'pl_k'], axis=1)

penn = penn.rename(columns={'countrycode': 'ISO'})

penn.to_csv('penn.csv', index=None)