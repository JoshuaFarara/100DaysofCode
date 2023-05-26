'''
Day Twelve of 100 Days of Code

May 22nd, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and co\\\\

# Todays Schedule

*args and **kwargs in Python
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

# *args - used for a function to take in variable number of arguments 
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hola', 'Joshua', 'is your age', 27)

# can use a first argument, along with varible number of arguments
def tryIt(arg1, *argv):
    print("The first argument is: ", arg1)
    for arg in argv:
        print("The next argument is: ", arg)

tryIt('black', 'and', 'yellow', 'by Wiz Khalifa')