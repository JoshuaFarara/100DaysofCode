'''
Day Thirty-Second of 100 Days of Code

July 18th-19th, 2023

Todays program demonstrates the implementation of a priority queue using an array.

# Todays Schedule represented by *

Queues
Linked List
Trees
Tries
Hashing
*Heaps
Graphs (BFS and DFS)
Sorting
Searching
'''

# Heaps
# A Heap is a special Tree-based data structure in which the tree is a complete binary tree.
import heapq # using the  library of heapq to implement this data structure of the abstreact description for a priority queue

# initializing a list called data
data = [5, 6, 12, 23, 1, 17]

#converts the example list into heap
heapq.heapify(data)
print("the crerated heap is: ", (list(data)))

'''
The structure explained
i           is the first node, at index i
2*i+1       the first child is at the index (2*i+1)
2*i+2       the second child is at the index (2*i+2)
(i -1)/2    the parent node
'''
