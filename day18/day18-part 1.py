# Advent of Code 2023 - Day 18
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from collections import deque
#with open("./day18/example.txt") as f:
with open("./day18/input.txt") as f:
    content = f.read().split("\n")

instructions = []

for line in content:
    direction, length, _ = line.split(" ")
    length = int(length)
    instructions.append((direction, length))

direction_mapping = {
    'R': 1,
    'L': -1,
    'U': -1j, # Reversed grid
    'D': 1j
}

# Create coordinates of trenches
trench_coordinates = [complex(0,0)]
current_coorindate = 0+0j
for instruction in instructions:
    direction, length = instruction
    for i in range(length):
        current_coorindate += direction_mapping[direction]
        trench_coordinates.append(current_coorindate)

# Create total grid
max_x = int(max([c.real for c in trench_coordinates]))
max_y = int(max([c.imag for c in trench_coordinates]))
min_x = int(min([c.real for c in trench_coordinates]))
min_y = int(min([c.imag for c in trench_coordinates]))

grid = []
for y in range(min_y-1, max_y+2): # At least a 1x1 border.
    for x in range(min_x-1, max_x+2):
        grid.append(complex(x, y))

# Flood it, remove all non-trench coordinates

passed = set()

q = deque([complex(min_x-1,min_y-1)])
neighbors = [1, -1, 1j, -1j]
while len(q) > 0:
    current = q.popleft()
    if current in passed:
        continue
    passed.add(current)
    if current not in grid:
        continue
    grid.remove(current)

    for direction in [1, -1, 1j, -1j]:
        new = current + direction
        if new in grid and new not in trench_coordinates:
            q.append(current + direction)

print(len(grid))
