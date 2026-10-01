"""
Algoritmo de Dijkstra El algoritmo de Dijkstra encuentra los caminos
más cortos desde un nodo fuente hacia todos los demás nodos en un 
grafo con pesos no negativos.
"""

# Implementación en Python:

import heapq

def dijkstra(graph, start):
    # Tabla de distancias: guarda la distancia mínima desde el nodo inicio a cada nodo
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Cola de prioridad para procesar nodos
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Procesar solo si encontramos un mejor camino
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Actualizar si se encuentra un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Ejemplo de grafo como lista de adyacencia
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Caminos más cortos desde 'A'
shortest_paths = dijkstra(graph, 'A')
print("Caminos más cortos desde A:", shortest_paths)