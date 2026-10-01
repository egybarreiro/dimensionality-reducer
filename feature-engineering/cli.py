# Propósito: CLI para aplicar reducción de dimensionalidad sobre un CSV.
# Autor: Edgar Barreiro
# Versión: 1.0.0

import argparse

import pandas as pd
from dimensionality_reducer import DimensionalityReducer


def main():
    parser = argparse.ArgumentParser(description="Aplicación de reducción de dimensionalidad.")
    parser.add_argument("-f", "--file", required=True, help="Ruta al archivo CSV.")
    parser.add_argument("-m", "--method", required=True, choices=["pca", "tsne", "umap", "lda"], help="Método de reducción.")
    parser.add_argument("-t", "--target-column", default=None, help="Columna objetivo (solo para LDA).")
    parser.add_argument("--no-normalize", action="store_true", help="Desactiva la normalización.")
    parser.add_argument("--no-plot", action="store_true", help="No mostrar gráfico.")
    args = parser.parse_args()

    data = pd.read_csv(args.file)
    reducer = DimensionalityReducer(data, target_column=args.target_column, normalize=not args.no_normalize)

    methods = {
        "pca": reducer.reduce_with_pca,
        "tsne": reducer.reduce_with_tsne,
        "umap": reducer.reduce_with_umap,
        "lda": reducer.reduce_with_lda,
    }

    embedding = methods[args.method]()
    print(f"Método: {args.method}\nPrimeras 5 filas:\n", embedding[:5])

    if not args.no_plot:
        reducer.plot_2d(embedding, labels=reducer.y, title=args.method.upper())


if __name__ == "__main__":
    print("Mi aplicación de reducción de dimensionalidad")
    main()
