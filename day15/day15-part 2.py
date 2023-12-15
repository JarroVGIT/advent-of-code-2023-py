# Advent of Code 2023 - Day 15
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from collections import defaultdict
from rich import print

#with open("./day15/example.txt") as f:
with open("./day15/input.txt") as f:
    content = f.read().split("\n")

instructions = []
for line in content:
    for piece in line.split(","):
        instructions.append(piece)

boxes = defaultdict(dict) # Note: dicts in Python 3 are ordered, no need for ordered dicts anymore yay

def hash_algo(string: str) -> int:
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current %= 256
    return current

for step in instructions:
    letters = re.search("^[a-zA-Z]*", step)[0]
    if strength:=re.search("[0-9]*$", step)[0]:
        strength = int(strength)
        operation = step[-2]
    else:
        operation = step[-1]
    
    hash_value = hash_algo(letters)
    if operation == "=":
            # replaces or adds it
            boxes[hash_value][letters] = strength
    else:
        if letters in boxes[hash_value]:
            # remove
            boxes[hash_value].pop(letters)
        else:
            # do nothing
            pass
lens_power = []
for boxid in range(0,256):
    lenses = boxes[boxid]
    i = 1
    for k, v in lenses.items():
        lens_power.append((boxid+1) * i * v)
        i += 1

print(sum(lens_power))
    
