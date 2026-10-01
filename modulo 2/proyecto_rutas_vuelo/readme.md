Proyecto de Rutas de Vuelo
Algoritmo de Dijkstra + Generación dinámica de ciudades y vuelos.

Descripción General
Este proyecto implementa un sistema dinámico para calcular la ruta óptima entre dos ciudades utilizando el algoritmo de Dijkstra.
El usuario define el origen y el destino, y el sistema construye automáticamente el grafo, agregando ciudades y generando vuelos aleatorios cuando estas no existen en el dataset.

El dataset inicial es un template vacío, lo que permite que el sistema crezca dinámicamente según la interacción del usuario.

Características Principales
Dataset inicial vacío (plantilla).

El usuario define origen y destino.

Ciudades nuevas se agregan automáticamente al dataset.

Vuelos aleatorios se generan dinámicamente.

Grafo dirigido ponderado.

Algoritmo de Dijkstra para encontrar la ruta óptima.

Dataset se actualiza en cada ejecución.

Compatible con datasets vacíos o datasets completos importados.

Estructura del Proyecto
Code
proyecto_rutas_vuelo/
│
├── main.py
├── utils.py
├── graph.py
├── dijkstra.py
│
├── datasets/
│   └── dataset.json
│
├── README.md
└── requirements.txt
Dataset (template inicial)
El proyecto utiliza un dataset tipo plantilla, vacío, que permite que el sistema genere ciudades y vuelos dinámicamente.

json
{
    "ciudades": [],
    "vuelos": [],
    "origen": null,
    "destino": null
}
Se puede importar un dataset lleno.
Si decides reemplazar este archivo por uno con ciudades y vuelos reales, el sistema no debería romperse.
Simplemente utilizará esos datos como base y seguirá expandiendo el dataset dinámicamente.

Archivos del Proyecto
main.py
Controla el flujo principal del programa:

-carga el dataset

-solicita origen y destino

-agrega ciudades nuevas si no existen

-genera vuelos aleatorios

-construye el grafo

-ejecuta Dijkstra

-muestra la ruta óptima

utils.py
Funciones auxiliares:

-cargar y guardar dataset

-validar entradas

-reconstruir ruta

-agregar ciudades nuevas

-generar vuelos aleatorios

graph.py
Construye el grafo dirigido ponderado a partir del dataset.

dijkstra.py
Implementación del algoritmo de Dijkstra para calcular rutas óptimas.

Cómo Ejecutar el Proyecto
Abrir terminal en la carpeta del proyecto

Ejecutar:

Code
python main.py
Ingresar ciudad de origen.

Ingresar ciudad de destino.

El sistema generará vuelos, construirá el grafo y mostrará la ruta óptima

requirements.txt
Este proyecto utiliza únicamente librerías estándar de Python.

Code
Dependencias externas no son requeridas.
Comportamiento del Sistema
-Dataset vacío
El sistema agrega ciudades nuevas y genera vuelos automáticamente.

-Dataset lleno
El sistema utiliza los datos existentes y continúa expandiéndolos dinámicamente.

-Ciudades inexistentes
Se agrega la ciudad al dataset y se generan vuelos aleatorios hacia otras ciudades registradas.

Estado del Proyecto
Proyecto completo, funcional y listo para evaluación.
Incluye documentación, estructura profesional y dataset plantilla.