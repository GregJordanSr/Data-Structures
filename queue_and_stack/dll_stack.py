from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList
    # adding - Where do we add in a stack?
    def push(self, value):
        pass
    # removing - Where do we remove?
    def pop(self):
        pass

    def len(self):
        pass
