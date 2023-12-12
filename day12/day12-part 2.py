# Advent of Code 2023 - Day 12
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from functools import cache

#with open("./day12/example.txt") as f:
with open("./day12/input.txt") as f:
    content = f.read().split("\n")

grid_lines = []
grid_continguous_groups = []
for line in content:
    parts = line.split(" ")
    grid_lines.append((parts[0]+'?')*4) # String because hashable
    grid_lines[-1] += parts[0] # final line is not followed by a ?
    grid_continguous_groups.append(tuple([int(c) for c in parts[1].split(",")])*5) # Tuple so its hashable


@cache
def fits(grid_line: str, cont_group: tuple[int]):
    if not grid_line:
        if not cont_group:
            return 1 # Mapped all groups
        else:
            return 0 # Didn't map all groups
    
    if not cont_group:
        if grid_line.count('#') == 0:
            return 1 # all mapped, rest of line is . or ?
        else:
            return 0 # all mapped, but there is a group in line left.
    
    if grid_line[0] == '.':
        # Skip the dot
        return fits(grid_line[1:], cont_group)

    if grid_line[0] == '?':
        # Treat as possible . or #
        broken = "#" + grid_line[1:]
        dot = "." + grid_line[1:]
        return fits(broken, cont_group) + fits(dot, cont_group)
    
    if grid_line[0] == '#':
        # Try to fit the first group.

        if len(grid_line) >= cont_group[0]:
            # Only try to match if there is enough space left on line.
            sub_line = grid_line[:cont_group[0]]
            if all([c!='.' for c in sub_line]):
                # The next x chars are not '.' (so they are # or ?)
                if (len(grid_line) >= cont_group[0] + 1) and (grid_line[cont_group[0]] == '#'):
                    # The next char is #, so this group is too big.
                    return 0 
                else:
                    # Plus one the slice because we don't want to process the next one.
                    return fits(grid_line[cont_group[0] + 1:], cont_group[1:])
            else:
                # The next x chars are not all # or ? (so they contain .)
                # This does not correspond with the group size.
                return 0

        else:
            # group size doesn't fit next group of possible #s
            return 0
    raise Exception("This shouldn't happen")

count = 0
for grid_line, cont_group in zip(grid_lines, grid_continguous_groups):
    count += fits(grid_line, cont_group)

print(f"Total possible fits: {count}")