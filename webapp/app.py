import os
from importlib import import_module

import pandas as pd
from flask import Flask, render_template, request

# Import directo del reducer con fallback para ejecución como script o como paquete
try:
    run_reducer = import_module("webapp.dimensionality_reducer.reducer").run_reducer
except ModuleNotFoundError:  # pragma: no cover
    run_reducer = import_module("dimensionality_reducer.reducer").run_reducer

# -----------------------------
# Configurar Flask correctamente
# -----------------------------
app = Flask(
    __name__,
    static_folder="webapp/static",
    template_folder="webapp/templates"
)

# -----------------------------
# Página principal
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# -----------------------------
# Procesar CSV y ejecutar reducer
# -----------------------------
@app.route("/process", methods=["POST"])
def process():
    try:
        file = request.files.get("file")
        method = request.form.get("method")

        if not file:
            return render_template("error.html", message="No file uploaded")

        # Normalizar método (evita error: "Unknown reduction method: PCA")
        method = (method or "").lower().strip()

        # Leer CSV
        df = pd.read_csv(file.stream)

        # Convertir solo columnas numéricas
        df = df.select_dtypes(include=["number"])

        # Eliminar filas con NaN
        df = df.dropna()

        # Limitar filas para Railway Free
        MAX_ROWS = 1000
        if len(df) > MAX_ROWS:
            df = df.sample(MAX_ROWS, random_state=42)

        print("SHAPE FINAL:", df.shape)

        # Ejecutar el reducer
        result = run_reducer(df, method)

        # Renderizar resultados
        return render_template("result.html", result=result)

    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as e:
        return render_template("error.html", message=str(e))

# -----------------------------
# Servidor compatible con Railway
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
