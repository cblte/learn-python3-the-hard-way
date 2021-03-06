#!/usr/bin/env python3

# Exercise 32. Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of loop goes through a list
for number in the_count:
    print(f"This count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also wen can go throuugh mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# we can also just do like this, as range is a type
# elements = range(0, 6)


# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
