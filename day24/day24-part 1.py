# Advent of Code 2023 - Day 24
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from dataclasses import dataclass
import itertools
#with open("./day24/example.txt") as f:
with open("./day24/input.txt") as f:
    content = f.read().split("\n")

@dataclass
class Hailstone:
    id: int
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int
    a: int | None = None
    b: int | None = None

hail_stones: list[Hailstone] = []


pattern = r'-?\d+'
for id, line in enumerate(content):
    x, y, z, dx, dy, dz = map(int, re.findall(pattern, line))
    hail_stones.append(Hailstone(id, x, y, z, dx, dy, dz))


# Need lineair functions for each hailstone (y=ax+b)
for hailstone in hail_stones:
    # Each nanosecond, dx and dy happens. This means: if x increases with dx, then y increases with dy.
    # So, if we want dy for dx=1 (=a), then a = dy/dx
    hailstone.a = hailstone.dy / hailstone.dx
    # y = a * x + b, we know y, x and a, so we can calculate b
    hailstone.b = hailstone.y - hailstone.a * hailstone.x

def intersection(h1: Hailstone, h2: Hailstone) -> tuple[float, float] | None:
    # Calculate the intersection of 2 hailstones
    # y = a * x + b
    # y = c * x + d
    # a * x + b = c * x + d
    # a * x - c * x = d - b
    # x * (a - c) = d - b
    # x = (d - b) / (a - c)
    if h1.a == h2.a:
        # Parallel lines
        return None

    x = (h2.b - h1.b) / (h1.a - h2.a)
    y = h1.a * x + h1.b
    return (x, y)

test_min_x, test_max_x = 200000000000000, 400000000000000
test_min_y, test_max_y = 200000000000000, 400000000000000

count = 0
for combination in itertools.combinations(hail_stones, 2):
    # Check if the hailstones intersect
    intersection_point = intersection(combination[0], combination[1])
    if intersection_point is not None:
        x, y = intersection_point
        if ((test_min_x <= x <= test_max_x) and (test_min_y <= y <= test_max_y)
            and ((combination[0].x < x and combination[0].dx > 0) or (combination[0].x > x and combination[0].dx < 0))
            and ((combination[0].y < y and combination[0].dy > 0) or (combination[0].y > y and combination[0].dy < 0))
            and ((combination[1].x < x and combination[1].dx > 0) or (combination[1].x > x and combination[1].dx < 0))
            and ((combination[1].y < y and combination[1].dy > 0) or (combination[1].y > y and combination[1].dy < 0))
            ):
            count += 1
print(count)