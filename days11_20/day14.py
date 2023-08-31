'''
Day Fourteen of 100 Days of Code

June 4th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and co\\\\

# Todays Schedule

### Python OOP
Python Classes and Objects
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
# Python Classes and Objects
class Card:
    front = "question"
    back = "answer"

    def getCard(self):
        print("I am the front of the card showing the ", self.front)
        print("I am the back of the card showing the  ", self.back)

deck1 = Card()

print(deck1.front)
deck1.getCard()

# Self Parameter
# When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 
# self can be renamned to any other name, 

# __init__(), similar to constructor in  java. Used to initialize the obnjects state. 
# ex1
class Deck:
    def __init__(self, deck) -> None:
        self.deck = deck

    def add_card(self):
        print("You just added a card to ", self.deck)

chapter1 = Deck('Chapter1')
chapter1.add_card()

# ex2
# Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Asa')
p.say_hi()

# Class and Instance Variables
# Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class.
# Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.
class CreateDeck:

    # class variable
    deck = 'deck of cards'

    def __init__(self, subject, color):
        self.subject = subject
        self.color = color

BarberExam = CreateDeck("chapter1", "blue")
Part107 = CreateDeck("chapter2", "red")

print('BarberExam Details:')
print('BarberExam has a deck of', BarberExam.deck)
print('Subject:', BarberExam.subject)
print('Color:', BarberExam.color)

print('Part107 is a', Part107.deck)
print('Subject:', Part107.subject)
print('Color:', Part107.color)




