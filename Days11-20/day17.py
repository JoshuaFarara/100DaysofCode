'''
Day Seventeen of 100 Days of Code

June 12th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

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