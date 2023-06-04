'''
Day Thirteen of 100 Days of Code

June 3rd, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and co\\\\

# Todays Schedule

When to use yield instead of return in Python?
Generators in Python
Python lambda
Global and Local Variables in Python
Global keyword in Python
First Class functions in Python
Python Closures
Decorators in Python
Decorators with parameters in Python
Memoization using decorators in Python

'''

# When to use yield instead of return in Python?

# A Python program to generate squares from 1
# to 100 using yield and therefore generator
 
# An infinite generator function that prints
# next square number. It starts with 1
 
 
def nextSquare():
    i = 1
 
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
        # from this point
 
 
# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)