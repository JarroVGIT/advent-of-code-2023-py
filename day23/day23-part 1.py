# Advent of Code 2023 - Day 23
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
import sys
sys.setrecursionlimit(100000)  # Set maximum recursion depth to 10000
#with open("./day23/example.txt") as f:
with open("./day23/input.txt") as f:
    content = f.read().split("\n")

coordinates = {}
next_possible_coords = {}

for y, line in enumerate(content):
    for x, char in enumerate(line):
        coordinates[complex(x, y)] = char
       
for coord, char in coordinates.items():
    if char == "#":
        continue
    next_possible_coords[coord] = []
    if char == ">":
        next_possible_coords[coord].append(coord + 1)
        continue
    if char == "<":
        next_possible_coords[coord].append(coord - 1)
        continue
    if char == "^":
        next_possible_coords[coord].append(coord - 1j)
        continue
    if char == "v":
        next_possible_coords[coord].append(coord + 1j)
        continue
    for n in [1,-1, 1j, -1j]:
        next_coord = coord + n
        if next_coord in coordinates and coordinates[next_coord] != "#":
            next_possible_coords[coord].append(next_coord)

start = complex(1, 0)
#target = complex(21, 22)
target = complex(139,140)
def get_longest_path(start: complex, target: complex, visited: frozenset) -> list[complex]:
    path_lengths= []
    for n in next_possible_coords[start]:
        if n in visited:
            continue
        if n == target:
            return len(visited)+1
        path_lengths.append(get_longest_path(n, target, visited | frozenset([n])))
    if len(path_lengths) == 0:
        return 0
    else:
        return max(path_lengths)

print(get_longest_path(start, target, frozenset([start])) - 1)