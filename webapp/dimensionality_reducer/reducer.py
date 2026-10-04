import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64

# ============================
# CONFIGURACIÓN OPTIMIZADA
# ============================

MAX_ROWS = 5000          # Mantén 5000 filas para evitar SIGKILL
MAX_COLS = 200           # Reduce columnas para evitar explosión de RAM

# ============================
# FUNCIONES AUXILIARES
# ============================

def df_to_numpy(df):
    """Convierte DataFrame a numpy y reduce columnas si es necesario."""
    if df.shape[1] > MAX_COLS:
        df = df.iloc[:, :MAX_COLS]  # Reducir columnas
    return df.to_numpy()


def fig_to_base64(fig):
    """Convierte figura Matplotlib a base64."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


# ============================
# MÉTODOS DE REDUCCIÓN
# ============================

def run_pca(df):
    """PCA sin normalización (mucho más rápido en Railway)."""
    X = df_to_numpy(df)
    pca = PCA(n_components=3)
    embedding = pca.fit_transform(X)
    return embedding


def run_tsne(df):
    """t-SNE optimizado para datasets grandes."""
    X = df_to_numpy(df)
    tsne = TSNE(n_components=3, perplexity=30, n_iter=500)
    embedding = tsne.fit_transform(X)
    return embedding


def run_umap(df):
    """UMAP optimizado para Railway."""
    X = df_to_numpy(df)
    reducer = umap.UMAP(n_components=3, n_neighbors=15, min_dist=0.1)
    embedding = reducer.fit_transform(X)
    return embedding


# ============================
# VISUALIZACIONES
# ============================

def plot_corr(df):
    """Heatmap de correlación."""
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.matshow(corr, cmap="coolwarm")
    fig.colorbar(cax)
    ax.set_title("Correlation Heatmap")
    return fig_to_base64(fig)


def plot_compare(df):
    """Comparativo simple entre columnas."""
    fig, ax = plt.subplots(figsize=(8, 6))
    df.mean().plot(kind="bar", ax=ax)
    ax.set_title("Column Means Comparison")
    return fig_to_base64(fig)


# ============================
# FUNCIÓN PRINCIPAL
# ============================

def run_reducer(df, method):
    """Ejecuta PCA, t-SNE o UMAP y devuelve todo lo necesario para la web app."""

    # Limitar filas
    if df.shape[0] > MAX_ROWS:
        df = df.sample(MAX_ROWS)

    # Limitar columnas
    if df.shape[1] > MAX_COLS:
        df = df.iloc[:, :MAX_COLS]

    # Seleccionar solo columnas numéricas
    df = df.select_dtypes(include=["number"]).dropna()

    print("SHAPE FINAL:", df.shape)

    if df.shape[0] < 5 or df.shape[1] < 3:
        raise ValueError("Dataset demasiado pequeño para generar visualizaciones.")

    # Ejecutar el método de reducción
    if method == "pca":
        embedding = run_pca(df)
    elif method == "tsne":
        embedding = run_tsne(df)
    elif method == "umap":
        embedding = run_umap(df)
    else:
        raise ValueError("Método no reconocido.")

    # Visualizaciones
    corr_plot = plot_corr(df)
    compare_plot = plot_compare(df)

    # Tabla y estadísticas
    stats = df.describe().to_html()
    table = df.head(20).to_html()

    # Retorno final para la web app
    return {
        "embedding": np.asarray(embedding).tolist(),
        "labels": list(range(df.shape[0])),
        "corr_plot": corr_plot,
        "compare_plot": compare_plot,
        "stats": stats,
        "table": table
    }
