# main.py

from graph import construir_grafo
from dijkstra import dijkstra
from utils import (
    cargar_dataset,
    validar_entradas,
    reconstruir_ruta,
    agregar_ciudad,
    guardar_dataset
)

def main():
    """
    Flujo principal del programa:
    - Carga dataset vacío o existente
    - Usuario define origen y destino
    - Si no existen, se agregan dinámicamente
    - Se generan vuelos aleatorios
    - Se construye el grafo
    - Se ejecuta Dijkstra
    - Se muestra ruta óptima
    """
    try:
        ciudades, vuelos, _, _ = cargar_dataset()

        print("\n=== Bienvenido a Optimus Travel ===")
        print("El buscador de rutas y vuelos preferido.")
        print("¿Cuál es tu próxima aventura?")

        origen = input("\nIngrese ciudad de origen: ").strip()
        destino = input("Ingrese ciudad de destino: ").strip()

        # Agregar ciudades si no existen
        if origen not in ciudades:
            ciudades, vuelos = agregar_ciudad(ciudades, vuelos, origen)

        if destino not in ciudades:
            ciudades, vuelos = agregar_ciudad(ciudades, vuelos, destino)

        # Guardar dataset actualizado
        guardar_dataset(ciudades, vuelos)

        # Validar
        validar_entradas(ciudades, vuelos, origen, destino)

        # Construir grafo
        grafo = construir_grafo(ciudades, vuelos)

        print("\n=== Ruta potencial (Grafo construido) ===")
        for ciudad, conexiones in grafo.items():
            print(f"{ciudad}: {conexiones}")

        # Ejecutar Dijkstra
        distancias, previo = dijkstra(grafo, origen)

        print("\n=== Costos mínimos ===")
        for ciudad, costo in distancias.items():
            print(f"{ciudad}: {costo}")

        # Reconstruir ruta
        ruta = reconstruir_ruta(previo, origen, destino)

        if not ruta:
            print("\nNo existe ruta posible entre las ciudades seleccionadas.")
            return

        print("\n=== Resultado final ===")
        print("Ruta óptima:", ruta)
        print("Costo total:", distancias[destino])
        print("Que disfrutes! Gracias por elegir Optimus Tavel.aSa" \
        "Hasta la próxima.")

    except Exception as e:
        print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    main()
