"""Análisis de complejidad de algoritmos"""

#Here we import the time module to measure execution time
#This is the code for the linear search algorithm and a function to measure its execution time
import time

def linear_search(arr, target):
    """Realiza una búsqueda lineal en la lista arr para encontrar el target."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Ejemplo de uso de la función de búsqueda lineal
import time

def linear_search(books, target):
    """Realiza una búsqueda lineal en la lista arr para encontrar el target."""
    for i in range(len(books)):
        if books[i] == target:
            return i
    return -1

#Probando el algoritmo de búsqueda lineal con una lista de libros
books = ["The Hobbit", "To Kill a Mockingbird",  "Pride and Prejudice"] * 100000000 + ["1984"]    # Lista de libros con 100,000,000 elementos
#print(books)

start_time = time.time()


print("Book found at index:", linear_search(books, "1984"))

end_time = time.time()
print(end_time)

print("Total Execution time:", end_time - start_time, "seconds")



#How to use the measure_time function
def measure_time(func, *args):
    """Mide el tiempo de ejecución de una función."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time


#Resoluciones iterativas y recursivas

FACTORIAL_INPUT = 100

def factorial_recursive(n):
    if n == 1: # Caso base
        return 1
    else: # Caso recursivo
        return n * factorial_recursive(n - 1)

# Probar la función
start_time = time.time()
#print(f"Factorial de {FACTORIAL_INPUT}:", factorial_recursive(FACTORIAL_INPUT))
end_time = time.time()
recursive_time = end_time - start_time
print(f"Recursive Total runtime of the program is {end_time - start_time} seconds")

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Probar la función
start_time = time.time()
#print(f"Factorial de {FACTORIAL_INPUT}:", factorial_iterative(FACTORIAL_INPUT))
end_time = time.time()
iterative_time = end_time - start_time
print(f"Iterative Total runtime of the program is {end_time - start_time} seconds")

if iterative_time < recursive_time:
    print('Iterative is faster', iterative_time - recursive_time)
elif iterative_time > recursive_time:
    print('Recursive is faster', iterative_time - recursive_time)
else:
    print("They are both the same", iterative_time - recursive_time)


# Algoritmo de Fibonacci Iterativo
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Probar la función fibonacci_iterative
import time

start_time = time.time()
print("Numero iterado de Fibonacci en la posicion 10:", fibonacci_iterative(10))  # Salida: 55
end_time = time.time()

print("Total Execution time iterative:", end_time - start_time, "seconds")



# Algoritmo de Fibonacci Recursivo
def fibonacci_recursive(n):
    if n <= 1:  # Casos base
        return n
    else:  # Caso recursivo
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Probar la función fibonacci_recursive
import time

start_time = time.time()
print(f"Fibonacci recursivo de 10:", fibonacci_recursive(10))  # Salida: 55
end_time = time.time()

print("Total Execution time recursive:", end_time - start_time, "seconds")



