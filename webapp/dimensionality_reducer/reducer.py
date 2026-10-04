import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# ============================
# CONFIGURACIÓN PARA RAILWAY FREE
# ============================

MAX_ROWS = 3000     # Reduce carga para PCA, TSNE, UMAP
MAX_COLS = 100      # Reduce SVD y nearest neighbors

# ============================
# UTILIDADES
# ============================

def df_to_numpy(df):
    """Convierte DataFrame a numpy y aplica límites."""
    df = df.select_dtypes(include=[np.number])

    # Limitar filas y columnas
    df = df.iloc[:MAX_ROWS, :MAX_COLS]

    return df.to_numpy()


def fig_to_base64(fig):
    """Convierte figura Matplotlib a base64."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


# ============================
# PCA (Railway Safe)
# ============================

def run_pca(df):
    X = df_to_numpy(df)

    pca = PCA(n_components=3)
    embedding = pca.fit_transform(X)

    # ====== Gráfico de correlación (solo si columnas <= 30) ======
    if df.shape[1] <= 30:
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        sns.heatmap(df.corr(), cmap="coolwarm", ax=ax1)
        corr_plot = fig_to_base64(fig1)
        plt.close(fig1)
    else:
        corr_plot = ""

    # ====== Gráfico comparativo (solo si columnas >= 5) ======
    if df.shape[1] >= 5:
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        df.iloc[:, :5].plot(kind="line", ax=ax2)
        compare_plot = fig_to_base64(fig2)
        plt.close(fig2)
    else:
        compare_plot = ""

    # ====== Estadísticas ======
    stats_html = df.describe().to_html()

    # ====== Tabla ======
    table_html = df.head(20).to_html()

    return embedding, corr_plot, compare_plot, stats_html, table_html


# ============================
# t-SNE
# ============================

def run_tsne(df):
    X = df_to_numpy(df)

    tsne = TSNE(n_components=3, perplexity=30, n_iter=500)
    embedding = tsne.fit_transform(X)

    return embedding


# ============================
# UMAP (modo sin Numba para Railway)
# ============================

def run_umap(df):
    X = df_to_numpy(df)

    reducer = umap.UMAP(
        n_components=3,
        n_neighbors=10,
        min_dist=0.1,
        low_memory=True,
        force_approximation_algorithm=True
    )

    embedding = reducer.fit_transform(X)
    return embedding


# ============================
# FUNCIÓN PRINCIPAL
# ============================

def run_reducer(df, method):
    """Ejecuta el método y devuelve JSON uniforme para el frontend."""

    if method == "pca":
        embedding, corr_plot, compare_plot, stats, table = run_pca(df)

    elif method == "tsne":
        embedding = run_tsne(df)
        corr_plot = ""
        compare_plot = ""
        stats = ""
        table = ""

    elif method == "umap":
        embedding = run_umap(df)
        corr_plot = ""
        compare_plot = ""
        stats = ""
        table = ""

    else:
        raise ValueError("Método inválido")

    # Respuesta uniforme para evitar errores en el frontend
    toarray = getattr(embedding, "toarray", None)
    embedding_array = toarray() if callable(toarray) else embedding

    return {
        "embedding": np.asarray(embedding_array).tolist(),
        "corr_plot": corr_plot,
        "compare_plot": compare_plot,
        "stats": stats,
        "table": table
    }
