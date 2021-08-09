#!/usr/bin/env python3

# Exercise 13. Parameters, Unpacking, Variables

from sys import argv
script, first = argv

print(f'You passed argument: {first}')
answer = input('Please enter something else: ')

print(f'You entered: {answer}')