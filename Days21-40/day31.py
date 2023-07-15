'''
Day Thirty-First of 100 Days of Code

July 14th, 2023

Todays program demonstrates the implementation of a priority queue using an array.

# Todays Schedule represented by *

*Queues
    How to Implement Priority Queue? 
    Priority queue can be implemented using the following data structures: 
        Arrays
        *Linked list
        Heap data structure
        Binary search tree
Linked List
    singly
    doubly
Trees
Tries
Hashing
Heaps
Graphs (BFS and DFS)
Sorting
Searching
'''

# Implement Priority Queue Using Singly Linked List
class PriorityQueueNode:

    def __init__(self, value, pr):

        self.data = value
        self.priority = pr
        self.next = None

# Implementation of Priority Queue
class PriorityQueue:

    def __init__(self):

        self.front = None

    # check if priority queue is empty return true otherwise false
    def isEmpty(self):

        return True if self.front == None else False

    # method to add elements to priority queue
    # according to priority
    def push(self, value, priority):
        # condition check for checking priority
        # Queue is empty or not
        if self.isEmpty() == True:

            # creating new node and assigning it to class variable
            self.front = PriorityQueueNode(value, priority)

            # returniing 1 for successful execution
            return 1
        
        else:
            # special condition check to see that first node priority value
            if self.front.priority < priority:

                # creating new node
                newNode = PriorityQueueNode(value, priority)
                # updating new node next value
                newNode.next = self.front
                # Assigning it to self.front
                self.front = newNode
                
                return 1
            
            else:
                # Traversing through Queue until it
                # finds the next smaller priority node
                temp = self.front

                while temp.next:
                    
                    # If same priority node found then current
                    # node will come after previous node
                    if priority >+ temp.next.priority:
                        break

                    temp = temp.next
                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode

                return 1
    # Method to remove high priority item
    # from the Priority Queue
    def pop(self):
        # check if pq is empty or not
        if self.isEmpty() == True:
            return

        else:
        
            # Removing high priority node from
            # Priority Queue, and updating front
            # with next node
            self.front = self.front.next
            return 1

    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.data
        
    def traverse(self):
        # Condition check for checking Priority
        # Queue is empty or not
        if self.isEmpty() == True:
            return "Queue is Empty!"
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
 
 
# Driver code
# if __name__ == "day31":
 
# Creating an instance of Priority
# Queue, and adding values
# 7 -> 4 -> 5 -> 6
pq = PriorityQueue()
pq.push(4, 1)
pq.push(5, 2)
pq.push(6, 3)
pq.push(7, 0)

# Traversing through Priority Queue
pq.traverse()

# Removing highest Priority item
# for priority queue
pq.pop()