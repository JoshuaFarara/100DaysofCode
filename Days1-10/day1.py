import math
import random

'''
Day One of 100 Days of Code

May 5th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!
'''

# Lets retouch on the basic fundamentals https://www.geeksforgeeks.org/python-programming-language/

# Variables - declare some variables
myNumber = 4
mySecondNumber = 25
print("My two favorite numbers are: ", myNumber, "and", mySecondNumber)

price = 40
n = 10
multiplier = price * n

total = 0

# Lists
favoriteNumbers = []

favoriteNumbers.append(myNumber)
favoriteNumbers.append(mySecondNumber)
favoriteNumbers.append("seven")

print(favoriteNumbers)

# input from user
name = input("Enter your name: ") # run in terminal, vscode extension code runner

print("Whats up", name)

# update number with int conversion for input
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
product = num3
print("Product is: ", product)

# add selection statement in this section
if (product < 50):
    print("Product is below the threshold of 50")
elif(product > 50):
    print("Product is above the average max of 50, where p = ", product)
else:
    print("Product is...loading")

#Functions Section
# 

def get_userInfo():
    firstName = input("What is Your  name?")
    lastName = input("What is Your last  name?") 
    age = int(input("How old are you?"))
    return firstName, lastName, age

#Iteration and Looping
for i in range(10):
    favoriteNumbers.append(i)
    print(favoriteNumbers)
    if i == 7:
        break

def getAbs(num):
    absVal = math.fabs(num)
    return absVal

def Main():
    username = get_userInfo()
    print(username)
    print(getAbs(-39))

if __name__=="__main__":
    Main()
