# Advent of Code 2023 - Day 11
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
import pandas as pd
# import numpy as np
# import re
from rich import print
from itertools import product
#with open("./day11/example.txt") as f:
with open("./day11/input.txt") as f:
    content = f.read().split("\n")

grid = []
for line in content:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)

empty_rows = []
for idx, row in enumerate(grid):
    if all(r == "." for r in row):
        empty_rows.append(idx)
for row_idx in reversed(empty_rows):
    grid.insert(row_idx, ["."]*len(grid[0]))

# Transpose the grid
grid = list(map(list, zip(*grid)))

empty_cols = []
for idx, col in enumerate(grid):
    if all(c == "." for c in col):
        empty_cols.append(idx)
for col_index in reversed(empty_cols):
    grid.insert(col_index, ["."]*len(grid[0]))

# Transpose the grid back
grid = list(map(list, zip(*grid)))

# Distance is measured in manahttan distance, yay!
# We can use complex numbers again. 

galaxies = [complex(x, y) for y, row in enumerate(grid) for x, col in enumerate(row) if col == "#"]

pair_distances = []
while galaxies:
    galaxy = galaxies.pop()
    for other_galaxy in galaxies:
        distance = abs(galaxy.real - other_galaxy.real) + abs(galaxy.imag - other_galaxy.imag)
        pair_distances.append(distance)

print("Part 1: ", sum(pair_distances))