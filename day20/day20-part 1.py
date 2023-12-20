# Advent of Code 2023 - Day 20
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
# import pandas as pd
# import numpy as np
# import re
from rich import print
from typing import Literal
from collections import defaultdict, deque
#with open("./day20/example.txt") as f:
with open("./day20/input.txt") as f:
    content = f.read().split("\n")


class Module:
    def __init__(self, id: str, module_type: Literal['flipflop','conjunction', 'broadcaster'], send_to: list[str]):
        self.id = id
        self.module_type = module_type
        self.send_to = send_to
        self.power_state = False
        self.previous_pulse = {}

    def receive_pulse(self, pulse: int, from_module: str) -> list[tuple[str, int, str]]:
        """Returns a list of tuples containing the receiver id and the pulse, and the sender id """
        to_send = []

        if self.module_type == 'flipflop':
            if pulse == -1:
                self.power_state = not self.power_state
                for module in self.send_to:
                    to_send.append((module, 1 if self.power_state else -1, self.id))

        elif self.module_type == 'conjunction':
            self.previous_pulse[from_module] = pulse
            send_pulse = 1 if not all([x == 1 for x in self.previous_pulse.values()]) else -1
            for module in self.send_to:
                to_send.append((module, send_pulse, self.id))
        
        elif self.module_type == 'broadcaster':
            for module in self.send_to:
                to_send.append((module, pulse, self.id))
        else:
            raise NotImplementedError
        return to_send

    def add_input(self, input_id: str):
        self.previous_pulse[input_id] = -1
    
    def __repr__(self):
        return f"Module {self.id}, P: {self.power_state}, Prev: {self.previous_pulse} "


modules = {}
for line in content:
    m, to = line.split(" -> ")
    if m.startswith("%"):
        m_id = m[1:]
        m_type = 'flipflop'
    if m.startswith("&"):
        m_id = m[1:]
        m_type = 'conjunction'
    if m.startswith("broadcaster"):
        m_id = m
        m_type = 'broadcaster'
    to = to.split(", ")
    modules[m_id] = Module(m_id, m_type, to)

for id, module in modules.items():
    for send_to in module.send_to:
        if send_to in modules:
            modules[send_to].add_input(id)

q = deque()
low_pulse = 0
high_pulse = 0
for i in range(1000):
    button_pulse = ('broadcaster', -1, 'button')
    q.append(button_pulse)
    while q:
        module, pulse, sender = q.popleft()
        if pulse == -1:
            low_pulse += 1
        else:
            high_pulse += 1

        if module in modules:
            to_send = modules[module].receive_pulse(pulse, sender)
            for send in to_send:
                q.append(send)

print(low_pulse*high_pulse)

# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output