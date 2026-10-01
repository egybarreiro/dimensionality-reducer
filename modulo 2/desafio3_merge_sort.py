""" Implementando Merge Sort para cadena de caracteres."""

import time

array = ["banana", "apple", "Cherry", "date", "fig", "grape", "kiwi"]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].lower() < right_half[j].lower():
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Probar la función merge_sort
start_time = time.time()
sorted_array = merge_sort(array)
end_time = time.time()
print("Sorted array  is:", sorted_array)
print("Total Execution time merge sort:", end_time - start_time, "seconds")