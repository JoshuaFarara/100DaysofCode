'''
Day Twenty-Second of 100 Days of Code

June 22nd, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Stack Data Structure

definition: linear data structure that follows a particular order in which operations are performed. 
LIFO - last in first out - element that was last added to stack is the first to come out
FIlO - first in first out - element that is added first is the last to come out
(termonology interchangable)

push and pop

real world examples:
    plates stacked
    standing in line

stack Functions:
    empty() - Returns whether the stack is empty - Time Complexity: O(1)
    size() - Returns the size of the stack - Time Complexity: O(1)
    top() / peek() - Returns a reference to the topmost element of the stack - Time Complexity: O(1)
    push(a) - Inserts the element 'a' at the top of the stack - Time Complexity: O(1)
    pop() - Deletes the topmost element of the stack - Time Complexity: O(1)
    
'''
# stack implementation using list
stackIt = []
# function tyo push elements into the stack
stackIt.append('a')
stackIt.append('b')
stackIt.append('c')

print('Initial stack')
print(stackIt)

# pop function from stack in LIFO order 
print('\nElements popped from stack: ')
print(stackIt.pop())
print(stackIt.pop())
print(stackIt.pop())

print('\nStack after elements are popped: ')
print(stackIt)

# Using collections.deque is preffered ove r the list
from collections import deque

stackEm = deque()

stackEm.append('d')
stackEm.append('e')
stackEm.append('q')
stackEm.append('u')
stackEm.append('e')

print('\nInitial stack')
print(stackEm)

print(stackEm.pop())


# Queue module implementation also uses LIFO
'''
maxsize - Number of items allowed in the queue.
empty() - Return True if the queue is empty, False otherwise.
full() - Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() - Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() - Return an item if one is immediately available, else raise QueueEmpty.
put(item) - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() - Return the number of items in the queue.

'''
from queue import LifoQueue

stackQueue = LifoQueue(maxsize=3)

# show number of elements in the stack
print(stackQueue.qsize())

# put() function to push elements into stack
stackQueue.put(4)
stackQueue.put(9)
stackQueue.put(16)

print("Full: ", stackQueue.full()) 
print("Size: ", stackQueue.qsize())

print('\nElements popped from the stack')
print(stackQueue.get())
print(stackQueue.get())
print(stackQueue.get())
 
print(stackQueue)
print("\nEmpty: ", stackQueue.empty())