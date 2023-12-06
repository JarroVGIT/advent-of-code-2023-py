# Advent of Code 2023 - Day 06
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from math import prod

with open("./day06/example.txt") as f:
    # with open("./day06/input.txt") as f:
    content = f.read().split("\n")

# Nasty! TO DO: solve quadratic equation
# f(x) = (t - x) * x > d where t = time allowed, x is time pressed and d is distance

times = list(map(int, content[0].split()[1:]))
distances = list(map(int, content[1].split()[1:]))
count_of_possible_distances = []
for idx, t in enumerate(times):
    possible_distances = []
    for i in range(0, t + 1):
        if x := (t - i) * i > distances[idx]:
            possible_distances.append(x)
    count_of_possible_distances.append(len(possible_distances))

print(prod(count_of_possible_distances))
