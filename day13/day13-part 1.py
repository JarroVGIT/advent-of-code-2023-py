# Advent of Code 2023 - Day 13
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

with open("./day13/example.txt") as f:
    # with open("./day13/input.txt") as f:
    content = f.read().split("\n\n")

grids = []
for block in content:
    grid = []
    for line in block.split("\n"):
        grid.append(line)

    grids.append(grid)

score = 0
for grid in grids:
    # Check for rows first:
    intermediate_score = 0
    for i in range(len(grid)):
        if (i+1<len(grid)) and  grid[i] == grid[i+1]:
            # Check if rest of rows is mirrored as well:
            if i < len(grid)/2:
                # Ignore last rows
                if grid[:i+1] == grid[i+1:(i*2)+1:-1]:
                    intermediate_score += 100*(i+1)
                    break
            else:
                # Ignore first rows
                if grid[i+1:] == grid[i-(len(grid)-1):i:-1]:
                    intermediate_score += 100*(len(grid)-i)
                    break
    # If not mirrored, check for columns:
    if not intermediate_score:
        # Transpose grid:
        grid = list(map(list, zip(*grid)))
        # First row is now first column.
        for i in range(len(grid)):
            if (i+1<len(grid)) and grid[i] == grid[i+1]:
                # Check if rest of rows is mirrored as well:
                if i < len(grid)/2:
                    # Ignore last rows
                    if grid[:i+1] == grid[i+1:i*2+1:-1]:
                        intermediate_score += 1*(i+1)
                        break
                else:
                    # Ignore first rows
                    if grid[i+1:] == grid[i-(len(grid)-1):i:-1]:
                        intermediate_score += 1*(len(grid)-i)
                        break
    score += intermediate_score

print(score)