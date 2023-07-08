'''
Day Twenty-Ninth of 100 Days of Code

July 7th, 2023

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

Tree Terminologies:

Node: Node is the main component of a tree that stores the data along with the links to other nodes.
Edge: Edge( also called branch) connects two nodes of a tree. A node can have more than one edge.
Parent: Parent node is a predecessor to any other node. In simple words, it is a node in the tree that has branches to other nodes.
Child: The node which is connected below to another node is called a child of that node. All nodes except the root node are child nodes.
Root: The first node of the tree which originates it is called the root of the tree. A tree can have only one root.  
Leaf node(External node): Nodes with no child are called leaf nodes or external nodes.
Internal node(Non-Leaf node): Nodes with at least one child is called an internal node or non-leaf nodes.  
Siblings: Nodes having the same parent are called siblings.
Cousins: The nodes belonging to the same level with different parent nodes.
Degree: Degree of a node is defined as the number of children of that node. The degree of the tree is the highest degree of a node among all the nodes.
Path: The nodes in the tree has to be reachable from other nodes through a unique sequence of edges called path. The number of edges in a path is called the length of the path.
Level of a node: The level of a node is defined as the number of edges in the unique path between the root and the node.
Subtree: A tree formed by a node and all of its descendants in the tree is called a subtree.
'''

# Trees
# Binary Tree
# Dynamic Node Representation(Linked Representation):

# Array Representaton(Sequential Rep):
tree = [None] * 10 # numbering starting from 0 to n - 1. 

def root(key): # key used for the value of the root node
    if tree[0] != None: # check to see if tree has a root node, and it does ->
        print("Tree already had root")
    else: # if root does not exist, first index of the tree becomes the root.
        tree[0] = key

def set_left(key, parent): # key is the value of the child node
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else: 
        tree[(parent * 2) + 1] = key

def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key

def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()

root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()
 
