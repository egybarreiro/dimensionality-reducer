""" Algoritmos de Ordenamiento y Busqueda. """

import time

array = [64, 34, 25, 12, 22, 11, 90] * 1000  # Aumentar el tamaño del array para probar el rendimiento

# Algoritmo de Ordenamiento por Burbuja (Bubble Sort)
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


# Algoritmo de Ordenamiento por Selección (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Probar la función selection_sort
array = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
sorted_array = selection_sort(array)
end_time = time.time()
print("Sorted array is:", sorted_array)
print("Total Execution time selection sort:", end_time - start_time, "seconds")


# Algoritmo de Ordenamiento por Inserción (Insertion Sort)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Probar la función insertion_sort
array = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
sorted_array = insertion_sort(array)
end_time = time.time()
print("Sorted array is:", sorted_array)
print("Total Execution time insertion sort:", end_time - start_time, "seconds")