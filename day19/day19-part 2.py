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
#with open("./day19/example.txt") as f:
with open("./day19/input.txt") as f:
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


r_obj = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
}

def calculate_combinations(r_obj: dict[str, tuple[int, int]]) -> int:
    c = [r[1] - r[0] + 1 for r in r_obj.values()]
    return c[0] * c[1] * c[2] * c[3]
    # for r in r_obj.values():
    #     total *= r[1] - r[0] + 1
    # return total

def process_range(workflow: str, r_obj: dict[str, tuple[int, int]], rule_idx: int = 0) -> int:
    # Assert rule for ranges, and determine which part will move to new rule. If R then return 0, 
    # if Accepted return the total possible combinations of the ranges. 
    if workflow == "A":
            return calculate_combinations(r_obj)
    elif workflow == "R":
            return 0
    rule = workflows[workflow][rule_idx]
    if rule.attr is None and rule.operation is None and rule.value is None:
        return process_range(rule.go_to_workflow, r_obj)
    else: 
        # Check if we have to split up the range.
        r_start, r_end = r_obj[rule.attr]
        if rule.operation == '<':
            if r_end < rule.value:
                # entire range moves to next workflow.
                return process_range(rule.go_to_workflow, {**r_obj})
            elif r_start < rule.value:
                # split up the range.
                matched_r = {**r_obj}
                not_matched_r = {**r_obj}
                not_matched_r[rule.attr] = (rule.value, r_end)
                matched_r[rule.attr] = (r_start, rule.value - 1)
                return (process_range(workflow, not_matched_r, rule_idx+1) +
                        process_range(rule.go_to_workflow, matched_r))
            else:
                # Entire range move to next rule
                return process_range(rule.go_to_workflow, {**r_obj}, rule_idx+1)
        elif rule.operation == '>':
            if r_start > rule.value:
                # entire range moves to next workflow.
                return process_range(rule.go_to_workflow, {**r_obj})
            elif r_end > rule.value:
                matched_r = {**r_obj}
                not_matched_r = {**r_obj}
                matched_r[rule.attr] = (rule.value + 1, r_end)
                not_matched_r[rule.attr] = (r_start, rule.value)
                return (process_range(workflow, not_matched_r, rule_idx+1) +
                        process_range(rule.go_to_workflow, matched_r))
            else:
                return process_range(rule.go_to_workflow, r_obj, rule_idx+1) 

print(process_range("in", r_obj))