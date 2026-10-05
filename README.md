# Dimensionality Reducer – Proyecto Práctico de Ingeniería de Características

Este proyecto implementa una clase de Python llamada **DimensionalityReducer**, diseñada para procesar datos tabulares y aplicar reducción de dimensionalidad utilizando cuatro técnicas fundamentales en Machine Learning:

- **PCA** (Principal Component Analysis)  
- **t‑SNE** (t‑Distributed Stochastic Neighbor Embedding)  
- **UMAP** (Uniform Manifold Approximation and Projection)  
- **LDA** (Linear Discriminant Analysis)

El proyecto incluye:

- Una **clase** con los cuatro métodos de reducción.  
- Una **CLI** funcional para ejecutar los métodos desde terminal.  
- Un **dashboard web** (Flask) para visualización interactiva, exportación de resultados y manejo de historial.

---

## 📌 Objetivos del proyecto

1. Construir una clase llamada **DimensionalityReducer** que:
   - Se inicialice con datos tabulares.
   - Ofrezca los métodos:
     - `reduce_with_pca()`
     - `reduce_with_tsne()`
     - `reduce_with_umap()`
     - `reduce_with_lda()`
   - Reduzca los datos a **dos componentes** para facilitar la visualización.
   - Genere un **diagrama de dispersión** de los datos reducidos.
   - Permita elegir si se desea aplicar **normalización**.

2. Crear una **CLI** en Python con `argparse` que permita:
   - Cargar un archivo CSV.
   - Seleccionar el método de reducción.
   - Ejecutar la clase desde terminal.

3. Implementar un **dashboard web** opcional con:
   - Upload de CSV.
   - Visualización de clusters.
   - Estadísticas descriptivas.
   - Tabla de las primeras filas.
   - Exportación del CSV reducido.
   - Descarga de imágenes generadas.
   - Historial de ejecuciones.
   - Loading overlay y animación del logo.

---

## 📁 Estructura del proyecto

Terminal34_Bootcamp/
│
├── main.py
├── cli.py
├── requirements.txt
├── README.md
│
├── webapp/
│   ├── app.py
│   ├── history.json
│   ├── dimensionality_reducer/
│   │   └── reducer.py
│   ├── static/
│   │   ├── dimred_dark.css
│   │   ├── dimred-logo.png
│   │   ├── pca_plot.png
│   │   ├── tsne_plot.png
│   │   ├── umap_plot.png
│   │   └── lda_plot.png
│   └── templates/
│       └── index.html
│
└── datasets/
├── mnist_small.csv
└── unit_1_feature_engineering_exercise_data.csv

---

## ▶️ CLI – Uso desde terminal

Ejemplo:

```bash
python cli.py -f datasets/mnist_small.csv -m pca --normalize
-f, --file        Ruta del archivo CSV
-m, --method      pca | tsne | umap | lda
--normalize       Normaliza los datos antes de reducir

🌐 Dashboard Web
Ejecutar:
python main.py

Abrir en navegador:
http://127.0.0.1:5000

Funciones disponibles:

Upload de CSV

Selección de método

Visualización de clusters

Estadísticas descriptivas

Tabla (primeras 20 filas)

Exportación de CSV reducido

Descarga de imagen generada

Historial de ejecuciones

Loading overlay

Animación del logo

📦 Requisitos
Python 3.x
Librerías:

numpy

pandas

scikit-learn

matplotlib

seaborn

umap-learn

flask

📊 Dataset de prueba
MNIST reducido:
https://drive.google.com/file/d/1dbmDMVvzQ2_frxKAhFRxXyVs1wvX1-nY/view?usp=sharing

Dataset adicional:
unit_1_feature_engineering_exercise_data.csv

✔️ Estado del proyecto
100% completo y funcional.  
Cumple todos los requisitos del profesor y añade un dashboard profesional.
PCA – OK  
t‑SNE – OK  
UMAP – OK  
LDA – OK  
Normalización – OK  
Visualización 2D – OK  
CLI – OK  
Clase DimensionalityReducer – OK  
Dashboard – OK  
Exportación – OK  
Historial – OK  

👨‍🏫 Autor
Edgar Barreiro Serrano
Terminal 34 Bootcamp
2026
https://github.com/egybarreiro/dimensionality-reducer
