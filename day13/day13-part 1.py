# Advent of Code 2023 - Day 13
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

with open("./day13/example.txt") as f:
#with open("./day13/input.txt") as f:
    content = f.read().split("\n\n")

grids = []
for block in content:
    grid = []
    for line in block.split("\n"):
        grid.append(line)

    grids.append(grid)


def overlapping_rows(grid):
    intermediate_score = 0
    for row_id in range(len(grid)):
        if (row_id+1<len(grid)) and  grid[row_id] == grid[row_id+1]:
            # Check if rest of rows is mirrored as well:
            if row_id < len(grid)//2:
                # Ignore last rows
                if grid[ : row_id+1 ] == grid[ (row_id*2)+1 : row_id : -1 ]:
                    intermediate_score += row_id+1
                    break
            else:
                # Ignore first rows
                if grid[ row_id+1 : ] == grid[ row_id : row_id-(len(grid)-row_id) + 1 : -1 ]:
                    intermediate_score += row_id+1
                    break
    return intermediate_score

score = 0
for idx, grid in enumerate(grids):
    s = overlapping_rows(grid) * 100
    if not s:
        transposed = list(map(list, zip(*grid)))
        s = overlapping_rows(transposed)
    score += s

print(score)