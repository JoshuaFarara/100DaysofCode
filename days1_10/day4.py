'''
Day four of 100 Days of Code

May 8th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


### Python Conditional Loop Statements ### finish control flow


'''
# if-else statements
bladed_moth_color = "Black"

if bladed_moth_color == "Black":
    print("bladed moth is Black")

else:

    if bladed_moth_color == "Red":
        print("bladed moth is Red")
    
    else:

        if bladed_moth_color == "White":
            print("bladed moth is White")

        else:
            print("bladed moth isn't White, Black, and Red")


# nested-if statements
blade_count = 10

if blade_count > 5:
    print("Bigger than 5")

    if blade_count <= 15:
        print("Between 5 and 15")

# if-elif
# performaed when none of the above if-elif statement is true
bladed_moth_color = "green"

if bladed_moth_color == "Black":
    print("bladed moth is Black")

elif bladed_moth_color == "Red":
    print("bladed moth is Red")
    
elif bladed_moth_color == "White":
    print("bladed moth is White")

else:
    print("bladed moth isn't White, Black, and Red")

# Input/Output
# input(), takes an input from a use and converts it into a string
moth_draft = input('How many bladed moths do you want to purchase?\n')
print(moth_draft)

# multiple inputs from user
# split(), 
x, y = input('Enter two values: ').split()
print("Number of boys: ", y)
print("Number of girls: ", x)

# end=
# file argument
# print without new line
# remember to use print() to its full capacity to display outputs more clearly

# Operators
print(boy_girl_ratio= y/x)
# print(girl_boy_ratio= x/y)

