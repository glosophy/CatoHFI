import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import math

warnings.simplefilter(action='ignore', category=FutureWarning)

# read csv
df = pd.read_csv('../../2023/cleaning/hfi2023_cc.csv')

# calculate women's freedoms
df['pf_women'] = df[['pf_movement_vdem_women', 'pf_identity_same_f', 'pf_identity_inheritance',
                     'pf_identity_divorce', 'pf_identity_fgm', ]].mean(axis=1)

# main
main = ['hf_score', 'pf_score', 'ef_score']

# main categories
all_categories = ['hf_score', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
                  'pf_identity', 'pf_score', 'ef_government',
                  'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'ef_score']

# 123 countries
countries = ['Angola', 'Armenia', 'Azerbaijan', 'Belarus', 'Bhutan', 'Bosnia and Herzegovina', 'Brunei Darussalam',
             'Burkina Faso', 'Cabo Verde', 'Cambodia', 'Comoros', 'Djibouti', 'Eswatini', 'Ethiopia', 'Gambia, The',
             'Guinea', 'Georgia', 'Iraq', 'Kazakhstan', 'Kyrgyz Republic', 'Lao PDR', 'Lebanon', 'Lesotho', 'Liberia',
             'Libya', 'Mauritania', 'Moldova', 'Mongolia', 'Montenegro', 'Mozambique', 'North Macedonia', 'Qatar',
             'Saudi Arabia', 'Serbia', 'Seychelles', 'Somalia', 'Sudan', 'Suriname', 'Tajikistan', 'Timor-Leste',
             'Vietnam', 'Yemen, Rep.']

regions = df['region'].unique()

# selecting rows based on condition | ~ is not in
selected_df = df[~df['countries'].isin(countries)]
selected_df.to_csv('../../2023/selected_countries.csv', index=False)


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

            plt.legend(prop={'size': 16}, title='{}'.format(indicator))
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
    print('Change in {0} ({1}-{2}):'.format(indicator, year1, year2), round(diff_mean, 3))
    print('{0} {1}:'.format(indicator, year1), round(float(np.mean(np.array(selected_base))), 3))
    print('{0} {1}:'.format(indicator, year2), round(float(np.mean(np.array(selected_comparison))), 3))

    all_comparison = df.loc[df['year'] == year2, indicator]
    all_previous = df.loc[df['year'] == year3, indicator]
    all_diff = np.array(all_comparison) - np.array(all_previous)
    all_change_hf = np.mean(np.array(all_comparison)) - np.mean(np.array(all_previous))

    print('-' * 25)
    print('Change in {0} ({1}-{2}):'.format(indicator, year3, year2), round(all_change_hf, 3))
    print('{0} {1}:'.format(indicator, year3), round(float(np.mean(np.array(all_previous))), 3))
    print('{0} {1}:'.format(indicator, year2), round(float(np.mean(np.array(all_comparison))), 3))
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
    """
    Did the top/bottom 10% countries gained or lost freedom between a given period of time?
    :param indicator: indicator to compare. Overall HFI score set by default
    :param top: if True, returns changes for top 10%. If False, returns changes for bottom 10%.
    :param year1: base year
    :param year2: comparison year
    :return: integers with values corresponding to changes in freedom for the top10%
    """

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


# quartiles over time
def plot_quartiles(year1, year2, indicator='hf_score'):
    """
    Calculates the gap between quartiles
    :param indicator: indicator to compare. Overall HFI score set by default
    :param year1: base year
    :param year2: latest year
    :return: a plot of the evolution of quartiles over time and the corresponding scores for each quartile for each year
    """

    quartile = selected_df['hf_quartile'].unique()
    by_quartile = selected_df.groupby(['year', 'hf_quartile'])[indicator].mean().reset_index()

    by_quartile = by_quartile.pivot(index='year', columns='hf_quartile', values=indicator)
    by_quartile['diff_quartile'] = by_quartile.iloc[:, 0] - by_quartile.iloc[:, -1]
    print(by_quartile)
    print('-' * 25)

    for i in quartile:
        a = by_quartile.loc[by_quartile['hf_quartile'] == i, indicator].to_list()
        plt.plot((list(range(year1, year2 + 1))), a, label=i)
        plt.legend(title='Quartiles', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.title('{0} Score by HFI Quartile Over Time ({1}-{2})'.format(indicator, year1, year2))
        plt.xlabel('Year')
        plt.ylabel('Score')
    return plt.show()


# highest and lowest HFI score over time
def gap_scores(year1, year2, indicator='hf_score'):
    """
    Calculates and plots the gap between the highest and lowest score for a given indicator over a set of years
    :param indicator: indicator to compare. Overall HFI score set by default
    :param year1: base year
    :param year2: latest year
    :return: a plot of the evolution of highest and lowest score over time and printed difference of the gap
    """

    low = []
    high = []

    for i in range(year1, year2 + 1):
        a = selected_df.loc[selected_df['year'] == i, indicator]
        minValue = a.min()
        maxValue = a.max()
        low.append(minValue)
        high.append(maxValue)

    plt.plot(list(range(year1, year2 + 1)), high, label='Highest Score')
    plt.plot(list(range(year1, year2 + 1)), low, label='Lowest Score')
    plt.legend(title='Score', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title('Highest and Lowest {0} Score ({1}-{2})'.format(indicator, year1, year2))
    plt.xlabel('Year')
    plt.ylabel('Score')

    diff1 = high[0] - low[0]
    diff2 = high[-1] - low[-1]
    print('Gap between highest and lowest {} score (141 countries):'.format(indicator))
    print('Gap {}:'.format(year1), round(diff1, 2))
    print('Gap {}:'.format(year2), round(diff2, 2))
    print('-' * 25)

    return plt.show()


# top 10% countries
def gap_10_percent(year1, year2, indicator='hf_score'):
    """
    Calculates and plots the gap between the highest and lowest score for a given indicator over a set of years
    :param indicator: indicator to compare. Overall HFI score set by default
    :param year1: base year
    :param year2: latest year
    :return: a plot of the evolution of highest and lowest score over time and printed difference of the gap
    """

    lowest10 = []
    highest10 = []
    for i in range(year1, year2 + 1):
        a = selected_df.loc[selected_df['year'] == i, indicator]
        a = np.sort(a)
        highest = a[-14:].mean()
        lowest = a[:14].mean()
        lowest10.append(lowest)
        highest10.append(highest)

    plt.plot(list(range(int(year1), int(year2 + 1))), highest10, label='Highest 10%')
    plt.plot(list(range(int(year1), int(year2 + 1))), lowest10, label='Lowest 10%')
    plt.legend(title='Score', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title('Gap Between Highest and Lowest 10% {0} Score ({1}-{2})'.format(indicator, year1, year2))
    plt.xlabel('Year')
    plt.ylabel('Score')

    diff1_10 = highest10[0] - lowest10[0]
    diff2_10 = highest10[-1] - lowest10[-1]
    print('Gap in {} between highest and lowest 10% (141 countries):'.format(indicator))
    print('Gap 2008:', round(diff1_10, 2))
    print('Gap 2019:', round(diff2_10, 2))
    print('-' * 25)

    return plt.show()


# plot indicators over time
def plot_indicators(indicators=main):
    """
    It plots a set of given indicators over time (2000-2020) for all countries.
    :param indicators: 'main' == hf_score, pf_score, ef_score. Can also pass a list with other indicators.
    :return: a plot with the evolution of indicators over time.
    """

    years = selected_df['year'].unique()

    if indicators == main:
        indicators = ['hf_score', 'ef_score', 'pf_score']
    else:
        indicators = indicators

    for i in indicators:
        selected_indicator = selected_df.groupby(['year'])[i].mean().reset_index()
        selected_indicator = selected_indicator.sort_values(by='year', ascending=False)
        plt.plot(years, selected_indicator[i], label=i)
        plt.legend(title='Indicators', loc='best')
        plt.title('Scores Over Time (2000-2020)')
        plt.xlabel('Year')
        plt.ylabel('Score')
    return plt.show()


def regions_analysis(indicators=main):
    """
    It plots a set of given indicators over time (2000-2020) for all regions.
    :param indicators: 'main' == hf_score, pf_score, ef_score. Can also pass a list with other indicators.
    :return: a plot with the evolution of indicators for regions over time.
    """

    if indicators == main:
        indicators = ['hf_score', 'ef_score', 'pf_score']
    else:
        indicators = indicators

    for i in indicators:
        by_region = selected_df.groupby(['year', 'region'])[i].mean().reset_index()
        region_pivot = by_region.pivot(index='year', columns='region', values=i)
        region_pivot.to_csv('../exports/category_{}.csv'.format(i), index=False)

        for j in selected_df['region'].unique():
            a = np.array(region_pivot[j])
            change = a[-1] - a[0]
            print('Change in {0} score in {1} (2000-2021): {2}'.format(j, i, round(change, 2)))

            plt.plot(range(2000, 2021 + 1), a, label=j)
            plt.legend(title='Regions', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.title('{} Over Time (2000-2021)'.format(i))
            plt.xlabel('Year')
            plt.ylabel('Score')

        plt.show()
        print('-' * 25)

# ----------------------------------- charts
# density_plot(2000, 2021, indicator='ef_score')

# improve_deteriorate(2000, 2021)

# top_bottom_10(2000, 2021)

# gap_10_percent(2000, 2021)

regions_analysis()