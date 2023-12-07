# Advent of Code 2023 - Day 07
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from collections import Counter
from functools import cmp_to_key
import itertools

# with open("./day07/example.txt") as f:
with open("./day07/input.txt") as f:
    content = f.read().split("\n")


card_strenght = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 0,  # Value of J is now the lowest!
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

# We might want to replace any J with one of the below.
alternative_cards = set(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"])


def relative_hand_strenght(hand: str) -> int:
    strenght = 0

    # We only need overlapping cards + A (potential high card), because other non-occured cards in hand never will lead to a better hand.
    overlap = list(set(hand + "A") & alternative_cards)

    # We need to know how many J's there are in this hand
    count_of_J = len(re.findall(r"J", hand))

    # We need to create all possible combinations of replacing cards (based on overlapping cards)
    # For example: if we have 2 J's and 3 overlapping cards, we need to create 3^2 = 9 combinations
    # combinations is a list of tuples, where each tuple is a combination of cards to replace J's with
    combinations = list(itertools.product(overlap, repeat=count_of_J))

    # We need to check each combination and store the highest hand strength
    for combination in combinations:
        intermediate_result = 0
        hand_combination = hand

        # Replace 'J' from hand with cards from this combination
        for i in range(count_of_J):
            hand_combination = hand_combination.replace("J", combination[i], 1)

        # Check hand strenght
        card_counts = Counter(hand_combination)
        if max(card_counts.values()) == 5:
            # Five of a kind
            # We can stop here, because this is the best possible hand
            return 8
        elif max(card_counts.values()) == 4:
            # Four of a kind
            intermediate_result = 7
        elif max(card_counts.values()) == 3 and len(card_counts) == 2:
            # Full house
            intermediate_result = 6
        elif max(card_counts.values()) == 3 and len(card_counts) == 3:
            # Three of a kind
            intermediate_result = 5
        elif max(card_counts.values()) == 2 and len(card_counts) == 3:
            # Two pair
            intermediate_result = 4
        elif max(card_counts.values()) == 2 and len(card_counts) == 4:
            # One pair
            intermediate_result = 3
        else:
            # High card
            intermediate_result = 2

        # Store strength if higher than current highest:
        strenght = max(intermediate_result, strenght)

    return strenght


def compare_hands(hand1: list[str], hand2: list[str]) -> int:
    # Compare two hands. Compare functions used in sort() should return
    # -1 if arg1 < arg2, 0 if arg1 == arg2 and 1 if arg1 > arg2.

    # Distille hand from input
    h1 = hand1[0]
    h2 = hand2[0]

    # Use walrus notation to store hand strength and compare to each other.
    if (s1 := relative_hand_strenght(h1)) > (s2 := relative_hand_strenght(h2)):
        return 1
    elif s1 < s2:
        return -1
    else:
        # Same hand strength, compare cards individually
        for c1, c2 in zip(h1, h2):
            if card_strenght[c1] > card_strenght[c2]:
                return 1
            elif card_strenght[c1] < card_strenght[c2]:
                return -1
        raise ValueError("Hands are equal")


hands = []
for line in content:
    hands.append(line.split())

# The `key` parameter is is used to select a value from a compounded object to be compared with.
# However, you can use functools.cmp_to_key() to provide a comparison function to this parameter.
# In python 2 this was different, and you had a `cmp` parameter instead of `key`. This is the 'new'
# Python 3 way of doing it.
sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))


win = 0
for idx, pair in enumerate(sorted_hands):
    win += (idx + 1) * int(pair[1])

print(f"Winning: {win}")
