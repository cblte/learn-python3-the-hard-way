#!/usr/bin/env python3

# Exercise 37. Symbol Review

# and - and compares two boolean operators and returns true, of both are true
if True == True:
    print(True)

if True == False:
    print(False)

# as - works only in combinatino with the 'with'-statement
# use it to import modules with a different namespace

import random as rd
print(rd.randint(1,6))

# assert
assert True
assert ( (5 > 6) == False), "5 is not greater than 6"

x = "hello"
assert x == "hello"

# break
# break will end a loop
print("--- starting a loop")
for i in range(1, 5):
    print(i)
    if i == 3:
        break
print("--- loops end")

# class
class Person(object):
    name = "A"
    age = 30

p = Person()
print(p.name, p.age)  # will print ' A 30'


# continue
for i in range(5):
    if i == 2:
        continue
    print(i) # will print numbers from 1 to 4, except 2


# def
def hello():
    print("hello")

hello()

# del
class MyClass():
    name = "John"

del MyClass

# print(MyClass)  # will give an error as MyClass is not defined anymore

# elif
a = 5
if a == 3:
    print("a == 3")
elif a == 5:
    print("a == 5")
else:
    print("What is a?")

# else
# see above ^^ 

# except
x = 10
try:
    if x > 5:
        raise Exception(f"x should not exceed 5. Value of x was {x}")
except:
    print("Caught the Exception that x should not exceed 5")

# exec
exec("print('Hello World')")

# finally
import sys

try:
    assert('windows' in sys.platform)
except:
    print("Not running on Windows")
finally:
    print("Even not running on windows, we can finally print something out.")

# for
for i in range(2,8,2):
    print(i)

# from
from random import randrange
r = randrange(2,10,2)
print(f"random number in range from 2 to 10 with step 2: {r}")

# global
g = 5
def print_five():
    global g
    print(g)
    g = 4
print_five()
print(g)

# if
if True == True:
    print(True)

# import
# import a module

# in
# in is a keyword used in for loops or to check if
# a number or string is part of a list e.g.

# is
# check if two objects are the same object  
l = ['a', 'b', 'c']
k = l
print(f"I l the same objects as k?: {k is l}")


# lambda
# a lambda is a small anonymous function
# it can take any amount of arguments
# assign a lambda to a variable. parameters before the ':', function things after
x = lambda a: a + 3
print(x)
print(x(5))

y = lambda a,b: a + b
print(y)
print(y(5,2))


# not
# keyword for logical operations. negates a True to False and vice versa
if not False:
    print("not False is True")

# or
# used in conditions. If the first expression is evaluated True, the second expression is not
# evaluated

if (3 == 3) or (5 == 4):
    print("3 equals 3, but 4 does not equal 4. So the OR is True")

# pass
# pass acts as a noop. Used when you need a syntactical correct statement
# which is not yet implemented. Should not be left in production code!
# The pass statement is a null operation; nothing happens when it executes. 
# The pass is also useful in places where your code will eventually go, 
# but has not been written yet (e.g., in stubs for example) 



# print
# prints out text or results of expressions

# raise
# raise an exception
import sys

try:
    assert('darwin' in sys.platform)
    print("This line is only printed when on macOS")
except:
    print("Exception happens on non macOS systems")
finally:
    print("This will always be printed out!")

# return
# return an object bak to the caller


# try
# try initiates a block which is handled by excpetion handling

# while
# the other looping mechanism in python. expression


# with
# with an expression as a variable do something
with open('temp.txt','w') as f:
    f.write("Hello World\n")

# yield
# pauses here and returns to the caller
def yield_function():
    yield 10
    yield 20
    yield 30

for y in yield_function():
    print(y)

print("New yield function")
def yield_func():
    n = range(3)
    for i in n:
        yield i * i

gen = yield_func()
print(gen)
for i in gen:
    print(i)