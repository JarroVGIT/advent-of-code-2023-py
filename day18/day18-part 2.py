# Advent of Code 2023 - Day 18
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print

from dataclasses import dataclass
from typing import Literal
#with open("./day18/example.txt") as f:
with open("./day18/input.txt") as f:
    content = f.read().split("\n")

direction_mapping = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}
pattern = r"#(?P<distance>[a-fA-F0-9]{5})(?P<direction>[a-fA-F0-9]*)"
instructions = []
for line in content:
    match = re.search(pattern, line)
    distance = int(match.group("distance"), 16)
    instructions.append((direction_mapping[int(match.group('direction'))], distance))

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    start: Point # lowest x or lowest y
    end: Point
    direction: Literal["H", "V"]
    length: int
    range: range

hranges: list[Line] = []
vranges: list[Line] = []

current_point = Point(0,0)

min_x = 0
min_y = 0
max_x = 0
max_y = 0

for i, instruction in enumerate(instructions):
    direction, length = instruction
    if direction == "R":
        # 0,0, 3 lenght -> 3,0
        new_point = Point(current_point.x + length, current_point.y)
        hranges.append(Line(current_point, new_point, "H", length, range(current_point.x, current_point.x + length + 1)))
        current_point = new_point
        min_x, max_x = min(min_x, current_point.x), max(max_x, current_point.x)
        min_y, max_y = min(min_y, current_point.y), max(max_y, current_point.y)
    elif direction == "L":
        # 0,0, 3 lenght -> -3,0
        new_point = Point(current_point.x - length, current_point.y)
        hranges.append(Line(new_point, current_point, "H", length, range(current_point.x - length, current_point.x + 1)))
        current_point = new_point
        min_x, max_x = min(min_x, current_point.x), max(max_x, current_point.x)
        min_y, max_y = min(min_y, current_point.y), max(max_y, current_point.y)
    elif direction == "U":
        # 0,0, 3 lenght -> 0,-3
        new_point = Point(current_point.x, current_point.y - length)
        vranges.append(Line(new_point, current_point, "V", length, range(current_point.y - length, current_point.y + 1)))
        current_point = new_point
        min_x, max_x = min(min_x, current_point.x), max(max_x, current_point.x)
        min_y, max_y = min(min_y, current_point.y), max(max_y, current_point.y)
    elif direction == "D":
        # 0,0, 3 lenght -> 0,3
        new_point = Point(current_point.x, current_point.y + length)
        vranges.append(Line(current_point, new_point, "V", length, range(current_point.y, current_point.y + length + 1)))
        current_point = new_point
        min_x, max_x = min(min_x, current_point.x), max(max_x, current_point.x)
        min_y, max_y = min(min_y, current_point.y), max(max_y, current_point.y)    
    else:
        raise Exception("Unknown direction")

filled = 0

for y in range(min_y, max_y+1):
    # All vertical lines crossing this Y
    vertical_lines = sorted([vrange for vrange in vranges if y in vrange.range], key=lambda x: x.start.x)
    # All horizontal lines on this Y
    horizontal_lines = sorted([hrange for hrange in hranges if y == hrange.start.y], key=lambda x: x.start.x)
    
    x_start = None
    h_line_idx = None
    hl_starts = [hline.start.x for hline in horizontal_lines]

    for v_idx, vline in enumerate(vertical_lines):
        if x_start == None:
            x_start = vline.start.x
            if x_start in hl_starts:
                h_line_idx = hl_starts.index(x_start)
            continue
        elif h_line_idx != None and x_start != None: 
            # We have a starting line, but are following a horizontal line.
            # If second line is going same direction als prev line, then count
            # the horizontal line as filled and reset x_start and h_line
            prev_line = vertical_lines[v_idx - 1]
            if prev_line.start.y == vline.start.y or prev_line.end.y == vline.end.y:
                if prev_line.start.x != x_start:
                    # This is a top end in a counting line, prev-line is not the start. Just continue.
                    h_line_idx = None
                    continue
                else:   
                    # Same direction
                    filled += vline.start.x - x_start + 1
                    # print(f"{y}: {vline.start.x} - {x_start} + 1 = {vline.start.x - x_start + 1}")
                    x_start = None
                    last_h_line_idx = h_line_idx
                    h_line_idx = None
                    continue
            else:
                if prev_line.start.x != x_start:
                    filled += vline.start.x - x_start+ 1
                    # print(f"{y}: {vline.start.x} - {x_start} + 1 = {vline.start.x - x_start + 1}")
                    x_start = None
                    h_line_idx = None
                else:
                    # Different direction, keep going and ignore line.
                    h_line_idx = None
                    continue
        else:
            # We have a starting line, but not following a horizontal line.
            # But if second vline starts/stops at horizontal line, keep going. 
            if vline.start.x in hl_starts:
                h_line_idx = hl_starts.index(vline.start.x)
                continue
            else:
                # Second line does not start/stop at horizontal line, so count first line as filled.
                filled += vline.start.x - x_start+ 1
                # print(f"{y}: {vline.start.x} - {x_start} + 1 = {vline.start.x - x_start + 1}")
                x_start = None
                continue

print(filled)