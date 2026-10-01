"""
Invertir los primeros K elementos de una cola: Escribe una función que invierta 
los primeros K elementos de una cola. Ejemplo: Para Queue = [1, 2, 3, 4, 5] y K = 3, 
la nueva cola debe ser [3, 2, 1, 4, 5].
"""

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