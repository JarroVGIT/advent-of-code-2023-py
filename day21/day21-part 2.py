# Advent of Code 2023 - Day 21
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from copy import deepcopy
with open("./day21/example.txt") as f:
    # with open("./day21/input.txt") as f:
    content = f.read().split("\n")

start = None
tiles = {}
bushes = {}
for y, row in enumerate(content):
    for x, val in enumerate(row):
        # Process other tiles
        if val == 'S':
            start = complex(x, y)
            tiles[complex(x, y)] = []
        if val == '.':
            tiles[complex(x, y)] = []

max_y = len(content) - 1
max_x = len(content[0]) - 1

def map_back(c: complex):
    x,y = int(c.real), int(c.imag)
    new_x = x % (max_x+1)
    new_y = y % (max_y+1)
    return complex(new_x, new_y)

# add all neigebours in (complex, complex) number where the second complex is either [1, -1, 1j, -jj, 0]
for c in tiles.keys():
    for n in [1, -1, 1j, -1j]:
        n_c = c + n
        n_g = 0
        if n_c.real < 0:
            n_c = complex(max_x, n_c.imag)
            n_g = -1
        elif n_c.real > max_x:
            n_c = complex(0, n_c.imag)
            n_g
        elif n_c.imag < 0:
            n_c = complex(n_c.real, max_y)
        elif n_c.imag > max_y:
            n_g[1] = grid_id[1]+1
            n_c = complex(n_c.real, 0)
        if n_c in tiles:
            tiles[c].append(n_c, 0)




def get_neighbours(c: complex, grid_id: tuple[int, int]) -> list[tuple[complex, tuple[int,int]]]:
    # Map coordinate to original position:
    neighbours = []
    for n in [1,-1, 1j, -1j]:
        n_c = c + n
        n_g = list(grid_id)
        if n_c.real < 0:
            n_g[0] = grid_id[0]-1
            n_c = complex(max_x, n_c.imag)
        elif n_c.real > max_x:
            n_g[0] = grid_id[0]+1
            n_c = complex(0, n_c.imag)

        if n_c.imag < 0:
            n_g[1] = grid_id[1]-1
            n_c = complex(n_c.real, max_y)
        elif n_c.imag > max_y:
            n_g[1] = grid_id[1]+1
            n_c = complex(n_c.real, 0)
        if n_c in tiles:
            neighbours.append((n_c, tuple(n_g)))
    return neighbours
        

        
    return set(neighbours)

def get_next_possible_steps(current_tiles: dict[complex, set[tuple[int, int]]], steps_left: int):
    if steps_left == 0:
        return current_tiles
    c_tiles = deepcopy(current_tiles)
    for tile, grids in current_tiles.items():
        for grid_id in grids:
            for n_tile, n_grid_id in get_neighbours(tile, grid_id):
                c_tiles[n_tile].add(n_grid_id)
    return get_next_possible_steps(c_tiles, steps_left - 1)

# current_tiles: add only start grid_id to start_coord.
current_tiles = deepcopy(tiles)
current_tiles[start].add((0,0))

for i in [6, 10, 50, 100]:  
    possible_tiles = get_next_possible_steps(current_tiles, i)
    count = 0
    for c, grids in possible_tiles.items():
        count += len(grids)
    print(count)