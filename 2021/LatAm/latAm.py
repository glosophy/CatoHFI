import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LatAm
latAm = selected_df.loc[selected_df['region'] == 'Latin America & the Caribbean']

latAm_group = latAm.groupby(['year']).mean().reset_index()

# print(np.array(latAm_group['hf_score']))
f = np.array(latAm_group['hf_score'])

plt.plot(range(2008, 2020), f)
plt.show()
