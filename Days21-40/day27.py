'''
Day Twenty-Seventh of 100 Days of Code

July 5th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Queues
*Linked List
    singly
    *doubly
*Trees
Tries
Graphs (BFS and DFS)
Hashing
Heaps
Sorting
Searching
'''

# Doubly linked list
class Node:
    def __init__(self, data):
        self.previous = None #requires additional memory for the backward reference.
        self.data = data
        self.next = None

class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
         # if linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None: 
            self.head = Node(data)
            self.last_node = self.head
        # adding node to the tail of linked list
        else:
            new_node = Node(data)
            self.last_node.next = new_node
            new_node.previous = self.last_node
            new_node.next = None
            self.last_node = new_node

    def insertFront(self, data): # add a node to the beginning of the linked list
        if self.last_node is None: 
            self.head = Node(data)
            self.last_node = self.head
        else:
            # Allocate the Node and put in the data
            new_node = Node(data)
            # Make next of new Node as head
            new_node.next = self.head
            # Move the head to point to new Node
            self.head = new_node
            new_node.previous = self.last_node


    def display(self, Type):
        if Type == 'Left_To_Right':
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
            print()
        else:
            current = self.last_node
            while current is not None:
                print(current.data, end=' ')
                current = current.previous
            print()

DoublyLinkedList = DoublyLinkedList()
DoublyLinkedList.append(1)
DoublyLinkedList.append(2)
DoublyLinkedList.append(3)
print("\nInitial List with appened to tail.")
DoublyLinkedList.display('Left_To_Right')
DoublyLinkedList.display('Right_To_Left')

DoublyLinkedList.insertFront(4)
DoublyLinkedList.insertFront(5)
DoublyLinkedList.insertFront(6)
DoublyLinkedList.append(7) # proves adding node to tail
print("\nInitial List with inserted nodes to beginning.")


# DoublyLinkedList.display()
DoublyLinkedList.display('Left_To_Right')
DoublyLinkedList.display('Right_To_Left')


# Tree