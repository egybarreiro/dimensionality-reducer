import pandas as pd
import os

def main():
    """
    Crea una versión reducida del dataset MNIST tabular
    para que pueda ser procesado en plataformas gratuitas.
    """

    # Ruta correcta del archivo grande
    input_path = os.path.join("data", "mnist_tabular.csv")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encontró el archivo: {input_path}")

    # Cargar dataset grande
    df = pd.read_csv(input_path)

    # Reducir a 5000 filas (puedes bajar a 3000 si Railway se queja)
    df_small = df.head(5000)

    # Guardar dataset reducido en la misma carpeta
    output_path = os.path.join("data", "mnist_small.csv")
    df_small.to_csv(output_path, index=False)

    print(f"Archivo creado: {output_path} con {len(df_small)} filas.")

if __name__ == "__main__":
    main()
