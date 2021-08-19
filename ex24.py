#!/usr/bin/env python3

# Exercise 24. More Practice

# print out some text using different escaping
# formats
print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# multiline string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

# print the multiline string
print("----------")
print(poem)
print("----------")

# do a calculation and print it with an f"" string
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# define a function with a parameter to
# calculate the amount of jars and crates for jelly beans
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# set a variable and call the secret formula function
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with and f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# set a starting point again, lower, and demonstrate 
# a differnt way of displaying the results
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
#  this unpacks the contents of formula at runtime ^^
