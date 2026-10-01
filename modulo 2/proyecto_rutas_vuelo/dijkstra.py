# dijkstra.py

import heapq

def dijkstra(grafo, origen):
    """
    Implementación del algoritmo de Dijkstra.
    Calcula el costo mínimo desde 'origen' hacia todas las ciudades del grafo.
    """
    distancias = {ciudad: float("inf") for ciudad in grafo}
    distancias[origen] = 0

    previo = {ciudad: None for ciudad in grafo}

    heap = [(0, origen)]

    while heap:
        costo_actual, ciudad_actual = heapq.heappop(heap)

        if costo_actual > distancias[ciudad_actual]:
            continue

        for vecino, costo in grafo[ciudad_actual]:
            nuevo_costo = costo_actual + costo

            if nuevo_costo < distancias[vecino]:
                distancias[vecino] = nuevo_costo
                previo[vecino] = ciudad_actual
                heapq.heappush(heap, (nuevo_costo, vecino))

    return distancias, previo
