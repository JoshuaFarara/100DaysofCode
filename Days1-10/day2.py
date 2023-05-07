'''
Day Two of 100 Days of Code

May 6th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!

####  Name Spaces   ####
Directories with different names, specify absolute path to the file. 

Understanding namespace helps you improve your uderstanding of structure within development. 
Its about access within a program. What objects can be accessed amongst others. 

WHen a user creates a module, a global namespace getes created, later the creation of local functions creates local namespace.
built-in namespace encompasses global namespace an dthe gloabal namespace encompasses the local namespace. 

####  Scope  ####
####  Statement, Indentation and Comment in Python  ####
'''

# variable is in the global namespace
moth1 = 10
def moth_it():
    # var2 is in the local namespace
    moth2 = 11
    def moth_it_inner(): # inner function

        #var3 is int he nested local namespace
        moth3 = 12


# Scope
# Access is addressed in the section. Allowed by the scope of the object. 
# def action():
#     print("Mothy is ready to take an action!")
#     def moth_it_inner(): # inner function
#         action_blades = 10
#         print("Mothy has ", action_blades, " action blades.")
#     moth_it_inner()
#     print("Try printing variable from outer function: ", action_blades) #error lines, see below for fix
# action()

#fix
def action():
    print("Mothy is ready to take an action!")
    def moth_it_inner(): # inner function
        action_blades = 10
        print("Mothy has ", action_blades, " action blades.")
    moth_it_inner()
action()     

# Statement
''' 
Now we will start the various types of statements. Although it may feel trivial, it is worth it!

'''

# Multi-line
# Purpose: ability to divide a long statement into numerois lines(\).
fta = "Farara\
The\
Artist"
print(fta)

#Explicit line continuation:
text = "This is my 100 Days of Code Journey.\
    This is day 2 of the 1-10 day segment\
        from geeks for geeks."
print('\n  Initializing a text using\
      the Explicit multi-line statement', text)

add = 25 + \
    4 - \
    7
print('\n Initializing a mathematical expression\
      using the Explicit multi-line statement', add)