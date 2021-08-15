#!/usr/bin/python3

# Exercise 19. Functions and Variables
# Studydrill 3. 
#   Write at least one more function 
#   of your own design, and run it 10 different ways.

def sum(a, b):
    """
    sum prints the addition of a and b
    """
    print(a + b)

sum(1,2)
sum(12*3,4/2)
a = 2
b = 5
sum(a,b)
sum(a*2, b*2)

a = int(input("Enter Number:"))
b = int(input("Enter second Number:"))
print("result of {a} and {b} is:")
sum(a,b)