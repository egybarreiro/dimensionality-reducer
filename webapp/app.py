import importlib.util
import os
import sys
import types
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent
for import_root in (PROJECT_ROOT, APP_DIR):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))


def _load_run_reducer():
    package_name = "dimensionality_reducer"
    candidates = (
        PROJECT_ROOT / package_name / "reducer.py",
        APP_DIR / package_name / "reducer.py",
    )

    for reducer_path in candidates:
        if reducer_path.exists():
            package = sys.modules.get(package_name)
            if package is None:
                package = types.ModuleType(package_name)
                package.__path__ = [str(reducer_path.parent)]
                sys.modules[package_name] = package

            spec = importlib.util.spec_from_file_location(
                f"{package_name}.reducer", reducer_path
            )
            if spec is None or spec.loader is None:
                continue

            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            return module.run_reducer

    raise ImportError(f"Could not resolve {package_name}.reducer")


run_reducer = _load_run_reducer()

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

        # Convertir solo columnas numéricas
        df = df.select_dtypes(include=["number"])

        # Eliminar filas con NaN
        df = df.dropna()

        # Limitar filas para Render Free
        MAX_ROWS = 5000
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
# Render Free compatible server
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
