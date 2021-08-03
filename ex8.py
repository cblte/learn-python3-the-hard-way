#!/usr/bin/env python3

# Exercise 8: Printing, Printing

# define a formatter variable to be used later
formatter = "{} {} {} {}"

# use formatter to print out 1 2 3 4
print(formatter.format(1, 2, 3, 4))
# use formatter to print out four strings
print(formatter.format("one", "two", "three", "four"))
# use formatter to print out four boolean values
print(formatter.format(True, False, False, True))
# use the formatter to print itsefl four times
print(formatter.format(formatter, formatter, formatter, formatter))

# use formatter to print out a longer text.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear."
))
