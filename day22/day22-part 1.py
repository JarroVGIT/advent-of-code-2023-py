# Advent of Code 2023 - Day 22
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from dataclasses import dataclass
#with open("./day22/example.txt") as f:
with open("./day22/input.txt") as f:
    content = f.read().split("\n")

# Check to see it's all 1 line per brick.
# for line in content:
#     a,b = line.split("~")
#     a1, a2, a3 = map(int, a.split(","))
#     b1, b2, b3 = map(int, b.split(","))
#     if not ((a1 == b1 and a2 == b2) or
#             (a1 == b1 and a3 == b3) or
#             (a2 == b2 and a3 == b3)):
#         print(line)
        

# Create a dictionary with key = z, value = list of tuples (brick_id, xy)
# create also a dictionary with all brick_ids and list of xy. Xy will never change, only z. 
layers = {}
bricks_xy = {}
bricks_supported_by = {} # dict to keep track which brick is supporting what.
for brick_id, line in enumerate(content):
    start, end = line.split("~")
    # Create xy tuples
    start_x, start_y, start_z = map(int, start.split(","))
    end_x, end_y, end_z = map(int, end.split(","))
    if start_z == end_z:
        # horizontal brick
        if start_z not in layers:
            layers[start_z] = []
        if start_x != end_x:
            # length in x direction
            bricks_xy[brick_id] = [(x, start_y) for x in range(start_x, end_x + 1)]
            layers[start_z].extend([(brick_id, (x, start_y)) for x in range(start_x, end_x + 1)])
        else:
            # length in y direction
            bricks_xy[brick_id] = [(start_x, y) for y in range(start_y, end_y + 1)]
            layers[start_z].extend([(brick_id, (start_x, y)) for y in range(start_y, end_y + 1)])
    else:
        bricks_xy[brick_id] = [(start_x, start_y)]
        for z in range(start_z, end_z + 1):
            if z not in layers:
                layers[z] = []
            layers[z].extend([(brick_id, (start_x, start_y))])

# Now we have a dictionary with all layers and a dictionary with all bricks and their xy coordinates
# Add empty layers:
for z in range(min(layers.keys()), max(layers.keys()) + 1):
    if z not in layers.keys():
        layers[z] = []

# Now let's lower all bricks that are floating, starting from the bottom
for z in range(1, len(layers.keys())+1):
    # Get bricks on this layer, vertical bricks will be in multiple layers
    if z == 1:
        continue
    bricks_current_layer = set([brick_id for brick_id, _ in layers[z]])
    for brick_id in bricks_current_layer:
        current_brick_coords = bricks_xy[brick_id]
        current_z_of_brick = z
        bricks_supported_by[brick_id] = [] if brick_id not in bricks_supported_by else bricks_supported_by[brick_id]
        while True:
            if current_z_of_brick == 1:
                break # Cannot go lower. Brick is on the floor.
            bricks_below_coords = set([xy for _, xy in layers[current_z_of_brick - 1]])
            overlapping_coords = bricks_below_coords.intersection(current_brick_coords)
            if len(overlapping_coords) > 0:
                # This brick is supported. Check which one(s) and move on.
                supported_by = []
                for coord in overlapping_coords:
                    brick_below_id = [below_brick_id for below_brick_id, below_coord
                                        in layers[current_z_of_brick - 1] if below_coord == coord][0]
                    if brick_below_id != brick_id:
                        supported_by.append(brick_below_id)
                bricks_supported_by[brick_id].extend(list(set(supported_by)))
                break # Break out of while loop
            else:
                # move brick down, and try again
                layers[current_z_of_brick] = [(b_id, coord)  for b_id, coord in layers[current_z_of_brick] if b_id != brick_id] # keep others, remove this one.
                layers[current_z_of_brick - 1].extend([(brick_id, coord) for coord in current_brick_coords])
                current_z_of_brick -= 1                

count = 0
for brick_id in bricks_xy.keys():
    # Check if this brick_id is anywhere lone supporter, if not, count it.
    is_lone_support = False
    if [brick_id] in bricks_supported_by.values():
        is_lone_support = True
    if not is_lone_support:
        count += 1
layers = dict(sorted(layers.items()))
print(layers)
print(count)