# Advent of Code 2023 - Day 21
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

#with open("./day21/example.txt") as f:
with open("./day21/input.txt") as f:
    content = f.read().split("\n")

# Store all tiles, then create a dict with adjecent tiles.

start = None
tiles = {}
bushes = {}
for y, row in enumerate(content):
    for x, val in enumerate(row):
        if val == 'S':
            start = complex(x, y)
            tiles[complex(x, y)] = set()
        elif val == '.':
            tiles[complex(x, y)] = set()
        else:
            bushes[complex(x, y)] = set()

for tile in tiles.keys():
    for direction in [1, -1, 1j, -1j]:
        if tile + direction in tiles:
            tiles[tile].add(tile + direction)

# @cache
# def get_neighbours(current_tile, steps_left):
#     if steps_left == 1:
#         return tiles[current_tile]
#     else:
#         next_tiles = []
#         for neighbour in tiles[current_tile]:
#             next_tiles.extend(get_neighbours(neighbour, steps_left - 1))
#         return next_tiles

def get_next_possible_steps(current_tiles: set[complex], steps_left: int):
    if steps_left == 0:
        return current_tiles
    next_tiles = set()
    for tile in current_tiles:
        next_tiles = next_tiles | tiles[tile]
    return get_next_possible_steps(next_tiles, steps_left - 1)

print(len(get_next_possible_steps([start], 64)))