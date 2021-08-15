#!/usr/bin/env python3

# Exercise 17. More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv
# we vould do these two on one line, how?
open(to_file, 'w').write(open(from_file).read())

