import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load data
df = pd.read_csv('./../2021/all_countries.csv')

# keep category columns
columns = ['year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score']

df_pca = df[columns]

# Drop NaN
df_pca = df_pca.dropna()

# Select features
pca_features = df_pca.drop(['year', 'countries', 'hf_score'], axis=1)

# Standardize features
x = StandardScaler().fit_transform(pca_features)

# Create PCA class anf fit data
pca = PCA(n_components=4)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['PC1', 'PC2', 'PC3', 'PC4'])

# Concat dfs
finalDf = pd.concat([principalDf, df_pca[['year', 'countries', 'hf_score']]], axis=1)

print(finalDf)
