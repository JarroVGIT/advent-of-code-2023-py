# Advent of Code 2023 - Day 04
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from functools import cache


# with open("./day04/example.txt") as f:
with open("./day04/input.txt") as f:
    content = f.read().split("\n")

winning_numbers_dict = {}
card_numbers_dict = {}


for line in content:
    card_id = int(line.split(":")[0].split()[1])
    numbers = line.split(":")[1]
    winning_numbers_dict[card_id] = [int(n) for n in numbers.split("|")[0].split()]
    card_numbers_dict[card_id] = [int(n) for n in numbers.split("|")[1].split()]


@cache
def get_won_cards(card_id):
    total = 0
    winning_numbers = winning_numbers_dict[card_id]
    card_numbers = card_numbers_dict[card_id]
    overlap = len(set(winning_numbers) & set(card_numbers))
    total += overlap
    for i in range(overlap):
        total += get_won_cards(card_id + 1 + i)
    return total


total = 0
for card_id in card_numbers_dict.keys():
    total += 1 + get_won_cards(card_id)

print(f"Part 2: {total}")
