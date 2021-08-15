#!/usr/bin/env python3

# Exercise 17. More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv
# we vould do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).read()
out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
print(f"Copied {len(indata)} bytes from {from_file} to {to_file}")

