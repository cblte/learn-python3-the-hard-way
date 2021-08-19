#!/usr/bin/env python3

# Exercise 23. Strings, Bytes, and Character Encodings

import sys
script, encoding, error = sys.argv
i = 1

def main(language_file, encoding, errors, i):
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors, i)
		i += 1
		return main(language_file, encoding, errors, i)


def print_line(line, encoding, errors, i):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print("Line", i, ":", raw_bytes, "<===>", cooked_string)


language_file = open("languages.txt", encoding="utf-8")

main(language_file, encoding, error, i)