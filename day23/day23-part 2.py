# Advent of Code 2023 - Day 23
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
import sys
from collections import defaultdict
from copy import deepcopy

sys.setrecursionlimit(1000000)  # Set maximum recursion depth to 10000
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
    else:
        next_possible_coords[coord] = []
        for n in [1,-1, 1j, -1j]:
            next_coord = coord + n
            if next_coord in coordinates and coordinates[next_coord] != "#":
                next_possible_coords[coord].append(next_coord)

# Create new adjecent matrix with only the split-points; start is considered a splitpoint with only 1 next step:
# the first actual split point. That splitpoint will have 3 or 4 next steps (splitpoints) and add weight to them.

next_possible_coords_2 = deepcopy(next_possible_coords)

sp_next_steps = defaultdict(lambda: [])
start = complex(1, 0)
target = complex(len(content[0])-2,len(content)-1)

for coord in next_possible_coords.keys():
    if coord == start or coord == target or len(next_possible_coords[coord]) > 2:
        for neighbour in next_possible_coords[coord]:
            step = 1
            prev = coord
            while (len(next_possible_coords[neighbour]) <= 2) and (neighbour not in [start, target]):
                if len(next_possible_coords[neighbour]) == 1:
                    break # dead end
                step += 1
                new_prev = neighbour
                neighbour = [next for next in next_possible_coords[neighbour] if next != prev][0]
                prev = new_prev
            else: # splitpoint
                sp_next_steps[coord].append((neighbour, step))




def get_longest_path(current: complex, target: complex, visited: set, steps: int) -> list[complex]:
    path_lengths= []
    for neighbour, n_steps in sp_next_steps[current]:
        if neighbour in visited:
            continue
        if neighbour == target:
            return steps + n_steps
        else:
            path_lengths.append(get_longest_path(neighbour, target, visited | set([neighbour]), steps + n_steps))
    if len(path_lengths) == 0:
        return 0
    else:
        return max(path_lengths)

print(get_longest_path(start, target, set([start]),0))
