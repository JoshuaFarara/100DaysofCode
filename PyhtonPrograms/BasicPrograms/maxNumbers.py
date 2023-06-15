'''
Program to get the max numbers

'''

# function with return value
def getMax(num1, num2):
    maxNum = max(num1, num2)
    return maxNum

# function with print statement addition
def maxnumber(number1, number2):
    print("The maximum number is: ", max(number1, number2))

# lines of code that take user input for choosing max of 2 numbers
x = input("Enter the x coordinate: ")
xprime = input("Enter the xprime coordinate: ")
bestX = max(x, xprime)
print(bestX)

getMax(15, 39)
maxnumber(34, 95)