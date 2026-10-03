import sys
import os
import time
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from flask import Flask, render_template, request, send_file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from dimensionality_reducer_proyect.reducer import DimensionalityReducer

app = Flask(__name__)

UPLOAD_FOLDER = "data"
OUTPUT_IMAGE = "webapp/static/output.png"
OUTPUT_TABLE = "webapp/static/table.png"
OUTPUT_CSV = "data/reduced_output.csv"

HISTORY = []  # historial simple en memoria


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_time = time.time()

        file = request.files.get("file")
        method = request.form.get("method")
        normalize = "normalize" in request.form

        if not file or not file.filename:
            return render_template("index.html",
                                   image=None,
                                   table=None,
                                   error="No se seleccionó ningún archivo.",
                                   history=HISTORY)

        filename = str(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Cargar dataset (más estable)
        df = pd.read_csv(filepath, low_memory=False)

        # Crear reducer optimizado
        reducer = DimensionalityReducer(df, normalize=normalize)

        # Ejecutar método seleccionado
        if method == "pca":
            reducer.reduce_with_pca()
        elif method == "tsne":
            reducer.reduce_with_tsne()
        elif method == "umap":
            reducer.reduce_with_umap()
        elif method == "lda":
            labels = df.iloc[:, -1]
            reducer.reduce_with_lda(labels)
        else:
            return render_template("index.html",
                                   image=None,
                                   table=None,
                                   error="Método no soportado.",
                                   history=HISTORY)

        # Graficar reducción
        fig = reducer.plot_reduction()
        fig.savefig(OUTPUT_IMAGE)
        plt.close(fig)

        # Crear imagen de la tabla reducida (primeras 20 filas)
        reduced_df = pd.DataFrame(reducer.reduced_data, columns=["Comp1", "Comp2"])
        preview = reduced_df.head(20)

        # Guardar CSV reducido para descarga
        reduced_df.to_csv(OUTPUT_CSV, index=False)

        plt.figure(figsize=(6, 4))
        sns.heatmap(preview, cmap="viridis", annot=False)
        plt.title("Tabla Reducida (primeras 20 filas)")
        plt.savefig(OUTPUT_TABLE)
        plt.close()

        elapsed = round(time.time() - start_time, 2)

        # Actualizar historial
        HISTORY.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filename": filename,
            "method": method,
            "normalize": normalize,
            "time": elapsed
        })

        return render_template(
            "index.html",
            image="static/output.png",
            table="static/table.png",
            csv_available=True,
            elapsed=elapsed,
            history=HISTORY
        )

    return render_template("index.html",
                           image=None,
                           table=None,
                           csv_available=False,
                           history=HISTORY)


@app.route("/download/csv")
def download_csv():
    if os.path.exists(OUTPUT_CSV):
        return send_file(OUTPUT_CSV,
                         as_attachment=True,
                         download_name="reduced_output.csv")
    return "No hay archivo CSV reducido disponible.", 404


@app.route("/download/image")
def download_image():
    if os.path.exists(OUTPUT_IMAGE):
        return send_file(OUTPUT_IMAGE,
                         as_attachment=True,
                         download_name="reduction_plot.png")
    return "No hay imagen disponible.", 404


if __name__ == "__main__":
    app.run(debug=False)
