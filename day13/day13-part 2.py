# Advent of Code 2023 - Day 13
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

with open("./day13/example.txt") as f:
    # with open("./day13/input.txt") as f:
    content = f.read().split("\n")

# need to go line by line, first check if there is a match. If there is not 
# a match, check if one change (smutch) makes a difference if there is not already a smutch used.

grids = []
for block in content:
    grid = []
    for line in block.split("\n"):
        grid.append(line)

    grids.append(grid)

def compare_row_sets(row_set_1, row_set_2, with_smutch: bool) -> bool:


    if not smutch_allowed:
        return row1 == row2
    else:
        # Check if there is one smutch:
        not_same = [idx for idx, i, j in enumerate(zip(row1, row2)) if i != j]
        if len(not_same) == 1: 
            return True
        else:
            return False

def overlapping_rows(grid):
    smutch_used = False

    intermediate_score = 0

    for row_id in range(len(grid)-1):
        # First check if there is a potential match, otherwise continue:
        if compare_row_sets([grid[row_id]], [grid[row_id+1]], False):
            # Check if rest of rows is mirrored as well, without smutch. 
            # Create row set 1 and 2, and feed into compare rowsets.
            pass # some recursive function to do here.

        elif compare_row_sets(grid[row_id], grid[row_id+1], True):
            # Check if rest of rows is mirrored as well, with smutch.
            pass # some recursive function to do here.
        else:
            continue




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