'''
Day Twenty-Sixth of 100 Days of Code

July 6th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code

# Todays Schedule

Queues
Linked List
    singly
    doubly
* Trees
Tries
Graphs (BFS and DFS)
Hashing
Heaps
Sorting
Searching

'''

# Trees
# Syntax Trees
# e1 = 3*(y + x)
# e2 = 3 * y + x
class Expr:
    # __ini
    pass
class Times (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "*" + str(self.r) + ")"

class Plus (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "+" + str(self.r) + ")"

class Const (Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    
class Var (Expr):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

e1 = Times(Const(3), Plus(Var("y"), Var("x")))
e2 = Plus(Times(Const(3), Var("y")), Var("x"))

print(e1)
print(e2)