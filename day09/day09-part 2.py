# Advent of Code 2023 - Day 09
# Author: Jarro van Ginkel
# Part 2

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
    return [j-i for i, j in zip(sequence[:-1], sequence[1:])]

def predict_prev(sequence: list[int]) -> list[int]:
    first_numbers = [sequence[0]]
    differences = calculate_differences(sequence)
    while not all([n == 0 for n in differences]):
        first_numbers.append(differences[0])
        differences = calculate_differences(differences)
    
    first_numbers.append(0)
    new_first_numbers = []
    for i, n in enumerate(reversed(first_numbers)):
        if i == 0:
            new_first_numbers.append(n)
            continue
        new_first_numbers.append(n - new_first_numbers[-1])
    sequence.insert(0, new_first_numbers[-1])
    return sequence

new_content = []
for line in content:
    new_content.append(predict_prev(line))

print(sum([x[0] for x in new_content]))