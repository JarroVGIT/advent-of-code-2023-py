# Advent of Code 2023 - Day 02
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
import numpy as np
# import re
from rich import print
from collections import defaultdict

# with open("./day02/example.txt") as f:
with open("./day02/input.txt") as f:
    content = f.read().split("\n")

powers = []

for line in content:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    split = line.split(": ")
    game = split[0].split(" ")[1]
    hands = split[1].replace(";", ",").split(",")
    possible_bag = defaultdict(lambda: -1)
    for hand in hands:
        amount, color = hand.split()
        if possible_bag[color] < int(amount):
            possible_bag[color] = int(amount)
    power = np.prod([abs(x) for x in possible_bag.values()])
    powers.append(power)

print(f"Part 2: {sum(powers)}")
