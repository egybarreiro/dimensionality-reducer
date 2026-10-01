# Desafio 1 : Suma de filas en una matriz.

matrix = [[1,2,3], [4,5,6]]

#salida debe ser [6, 15]

def sum_rows(matrix):
    return [sum(row) for row in matrix]

print(sum_rows(matrix))


#============================================================================

# Desafio 2: Transponer una matriz.

matrix = [[1,2,], [3,4], [5,6]]

#La salida transpuesta debe ser [[1, 3, 5], [2, 4, 6]]

T = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])

    T.append(row)

print(T)

# Formato list comprehension

T = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("List comprehension result:", T)

# Transponiendo con funcion en list comprehension

def transpose(matrix):
    T = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return(T)
print("Function with list comprehension result:", transpose(matrix))


#============================================================================

# Desafio 3: Aplanar una lista anidada.


nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

flat_list = []

for sub_list in nested_list:
    for i in sub_list:
        flat_list.append(i)

print(flat_list)


# Formato list comprehension

nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

flat_list = [i for sub_list in nested_list for i in sub_list]
print ("List comprehension result:", flat_list)

# Formato funcion con list comprehension 

nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

def list_flattner(nested_list):
    flat_list = [i for sub_list in nested_list for i in sub_list]
    return flat_list

print ("Using a function with list comprehension result:", list_flattner(nested_list))


#============================================================================

# Desafio 4: Este desafio consiste en implementar una funcion 
# que use una pila para verificar si una expresion tiene 
# caracteres balanceados.

from stack import Stack


def balanced_character_checker(expression):

    stack = Stack()

    pairs = {')' : '(', ']' : '[', '}' : '{'}


    for char in expression:
        if char in pairs.values():
            stack.push(char)

        elif char in pairs:
            if stack.is_empty():
                return False

            if stack.pop() != pairs[char]:
                return False

        else:
            return False
            

    return stack.is_empty()

def main():
    print("Character Checker")

    result = balanced_character_checker("([{])")
    print(f"Balanced: {result}")

    return


if __name__ == "__main__":
    main()


    #============================================================================


# Desafio 5: Invertir los primeros K elementos de una cola: 
# Escribe una función que invierta los primeros K elementos 
# de una cola. Ejemplo: Para Queue = [1, 2, 3, 4, 5] y K = 3, 
#la nueva cola debe ser [3, 2, 1, 4, 5].


from stack import Stack
from queue import Queue


def reverse_queue(queue, K):

    stack = Stack()

    for k in range(K):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    for e in range(len(queue.items) - K):
        queue.enqueue(queue.dequeue())

    return queue


def main():

    print('K Reverse')

    K = 3 # input("Insert K: ")

    # define the queue
    queue = Queue()
    for number in [1, 2, 3, 4, 5]:
        queue.enqueue(number)

    print(reverse_queue(queue, K).items)

    return


if __name__ == "__main__":
    main()


#============================================================================

# Desafio 6: Implementación de una cola utilizando dos pilas 
# con operaciones de enqueue y dequeue.

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            raise IndexError("La cola está vacía.")

        return self.stack_out.pop()

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)
    


queue = QueueUsingStacks()


queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


print("Salida 1:", queue.dequeue())  
print("Salida 2:", queue.dequeue())  
print("Salida 3:", queue.dequeue())


#============================================================================

# Desafio 7: Siguiente elemento mayor: Dado un arreglo, 
# imprime el siguiente elemento mayor (NGE) para cada elemento 
# usando una pila. El siguiente elemento mayor de x es el 
# primer elemento mayor a la derecha de x en el arreglo. 
# Ejemplo: Para el arreglo [4, 5, 2, 25], 
# la lista NGE es [5, 25, 25, -1].

arr = [4, 5, 2, 25]

def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result


print("Arreglo:", arr)
print("NGE:", next_greater_element(arr))