'''
Day Tweny-Fourth of 100 Days of Code

July 3rd, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Queues
Linked List
Trees
Tries
Graphs (BFS and DFS)
Hashing
Heaps
Sorting
Searching
'''

# Queue Data Structure
# A Queue is defined as a linear data structure that is open at both ends and the operations are performed in First In First Out (FIFO) order.
# implementation using list
queue = []
# adding elements to the queue with append
queue.append('q')
queue.append('u')
queue.append('e')
queue.append('u')
queue.append('e')

print("Initial queue")
print(queue)

# remove elements from the queue with pop()
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# queue implementation with using collection.deque
from collections import deque
q = deque()
# adding elements to queue
q.append('l')
q.append('o')
q.append('o')
q.append('k')

print("initial Queeue")
print(q)

# removing elements from queue with popleft()
print("\nElements dequeued from queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# also can be implemented using the Queue Module and using put(), and get()