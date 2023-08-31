'''
Day Twenty-Eigth of 100 Days of Code

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
# Syntax Trees -  https://www.youtube.com/watch?v=7tCNu4CnjVc
# e1 = 3*(y + x)
# e2 = 3 * y + x
# note -  data structure like a tree and want to process it, recursively call itself on the substructure
class Expr:
    # __ini
    pass
class Times (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "*" + str(self.r) + ")"
    
    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


class Plus (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "+" + str(self.r) + ")"
    
    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)

class Const (Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def eval(self, env):
        return self.val
    
class Var (Expr):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def eval(self, env):
        return env[self.name]

e1 = Times(Const(3), Plus(Var("y"), Var("x")))
e2 = Plus(Times(Const(3), Var("y")), Var("x"))

print(e1)
print(e2)

'''
evalute expression with variables using a dictionary
currently just trees
assignment of variable to numbers (strings to numbers)
'''

env = {"x": 2, "y" : 4}
env["x"]
env["y"]

print(e1.eval(env))
print(e2.eval(env))

# Full Binary Tree
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class FullBinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if not currentNode.left:
                    currentNode.left = newNode
                    break
                elif not currentNode.right:
                    currentNode.right = newNode
                    break
                else:
                    currentNode = currentNode.left

    def display(self):
        pass

tree = FullBinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)


