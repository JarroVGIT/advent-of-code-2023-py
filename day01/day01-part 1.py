# Advent of Code 2023 - Day 01
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print

# with open("./day01/example1.txt") as f:
with open("./day01/input.txt") as f:
    content = f.read().split("\n")


# option 1
def using_join(content: list[str]):
    total = 0
    for line in content:
        numbers = "".join([c for c in line if c.isdigit()])
        total += int(numbers[0] + numbers[-1])
    return total


# option 2
def using_regex(content: list[str]):
    total = 0
    for line in content:
        numbers = re.sub("[^0-9]", "", line)
        total += int(numbers[0] + numbers[-1])
    return total


# Which is faster?
# import timeit
# print(timeit.timeit("using_join(content)", globals=globals(), number=1000))
# print(timeit.timeit("using_regex(content)", globals=globals(), number=1000))

print(f"Part 1 (join): {using_join(content)}")
print(f"Part 1 (regex): {using_regex(content)}")
