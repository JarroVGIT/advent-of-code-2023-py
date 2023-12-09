# Advent of Code 2023 - Day 09
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print

#with open("./day09/example.txt") as f:
with open("./day09/input.txt") as f:
    content = f.read().split("\n")

content = [[int(x) for x in line.split()] for line in content]

def calculate_differences(sequence: list[int]) -> list[int]:
    # Calculate the differences between each number in a sequence of ints
    return [j-i for i, j in zip(sequence[:-1], sequence[1:])]

def predict_next(sequence: list[int]) -> list[int]:
    # We are only interested in the last number of each sequence and subsequent difference-sequences
    last_numbers = [sequence[-1]]

    # Create a first new sequence (of differences) from the original sequence.
    differences = calculate_differences(sequence)

    # Keep doing so, untill all differences are 0
    while not all([n == 0 for n in differences]):
        # Store the last number of this new sequence
        last_numbers.append(differences[-1])
        # Create a new sequence (of differences) from the previous sequence
        differences = calculate_differences(differences)
    
    # The final 'last_number' must be 0.
    last_numbers.append(0)
    new_last_numbers = []
    for i, n in enumerate(reversed(last_numbers)):
        if i == 0:
            # The first number is always 0
            new_last_numbers.append(n)
            continue
        # The next last_number is the previous last_number plus the current number
        new_last_numbers.append(new_last_numbers[-1] + n)
    sequence.append(new_last_numbers[-1])
    return sequence

new_content = []
for line in content:
    new_content.append(predict_next(line))

print(sum([x[-1] for x in new_content]))