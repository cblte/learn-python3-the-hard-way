#!/usr/bin/python3

# Exercise 18. Names, Variables, Code, Functions

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")

print_two("Firstname", "Lastname")
print_two_again("Print", "two again")
print_one("One Argument Only")
print_none()

