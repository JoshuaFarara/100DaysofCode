'''
Day four of 100 Days of Code

May 8th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!

Data Types
Python | Set 3 (Strings, Lists, Tuples, Iterations)
Python String
Python Lists
Python Tuples
Python Sets
Python Dictionary
Python Arrays


'''

### Set 3 (Strings, Lists, Tuples, Iterations)

# Strings - sequence of characters in acombination, words, letters numbers, special characters.
a = ' Is a Brand string'
bm = 'Bladed Moth'

print(bm, a)

# Lists - powerful data structure. Seguenced data types.
# Declare list
bladed_moths = [1, 4, "name", "color", "background", bm]
bladed_moths.append(10)
print(bladed_moths)

bladed_moths.pop() # deleting last element from a list
print(bladed_moths)

print(bladed_moths[4])

#  Tuples - -immutable lists
tup = (9,  "name", "color", 4+5)
print(tup)
print(tup[1])

# Iterations - while loops, for loops
i = 1
while(i < 10):
    print(i)
    i += 1

click = "You just flipped the card"
for i in click:
    print(i)

L = [1, 3, 6, 5, 8, 4]
for i in L: 
    print(i)

# Strings - data structure
# can use single or double quotes, triple
# printing a character in a string
String1 = "Bladed Moths"
print(String1[0])




