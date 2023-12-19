# Advent of Code 2023 - Day 19
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
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

parts = []
for part in parts_raw:
    part = part.strip('{}')
    p = part.split(',')
    part_dict = {}
    for i in p:
        key, value = i.split('=')
        part_dict[key] = int(value)
    parts.append(part_dict)



def resolve_workflow(workflow: str, part: dict):
    if workflow == "A":
        return True
    if workflow == "R":
        return False
    
    for rule in workflows[workflow]:
        if rule.attr is None:
            return resolve_workflow(rule.go_to_workflow, part)
        else: 
            attr = part[rule.attr]
            if operation_mapping[rule.operation](attr, rule.value):
                 return resolve_workflow(rule.go_to_workflow, part)
            else:
                continue
    raise Exception("No rule found")

score = 0

for part in parts:
    if resolve_workflow("in", part):
        score += sum(part.values())

print(score)




# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}