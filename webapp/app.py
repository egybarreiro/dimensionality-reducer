from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

from webapp.dimensionality_reducer.reducer import run_reducer

app = Flask(__name__)

# ============================
# RUTA PRINCIPAL
# ============================

@app.route("/")
def index():
    return render_template("index.html")

# ============================
# PROCESAR ARCHIVO Y MÉTODO
# ============================

@app.route("/process", methods=["POST"])
def process():
    try:
        # Archivo CSV
        file = request.files.get("file")
        if file is None:
            return jsonify({"error": "No se envió archivo"}), 400

        # Método seleccionado: pca, tsne, umap
        method = request.form.get("method")
        if method not in ["pca", "tsne", "umap"]:
            return jsonify({"error": "Método inválido"}), 400

        # Leer CSV
        df = pd.read_csv(file.stream)

        # Ejecutar reducción
        result = run_reducer(df, method)

        # Responder JSON
        return jsonify(result)

    except (ValueError, pd.errors.ParserError) as e:
        return jsonify({"error": str(e)}), 500

# ============================
# EJECUTAR SERVIDOR
# ============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
