import os
import sys
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dimensionality_reducer.reducer import run_reducer  # pyright: ignore[reportMissingImports]

app = Flask(__name__)

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

        # Leer CSV
        df = pd.read_csv(file.stream)

        # 🔥 LIMITAR dataset para Render Free
        MAX_ROWS = 5000
        if len(df) > MAX_ROWS:
            df = df.sample(MAX_ROWS, random_state=42)

        # Ejecutar el reducer
        result = run_reducer(df, method)

        # Renderizar resultados
        return render_template("result.html", result=result)

    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as e:
        return render_template("error.html", message=str(e))


# -----------------------------
# Render Free compatible server
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
