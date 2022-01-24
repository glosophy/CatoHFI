import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./../2021/all_countries.csv')

# keep category columns
columns = ['year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score']

pca = df[columns]

# drop NaNs
pca = pca.dropna()

# PCA
features = ['pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
            'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation']

# Separate data into Y and X
y = pca['hf_score']
X = pca[features]

# Subtract the mean
X = X - X.mean()

# Normalize
Z = X / X.std()

# Check mean = 0 and the standard deviation = 1
print('MEAN:')
print(Z.mean())
print('---' * 15)
print('STD:')
print(Z.std())

# covariance matrix of Z
Z = np.dot(Z.T, Z)

# Get an array of computed eigenvalues and a matrix whose columns are the normalized eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(Z)

# Assign P to the matrix of eigenvectors and D to the diagonal matrix with eigenvalues
D = np.diag(eigenvalues)
P = eigenvectors

# centered or standardized version of X with each observation as a combination of the original variables
Z_new = np.dot(Z, P)

# Calculate the proportion of variance explained by each feature
sum_eigenvalues = np.sum(eigenvalues)
prop_var = [i / sum_eigenvalues for i in eigenvalues]

# Calculate the cumulative variance
cum_var = [np.sum(prop_var[:i + 1]) for i in range(len(prop_var))]

# Plot scree plot from PCA
x_labels = ['PC{}'.format(i + 1) for i in range(len(prop_var))]

plt.plot(x_labels, prop_var, marker='o', markersize=6, color='skyblue', linewidth=2, label='Proportion of variance')
plt.plot(x_labels, cum_var, marker='o', color='orange', linewidth=2, label="Cumulative variance")
plt.legend()
plt.title('Scree plot')
plt.xlabel('Principal components')
plt.ylabel('Proportion of variance')
plt.show()

# see eigenvalues for each PC
Zdata = pd.DataFrame(Z_new)
Zdata.insert(0, 'Features', features)
Zdata.columns = ['Features', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12']
pd.options.display.float_format = "{:,.2f}".format

Zdata.to_csv('./eigenvalues.csv', index=False)
