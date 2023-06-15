'''
Write a program that adds two numbers together.


'''

x = 0 
y = 0

d = 24
h = 60

# simple add
add = d + h

# add with function that returns addition
def addition():
    return d + h

# function that adds on incrementation
def addItUp():
    x = 0
    while x < 10:
        x += 1
        total_minutes = x + h
        
    return x, total_minutes
    
print(addition())
print(addItUp())

# function that takes two arguments to add together. 
def addParams(x, y):
    total = x + y
    print(f"The added values {x} and {y} is: {total}")

addParams(8, 24)
