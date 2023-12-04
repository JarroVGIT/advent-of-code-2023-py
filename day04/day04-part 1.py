# Advent of Code 2023 - Day 04
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

# with open("./day04/example.txt") as f:
with open("./day04/input.txt") as f:
    content = f.read().split("\n")

winning_numbers_list = []
card_numbers_list = []

for line in content:
    numbers = line.split(":")[1]
    winning_numbers_list.append([int(n) for n in numbers.split("|")[0].split()])
    card_numbers_list.append([int(n) for n in numbers.split("|")[1].split()])

total_win = 0
for idx, winning_number in enumerate(winning_numbers_list):
    count = len(set(winning_number) & set(card_numbers_list[idx]))
    total_win += 2 ** (count - 1) if count > 1 else 0 if count == 0 else 1

print(total_win)
