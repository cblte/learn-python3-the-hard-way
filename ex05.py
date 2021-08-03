#!/usr/bin/env python3

# Exercise 5: More variables and printing

# save the name in a variable
name = "John Doe"
# save age in a variable
age = 35
# save height in cm and inches
height = 190  # cm
height_inches = round(height * 0.39370)
# save weight in kilogram and pounds
weight = 98  # kg
weight_pounds = round(weight * 2.2046)
# set personal characteristica
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


# print block
print(f"Let's talk about {name}.")
print(f"He's {height} cm tall. That's {height_inches} in inches")
print(f"He's {weight} kilogram heavy. Which is {weight_pounds} in pounds.")
print(f"Actually thats not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair. ")
print(f"His teeth are usually {teeth} depening on the coffee.")

# this line is tricky, try to to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and my {weight} I get {total}")
