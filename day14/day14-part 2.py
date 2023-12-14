# Advent of Code 2023 - Day 14
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from typing import Literal

from time import time

#with open("./day14/example.txt") as f:
with open("./day14/input.txt") as f:
    content = f.read().split("\n")

start = time()

grid = []
for line in content:
    grid.append(list(line))

coordinates = {}
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        coordinates[complex(x, y)] = val

def roll_north(grid: dict[complex, str]) -> dict[complex, str]:
    new_grid = {}
    for x in range(int(max(grid.keys(), key=lambda x: x.real).real + 1)):
        # For each column, create list of coordinates:
        column = [coord for coord in grid.keys() if coord.real == x]
        # Get rocks in column:
        rocks = [coord for coord in column if grid[coord] == '#']
        # Ensure sorting is done.
        rocks.sort(key=lambda x: x.imag)
        stop = -1
        for group_id in range(len(rocks)+1):
            rock = rocks[group_id] if group_id < len(rocks) else complex(x, len(column))
            count = sum([1 for k in column if stop <= k.imag < rock.imag and grid[k] == 'O'])
            for i in range(stop + 1, int(rock.imag)):
                if i-(stop+1) < count:
                    new_grid[complex(rock.real, i)] = 'O'
                else:
                    new_grid[complex(rock.real, i)] = '.'
            if group_id < len(rocks):
                new_grid[rock] = '#'
            stop = int(rock.imag)
    return new_grid

def roll_south(grid: dict[complex, str]) -> dict[complex, str]:
    new_grid = {}
    for x in range(int(max(grid.keys(), key=lambda x: x.real).real + 1)):
        # For each column, create list of coordinates:
        column = [coord for coord in grid.keys() if coord.real == x]
        # Get rocks in column:
        rocks = [coord for coord in column if grid[coord] == '#']
        rocks.sort(key=lambda x: x.imag, reverse=True)
        stop = len(column)
        for group_id in range(len(rocks)+1):
            rock = rocks[group_id] if group_id < len(rocks) else complex(x, -1)
            count = sum([1 for k in column if rock.imag <= k.imag < stop and grid[k] == 'O'])
            for i in range(stop - 1, int(rock.imag), -1):
                if (stop-1-i) < count:
                    new_grid[complex(rock.real, i)] = 'O'
                else:
                    new_grid[complex(rock.real, i)] = '.'
            if group_id < len(rocks):
                new_grid[rock] = '#'
            stop = int(rock.imag)
    return new_grid

def roll_west(grid: dict[complex, str]) -> dict[complex, str]:
    new_grid = {}
    for y in range(int(max(grid.keys(), key=lambda x: x.imag).imag + 1)):
        # For each row, create list of coordinates:
        row = [coord for coord in grid.keys() if coord.imag == y]
        # Get rocks in row:
        rocks = [coord for coord in row if grid[coord] == '#']
        # Ensure sorting is done.
        rocks.sort(key=lambda x: x.real)
        stop = -1
        for group_id in range(len(rocks)+1):
            rock = rocks[group_id] if group_id < len(rocks) else complex(len(row), y)
            count = sum([1 for k in row if stop <= k.real < rock.real and grid[k] == 'O'])
            for i in range(stop + 1, int(rock.real)):
                if i-(stop+1) < count:
                    new_grid[complex(i, rock.imag)] = 'O'
                else:
                    new_grid[complex(i, rock.imag)] = '.'
            if group_id < len(rocks):
                new_grid[rock] = '#'
            stop = int(rock.real)
    return new_grid

def roll_east(grid: dict[complex, str]) -> dict[complex, str]:
    new_grid = {}
    for y in range(int(max(grid.keys(), key=lambda x: x.imag).imag + 1)):
        # For each column, create list of coordinates:
        row = [coord for coord in grid.keys() if coord.imag == y]
        # Get rocks in column:
        rocks = [coord for coord in row if grid[coord] == '#']
        rocks.sort(key=lambda x: x.real, reverse=True)
        stop = len(row)
        for group_id in range(len(rocks)+1):
            rock = rocks[group_id] if group_id < len(rocks) else complex(-1, y)
            count = sum([1 for k in row if rock.real <= k.real < stop and grid[k] == 'O'])
            for i in range(stop - 1, int(rock.real), -1):
                if (stop-1-i) < count:
                    new_grid[complex(i, rock.imag)] = 'O'
                else:
                    new_grid[complex(i, rock.imag)] = '.'
            if group_id < len(rocks):
                new_grid[rock] = '#'
            stop = int(rock.real)
    return new_grid

def roll(coordinates: dict[complex, str], direction: Literal['n', 's', 'e', 'w']) -> dict[complex, str]:
    # Grid coordinates are complex numbers. Based on direction, calculate new grid coordinates.
    if direction == 'n':
        return roll_north(coordinates)
    elif direction == 's':
        return roll_south(coordinates)
    elif direction == 'e':
        return roll_east(coordinates)
    elif direction == 'w':
        return roll_west(coordinates)

past_results = [coordinates]
i = 1
target = 1000000000
found = False
height = max(coordinates.keys(), key=lambda x: x.imag).imag + 1

while i <= target:
    for direction in ['n', 'w', 's', 'e']:
        coordinates = roll(coordinates, direction)
    if not found and coordinates in past_results:
        cycle_length = i - past_results.index(coordinates)
        new_i = (target - i - 1) % cycle_length
        found = True
        i = target-new_i
    else:
        i += 1
        past_results.append(coordinates)


weight = 0
for k,v in coordinates.items():
    if v == 'O':
        weight += height - k.imag
print(weight)

end = time()
print(f"Runtime in seconds: {end - start}")


    