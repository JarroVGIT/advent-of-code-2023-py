# Advent of Code 2023 - Day 22
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
import itertools
from functools import cache
from collections import defaultdict
#with open("./day22/example.txt") as f:#
with open("./day22/input.txt") as f:
    content = f.read().split("\n")

# Create a dictionary with key = z, value = list of tuples (brick_id, xy)
layers = defaultdict(list)

# create also a dictionary with all brick_ids and list of xy. xy will never change, only z. 
bricks_xy = defaultdict(list)

# Create a list of all vertical brick_ids
vertical_bricks = []

bricks_supported_by = defaultdict(list) # dict to keep track which brick is supported by which bricks.

for brick_id, line in enumerate(content):
    start, end = line.split("~")
    start_x, start_y, start_z = map(int, start.split(","))
    end_x, end_y, end_z = map(int, end.split(","))

    if start_z == end_z:
        # horizontal brick
        if start_x != end_x:
            # length in x direction
            bricks_xy[brick_id].extend([(x, start_y) for x in range(start_x, end_x + 1)])
            layers[start_z].extend([(brick_id, (x, start_y)) for x in range(start_x, end_x + 1)])
        else:
            # length in y direction or 1x1 brick
            bricks_xy[brick_id].extend([(start_x, y) for y in range(start_y, end_y + 1)])
            layers[start_z].extend([(brick_id, (start_x, y)) for y in range(start_y, end_y + 1)])
    else:
        bricks_xy[brick_id].extend([(start_x, start_y)])
        vertical_bricks.append((brick_id, (start_x, start_y)))
        for z in range(start_z, end_z + 1):
            layers[z].extend([(brick_id, (start_x, start_y))])

# Now we have a dictionary with all layers and a dictionary with all bricks and their xy coordinates
# Add empty layers:
for z in range(min(layers.keys()), max(layers.keys()) + 1):
    if z not in layers.keys():
        layers[z] = []

layers = dict(sorted(layers.items()))

# Now let's lower all bricks that are floating, starting from the bottom
for z in range(1, len(layers.keys())+1):
    # Get bricks on this layer, vertical bricks will be in multiple layers
    if z == 1:
        continue
    bricks_current_layer = set([brick_id for brick_id, _ in layers[z]])
    for brick_id in bricks_current_layer:
        current_brick_coords = bricks_xy[brick_id]
        current_z_of_brick = z
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


# We have a dict where for each brick, it says who it is supported by. For brick id 1, check how often [1] is in 
# suported by values, and then continue counting. Recursive function.
@cache
def get_falling_bricks(fallen_bricks: frozenset[int], total_v_bricks_fallen: frozenset[int], total_bricks_fallen: frozenset[int]):
    # Get all possible combinations of brick_ids that might be supportive of a brick. For example
    # if brick 1 and 2 are both supported by 0, and are both supporting 3 but only 1 is supporting 4, 
    # then when 0 falls, it takes away 1 and 2, but we need to look for [1], [2] and [1,2].
    combinations = []
    bricks = fallen_bricks | total_v_bricks_fallen # union
    for i in range(1, len(bricks)+1):
        combinations.extend(list(map(set, itertools.combinations(bricks, i))))
    
    bricks_supported_by_these_bricks = [k for k,v in bricks_supported_by.items() if set(v) in combinations and k not in total_bricks_fallen]
    if len(bricks_supported_by_these_bricks) == 0:
        return 0
    else:
        v_bricks = total_v_bricks_fallen
        for brick in bricks_supported_by_these_bricks:
            if brick in vertical_bricks:
                v_bricks.add(brick)
        
        return (len(bricks_supported_by_these_bricks) + 
                get_falling_bricks(frozenset(bricks_supported_by_these_bricks), 
                                   frozenset(v_bricks), 
                                   total_bricks_fallen | frozenset(bricks_supported_by_these_bricks)))

layers = dict(sorted(layers.items()))
bricks_xy = dict(sorted(bricks_xy.items()))

count = 0
for brick_id in bricks_xy.keys():
    if brick_id in vertical_bricks:
        count += (get_falling_bricks(frozenset([brick_id]), frozenset([brick_id]), frozenset()))
    else:
        count += (get_falling_bricks(frozenset([brick_id]), frozenset(), frozenset()))
print(count)