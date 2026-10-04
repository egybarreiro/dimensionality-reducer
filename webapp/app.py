import os
from importlib import import_module

import pandas as pd
from flask import Flask, render_template, request

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from sklearn.cluster import KMeans

try:
    run_reducer = import_module("webapp.dimensionality_reducer.reducer").run_reducer
except ModuleNotFoundError:
    run_reducer = import_module("dimensionality_reducer.reducer").run_reducer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    try:
        file = request.files.get("file")
        method = request.form.get("method")
        normalize = bool(request.form.get("normalize"))

        if not file:
            return render_template("error.html", message="No file uploaded")

        method = (method or "").lower().strip()

        df = pd.read_csv(file.stream, encoding="latin1")
        df = df.select_dtypes(include=["number"])
        df = df.dropna()

        MAX_ROWS = 1000
        if len(df) > MAX_ROWS:
            df = df.sample(MAX_ROWS, random_state=42)

        print("SHAPE FINAL:", df.shape)

        # Embedding principal
        result = run_reducer(df, method, normalize=normalize)
        embedding = np.asarray(result)

        # Clusters
        n_points = len(embedding)
        if n_points > 1:
            n_clusters = min(4, n_points)
            kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            labels = kmeans.fit_predict(embedding)
        else:
            labels = np.zeros(n_points, dtype=int)

        # Stats
        stats = {
            "min_x": float(embedding[:, 0].min()),
            "max_x": float(embedding[:, 0].max()),
            "mean_x": float(embedding[:, 0].mean()),
            "std_x": float(embedding[:, 0].std()),
            "min_y": float(embedding[:, 1].min()),
            "max_y": float(embedding[:, 1].max()),
            "mean_y": float(embedding[:, 1].mean()),
            "std_y": float(embedding[:, 1].std()),
        }

        # Tabla head
        table = df.iloc[:, :2].head(5).to_html(classes="table table-striped")

        # CSV reducido
        reduced_df = pd.DataFrame(embedding, columns=["x", "y"])
        reduced_csv = reduced_df.to_csv(index=False)

        # Heatmap correlación
        corr = df.corr()
        plt.figure(figsize=(4, 3))
        plt.imshow(corr, cmap="viridis", aspect="auto")
        plt.colorbar()
        plt.xticks(range(len(corr.columns)), list(corr.columns), rotation=90)
        plt.yticks(range(len(corr.columns)), list(corr.columns))

        plt.tight_layout()
        buf_corr = io.BytesIO()
        plt.savefig(buf_corr, format="png", dpi=100)
        buf_corr.seek(0)
        corr_plot = base64.b64encode(buf_corr.read()).decode("utf-8")
        plt.close()

        # Comparativo entre métodos
        methods = ["pca", "tsne", "umap", "lda"]
        fig, axes = plt.subplots(1, len(methods), figsize=(4 * len(methods), 3))

        for ax, m in zip(axes, methods):
            try:
                emb_m = np.asarray(run_reducer(df, m, normalize=normalize))
                ax.scatter(emb_m[:, 0], emb_m[:, 1], s=10)
                ax.set_title(m.upper())
            except Exception:
                ax.set_title(m.upper() + " (error)")

            ax.set_xticks([])
            ax.set_yticks([])

        plt.tight_layout()
        buf_cmp = io.BytesIO()
        plt.savefig(buf_cmp, format="png", dpi=100)
        buf_cmp.seek(0)
        compare_plot = base64.b64encode(buf_cmp.read()).decode("utf-8")
        plt.close()

        return render_template(
            "result.html",
            method=method,
            result=result,
            result_json=embedding.tolist(),
            labels_json=labels.tolist(),
            table=table,
            stats=stats,
            corr_plot=corr_plot,
            compare_plot=compare_plot,
            reduced_csv=reduced_csv,
        )

    except Exception as e:
        return render_template("error.html", message=str(e))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
