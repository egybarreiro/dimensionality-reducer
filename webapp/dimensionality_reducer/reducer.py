import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import umap
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from datetime import datetime

MAX_ROWS = 3000
MAX_COLS = 100

HISTORY_FILE = "webapp/history.json"

def save_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

def fig_to_png_file(fig, filename):
    fig.savefig(filename, format="png", bbox_inches="tight")
    plt.close(fig)

def split_features_labels(df):
    if "Target" not in df.columns:
        raise ValueError("La columna 'Target' no existe en el dataset.")

    y = df["Target"]
    X = df.drop(columns=["Target"], errors="ignore")

    if "Unnamed: 0" in X.columns:
        X = X.drop(columns=["Unnamed: 0"], errors="ignore")

    X_num = X.select_dtypes(include=[np.number])
    X_num = X_num.iloc[:MAX_ROWS, :MAX_COLS]
    y = y.iloc[:MAX_ROWS]

    return X_num, y

def make_cluster_plot(embedding, y, title, filename):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(embedding[:, 0], embedding[:, 1], c=y, cmap="tab10", s=10)
    ax.set_title(title)
    ax.set_xlabel("Componente 1")
    ax.set_ylabel("Componente 2")

    fig_to_png_file(fig, filename)
    return fig_to_base64(fig)

def save_csv(embedding, filename):
    df = pd.DataFrame(embedding, columns=["Comp1", "Comp2", "Comp3"])
    df.to_csv(filename, index=False)

def run_pca(df):
    X_num, y = split_features_labels(df)
    X = X_num.to_numpy()

    pca = PCA(n_components=3)
    embedding = pca.fit_transform(X)

    corr_plot = ""
    if X_num.shape[1] <= 30:
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        sns.heatmap(X_num.corr(), cmap="coolwarm", ax=ax1)
        corr_plot = fig_to_base64(fig1)
        plt.close(fig1)

    cluster_plot = make_cluster_plot(
        embedding, y.to_numpy(),
        "Clusters PCA (Target)",
        "webapp/static/pca_plot.png"
    )

    save_csv(embedding, "webapp/static/pca_reduced.csv")

    stats_html = X_num.describe().to_html()
    table_html = X_num.head(20).to_html()

    save_history({
        "timestamp": str(datetime.now()),
        "method": "PCA",
        "csv": "pca_reduced.csv",
        "image": "pca_plot.png"
    })

    return embedding, corr_plot, cluster_plot, stats_html, table_html

def run_tsne(df):
    X_num, y = split_features_labels(df)
    X = X_num.to_numpy()

    tsne = TSNE(n_components=3, perplexity=30, max_iter=500)
    embedding = tsne.fit_transform(X)

    cluster_plot = make_cluster_plot(
        embedding, y.to_numpy(),
        "Clusters t-SNE (Target)",
        "webapp/static/tsne_plot.png"
    )

    save_csv(embedding, "webapp/static/tsne_reduced.csv")

    stats_html = X_num.describe().to_html()
    table_html = X_num.head(20).to_html()

    save_history({
        "timestamp": str(datetime.now()),
        "method": "t-SNE",
        "csv": "tsne_reduced.csv",
        "image": "tsne_plot.png"
    })

    return embedding, cluster_plot, stats_html, table_html

def run_umap(df):
    X_num, y = split_features_labels(df)
    X = X_num.to_numpy()

    reducer = umap.UMAP(
        n_components=3,
        n_neighbors=10,
        min_dist=0.1,
        low_memory=True,
        force_approximation_algorithm=True
    )
    embedding = reducer.fit_transform(X)

    cluster_plot = make_cluster_plot(
        embedding, y.to_numpy(),
        "Clusters UMAP (Target)",
        "webapp/static/umap_plot.png"
    )

    save_csv(embedding, "webapp/static/umap_reduced.csv")

    stats_html = X_num.describe().to_html()
    table_html = X_num.head(20).to_html()

    save_history({
        "timestamp": str(datetime.now()),
        "method": "UMAP",
        "csv": "umap_reduced.csv",
        "image": "umap_plot.png"
    })

    return embedding, cluster_plot, stats_html, table_html

def run_lda(df):
    X_num, y = split_features_labels(df)
    X = X_num.to_numpy()
    y_arr = y.to_numpy()

    lda = LinearDiscriminantAnalysis(n_components=3)
    embedding = lda.fit_transform(X, y_arr)

    cluster_plot = make_cluster_plot(
        embedding, y_arr,
        "Clusters LDA (Target)",
        "webapp/static/lda_plot.png"
    )

    save_csv(embedding, "webapp/static/lda_reduced.csv")

    stats_html = X_num.describe().to_html()
    table_html = X_num.head(20).to_html()

    save_history({
        "timestamp": str(datetime.now()),
        "method": "LDA",
        "csv": "lda_reduced.csv",
        "image": "lda_plot.png"
    })

    return embedding, cluster_plot, stats_html, table_html

def run_reducer(df, method):
    if method == "pca":
        embedding, corr_plot, cluster_plot, stats, table = run_pca(df)
    elif method == "tsne":
        embedding, cluster_plot, stats, table = run_tsne(df)
        corr_plot = ""
    elif method == "umap":
        embedding, cluster_plot, stats, table = run_umap(df)
        corr_plot = ""
    elif method == "lda":
        embedding, cluster_plot, stats, table = run_lda(df)
        corr_plot = ""
    else:
        raise ValueError("Método inválido")

    return {
        "embedding": embedding.tolist(),
        "corr_plot": corr_plot,
        "compare_plot": cluster_plot,
        "stats": stats,
        "table": table
    }
