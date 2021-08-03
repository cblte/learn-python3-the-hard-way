#!/usr/bin/env python3

# Exercise 6: Strings and Text

# define varable with value 10
type_of_people = 10
# assign x the contents of the formatted string
x = f"There are {type_of_people} types of people."

# assign a variable a value
binary = "binary"
# assign a variable a value
do_not = "don't"
# assign y the value of the formatted string
y = f"Those who know {binary} and those who {do_not}."

# print values of x and y
print(x)
print(y)

# print values of x and y again
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assign boolean value to variable
hilarious = False
# create a string with a placeholder
joke_evaluation = "Isn't that joke so funny?! {}"

# print value of joke_evaluation after it hs been formatted
print(joke_evaluation.format(hilarious))

# assign values to variables
w = "This is the left side of..."
e = "a string with a right side."

# concatenate contents and print out
print(w + e)
