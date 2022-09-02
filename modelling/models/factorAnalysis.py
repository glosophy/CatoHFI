import pandas as pd
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
import matplotlib.pyplot as plt

# Load data
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../../2021/all_countries.csv')

# keep category columns
columns = ['ISO', 'year', 'countries', 'pf_rol', 'pf_ss', 'pf_movement', 'pf_religion', 'pf_assembly', 'pf_expression',
           'pf_identity', 'ef_government', 'ef_legal', 'ef_money', 'ef_trade', 'ef_regulation', 'hf_score', 'hf_quartile']

df_fa = df[columns]

# Drop NaN
df_fa = df_fa.dropna()

# Select features
fa_features = df_fa.drop(['ISO', 'year', 'countries', 'hf_score', 'hf_quartile'], axis=1)

# Evaluate the “factorability” of the data. Can we find the factors in the dataset?
# Barlett-s Test
chi_square_value, p_value = calculate_bartlett_sphericity(fa_features)
print('Chi-Sq:', chi_square_value)
print('p-value:', p_value)
print('------' * 7)

# Kaiser-Meyer-Olkin KMO test: calculates proportion of variance among all observed variables
kmo_all, kmo_model = calculate_kmo(fa_features)
print('KMO score:', kmo_model)
print('------' * 7)

# Subtract mean and divide by var
x = StandardScaler().fit_transform(fa_features)

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.set_params(n_factors=12, rotation=None)
fa.fit(x)

# Eigenvalues
ev, v = fa.get_eigenvalues()
print('Eigenvalues:', ev)
for i in range(len(ev)):
    if ev[i] >= 1:
        print('Keep {} factor(s)'.format(i + 1))
print('------' * 7)

# Scree plot
plt.scatter(range(1, x.shape[1] + 1), ev)
plt.plot(range(1, x.shape[1] + 1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

# Restart FA class and check loadings
fa = FactorAnalyzer()
fa.set_params(n_factors=3, rotation=None)
factors = fa.fit_transform(x)

loadings = fa.loadings_
print('Loadings:')
print(loadings)
print('------' * 7)

# Get cumulative variance
print('Cumulative variance for 3 factors:', (fa.get_factor_variance()[-1][-1]) * 100)
print('------' * 7)

# Set df
principalDf = pd.DataFrame(data=factors,
                           columns=['F1', 'F2', 'F3'])

# Concat dfs
finalDf = pd.concat([principalDf, df_fa[['ISO', 'year', 'countries', 'hf_score', 'hf_quartile']]], axis=1)

finalDf = finalDf.apply(lambda x: pd.Series(x.dropna().values))

# Export csv
finalDf.to_csv('factors.csv', index=False)

