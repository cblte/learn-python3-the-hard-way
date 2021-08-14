#!/usr/bin/env python3

# Exercise 15. Reading Files

# import argv module from sys package
from sys import argv

# unpack arguments
script, filename = argv

# open file
txt = open(filename)

# print the filename
print(f"Here's your {filename}:")
# read in the filename and print the content
print(txt.read())

# print text
print(f"Type the filename again:")
# ask user for new input
file_again = input("> ")
# read in text from the file again
txt_again = open(file_again)

# print out text from the file
print(txt_again.read())
