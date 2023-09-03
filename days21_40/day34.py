'''
Day Thirty-Fourth of 100 Days of Code

August 31st, 2023

Todays program demonstrates the implementation of a priority queue using an array.

# Todays Schedule represented by *

Exception handling
User Input Exception Handling
try and except

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
'''

# practice
a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))

    print("Fourth element = %d" %(a[3]))
except:
    print ("An error occured.")

# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")

