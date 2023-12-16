# Advent of Code 2023 - Day 16
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from collections import defaultdict, deque


#with open("./day16/example.txt") as f:
with open("./day16/input.txt") as f:
    content = f.read().split("\n")
coordinates: dict[complex, str] = {}
for y, line in enumerate(content):
    for x, char in enumerate(line):
        coordinates[x + y*1j] = char

next_directions: dict[complex, dict[complex,list[complex]]] ={}
for coordinate in coordinates:
    next_directions[coordinate] = {}
    val = coordinates[coordinate]
    if val == '.':
        next_directions[coordinate][coordinate - 1] = [coordinate + 1] # from left passthrough
        next_directions[coordinate][coordinate + 1] = [coordinate - 1] # from right passthrough
        next_directions[coordinate][coordinate - 1j] = [coordinate + 1j] # from top passthrough
        next_directions[coordinate][coordinate + 1j] = [coordinate - 1j] # from bottom passthrough
    elif val == '|':
        next_directions[coordinate][coordinate - 1] = [coordinate - 1j, coordinate + 1j] # from left split
        next_directions[coordinate][coordinate + 1] = [coordinate - 1j, coordinate + 1j] # from right split
        next_directions[coordinate][coordinate - 1j] = [coordinate + 1j] # from top passthrough
        next_directions[coordinate][coordinate + 1j] = [coordinate - 1j] # from bottom passthrough
    elif val == '-':
        next_directions[coordinate][coordinate - 1] = [coordinate + 1] # from left passthrough
        next_directions[coordinate][coordinate + 1] = [coordinate - 1] # from right passthrough
        next_directions[coordinate][coordinate - 1j] = [coordinate - 1, coordinate + 1] # from top split
        next_directions[coordinate][coordinate + 1j] = [coordinate - 1, coordinate + 1] # from bottom split
    elif val == '/':
        next_directions[coordinate][coordinate - 1] = [coordinate - 1j] # from left turn up
        next_directions[coordinate][coordinate + 1] = [coordinate + 1j] # from right turn down
        next_directions[coordinate][coordinate - 1j] = [coordinate - 1] # from top turn left
        next_directions[coordinate][coordinate + 1j] = [coordinate + 1] # from bottom turn right
    elif val == '\\':
        next_directions[coordinate][coordinate - 1] = [coordinate + 1j] # from left turn down
        next_directions[coordinate][coordinate + 1] = [coordinate - 1j] # from right turn up
        next_directions[coordinate][coordinate - 1j] = [coordinate + 1] # from top turn right
        next_directions[coordinate][coordinate + 1j] = [coordinate - 1] # from bottom turn left

energized = defaultdict(lambda: defaultdict(lambda: False))

# Create queue with tuples: previous coordinate, current coordinate. Then, add new tuples to the queue if
# the current coordinate has not been energized yet (from this direction).
q = deque([(-1+0j, 0+0j)])
while q:
    prev, current = q.popleft()
    if not energized[current][prev]:
        energized[current][prev] = True
        for next in next_directions[current][prev]:
            if next.real >= 0 and next.imag >= 0 and next.real < len(content[0]) and next.imag < len(content):
                q.append((current, next))

print(len(energized))




        