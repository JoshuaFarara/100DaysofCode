'''
Day Fifteen of 100 Days of Code

June 5th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Constructors in Python
Destructors in Python
Inheritance in Python
Types of inheritance Python
Encapsulation in Python
Polymorphism in Python
Class or Static Variables in Python
Class method vs Static method in Python
Metaprogramming with Metaclasses in Python

'''

'''
!Objects! - briefly explain objects
Specific entity or concept in the real world. Example class Car, object would be Toyota Camry or Dodge Durango
Each car object would have its own unique attributes(e.g. color, model, year) and behaviors(engine, accelerate, brakes, lights) 
real world concepts of objects used in software systems
'''


# Constructors in Python
# Used for instantiating an object.
#  
# Example of default constructor:
class HundredDaysCode:
    #  default constructor
    def __init__(self):
        self.code = "100 Days of Code"

    # a method for printing data members
    def print_Code(self):
        print(self.code)

# creating object of the class
obj = HundredDaysCode()

# calling the instance method using ther object obj
obj.print_Code()


# Examle of the parameterized constructor: