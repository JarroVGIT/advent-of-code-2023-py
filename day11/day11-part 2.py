# Advent of Code 2023 - Day 11
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from itertools import product

with open("./day11/example.txt") as f:
#with open("./day11/input.txt") as f:
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

# Transpose the grid
grid = list(map(list, zip(*grid)))

empty_cols = []
for idx, col in enumerate(grid):
    if all(c == "." for c in col):
        empty_cols.append(idx)


# Transpose the grid back
grid = list(map(list, zip(*grid)))

def get_empty_cols_and_rows(coord_a: complex, coord_b: complex, repeater=10) -> int:
    if coord_a.real > coord_b.real:
        col_range = range(int(coord_b.real), int(coord_a.real))
    else:
        col_range = range(int(coord_a.real), int(coord_b.real))
    if coord_a.imag > coord_b.imag:
        row_range = range(int(coord_b.imag), int(coord_a.imag))
    else:
        row_range = range(int(coord_a.imag), int(coord_b.imag))
    empty_columns_between = [col for col in empty_cols if col in col_range]
    empty_rows_between = [row for row in empty_rows if row in row_range]
    return (len(empty_columns_between) + len(empty_rows_between)) * repeater 


# Distance is measured in manahttan distance, yay!
# We can use complex numbers again. 

galaxies = [complex(x, y) for y, row in enumerate(grid) for x, col in enumerate(row) if col == "#"]

pair_distances = []
while galaxies:
    galaxy = galaxies.pop()
    for other_galaxy in galaxies:
        distance = abs(galaxy.real - other_galaxy.real) + abs(galaxy.imag - other_galaxy.imag) + get_empty_cols_and_rows(galaxy, other_galaxy)
        pair_distances.append(distance)

print("Part 2: ", sum(pair_distances))
