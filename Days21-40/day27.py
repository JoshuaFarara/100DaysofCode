'''
Day Twenty-Seventh of 100 Days of Code

July 5th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Queues
*Linked List
Trees
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
        self.data = data
        self.next = None

class LinkedList:
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
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

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

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

singlyLinked = LinkedList()
singlyLinked.append(1)
singlyLinked.append(2)
singlyLinked.append(3)
print("\nInitial List with appened to tail.")
singlyLinked.display()

singlyLinked.insertFront(4)
singlyLinked.insertFront(5)
singlyLinked.insertFront(6)
singlyLinked.append(7) # proves adding node to tail
print("\nInitial List with inserted nodes to head.")


singlyLinked.display()
