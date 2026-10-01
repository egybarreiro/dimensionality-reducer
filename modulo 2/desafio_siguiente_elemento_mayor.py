""" Este desafio consiste en el escenario de dado un arreglo, 
imprime el siguiente elemento mayor (NGE) para cada elemento 
usando una pila. El siguiente elemento mayor de x es el primer 
elemento a la derecha de x que es mayor que x. """

# Para el arreglo [4, 5, 2, 25] la lista NGE debe ser [5, 25, 25, -1]


def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)  # Inicializar el resultado con -1

    for i in range(len(arr)):
        # Mientras la pila no esté vacía y el elemento actual sea 
        # mayor que el elemento en la cima de la pila
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

# Salida de prueba para verificar el resultado
print(next_greater_element([4, 5, 2, 25]))

