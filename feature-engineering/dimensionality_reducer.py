# Propósito: Clase para reducción de dimensionalidad y visualización 2D.
# Autor: Edgar Barreiro
# Versión: 1.0.0

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

try:
    import umap
except ImportError:
    umap = None


class DimensionalityReducer:
    """Aplica PCA, t-SNE, UMAP o LDA a datos tabulares."""

    def __init__(self, data, target_column=None, normalize=True):
        self.target_column = target_column
        self.y = data[target_column].values if target_column else None
        self.X = data.drop(columns=[target_column]).values if target_column else data.values
        if normalize:
            self.X = StandardScaler().fit_transform(self.X)

    def reduce_with_pca(self):
        return PCA(n_components=2, random_state=42).fit_transform(self.X)

    def reduce_with_tsne(self, perplexity=30):
        return TSNE(n_components=2, perplexity=perplexity, random_state=42).fit_transform(self.X)

    def reduce_with_umap(self, n_neighbors=15, min_dist=0.1):
        if umap is None:
            raise ImportError("Instala umap-learn para usar UMAP.")
        return umap.UMAP(n_components=2, n_neighbors=n_neighbors, min_dist=min_dist, random_state=42).fit_transform(self.X)

    def reduce_with_lda(self):
        if self.y is None:
            raise ValueError("LDA requiere una columna objetivo.")
        return LinearDiscriminantAnalysis(n_components=2).fit_transform(self.X, self.y)

    @staticmethod
    def plot_2d(embedding, labels=None, title="Reducción de dimensionalidad (2D)"):
        plt.figure(figsize=(8, 6))
        if labels is not None:
            plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap="viridis", s=40, alpha=0.8)
        else:
            plt.scatter(embedding[:, 0], embedding[:, 1], s=40, alpha=0.8, color="steelblue")
        plt.title(title)
        plt.xlabel("Componente 1")
        plt.ylabel("Componente 2")
        plt.grid(True, linestyle="--", alpha=0.3)
        plt.tight_layout()
        plt.show()
