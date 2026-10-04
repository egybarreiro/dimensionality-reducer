import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import umap.umap_ as umap


class DimensionalityReducer:
    def __init__(self, data, normalize=False):
        # Convertir DataFrame a ndarray
        self.data = data.values if hasattr(data, "values") else np.asarray(data)

        # Normalización opcional
        if normalize:
            self.data = (self.data - np.mean(self.data, axis=0)) / np.std(self.data, axis=0)

        self.reduced_data: np.ndarray | None = None

        # PCA previo para acelerar t-SNE, UMAP y LDA
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
        self.reduced_data = pca.fit_transform(self.data)

    def reduce_with_tsne(self):
        # Ajustar perplexity para datasets pequeños
        perplexity = min(3, len(self.data) - 1)

        tsne = TSNE(
            n_components=2,
            perplexity=perplexity,
            learning_rate="auto",
            init="pca",
            max_iter=500
        )
        self.reduced_data = tsne.fit_transform(self.pca_pre)

    def reduce_with_umap(self):
        # Ajustar n_neighbors para evitar warnings
        n_neighbors = min(10, len(self.data) - 1)

        reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=0.5,
            n_components=2
        )
        self.reduced_data = reducer.fit_transform(self.pca_pre)

    def reduce_with_lda(self, labels):
        # LDA requiere al menos 2 clases
        unique_classes = np.unique(labels)
        if len(unique_classes) < 2:
            raise ValueError("LDA requiere al menos 2 clases distintas en el dataset.")

        lda = LinearDiscriminantAnalysis(n_components=1)  # n_components <= n_classes - 1
        self.reduced_data = lda.fit_transform(self.pca_pre, labels)


# -----------------------------
# FUNCIÓN GLOBAL PARA FLASK
# -----------------------------
def run_reducer(df, method, normalize=False):
    reducer = DimensionalityReducer(df, normalize=normalize)

    method = (method or "").lower().strip()

    if method == "pca":
        reducer.reduce_with_pca()

    elif method == "tsne":
        reducer.reduce_with_tsne()

    elif method == "umap":
        reducer.reduce_with_umap()

    elif method == "lda":
        # Dummy labels → pero ahora LDA exige 2 clases
        labels = np.zeros(len(df))
        reducer.reduce_with_lda(labels)

    else:
        raise ValueError(f"Unknown reduction method: {method}")

    if reducer.reduced_data is None:
        raise ValueError("Reducer did not produce output.")
    return reducer.reduced_data.tolist()


# -----------------------------
# PRUEBA LOCAL
# -----------------------------
if __name__ == "__main__":
    import pandas as pd

    df_test = pd.DataFrame({
        "A": np.random.rand(100),
        "B": np.random.rand(100),
        "C": np.random.rand(100)
    })

    reducer = DimensionalityReducer(df_test, normalize=True)
    reducer.reduce_with_pca()
    if reducer.reduced_data is not None:
        print("PCA Result Shape:", reducer.reduced_data.shape)
    else:
        print("Reducer did not produce output.")

