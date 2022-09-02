import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

# Load data
df = pd.read_csv('../../2021/all_countries.csv')

# keep category columns
columns = ['ISO', 'year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score',
           'hf_quartile']

df_pca = df[columns]

# Drop NaN
df_pca = df_pca.dropna()

# Select features
pca_features = df_pca.drop(['ISO', 'year', 'countries', 'hf_score', 'hf_quartile'], axis=1)

# Standardize features
x = StandardScaler().fit_transform(pca_features)

# Create PCA class anf fit data
pca = PCA(n_components=12)
principalComponents = pca.fit_transform(x)

# Eigenvalues
eigenvalues = pca.explained_variance_
print('Eigenvalues:', eigenvalues)
for i in range(len(eigenvalues)):
    if eigenvalues[i] >= 1:
        print('Keep {} PC(s)'.format(i + 1))
print('------' * 7)

# Variance explained by each PC
for i in range(12):
    print('Variance explained by {} PC:'.format(str(i + 1)),
          np.cumsum(pca.explained_variance_ratio_ * 100)[i])
print('-----' * 7)

# Create new PCA class anf fit data
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(x)

# check for PCA loadings
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3'],
                        index=['pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
                               'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation'])
loadings.to_csv('pcaLoadings.csv')

# Set df
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['PC1', 'PC2', 'PC3'])

# Concat dfs
finalDf = pd.concat([principalDf, df_pca[['ISO', 'year', 'countries', 'hf_score', 'hf_quartile']]], axis=1)

finalDf = finalDf.apply(lambda x: pd.Series(x.dropna().values))

# Export csv
finalDf.to_csv('PCA.csv', index=False)
