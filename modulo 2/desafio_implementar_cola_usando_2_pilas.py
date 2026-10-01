""" Implementación de una cola utilizando dos pilas con operaciones 
de enqueue y dequeue. """

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

