import numpy as np
import matplotlib
matplotlib.use("Agg")  # Backend rápido para generar imágenes sin interfaz
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import umap.umap_ as umap



class DimensionalityReducer:
    def __init__(self, data, normalize=False):
        self.data = data.values if hasattr(data, "values") else data

        if normalize:
            self.data = (self.data - np.mean(self.data, axis=0)) / np.std(self.data, axis=0)

        self.reduced_data: np.ndarray | None = None

        # PCA previo para acelerar t-SNE, UMAP y LDA
        self.pca_pre = PCA(n_components=30, svd_solver="randomized").fit_transform(self.data)

    # -----------------------------
    # MÉTODOS DE REDUCCIÓN
    # -----------------------------

    def reduce_with_pca(self):
        pca = PCA(n_components=2, svd_solver="randomized")
        self.reduced_data = pca.fit_transform(self.data)

    def reduce_with_tsne(self):
        tsne = TSNE(
            n_components=2,
            perplexity=30,
            learning_rate="auto",
            init="pca",
            n_iter=500  # más rápido que 1000, resultados igual de buenos
        )
        self.reduced_data = tsne.fit_transform(self.pca_pre)

    def reduce_with_umap(self):
        reducer = umap.UMAP(
            n_neighbors=10,   # más rápido
            min_dist=0.5,     # más rápido
            n_components=2
        )
        self.reduced_data = reducer.fit_transform(self.pca_pre)

    def reduce_with_lda(self, labels):
        lda = LinearDiscriminantAnalysis(n_components=2)
        self.reduced_data = lda.fit_transform(self.pca_pre, labels)

    # -----------------------------
    # GRÁFICO DE RESULTADOS
    # -----------------------------

    def plot_reduction(self):
        if self.reduced_data is None:
            raise ValueError("No reduced data available. Run a reduction method first.")

        fig, ax = plt.subplots(figsize=(8, 6))

        x = self.reduced_data[:, 0]
        y = self.reduced_data[:, 1]

        ax.scatter(x, y, s=25, alpha=0.8)
        ax.set_title("Reducción de Dimensionalidad")
        ax.set_xlabel("Componente 1")
        ax.set_ylabel("Componente 2")

        return fig
