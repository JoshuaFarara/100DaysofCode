'''
Day Twenty-Sixth of 100 Days of Code

July 4th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Queues
*Linked List
    *singly
    doubly
Trees
Tries
Graphs (BFS and DFS)
Hashing
Heaps
Sorting
Searching
'''

# Linked List
# A linked list is a linear data structure, 
# in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

# Singly-linked List - forward direction traversaal only each node linking to its next node
# operations include - indertion, deletion, search, display 

class Node: # Contatiner for some data
    # initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None #initialize next as null
    
# SinglyLinked List class
class SinglyLinkedList:
    #linked list function initilize list object
    def __init__(self):
        self.head = None
    # Insert new node in the beginning of the linked list. 
    '''
    Make the first node of Linked List linked to the new node
    Remove the head from the original first node of Linked List
    Make the new node as the Head of the Linked List.
    '''
    def add_node(self, data):
        # Allocate the Node and put in the data
        new_node = Node(data)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next

# if __name__ =='__main__':
#     head = None
swimmer = Node('Swim')
runner = Node('Run')
cyclist = Node('Cycle')
lifter = Node('Lift')

# creating the linked list
# A -> B -> C -> D -> None
swimmer.next = runner
runner.next = cyclist
cyclist.next = lifter


def printLinkedList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next
    print("\n") 

printLinkedList(swimmer)

# this function does the same as the one above. The difference in this implementation lies in the use of a pointer, this function does not use a pinter such as current to take
# the place of the node recieved in the function call.
def printList(node):
    while (node != None):
        print(node.data, end=" ") # end=" " makes each value printed on one line"
        node = node.next
    print("\n") 

printList(swimmer)

activityList = SinglyLinkedList()
activityList.add_node('cash')
activityList.add_node('cashApp')
activityList.add_node('venmo')
activityList.add_node('zelle')

activityList.display()