# Advent of Code 2023 - Day 05
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
import time

# with open("./day05/example.txt") as f:
with open("./day05/input.txt") as f:
    content = f.read().split("\n")

start = time.time()
seeds = map(int, content[0].split()[1:])

seeds_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
mappings = []


def create_mapping(input: list[int]) -> tuple:
    dest, source, r = input
    return (range(source, source + r), source, dest, r)


blocks = []
current_block = []
for line in content[2:]:
    if line == "":
        blocks.append(current_block)
        current_block = []
        continue
    current_block.append(line)
blocks.append(current_block)

for block in blocks:
    current_mapping = []
    for line in block:
        if not (l := line.split())[0].isdigit():
            continue
        else:
            l = map(int, l)
            current_mapping.append(create_mapping(l))
    mappings.append(current_mapping)
final_loc = []
for seed in seeds:
    loc = seed
    for mapping in mappings:
        for m in mapping:
            if loc in m[0]:
                loc = loc + (m[2] - m[1])
                break
    final_loc.append(loc)

print(f"Part 1: {min(final_loc)}")
print("Time taken: " + str(time.time() - start) + " seconds")
