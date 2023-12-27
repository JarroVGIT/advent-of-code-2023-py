# Advent of Code 2023 - Day 25
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
import re
from rich import print
from collections import defaultdict
import itertools
import networkx as nx
#with open("./day25/example.txt") as f:
with open("./day25/input.txt") as f:
    content = f.read().split("\n")

pattern = r'[a-z]{3}'
nondirectional_connections: list[set[str]] = []
directional_connections: dict[str, list[str]] = defaultdict(list)
graph = nx.Graph()
for line in content:
    matches = re.findall(pattern, line)
    for i in range(1, len(matches)):
        graph.add_edge(matches[0], matches[i])

cut_value, partition = nx.stoer_wagner(graph)

print(cut_value)
print(len(partition[0])*len(partition[1]))
