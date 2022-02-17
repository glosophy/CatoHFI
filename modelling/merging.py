import pandas as pd

pca = pd.read_csv('PCA.csv')
kMeans = pd.read_csv('kmeans.csv')
factor = pd.read_csv('factors.csv')

# Merge dfs
result = pd.merge(pca, kMeans, how='outer', on=['year', 'countries', 'hf_score', 'hf_quartile'])
final = pd.merge(result, factor, how='outer', on=['year', 'countries', 'hf_score', 'hf_quartile'])

final.to_csv('modellingFile.csv', index=False)
