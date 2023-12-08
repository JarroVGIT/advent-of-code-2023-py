# Advent of Code 2023 - Day 08
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from itertools import cycle
# with open("./day08/example.txt") as f:
with open("./day08/input.txt") as f:
    content = f.read().split("\n")

leftright = content[0]

nodes = {}
for line in content[2:]:
    # find all three letters in line
    node, l, r = re.findall(r"[A-Z]{3}", line)
    nodes[node] = {"L": l, "R": r}

node = 'AAA'
steps = 0
for step, instruction in enumerate(cycle(leftright)):
    node = nodes[node][instruction]
    if node == 'ZZZ':
        print(f"Step: {step+1}")
        break