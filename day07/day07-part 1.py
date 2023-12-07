# Advent of Code 2023 - Day 07
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from collections import defaultdict
from functools import cmp_to_key

# with open("./day07/example.txt") as f:
with open("./day07/input.txt") as f:
    content = f.read().split("\n")

card_strenght = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def relative_hand_strenght(hand: str) -> int:
    card_counts = defaultdict(lambda: 0)
    for c in hand:
        card_counts[c] += 1
    if max(card_counts.values()) == 5:
        # Five of a kind
        return 8
    elif max(card_counts.values()) == 4:
        # Four of a kind
        return 7
    elif max(card_counts.values()) == 3 and len(card_counts) == 2:
        # Full house
        return 6
    elif max(card_counts.values()) == 3 and len(card_counts) == 3:
        # Three of a kind
        return 3
    elif max(card_counts.values()) == 2 and len(card_counts) == 3:
        # Two pair
        return 2
    elif max(card_counts.values()) == 2 and len(card_counts) == 4:
        # One pair
        return 1
    else:
        # High card
        return 0


def compare_hands(hand1: list, hand2: list) -> int:
    h1 = hand1[0]
    h2 = hand2[0]
    if (s1 := relative_hand_strenght(h1)) > (s2 := relative_hand_strenght(h2)):
        return 1
    elif s1 < s2:
        return -1
    else:
        # Same hand strength, compare cards
        for c1, c2 in zip(h1, h2):
            if card_strenght[c1] > card_strenght[c2]:
                return 1
            elif card_strenght[c1] < card_strenght[c2]:
                return -1
        raise ValueError("Hands are equal")


hands = []
for line in content:
    hands.append(line.split())

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

win = 0
for idx, pair in enumerate(sorted_hands):
    win += (idx + 1) * int(pair[1])

print(f"Winning: {win}")
