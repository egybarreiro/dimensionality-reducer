""" Implementacion del algoritmo de ordenamiento 
Quick Sort de manera iterativa."""


import time


def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_index = i + 1

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr


array = [10, 1, 8, 3, 1, 6, 2]

sorted_array = quick_sort(array)

print("Arreglo ordenado:", sorted_array)

# Probar la función quick_sort iterativa
array = [10, 1, 8, 3, 1, 6, 2]
start_time = time.time()
sorted_array = quick_sort(array)
end_time = time.time()
print("Sorted array is:", sorted_array)
print("Total Execution time quick sort:", end_time - start_time, "seconds")



""" Implementacion del algoritmo de ordenamiento
Quick Sort de manera recursiva."""

def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

    # Probar la función quick_sort_recursive
array = [10, 1, 8, 3, 1, 6, 2]
start_time = time.time()
sorted_array = quick_sort_recursive(array)
end_time = time.time()
print("Sorted array is:", sorted_array)
print("Total Execution time quick sort recursive:", end_time - start_time, "seconds")
