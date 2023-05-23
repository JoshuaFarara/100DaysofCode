'''
Day Nine of 100 Days of Code

May 19th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


# Todays Schedule
arrays - collection of items stored at contiguos memory locations. all elements of an array must have the same type. 

'''

import array as arr
#  a type code is used to denote the arrays data type
# such as 'i' for integers and 'd' for douubles, and many more
a = arr.array('i', [1, 2, 3, 1, 5])
print("The new created array is: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# adding elements to an Array, insert() and append()
# insert() , adds an element at a specific position
# append(), adds an element at the end of the array
a.insert(1,4)
print("Array after insertion : ", end=" ")
for i in a:
    print(i, end=" ")
print()

# 
a.append(6)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

# accessing elements from an Array
print("Accessing elementt of array ")
print("Access element of array ", a[4])

# remove elements from the array with pop() and remove()
# pop()
print(a.pop(2))

print("The new created array is: ", end=" ")
for i in range(0, 6):
    print(a[i], end=" ")
print()

# remove
a.remove(1)
print("The new created array is: ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()

# reverse an array with reverse()


