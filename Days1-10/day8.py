'''
Day Eight of 100 Days of Code

May 18th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


# Todays Schedule
Python Lists
Python Tuples
Python Sets

'''

# creating lists
bladed_moths = ["Red", "Green", "Blue", "Black", "White"]
print(bladed_moths[1])

# disctionaries, the power of key value pairs
# created with curly braces {}, seperated by a comma. 
# values can be anby datatype and duplicated, while keysomust be immutable and not repeated, also case sensitive and distinct
bladed_moths_dict = {1:bladed_moths[0], 2:bladed_moths[1], 3: bladed_moths[2], 4: bladed_moths[3], 5: bladed_moths[4]}
print(bladed_moths_dict)

# dictionary value setting with for loop
dict_pract = {}
for i in range(len(bladed_moths)):
    dict_pract[i] = bladed_moths[i] 

print(dict_pract)
