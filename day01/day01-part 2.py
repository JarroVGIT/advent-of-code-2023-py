# Advent of Code 2023 - Day 01
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day01/example2.txt") as f:
with open("./day01/input.txt") as f:
    content = f.read().split("\n")

# replace the words with numbers first on the entire input
numbers_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# To replace the words with numbers, we need the indexes of the words
# because words can overlap (eightwo needs to become 8wo)
lines_of_numbers: list[str] = []
for line in content:
    current_line = ""
    numbers_in_line = ""
    for c in line:
        current_line += c
        if c.isdigit():
            numbers_in_line += c
            current_line = ""
        else:
            for word, number in numbers_mapping.items():
                if word in current_line:
                    numbers_in_line += str(number)
                    current_line = current_line[len(current_line) - len(word) :]
    lines_of_numbers.append(numbers_in_line)


def using_join(content: list[str]):
    total = 0
    for line in content:
        numbers = "".join([c for c in line if c.isdigit()])
        total += int(numbers[0] + numbers[-1])
    return total


print(f"Part 2: {using_join(lines_of_numbers)}")
