#!/usr/bin/python3

# Exercise 19. Functions and Variables

# define a function 'cheese_and_crackers'
# accept two parameters to be used in the print out
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print amount of cheese
    print(f"You have {cheese_count} cheeses!")
    # print amount of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man, that's enough for a party!")
    # write out text and a new line
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# call function and pass numbers
cheese_and_crackers(20,30)

print("Or, we can use variables from our script:")
# set variable
amount_of_cheese = 10
# set variable
amount_of_crackers = 50
# call function and pass values of variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# call function and pass the result of the math operation
# the math operation is evaluated first, before the
# result is passed to the function
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two variables and math:")
# call function and pass the result of the math operation
# the math operation is evaluated first, before the
# result is passed to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)