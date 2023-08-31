'''
Day Nineteen of 100 Days of Code

June 14th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule



Class or Static Variables in Python
Class method vs Static method in Python
Metaprogramming with Metaclasses in Python

'''

# Static variables, dont require a ketyword
# class declaration variables, are class variables with values assigned

class Client:
    barber = 'FTA'
    def __init__(self, name, age):
        self.name = name
        self.age = age

Will = Client('Will', 25)
Sem =  Client('Sem', 32)

print(Will.barber)
print(Sem.barber)

Will.barber = 'BHB'
print(Will.barber)
print(Sem.barber)

Client.barber = 'JF'
print(Will.barber)
print(Sem.barber)