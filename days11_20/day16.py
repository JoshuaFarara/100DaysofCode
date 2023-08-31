'''
Day Sixteen of 100 Days of Code

June 11th, 2023

Todays program code demonstrates the concept of inheritance in Python, where classes can be derived from other classes to create hierarchies of related classes. 
It shows examples of single inheritance, multiple inheritance, and multilevel inheritance. The code also covers how constructors of parent classes are called, and different types of inheritance, such as single, multiple, multilevel, hierarchical, and hybrid inheritance. 
The examples illustrate how attributes and methods are inherited from parent classes, allowing for code reuse and organization.

# Todays Schedule

Inheritance in Python
Types of inheritance Python
Encapsulation in Python
Polymorphism in Python
Class or Static Variables in Python
Class method vs Static method in Python
Metaprogramming with Metaclasses in Python

'''

# Inheritance - hierachy of classes that share a set of properties and methods by deriving a scalss form another class.
'''
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
'''

class Agency(object):

    #constructor
    def __init__(self, name, clients):
        self.name = name
        self.clients = clients

    # to check if this person is an employee
    def Display(self):
        print(self.name, self.clients)

agency = Agency("LYFJOURNEY", 16) # An object of Client
agency.Display()


# creating a child class
class Client(Agency):
    
    # def __init__(self, name, clientID):
    #     self.name = name
    #     self.clientID = clientID
    
    def Print(self):
        print("Client class called")

client_details = Client("DMC", 6)

client_details.Display()

client_details.Print()

#Example of inheritance
class Parent(object):

    # constructor
    def __init__(self, dad):
        # self.mom = mom
        self.dad = dad

    # get mom and dad names
    def getName(self):
        return self.dad
    
    # to check if this parent has children
    def hasChildren(self):
        return False

# Inherited of subclass(note Parent in bracket)
class Children(Parent):
    
    def hasChildren(self):
        return True

parent = Parent("John") # an object of Parent
print(parent.getName(), parent.hasChildren())

parent = Children("Jonathon") # an obnject of Children
print(parent.getName(), parent.hasChildren())


# pexample of how parent cionstructors ar called
class Business(object):
    
    def __init__(self, bName, industry):
        self.bName = bName
        self.industry = industry

    def display(self):
        print(self.bName)
        print(self.industry)

class Project(Business):
    def __init__(self, bName, industry, project_name, revenue):
        self.project_name = project_name
        self.revenue = revenue

        # invoking the __init__ of the parent class
        Business.__init__(self, bName, industry)

a = Project("LYFJOURNEY", "Agency", "Website", 6000)

a.display()

# Example of multiple inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "ThaTruth"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Absolute"
        print("Base2")

class Derived(object):
    def __init__(self):

        # Calling constructors of BAse1 and base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str2, self.str1)

ob= Derived()
ob.printStrs()

# my ownm example
class Practice(Agency, Business):
    def __init__(self, name, clients, bName, industry, prac ):
        self.prac = prac
        Agency.__init__(self, name, clients)
        Business.__init__(self, bName, industry)
        print(self.bName, self.prac)

ins = Practice("CreAtive", 30, "Blissness", "webDev", "repeat")


# another practice of multilevel inheritance, this case(class) with 3 layers. 
class Profit(Agency, Project):
    def __init__(self, name, clients, bName, industry, project_name, revenue, dod):
        self.dod = dod
        Agency.__init__(self, name, clients)
        # Business.__init__(self, bName, industry)
        Project.__init__(self,bName, industry, project_name, revenue)
        print(self.bName, self.project_name, self.revenue, self.dod)
    
    def calculateProfit(self):
        profit = self.revenue * self.clients 
        print(profit)

moneyEarned = Profit('OptimalDesign', 8, 'FormulAte', 'webDesign', 'operationSellIt', 750, 'August 2nd')
moneyEarned.calculateProfit()


'''
Finally, lets discuss the different types of inheritance

Single
Multiple
Multilevel
Hiearchical
Hybrid
'''