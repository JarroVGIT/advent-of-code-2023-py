# Advent of Code 2023 - Day 19
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
import re
from rich import print
from dataclasses import dataclass
from typing import Literal
with open("./day19/example.txt") as f:
#with open("./day19/input.txt") as f:
    content = f.read().split("\n\n")

@dataclass
class Rule:
    attr: str | None
    operation: Literal["<", ">"] | None
    value: int | None
    go_to_workflow: str | None


operation_mapping = {
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
}

workflows_raw = content[0].split("\n")
parts_raw = content[1].split("\n")    

workflows: dict[str, list[Rule]] = {}
pattern = r"(?P<workflow>\w+)\{(?P<rules>.*)\}"
for wf in workflows_raw:
    match = re.match(pattern, wf)
    workflow = match.group("workflow")
    rules = match.group("rules").split(",")
    current_rules = []
    for rule in rules:
        rule_match = re.match(r"(?P<attr>\w+)(?P<operation>[<|>])(?P<value>\d+):(?P<go_to_workflow>\w+)", rule)
        if rule_match:
            current_rules.append(Rule(rule_match.group("attr"), rule_match.group("operation"), int(rule_match.group("value")), rule_match.group("go_to_workflow")))
        else:
            current_rules.append(Rule(None, None, None, rule))
    workflows[workflow] = current_rules


print(workflows)