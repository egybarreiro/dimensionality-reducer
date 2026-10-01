class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, char):
        self.items.append(char)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack vacío; no se puede ejecutar POP.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return not self.items
