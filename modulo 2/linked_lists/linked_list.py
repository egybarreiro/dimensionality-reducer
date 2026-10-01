# Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Uso
sll = SinglyLinkedList()
sll.insert_at_beginning(3)
sll.insert_at_beginning(2)
sll.insert_at_beginning(1)
print("Lista enlazada simple:")
sll.traverse()


# Double Linked List
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoubleNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Uso
dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
print("Lista enlazada doble:")
dll.traverse()