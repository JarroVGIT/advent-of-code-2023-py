# Advent of Code 2023 - Day 02
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day02/example.txt") as f:
with open("./day02/input.txt") as f:
    content = f.read().split("\n")

bag = {"red": 12, "green": 13, "blue": 14}

games_possible = []

for line in content:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    split = line.split(": ")
    game_id = split[0].split(" ")[1]
    hands = split[1].replace(";", ",").split(",")
    possible = True
    for hand in hands:
        amount, color = hand.split()
        if bag[color] < int(amount):
            possible = False
            break
    if possible:
        games_possible.append(int(game_id))

print(f"Part 1: {sum(games_possible)}")
