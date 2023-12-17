# Advent of Code 2023 - Day 17
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from dijkstar import Graph, find_path
#with open("./day17/example.txt") as f:
#with open("./day17/example-2.txt") as f:
with open("./day17/input.txt") as f:
    content = f.read().split("\n")

height = 0
width = 0

coordinates = {}
for y, line in enumerate(content):
    if y > height:
        height = y
    for x, val in enumerate(line):
        coordinates[complex(x,y)] = int(val)
        if x > width:
            width = x

graph = Graph()

target = complex(width, height)

# Create graph, where each coordinate has an additional property dir+value. For example:
# coordinate 4+6j with property 'r2' means that it has been coming from the right, and the previous step as well.

not_allowed_pairs = [('u', 'd'), ('d', 'u'), ('l', 'r'), ('r', 'l')]

for coordinate in coordinates:
    for c_from_direction in ['u', 'd', 'l', 'r']:
        for c_prev_steps in [1,2,3,4,5,6,7,8,9,10]:
            current_coordinate = (coordinate, c_from_direction + str(c_prev_steps))
            for n_from_direction, n_coord in [['u', 1j], ['d', -1j], ['l', 1], ['r', -1]]:
                if (c_from_direction, n_from_direction) in not_allowed_pairs:
                    continue # Don't allow going back
                if c_from_direction != n_from_direction:
                    # Only if there have been 4 consecutive steps in the same direction, allow a different direction.
                    if c_prev_steps >= 4:
                        neighbour = (coordinate + n_coord, n_from_direction + str(1))
                        minimal_achievable_coordinate_in_this_direction = coordinate + n_coord + n_coord + n_coord + n_coord
                        if neighbour[0] in coordinates and minimal_achievable_coordinate_in_this_direction in coordinates:
                                if neighbour[0] == target:
                                    graph.add_edge(current_coordinate, target, coordinates[target])
                                else:
                                    graph.add_edge(current_coordinate, neighbour, coordinates[neighbour[0]])
                else: # continouation of the direction.
                    if c_prev_steps < 10:
                        neighbour = (coordinate + n_coord, n_from_direction + str(c_prev_steps + 1))
                        if neighbour[0] in coordinates:
                            if neighbour[0] == target:
                                graph.add_edge(current_coordinate, target, coordinates[target])
                            else:
                                graph.add_edge(current_coordinate, neighbour, coordinates[neighbour[0]])
                    else:
                        pass # no more steps in this direction    

# Add start edges.
graph.add_edge(complex(0,0), (complex(0,1), 'u1'), coordinates[complex(0, 1)])
graph.add_edge(complex(0,0), (complex(1,0), 'l1'), coordinates[complex(1, 0)])

find = find_path(graph, complex(0,0), complex(width, height))
print(find.total_cost)

# Debugging...
# grid=[]
# for line in content:
#     grid.append([val for val in line])
# print(grid)

# for node in find.nodes:
#     if type(node) == tuple:
#         if node[1][0] == 'u':
#             grid[int(node[0].imag)][int(node[0].real)] = 'v'
#         elif node[1][0] == 'd':
#             grid[int(node[0].imag)][int(node[0].real)] = '^'
#         elif node[1][0] == 'l':
#             grid[int(node[0].imag)][int(node[0].real)] = '>'
#         elif node[1][0] == 'r':
#             grid[int(node[0].imag)][int(node[0].real)] = '<'

# print(grid)
