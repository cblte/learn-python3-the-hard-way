#!/usr/bin/env python3


# Exercise 33. While Loops
# Study Drill 1/2


def number_loop(max, incr = 1):
    """
    use a while loop up to number max, use incr to set the increment
    """

    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The Numbers")
    for num in numbers:
        print(num)


if __name__ == "__main__":
    number_loop(8,2)
