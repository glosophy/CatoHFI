import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

selected_df = pd.read_csv('./../selected_countries.csv')

# LatAm
latAm = selected_df.loc[selected_df['region'] == 'Latin America & the Caribbean']
latAm = latAm.groupby(['year']).mean().reset_index()

# Iterate over main categories
main_categories = ['hf_score', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
                   'pf_identity', 'pf_score', 'ef_government',
                   'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'ef_score']

for i in main_categories:
    cat = np.array(latAm[i])
    plt.plot(range(2008, 2020), cat)
    plt.title('Latin America | {0} score over time'.format(i))
    plt.savefig('latAm_{0}.jpg'.format(i))
    plt.show()

