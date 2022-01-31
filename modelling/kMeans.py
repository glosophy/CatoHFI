import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# # Load data
# X = np.load('features.npy')
# y = np.load('response.npy')
#
# # Standardize data
# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(X)
#
# # Initiate class
# kmeans = KMeans(init="random",
#                 n_clusters=4,
#                 n_init=10,
#                 max_iter=300,
#                 random_state=42)
#
# # Perform ten runs of the k-means algorithm on data with a maximum of 300 iterations per run
# kmeans.fit(scaled_features)
#
# # The lowest SSE value
# print("Lowest SSE value:", kmeans.inertia_)
#
# # The number of iterations required to converge
# print('Iterations required to converge:', kmeans.n_iter_)
#
# # Elbow plot
# sse = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(scaled_features)
#     sse.append(kmeans.inertia_)
#
# plt.plot(range(1, 11), sse)
# plt.xticks(range(1, 11))
# plt.xlabel("Number of Clusters")
# plt.ylabel("SSE")
# plt.show()
#
# # Silhouette coefficients for each k
# silhouette_coefficients = []
#
# for k in range(2, 11):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(scaled_features)
#     score = silhouette_score(scaled_features, kmeans.labels_)
#     silhouette_coefficients.append(score)
#
# plt.plot(range(2, 11), silhouette_coefficients)
# plt.xticks(range(2, 11))
# plt.xlabel("Number of Clusters")
# plt.ylabel("Silhouette Coefficient")
# plt.show()

df = pd.read_csv('./../2021/all_countries.csv')

# keep category columns
columns = ['year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score']

kmeans = df[columns]
kmeans = kmeans.replace([np.inf, -np.inf], np.nan, inplace=True)
kmeans_features = kmeans.drop(['year', 'countries', 'hf_score'], axis=1)

kms = KMeans(n_clusters=4)

kms.fit(kmeans_features)

kmeans['Cluster'] = kms.labels_

print(kmeans.head())

