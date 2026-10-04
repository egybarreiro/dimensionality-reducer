# Dimensionality Reducer

Aplicación web para reducir dimensionalidad en datasets y visualizar los resultados de forma clara y accesible.  
Permite aplicar cuatro algoritmos principales:

- **PCA** (Principal Component Analysis)  
- **t‑SNE** (t‑Distributed Stochastic Neighbor Embedding)  
- **UMAP** (Uniform Manifold Approximation and Projection)  
- **LDA** (Linear Discriminant Analysis)

La app genera gráficos 2D que muestran la estructura del dataset, clusters y relaciones entre variables, facilitando análisis exploratorio y visualización de datos complejos.

## Características

- Subida de archivos CSV directamente desde el navegador.  
- Selección de método de reducción desde la interfaz.  
- Preprocesamiento automático:
  - filtrado de columnas numéricas  
  - eliminación de valores nulos  
  - muestreo para datasets grandes  
- Visualización generada con Matplotlib.  
- Backend en Flask, optimizado para despliegue en Railway.  
- Implementación modular del reducer en `webapp/dimensional