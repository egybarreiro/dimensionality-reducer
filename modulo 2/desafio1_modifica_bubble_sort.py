"""Desafio 1: Modificar el algoritmo de ordenamiento por burbuja para que ordene el array en orden descendente."""
# Algoritmo de Ordenamiento por Burbuja (Bubble Sort) ascendente
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Probar la función bubble_sort
array = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
sorted_array = bubble_sort(array)
end_time = time.time()
print("Sorted array is:", sorted_array)
print("Total Execution time bubble sort:", end_time - start_time, "seconds")


# Algoritmo de Ordenamiento por Burbuja (Bubble Sort) descendente
def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:  # Cambiar el operador de comparación para orden descendente
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Probar la función bubble_sort_descending
array = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
sorted_array = bubble_sort_descending(array)
end_time = time.time()
print("Sorted array (descending) is:", sorted_array)
print("Total Execution time bubble sort (descending):", end_time - start_time, "seconds")