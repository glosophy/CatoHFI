import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# read csv
df = pd.read_csv('cleaning/hfi2022_cc.csv')

# 141 countries
countries = ['Belarus', 'Bhutan', 'Brunei Darussalam', 'Cabo Verde', 'Cambodia', 'Comoros', 'Djibouti', 'Eswatini',
             'Gambia, The', 'Guinea', 'Iraq', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Qatar',
             'Saudi Arabia', 'Seychelles', 'Somalia', 'Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste', 'Yemen, Rep.']

regions = df['region'].unique()

# selecting rows based on condition | ~ is not in
selected_df = df[~df['countries'].isin(countries)]


# -------------------------------------- function
# density plot
def density_plot(year1, year2, indicator='hf_score', all_regions=False):
    """
    It returns the density plot for a set of given years and indicator.
    year1: base year
    year2: comparison year
    indicator: any HFI indicator. Set to 'hf_score' by default
    all_regions: boolean for regions density plots
    """
    if all_regions:
        for i in range(len(regions)):
            reg1 = selected_df.loc[(selected_df['year'] == year1) & (selected_df['region'] == regions[i]), indicator]
            reg2 = selected_df.loc[(selected_df['year'] == year2) & (selected_df['region'] == regions[i]), indicator]
            sns.distplot(reg1, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year1))
            sns.distplot(reg2, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year2))
            plt.legend(prop={'size': 16}, title='{} Scores'.format(indicator))
            plt.title('Density Plot | {0} in {1}'.format(indicator, regions[i]))
            plt.xlabel('{}'.format(indicator))
            plt.ylabel('Density')
            plt.show()

    else:
        hfi1 = selected_df.loc[selected_df['year'] == year1, indicator]
        hfi2 = selected_df.loc[selected_df['year'] == year2, indicator]
        sns.distplot(hfi1, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year1))
        sns.distplot(hfi2, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year2))
        plt.legend(prop={'size': 16}, title='{} Scores'.format(indicator))
        plt.title('Density Plot | {} '.format(indicator))
        plt.xlabel('{}'.format(indicator))
        plt.ylabel('Density')

    return plt.show()

density_plot(2008, 2010, all_regions=False)