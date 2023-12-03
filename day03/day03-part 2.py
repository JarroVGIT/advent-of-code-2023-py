# Advent of Code 2023 - Day 03
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from collections import defaultdict

# with open("./day03/example.txt") as f:
with open("./day03/input.txt") as f:
    content = f.read()
content_in_lines = content.split("\n")

char_locations = set(
    [
        (row, column)
        for row in range(len(content_in_lines))
        for column in range(len(content_in_lines[row]))
        if content_in_lines[row][column] == "*"
    ]
)

numbers_to_chars = defaultdict(list)
for row, line in enumerate(content_in_lines):
    numbers = re.finditer(r"\d+", line)
    number: re.Match
    for number in numbers:
        neighbors = set(
            [
                (row + row_offset, column + column_offset)
                for row_offset in range(-1, 2)
                for column_offset in range(-1, 2)
                for column in range(number.span()[0], number.span()[1])
            ]
        )
        for char in neighbors & char_locations:
            numbers_to_chars[char].append(int(number[0]))

ans = sum(
    [
        numbers_to_char[0] * numbers_to_char[1]
        for numbers_to_char in numbers_to_chars.values()
        if len(numbers_to_char) == 2
    ]
)

print("Part 2: ", ans)
