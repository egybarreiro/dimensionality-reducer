import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau

# loading the penguins dataset
penguins = sns.load_dataset("penguins").dropna()

# running a correlation pearson
pearson_corr_flipper_body = pearsonr(
    penguins['flipper_length_mm'],
    penguins['body_mass_g']
)[0]

print(pearson_corr_flipper_body)
spearman_corr_flipper_body = spearmanr(
    penguins['flipper_length_mm'],
    penguins['body_mass_g']
)[0]

print(spearman_corr_flipper_body)
kendall_corr_flipper_body = kendalltau(
    penguins['flipper_length_mm'],
    penguins['body_mass_g']
)[0]

print(kendall_corr_flipper_body)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=penguins,
    x='flipper_length_mm',
    y='body_mass_g'
)
plt.show()