'''
Day Seventeen of 100 Days of Code

June 12th, 2023

Todays program explores encapsulation in Python, which is a mechanism for restricting direct access to attributes and methods of a class.
It introduces access modifiers, such as protected and private, to control the visibility of class members. The code demonstrates the use of protected members by inheriting from a base class and accessing its protected attributes.
It also introduces the concept of private members and data hiding, where certain attributes and methods are hidden and can only be accessed through public methods of the class.

# Todays Schedule


Encapsulation in Python


'''
# protected
class Services:
    def __init__(self, sname, serviceType, price):
        self.sname = sname
        self.serviceType = serviceType
        self.price = price

class Service(Services):
    def __init__(self):
        Services.__init__(self)
        print()

        

# Private