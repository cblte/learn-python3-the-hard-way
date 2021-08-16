#!/usr/bin/env python3

# Exercise 20. Functions and Files

# import the argv modules of sys package
from sys import argv

# unpacka arguments
script, input_file = argv


# define a function that takes a file handle and prints the contents
# of the whole file
def print_all(file):
    print(file.read())


# define a function to set the read cursor back
# for the passed file referene.
def rewind(file):
    file.seek(0)


# defina a functoin that only reads one line at a time
# this line is then printed to stdout
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines.")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
