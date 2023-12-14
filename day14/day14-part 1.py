# Advent of Code 2023 - Day 14
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

#with open("./day14/example.txt") as f:
with open("./day14/input.txt") as f:
    content = f.read().split("\n")

grid = []

for line in content:
    grid.append(list(line))



transposed = list(map(list, zip(*grid)))
transposed_cube_coords = []
for y, row in enumerate(transposed):
    transposed_cube_coords.append([])
    for x, val in enumerate(row):
        if val == "#":
            transposed_cube_coords[y].append((x, y))

transposed_without_dots = []
for y, row in enumerate(transposed):
    transposed_without_dots.append([])
    for x, val in enumerate(row):
        if val != ".":
            transposed_without_dots[y].append(val)

transposed_without_dots_cube_coords = []
for y, row in enumerate(transposed_without_dots):
    transposed_without_dots_cube_coords.append([])
    for x, val in enumerate(row):
        if val == "#":
            transposed_without_dots_cube_coords[y].append((x, y))

# Now we have a transposed grid, a transposed grid without the dots, 
# a list of original cube coordinates in t-grid and a list of cube coordinates in t-grid without dots
# Now we add points back in front of each cube coordinate in the t-grid without dots untill it is back at its orig position.

for y, orig_coords in enumerate(transposed_cube_coords):
    new_coords = transposed_without_dots_cube_coords[y]
    dots_added = 0
    for orig, new in zip(orig_coords, new_coords):
        new = new[0]+dots_added
        count_of_dots = orig[0] - new
        for _ in range(count_of_dots):
            transposed_without_dots[y].insert(new, ".")
            dots_added += 1
    if len(transposed_without_dots[y]) < len(transposed[y]):
        # pad dots to the left
        count_of_dots = len(transposed[y]) - len(transposed_without_dots[y])
        for _ in range(count_of_dots):
            transposed_without_dots[y].append(".")

score = 0
for y, row in enumerate(transposed_without_dots):
    for x, val in enumerate(row):
        if val == "O":
            score += len(row)-x

print("Part 1:", score)