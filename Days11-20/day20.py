'''
Day Twentieth of 100 Days of Code

June 20th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Arrays
append
insert
remove

'''
import array
# Simple array warm up


tries = 0
arrayPrac = array.array('i', [5, 9, 7, 1, 3])
for i in range (len(arrayPrac)):
    tries+=1
    print(arrayPrac[i], tries) 

# append

# Max Element in array and its position
for i in arrayPrac:
    if i in (arrayPrac[i] > arrayPrac[i + 1]):
        highScore = max(arrayPrac[i])
    print(highScore)

#