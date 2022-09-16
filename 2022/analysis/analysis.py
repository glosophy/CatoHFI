import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import math

warnings.simplefilter(action='ignore', category=FutureWarning)

# read csv
df = pd.read_csv('/Users/guillerminasutter/PycharmProjects/CatoHFI/2022/cleaning/hfi2022_cc.csv')

# 141 countries
countries = ['Belarus', 'Bhutan', 'Brunei Darussalam', 'Cabo Verde', 'Cambodia', 'Comoros', 'Djibouti', 'Eswatini',
             'Gambia, The', 'Guinea', 'Iraq', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Qatar',
             'Saudi Arabia', 'Seychelles', 'Somalia', 'Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste', 'Yemen, Rep.']

regions = df['region'].unique()

# selecting rows based on condition | ~ is not in
selected_df = df[~df['countries'].isin(countries)]


# -------------------------------------- functions
# density plot
def density_plot(year1, year2, indicator='hf_score', all_regions=False):
    """
    This function plots density plots for regions, and a set of given indicators.
    :param: year1: base year
    :param: year2: comparison year
    :param: indicator: any HFI indicator. Set to 'hf_score' by default
    :param: all_regions: boolean for regions density plots
    :return: It returns the density plot for a set of given years, indicators, and/or regions.
    """
    if all_regions:
        for i in range(len(regions)):
            reg1 = selected_df.loc[(selected_df['year'] == year1) & (selected_df['region'] == regions[i]), indicator]
            sns.distplot(reg1, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year1))

            reg2 = selected_df.loc[(selected_df['year'] == year2) & (selected_df['region'] == regions[i]), indicator]
            sns.distplot(reg2, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year2))

            plt.legend(prop={'size': 16}, title='{} Scores'.format(indicator))
            plt.title('Density Plot | {0} in {1}'.format(indicator, regions[i]))
            plt.xlabel('{}'.format(indicator))
            plt.ylabel('Density')
            plt.show()

    else:
        hfi1 = selected_df.loc[selected_df['year'] == year1, indicator]
        sns.distplot(hfi1, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year1))

        hfi2 = selected_df.loc[selected_df['year'] == year2, indicator]
        sns.distplot(hfi2, hist=False, kde=True, kde_kws={'linewidth': 3}, label='{}'.format(year2))

        plt.legend(prop={'size': 16}, title='{} Scores'.format(indicator))
        plt.title('Density Plot | {} '.format(indicator))
        plt.xlabel('{}'.format(indicator))
        plt.ylabel('Density')

    return plt.show()


# improved/deteriorated, overall scores
def improve_deteriorate(year1, year2, indicator='hf_score'):
    """
    It calculates drops and improvements in the overall HFI score for given years.
    :param year1: base year
    :param year2: comparison year
    :param indicator: indicator to compare. Overall HFI score set by default
    :return: 1) The overall change in HFI score for previous year and earliest year, 2) Number of countries that
    improved/decreased/didn't change their overall HFI scores for a set of given years
    """

    year3 = year2 - 1  # for YoY comparison

    selected_base, selected_comparison = selected_df.loc[selected_df['year'] == year1, indicator], \
                                         selected_df.loc[selected_df['year'] == year2, indicator]
    diff = np.array(selected_comparison) - np.array(selected_base)
    diff_mean = np.mean(np.array(selected_comparison)) - np.mean(np.array(selected_base))

    print('-' * 25)
    print('Change in {0} ({1}-{2}):'.format(indicator, year2, year1), round(diff_mean, 3))
    print('{0} {1}:'.format(indicator, year1), round(int(np.mean(np.array(selected_base))), 3))
    print('{0} {1}:'.format(indicator, year2), round(int(np.mean(np.array(selected_comparison))), 3))

    all_comparison = df.loc[df['year'] == year2, indicator]
    all_previous = df.loc[df['year'] == year3, indicator]
    all_diff = np.array(all_comparison) - np.array(all_previous)
    all_change_hf = np.mean(np.array(all_comparison)) - np.mean(np.array(all_previous))

    print('-' * 25)
    print('Change in {0} ({1}-{2}):'.format(indicator, year3, year2), round(all_change_hf, 3))
    print('{0} {1}:'.format(indicator, year3), round(int(np.mean(np.array(all_previous))), 3))
    print('{0} {1}:'.format(indicator, year2), round(int(np.mean(np.array(all_comparison))), 3))
    print('-' * 25)

    selected_decreased = 0
    selected_improved = 0
    selected_same = 0
    for i in diff:
        if i > 0:
            selected_improved += 1
        if i < 0:
            selected_decreased += 1
        if i == 0:
            selected_same += 1

    print('Countries that improved/decreased ({0}-{1}):'.format(year1, year2))
    print('Improved countries:', selected_improved)
    print('Decreased countries:', selected_decreased)
    print('No changes in score:', selected_same)
    print('-' * 25)

    decreased = 0
    improved = 0
    same = 0
    for i in all_diff:
        if i > 0:
            improved += 1
        if i < 0:
            decreased += 1
        if i == 0:
            same += 1

    print('Countries that improved/decreased ({0}-{1}):'.format(year3, year2))
    print('Improved countries:', improved)
    print('Decreased countries:', decreased)
    print('No changes in score:', same)
    print('-' * 25)


# top 10% countries lost or gained freedom between 2008 and 2019?
def top_bottom_10(year1, year2, top=True, indicator='hf_score'):
    '''
    Did the top/bottom 10% countries gained or lost freedom between a given period of time?
    :param indicator: indicator to compare. Overall HFI score set by default
    :param top: if True, returns changes for top 10%. If False, returns changes for bottom 10%.
    :param year1: base year
    :param year2: comparison year
    :return: integers with values corresponding to changes in freedom for the top10%
    '''

    hfi_base, hfi_comparison = selected_df.loc[selected_df['year'] == year1, indicator], \
                               selected_df.loc[selected_df['year'] == year2, indicator]

    total_countries = len(hfi_base)
    percent = math.floor(total_countries * .1)

    base = np.sort(hfi_base)
    comparison = np.sort(hfi_comparison)

    if top:
        mean_base = base[-percent:].mean()
        mean_comparison = comparison[-percent:].mean()

        print('{} for top 10% countries:'.format(indicator))
        print('Mean {}:'.format(year1), round(mean_base, 2))
        print('Mean {}:'.format(year2), round(mean_comparison, 2))
        print('-' * 25)

    if not top:
        mean_base = base[:percent].mean()
        mean_comparison = comparison[:percent].mean()

        print('{} for bottom 10% countries:'.format(indicator))
        print('Mean {}:'.format(year1), round(mean_base, 2))
        print('Mean {}:'.format(year2), round(mean_comparison, 2))
        print('-' * 25)


# top_bottom_10(2008, 2019, top=False, indicator='pf_expression')
