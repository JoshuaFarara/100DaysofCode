'''
Day Twenty-First of 100 Days of Code

June 21st, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Arrays

'''
arr = [10, 20, 30]  # This array will store integer
arr2 = ['c', 'd', 'e']  # This array will store characters
arr3 = [28.5, 36.5, 40.2]  # This array will store floating elements


# list of integers
my_list = [1, 2, 3, 4]
  
# Empty list
my_list = []
  
# list of mixed data types
my_list = ["Hello", 1, 5.5]

# 	Write a program to reverse the array
def reverseArray(arr):
    print("The original array is: ", arr)
    n = len(arr)
    start = 0
    end =  n- 1

    while start < end:
        # arr[start] = arr[end]
        # arr[end] = arr[start]
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    print("The reversed array is :", arr)

reverseArray(arr)
reverseArray(arr2)
reverseArray(arr3)


# recursive reverse the array
