# Propósito: Ejecutar reducción de dimensionalidad desde la línea de comandos
# Autor: Edgar Barreiro Serrano
# Versión: 1.0

import argparse
import pandas as pd
from webapp.dimensionality_reducer.reducer import run_reducer

def main():
    parser = argparse.ArgumentParser(
        description="Aplicación CLI para reducción de dimensionalidad usando PCA, t-SNE, UMAP o LDA."
    )

    parser.add_argument(
        "-f", "--file",
        required=True,
        type=str,
        help="Ruta del archivo CSV a procesar."
    )

    parser.add_argument(
        "-m", "--method",
        required=True,
        type=str,
        choices=["pca", "tsne", "umap", "lda"],
        help="Método de reducción de dimensionalidad."
    )

    parser.add_argument(
        "--normalize",
        action="store_true",
        help="Normaliza los datos antes de reducir."
    )

    args = parser.parse_args()

    print("\n=== Dimensionality Reducer CLI ===")
    print(f"Archivo: {args.file}")
    print(f"Método: {args.method}")
    print(f"Normalizar: {args.normalize}")
    print("----------------------------------\n")

    try:
        df = pd.read_csv(args.file)

        result = run_reducer(df, args.method)

        print("Reducción completada.\n")
        print("Primeros valores del embedding:\n")
        print(result["embedding"][:10])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Mi aplicación de reducción de dimensionalidad")
    main()
