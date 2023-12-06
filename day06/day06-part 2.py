# Advent of Code 2023 - Day 06
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day06/example.txt") as f:
with open("./day06/input.txt") as f:
    content = f.read().split("\n")


# text="""Time:        49     87     78     95
# Distance:   356   1378   1502   1882"""
# text = """Time:      7  15   30
# Distance:  9  40  200"""

from math import prod

t = int("".join(content[0].split(":")[1].strip().split()))
distance = int("".join(content[1].split(":")[1].strip().split()))

possible_distances = 0
for i in range(0, t + 1):
    if x := (t - i) * i > distance:
        possible_distances += 1

print(possible_distances)
