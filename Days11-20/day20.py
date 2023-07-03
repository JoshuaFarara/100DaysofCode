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
arrayPrac = array.array('i', [5, 9, 7, 12, 3])
for i in range (len(arrayPrac)):
    tries+=1
    print(arrayPrac[i], tries) 

# append

# sort array
arrPrac_sorted = sorted(arrayPrac)
min_value = arrPrac_sorted[0] 
max_value = arrPrac_sorted[-1]
print("The min value of the array is: ", min_value)
print("The max value of the array is: ", max_value)

# Max Element in array and its position
def getMax(arrayPrac):
    n = len(arrayPrac)
    res = arrayPrac[0]
    for i in range(1, n):
        res = max(res, arrayPrac[i])
    return res

# n = len(arrayPrac)
print(getMax(arrayPrac))

new_array = array.array('i',[12, 7, 9, 1, 22, 58])
print(max(new_array))

new_arraySorted = sorted(new_array)