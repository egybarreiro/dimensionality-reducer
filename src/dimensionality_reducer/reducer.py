import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import umap


class DimensionalityReducer:
    def __init__(self, data, normalize=False):
        self.data = np.asarray(data)
        self.normalize = normalize
        if self.normalize:
            self.data = StandardScaler().fit_transform(self.data)

    def reduce_with_pca(self, n_components=2):
        pca = PCA(n_components=n_components)
        return pca.fit_transform(self.data)

    def reduce_with_tsne(self, n_components=2, **kwargs):
        tsne = TSNE(n_components=n_components, **kwargs)
        return tsne.fit_transform(self.data)

    def reduce_with_umap(self, n_components=2, **kwargs):
        reducer = umap.UMAP(n_components=n_components, **kwargs)
        return reducer.fit_transform(self.data)

    def reduce_with_lda(self, labels, n_components=2):
        if labels is None:
            raise ValueError("labels are required to use LDA.")
        n_classes = len(np.unique(labels))
        lda_n_components = min(n_components, n_classes - 1)
        lda = LinearDiscriminantAnalysis(n_components=lda_n_components)
        return lda.fit_transform(self.data, labels)

    def plot_reduced_data(self, reduced_data, labels, title="Reduced Data"):
        reduced_data = np.asarray(reduced_data)
        if reduced_data.ndim != 2 or reduced_data.shape[1] < 2:
            raise ValueError("reduced_data must have at least two columns.")

        plt.figure(figsize=(8, 6))
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap="viridis")
        plt.colorbar()
        plt.xlabel("Component 1")
        plt.ylabel("Component 2")
        plt.title(title)
        plt.show()
