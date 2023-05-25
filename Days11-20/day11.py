'''
Day Eleven of 100 Days of Code

May 21st, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


# Todays Schedule
Functions
Python Functions
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

def fly():
    print("Where would you like your BladedMoth to go?")

fly()

# functions with parameters
def add(num1, num2):
    num3 = num1 + num2

    return num3

num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results to {ans}.")

# function arguments 
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(24)
evenOdd(25)

#  4 types of function arguments: default, keyword, positional, arbitrary (variable length)
# default - when a variable is not passed for a # of parameters, the default argument is assigned to y
def defaultArg(x, y=50):
    print("x: ", x)
    print("y: ", y)

defaultArg(12)
defaultArg(7, 28) # in this function call, the second variable is passed as an argument and takes the place of the default argument.

# keyword arg - allows for unorderd argument calls since they are explicitly defined, just must use correct paremeter names
def client(firstname, lastname):
    print(firstname, lastname)

client(firstname='Connor', lastname='Croix') 
client(lastname='Croix', firstname='Connor') 

# positional - the arguments passed must be in the order of the parameters of the function
# in order to obtain the correct expected output, arguments cannot be interchenged although the function will still run without errors

# docstrings - used to provide information about the functionality of a function
def docstring(x):
    '''This is an example of the use of the docstring in python.'''
    result = x + 2
    print(result)

print(docstring.__doc__)
docstring(8)

# nested functions - known as inner functions, functino within a function. Access varibale of enclosing scope. 
def funcy():
    trippy = "This is pretty tippy right?"

    def funcIt():
        print(trippy)

    funcIt()

funcy()

#  return statement - can be a variable, expression, or constant returned at the end of execution, 
# if none present, function returns None
def square_value(num):
    '''Returns square value of argument passed in function.'''
    return num**2  # expression provided in return statement``

print(square_value(2))
print(square_value(-4))
