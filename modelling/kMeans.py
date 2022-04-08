import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# Load data
df = pd.read_csv('./../2021/all_countries.csv')

# keep category columns
columns = ['ISO', 'year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score', 'hf_quartile']

df_kmeans = df[columns]

# Drop NaN
df_kmeans = df_kmeans.dropna()

# Select features
kmeans_features = df_kmeans.drop(['ISO', 'year', 'countries', 'hf_score', 'hf_quartile'], axis=1)

# Standardize data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(kmeans_features)

# Check number of k
# Elbow plot
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

# Silhouette coefficients for each k
silhouette_coefficients = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)

plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()

# Start Kmeans class and fit features
kms = KMeans(n_clusters=4)
kms.fit(scaled_features)

# Create df with cluster groups
df_kmeans['Cluster'] = kms.labels_
df_kmeans.to_csv('kmeans.csv', index=False)

# Plot blobs for fun
plt.subplots(figsize=(8, 8))
sns.scatterplot(x='pf_movement', y='pf_expression', hue='Cluster', data=df_kmeans, markers='*', palette='coolwarm')
plt.show()

