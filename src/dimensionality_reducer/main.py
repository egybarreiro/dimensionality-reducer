# Propósito: CLI para reducir dimensionalidad de datos tabulares
# Autor: Tu_nombre, tu_email
# Versión: 1.0

import argparse

import pandas as pd

from src.dimensionality_reducer.reducer import DimensionalityReducer


def main():
    parser = argparse.ArgumentParser(description='Reduce dimensionalidad de datos tabulares')
    parser.add_argument('-f', '--file', required=True, type=str, help='Ruta al archivo CSV')
    parser.add_argument('-m', '--method', required=True, default='pca', type=str,
                        help='Método de reducción (pca, tsne, umap, lda)')
    parser.add_argument('-n', '--normalize', action='store_true', help='Normalizar datos')
    args = parser.parse_args()

    data = pd.read_csv(args.file)
    target = data.iloc[:, -1]
    features = data.iloc[:, :-1]

    reducer = DimensionalityReducer(features, normalize=args.normalize)

    if args.method == 'pca':
        reduced_data = reducer.reduce_with_pca()
    elif args.method == 'tsne':
        reduced_data = reducer.reduce_with_tsne()
    elif args.method == 'umap':
        reduced_data = reducer.reduce_with_umap()
    elif args.method == 'lda':
        reduced_data = reducer.reduce_with_lda(target)
    else:
        print('Método no soportado')
        return

    reducer.plot_reduced_data(reduced_data, target)


if __name__ == '__main__':
    print("Aplicación de reducción de dimensionalidad")
    main()