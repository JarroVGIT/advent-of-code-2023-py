# Advent of Code 2023 - Day 15
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day15/example.txt") as f:
with open("./day15/input.txt") as f:
    content = f.read().split("\n")

instructions = []
for line in content:
    for piece in line.split(","):
        instructions.append(piece)

print(instructions)

hashes = []
for string in instructions:
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current %= 256
    hashes.append(current)

print(sum(hashes))