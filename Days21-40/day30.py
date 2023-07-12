'''
Day Thirtieth of 100 Days of Code

July 11th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

*Queues
    How to Implement Priority Queue? 
    Priority queue can be implemented using the following data structures: 
        Arrays
        Linked list
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

# Priority Queue
# Structure for the elements in the
# priority queue with array implementation
import sys
class item :
    value = 0
    priority = 0

class GFG:
    # store the element of a priority queue
    pr = [None] * (100000)
    # Pointer to last index
    size = -1

    def enqueue(value, priority):
        # increase the size
        GFG.size += 1

        # insert the element
        GFG.pr[GFG.size] = item()
        GFG.pr[GFG.size].value = value
        GFG.pr[GFG.size].priority = priority

    # function to check the top element
    @staticmethod
    def peek():
        highestPriority = -sys.maxsize
        ind = -1

        i = 0
        while (i <= GFG.size):
            # If priority is same choose
            # the element with the
            # highest value
            if (highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value < GFG.pr[i].value):
                highestPriority = GFG.pr[i].priority
                ind = i
            elif (highestPriority < GFG.pr[i].priority):
                highestPriority = GFG.pr[i].priority
                ind = 1
            i += 1

        # return position of the element
        return ind
    
    def 
