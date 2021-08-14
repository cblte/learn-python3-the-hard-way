#!/usr/bin/env python3

# Exercise 16. Reading and Writing files

# import argv from sys package
from sys import argv

# unpack command line arguments
script, filename = argv

# print out the passed filename
print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL+C (^C) now.")
print("If you do want that, press Enter")

# wait for input, not saving as ctrl+c will kill and enter will proceed
input("?")

# opening the file handle 
print("Opening the file...")
target = open(filename, 'w')

# truncating (emptying) the file
print("Truncating the file. Goodbye content.")
target.truncate()

# asking three times for user input
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# writing the input lines to the truncated file
print("I'm going to write these to the file now.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# closing file handle and saving the file this way
print("And finally, we close the file.")
target.close()
