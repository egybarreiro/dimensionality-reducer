class Queue:
        def __init__(self):
            self.items = []
    
        def enqueue(self, item):
            self.items.insert(0, item)
    
        def dequeue(self):
            return self.items.pop()
    
        def peek(self):
            return self.items[-1] if self.items else None
    
        def is_empty(self):
            return not self.items