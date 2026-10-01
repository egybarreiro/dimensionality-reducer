# utils.py

import json
import os
import random

def reconstruir_ruta(previo, origen, destino):
    """
    Reconstruye la ruta desde origen hasta destino usando el diccionario 'previo'.
    Si no existe ruta posible, devuelve una lista vacía.
    """
    ruta = []
    actual = destino

    if previo[actual] is None and actual != origen:
        return []

    while actual is not None:
        ruta.append(actual)
        if actual == origen:
            break
        actual = previo[actual]

    ruta.reverse()
    return ruta


def validar_entradas(ciudades, vuelos, origen, destino):
    """
    Valida que origen y destino existan en la lista de ciudades
    y que exista al menos un vuelo en el dataset.
    """
    if origen not in ciudades:
        raise ValueError(f"Origen '{origen}' no está en la lista de ciudades.")
    if destino not in ciudades:
        raise ValueError(f"Destino '{destino}' no está en la lista de ciudades.")
    if not vuelos:
        raise ValueError("No hay vuelos disponibles para calcular rutas.")


def cargar_dataset():
    """
    Carga el dataset desde datasets/dataset.json usando una ruta absoluta.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "datasets", "dataset.json")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"El archivo {filename} no existe.")

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    ciudades = data.get("ciudades", [])
    origen = data.get("origen")
    destino = data.get("destino")

    vuelos_json = data.get("vuelos", [])
    vuelos = [(v["origen"], v["destino"], v["costo"]) for v in vuelos_json]

    return ciudades, vuelos, origen, destino


def guardar_dataset(ciudades, vuelos):
    """
    Guarda el dataset actualizado en datasets/dataset.json.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "datasets", "dataset.json")

    data = {
        "ciudades": ciudades,
        "vuelos": [
            {"origen": o, "destino": d, "costo": c}
            for (o, d, c) in vuelos
        ],
        "origen": None,
        "destino": None
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def agregar_ciudad(ciudades, vuelos, nueva_ciudad):
    """
    Agrega una ciudad nueva al dataset y genera vuelos aleatorios
    hacia otras ciudades existentes (si existen).
    Si es la primera ciudad del dataset, no genera vuelos.
    """
    print(f"\n>>> La ciudad '{nueva_ciudad}' no existe actualmente en la base de datos. Será agregada automáticamente.")

    ciudades.append(nueva_ciudad)

    # Si es la primera ciudad, no hay destinos posibles
    if len(ciudades) == 1:
        print(f"No se generan vuelos porque '{nueva_ciudad}' es la primera ciudad del dataset.")
        return ciudades, vuelos

    # Generar entre 1 y 4 vuelos aleatorios
    cantidad_vuelos = random.randint(1, 4)
    print(f"Generando {cantidad_vuelos} vuelos aleatorios desde {nueva_ciudad}...")

    for _ in range(cantidad_vuelos):
        destino = random.choice([c for c in ciudades if c != nueva_ciudad])
        costo = random.randint(100, 900)

        vuelos.append((nueva_ciudad, destino, costo))
        print(f"  {nueva_ciudad} -> {destino} (costo: {costo})")

    return ciudades, vuelos
