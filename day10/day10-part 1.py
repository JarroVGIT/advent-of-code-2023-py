# Advent of Code 2023 - Day 10
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

example = False
if example:
    with open("./day10/example.txt") as f:
        content = f.read().split("\n")
else:
    with open("./day10/input.txt") as f:
        content = f.read().split("\n")

grid = {}
start_pos = None
for y, line in enumerate(content):
    for x, character in enumerate(line):
        if character == "S":
            start_pos = complex(x, y)
        grid[complex(x, y)] = character

possible_connections = {}
possible_connections['|'] = [-1j, 1j]
possible_connections['-'] = [-1, 1]
possible_connections['L'] = [-1j, 1]
possible_connections['J'] = [-1j, -1]
possible_connections['7'] = [1j, -1]
possible_connections['F'] = [1j, 1]

# Determined S on observation
grid[start_pos] = "F" if example else '|'

start_pos
next_pos = possible_connections[grid[start_pos]][0] + start_pos
target = possible_connections[grid[start_pos]][1] + start_pos

path = [start_pos]
previous_pos = start_pos
while next_pos != start_pos:
    path.append(next_pos)
    current_pos = next_pos
    neighbours = [next_pos + connection for connection in possible_connections[grid[next_pos]]]
    neighbours.remove(previous_pos)
    previous_pos = current_pos
    next_pos = neighbours[0]

print("Part 1: ", len(path) // 2)