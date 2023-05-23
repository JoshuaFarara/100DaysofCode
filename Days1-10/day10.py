'''
Day Ten of 100 Days of Code

May 20th, 2023

Todays program will create something out of the basics. Lets tell a story today through code. 
How Artistic can you be with your programming code? Lets just have fun, relax, and code!


# Todays Schedule
Control Flow
for loops
while loops
break statement
continue statement
pass statement
looping techniques
'''

clippers = ["Masters", "Seniors", "GoldFx", "SlimlinePro"]

for i in clippers:
    print(i)

# step size for loop
for i in range(0, 15, 3):
    print(i)

# nested for loop - for loop inside a for loop
for i in range(1, 4):
    for j in range(1,4):
        print(i, j)

# using zip() - iterate over two list in parallel
clipper_brands = ["Andis", "Wahl", "BabylissPro", "Andis"]

for clipper, brand in zip(clippers, clipper_brands):
    print(brand, " ", clipper)

# tuple for loops
t = ((1,2), (3,4), (5,6))
for a, b in t:
    print(a, b)

# continue statement -  returns control to the beginning of the loop
for letter in 'Clippers':
    if letter == 'C' or letter == 's':
        continue
    print(letter)

# break takes control out of the loop
# pass is used to write empty loops