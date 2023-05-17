'''
Day six of 100 Days of Code

May 16th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


Python Lists
Python Tuples
Python Sets
Python Dictionary
Python Arrays


'''

# Listst and Accessing List elements
# 
grocery_list = ["soap", "sugar", "milk", "cake", "coffee"]

print("Accessing an element from the grocery list ")
print(grocery_list[0])
print(grocery_list[2])

# multidimensinal lists accessing
floor_plan = [['1','Cereal', 'Oats'], ['2', 'Candy']]

print("Accessing an element from the floor plain aisles list")
print(floor_plan[0][2])
print(floor_plan[1][1])

# negative indexing
print(grocery_list[-1])

#  Size of python list with len()
print(len(grocery_list))

# # taking input of a python list
# string = input("Enter elements (Space-Seperated): ")
# # split th strings an sstore it a to a list
# lst = string.split()
# print('The list is: ', lst)

# adding to a list
# append
grocery_list.append(75)
grocery_list.append(35)
grocery_list.append(49)
print(grocery_list)

# using iterator to add elements to list
for i in range(1, 5):
    grocery_list.append(i)
print("\nList after addition of elements from 1-3: ")
print(grocery_list)

