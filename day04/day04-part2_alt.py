# Advent of Code 2023 - Day 04
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from collections import defaultdict, deque
import time

# with open("./day04/example.txt") as f:
with open("./day04/input.txt") as f:
    content = f.read().split("\n")

winning_numbers_list = []
card_numbers_list = []
winning_numbers_dict = {}
card_numbers_dict = {}
cards_processed = defaultdict(lambda: 0)

for line in content:
    card_id = int(line.split(":")[0].split()[1])
    numbers = line.split(":")[1]

    winning_numbers_dict[card_id] = [int(n) for n in numbers.split("|")[0].split()]
    card_numbers_dict[card_id] = [int(n) for n in numbers.split("|")[1].split()]
    # tuple of card_id and list of numbers
    card_numbers_list.append((card_id, [int(n) for n in numbers.split("|")[1].split()]))

## Initial solution to Part 2. Used list instead of deque, which was very slow.
start = time.time()
total_win = 0
while card_numbers_list:
    card_id, card_numbers = card_numbers_list.pop(0)
    cards_processed[card_id] += 1
    winning_numbers = winning_numbers_dict[card_id]
    count = len(set(winning_numbers) & set(card_numbers))
    cards_to_add = [
        (card_id + i, card_numbers_dict[card_id + i]) for i in range(1, count + 1)
    ]
    card_numbers_list.extend(cards_to_add)

print(sum([v for k, v in cards_processed.items()]))
print(f"Time passed (list): {time.time() - start} seconds")

## Second solution to Part 2. Used deque instead of list, which was much faster.
start = time.time()
total_win = 0
q = deque(card_numbers_list)
while len(q) > 0:
    card_id, card_numbers = q.popleft()
    cards_processed[card_id] += 1
    winning_numbers = winning_numbers_dict[card_id]
    count = len(set(winning_numbers) & set(card_numbers))
    cards_to_add = [
        (card_id + i, card_numbers_dict[card_id + i]) for i in range(1, count + 1)
    ]
    q.extendleft(cards_to_add)
    # card_numbers_list.extend(cards_to_add)

print(sum([v for k, v in cards_processed.items()]))
print(f"Time passed (deque): {time.time() - start} seconds")
