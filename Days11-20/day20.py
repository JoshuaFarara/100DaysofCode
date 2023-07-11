'''
Day Twentieth of 100 Days of Code

June 20th, 2023

Todays program demonstrates basic operations on arrays in Python.
It initializes an array and performs operations such as appending elements, sorting the array, finding the minimum and maximum values, 
and obtaining the maximum element in the array and its position.

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