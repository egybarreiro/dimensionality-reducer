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
        # Asegurar que data sea un ndarray
        self.data = data.values if hasattr(data, "values") else np.asarray(data)

        # Normalización opcional
        if normalize:
            self.data = (self.data - np.mean(self.data, axis=0)) / np.std(self.data, axis=0)

        self.reduced_data: np.ndarray | None = None

        # PCA previo para acelerar t-SNE, UMAP y LDA
        # Se limita a min(n_features, 30) para evitar errores en datasets pequeños
        n_features = self.data.shape[1]
        pca_components = min(30, n_features)

        self.pca_pre = PCA(
            n_components=pca_components,
            svd_solver="randomized"
        ).fit_transform(self.data)

    # -----------------------------
    # MÉTODOS DE REDUCCIÓN
    # -----------------------------

    def reduce_with_pca(self):
        pca = PCA(n_components=2, svd_solver="randomized")
