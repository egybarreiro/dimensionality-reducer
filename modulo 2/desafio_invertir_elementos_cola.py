""" Este desafio consiste en invertir los primeros K elementos 
de una cola: Escribe una funcion que invierta los primeros 
K elementos de una cola. Ejemplo: Para 'Queue = [1, 2, 3, 4, 5]' 
y 'K = 3', la nueva cola debe ser '[3, 2, 1, 4, 5]'.


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")

    def __str__(self):
        return str(self.items)

def reverse_first_k_elements(queue, k):
    if k > queue.size() or k < 0:
        raise ValueError("K debe ser un número válido dentro del rango de la cola")

    stack = []

    # Sacar los primeros K elementos de la cola y ponerlos en la pila
    for _ in range(k):
        stack.append(queue.dequeue())

    # Poner los elementos de la pila de nuevo en la cola (invertidos)
    while stack:
        queue.enqueue(stack.pop())

    # Rotar los elementos restantes de la cola para mantener el orden original
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())


# Salida de la cola invertida para verificar el resultado
q = Queue()
for n in [1, 2, 3, 4, 5]:
    q.enqueue(n)

reverse_first_k_elements(q, 3)
print(q.items) # Salida esperada: [3, 2, 1, 4, 5]
"""

