# Advent of Code 2023 - Day 08
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from itertools import cycle
from math import lcm

#with open("./day08/example-2.txt") as f:
with open("./day08/input.txt") as f:
    content = f.read().split("\n")

leftright = content[0]

nodes = {}
for line in content[2:]:
    # find all three letters in line
    node, l, r = re.findall(r"[0-9A-Z]{3}", line)
    nodes[node] = {"L": l, "R": r}

start_nodes = [node for node in nodes if node[-1] == 'A']

steps_until_z = [] # For each starting node, how many steps until Z
for node in start_nodes:
    for idx, instruction in enumerate(cycle(leftright)):
        node = nodes[node][instruction]
        if node[-1] == 'Z':
            steps_until_z.append(idx + 1)
            break

# Answer is the lowest common multiple of all steps_until_z
print(lcm(*steps_until_z))

