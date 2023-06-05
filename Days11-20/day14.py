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
        



