#!/usr/bin/env python3

# Exercise 16. Reading and Writing files

# import argv from sys package
from sys import argv

# unpack command line arguments
script, filename = argv

# print out the passed filename
print(f"We're going to read {filename}")

# opening the file in read mode
print("Opening the file...")
target = open(filename, 'r')

# writing the input lines to the truncated file
print("I'm going to read these lines now.")
print(target.readline(), end='')
print(target.readline(), end='')
print(target.readline(), end='')

# closing file handle and saving the file this way
print("And finally, we close the file.")
target.close()
