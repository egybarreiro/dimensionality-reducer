# graph.py

def construir_grafo(ciudades, vuelos):
    """
    Construye un grafo dirigido ponderado.
    grafo[ciudad] = lista de (vecino, costo)
    """
    grafo = {ciudad: [] for ciudad in ciudades}

    for origen, destino, costo in vuelos:
        grafo[origen].append((destino, costo))

    return grafo
