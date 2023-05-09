'''
Day Three of 100 Days of Code

May 7th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


### Python Conditional Loop Statements ###


'''
# if-else
# this section is about the control flow in python, 
# if statement, determines if statement of block statements will be executed or not. 
action_blades = 16
low = 0 # adding count for lower threshold numbers
overThresh = 0 # adding count for higher threshold numbers
if (action_blades < 15):
    print(action_blades, " is less than 15")
    print("im in if block")
    low += 1
else:
    print(action_blades, " is less than 15")
    print("im in else block")
    overThresh += 1
print("I am Not in if and not in else Block") # example of a statement with no if condition, just runs.
print("The action blades below 15 were ", low,\
      " and the action blades above 15 are: ", overThresh)


#Digitsum function
# ef else in a list comprehension
def get_bullets_shot(n):  
    bullets_shot = 0
    for bullet in str(n):
        bullets_shot += int(bullet)  # bullets are elements in the list
        selected = []
    return bullets_shot

List = [157, 97, 257, 38, 4, 25, 396, 12, 19]

# using the function on odd elements of the list
newList = [get_bullets_shot(i) for i in List if i & 1]  # how is this odd numbers?  the odd nubers in the list are odd numbers that 
# the digits are summed and assigned to a new list.

# Displaying new list
print(newList)



# nested-if statement
'''
syntax

if(condition):
    #Executes when condition1 is true
    if condition2);
        # Execute when condition 2 is true
    # if block is end here
#if Block is end here
'''
# i = 10
# if (i == 10):
    
#     first if statement
#     if(i<)



'''
#Post day3 Practice

'''
child = 3
children = []
parents = 0
m = False
d = False
if (child > 1):
    m = True
    d = True
    parents = (m,d) # create 2 parents for the child
print(parents)

if (children != empty):
    # match the children to the parent
    parents.m = 1
    for child in children:
        []


