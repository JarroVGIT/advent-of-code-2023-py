# Advent of Code 2023 - Day 13
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day13/example.txt") as f:
with open("./day13/input.txt") as f:
    content = f.read().split("\n\n")

# need to go line by line, first check if there is a match. If there is not 
# a match, check if one change (smutch) makes a difference if there is not already a smutch used.

grids = []
for block in content:
    grid = []
    for line in block.split("\n"):
        grid.append(line)

    grids.append(grid)

def compare_row_sets(row_set_1, row_set_2, smutch_used: bool) -> bool:
    if not row_set_1:
        # Exhausted both row_sets. 
        if smutch_used:
            return True
        else: 
            # Must fix a smutch!
            return False
    
    if row_set_1[0] == row_set_2[0]:
        return compare_row_sets(row_set_1[1:], row_set_2[1:], smutch_used)
    else:
        if not smutch_used:
            not_same_idx = [(i, j) for i, j in zip(row_set_1[0], row_set_2[0]) if i != j]
            if len(not_same_idx) == 1:
                return compare_row_sets(row_set_1[1:], row_set_2[1:], True)
        return False

def overlapping_rows(grid):
    for row_id in range(len(grid)-1):
        # Create rowsets to compare:
        if row_id < len(grid)//2:
            row_set_1 = grid[ : row_id+1 ]
            row_set_2 = grid[ (row_id*2)+1 : row_id : -1 ]
        else:
            row_set_1 = grid[ row_id+1 : ]
            row_set_2 = grid[ row_id : row_id-(len(grid)-row_id) + 1 : -1 ]

        # Compare:
        if compare_row_sets(row_set_1, row_set_2, False):
                return row_id+1
        else:
            continue
    # If this hits, it means we should look at columns instead.
    return 0


score = 0
for idx, grid in enumerate(grids):
    s = overlapping_rows(grid) * 100
    if not s:
        transposed = list(map(list, zip(*grid))) # Man I love this one!
        s = overlapping_rows(transposed)
    score += s

print(score)