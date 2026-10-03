import pandas as pd
import streamlit as st

from dimensionality_reducer import DimensionalityReducer

st.set_page_config(page_title="Reducción de dimensionalidad", layout="wide")
st.title("Aplicación de Reducción de Dimensionalidad")

st.markdown(
    """
    <style>
    body { background-color: #282727; color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("Archivo subido exitosamente")

    method = st.selectbox(
        "Selecciona el método de reducción",
        ["pca", "tsne", "umap", "lda"],
    )
    normalize = st.checkbox("Normalizar datos")

    if st.button("Reducir dimensionalidad"):
        if data.shape[1] < 2:
            st.error(
                "El archivo debe tener al menos dos columnas: una de características y una objetivo."
            )
        else:
            target = data.iloc[:, -1]
            features = data.iloc[:, :-1]

            reducer = DimensionalityReducer(features, normalize=normalize)
            if method == "pca":
                reduced_data = reducer.reduce_with_pca()
            elif method == "tsne":
                reduced_data = reducer.reduce_with_tsne()
            elif method == "umap":
                reduced_data = reducer.reduce_with_umap()
            elif method == "lda":
                reduced_data = reducer.reduce_with_lda(target)
            else:
                st.error("Método no soportado.")
                reduced_data = None

            if reduced_data is not None:
                reducer.plot_reduced_data(reduced_data, target)

st.markdown("Repositorio en GitHub: [Repositorio](https://github.com/egybarreiro/dimensionality-reducer)")