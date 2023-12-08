# Advent of Code 2023 - Day 05
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
import time
from dataclasses import dataclass

# with open("./day05/example.txt") as f:
with open("./day05/input.txt") as f:
    content = f.read().split("\n")


@dataclass
class Mapping:
    source_range: range
    operation: int
    destination_range: range = None


seeds = list(map(int, content[0].split()[1:]))
couples = []
for i in range(0, len(seeds), 2):
    couples.append(range(seeds[i], seeds[i] + seeds[i + 1]))

seed_ranges: list[range] = couples


def create_mapping(input: list[int]) -> tuple:
    dest, source, r = input
    # Tuple of input range, operation, source start,, desitnation start, range.
    return Mapping(range(source, source + r), (dest - source), range(dest, dest + r))


blocks = []
current_block = []
for line in content[2:]:
    if line == "":
        blocks.append(current_block)
        current_block = []
        continue
    current_block.append(line)
blocks.append(current_block)

mappings: list[list[Mapping]] = []
for block in blocks:
    current_mapping = []
    for line in block:
        if not (l := line.split())[0].isdigit():
            continue
        else:
            l = map(int, l)
            current_mapping.append(create_mapping(l))
    mappings.append(current_mapping)

# seed_ranges are the input ranges. For each layer, split up the seed ranges if they are
# not fully mapped to a destination, such that each seed range is fully mapped to a destination.
new_seed_ranges: list[range] = [] # List that will feed into next iteration

for mapping in mappings:
    
    while seed_ranges:
        seed_range = seed_ranges.pop(0) # If we must split, we can append the new ranges to the end of the list. 
        for mapping_range in mapping: # For each seed range, check if it is fully mapped to a destination.
            if seed_range.start in mapping_range.source_range and seed_range.stop - 1 in mapping_range.source_range:
                # Fully mapped
                new_seed_ranges.append(range(seed_range.start + mapping_range.operation, seed_range.stop + mapping_range.operation))
                break
            elif seed_range.start in mapping_range.source_range and seed_range.stop -1 not in mapping_range.source_range:
                # Partially mapped, seed range starts in mapping range, but does not end in it.
                # splitting seed range into 2 ranges, one that is mapped, and one that is not.
                new_seed_ranges.append(range(seed_range.start + mapping_range.operation, mapping_range.source_range.stop + mapping_range.operation))
                seed_ranges.append(range(mapping_range.source_range.stop, seed_range.stop))
                break
            elif seed_range.start not in mapping_range.source_range and seed_range.stop -1 in mapping_range.source_range:
                # Partially mapped, seed range ends in mapping range, but does not start in it.
                # splitting seed range into 2 ranges, one that is mapped, and one that is not.
                new_seed_ranges.append(range(mapping_range.source_range.start + mapping_range.operation, seed_range.stop + mapping_range.operation))
                seed_ranges.append(range(seed_range.start, mapping_range.source_range.start))
                break
            elif seed_range.start < mapping_range.source_range.start and seed_range.stop  > mapping_range.source_range.stop:
                # Partially mapped, seed range starts before mapping range, and ends after mapping range.
                # splitting seed range into 3 ranges, one that is mapped, and two that are not.
                new_seed_ranges.append(range(mapping_range.source_range.start + mapping_range.operation, mapping_range.source_range.stop + mapping_range.operation))
                seed_ranges.append(range(seed_range.start, mapping_range.source_range.start))
                seed_ranges.append(range(mapping_range.source_range.stop, seed_range.stop))
                break
            else:
                # Not mapped
                continue
        else: # cool feature of for loops; this is ran if the for loop is not broken out of. 
            new_seed_ranges.append(seed_range)
    
    # End of while loop. Seed ranges are now all splitted into ranges that are fully mapped to a destination.
    seed_ranges = new_seed_ranges
    new_seed_ranges = []


lowest_possible_location = sorted(seed_ranges, key=lambda x: x.start)[0].start
print(f"Part 2: lowest possible location: {lowest_possible_location}")

# reverse location to seed:
seed = lowest_possible_location
for mapping in reversed(mappings):
    for mapping_range in mapping:
        if seed in mapping_range.destination_range:
            seed = seed - mapping_range.operation
            break

print(f"Part 2: lowest possible seed: {seed}")
