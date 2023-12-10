import math
from itertools import compress
from math import lcm
import re


class Tree:
    reference = {}
    def __init__(self, name, left, right):
        self.reference[name] = self
        self.name = name
        self.left = left
        self.right = right


    def L(self):
        return self.reference[self.left]

    def R(self):
        return self.reference[self.right]

    def ends_with_z(self):
        return self.name[-1] == 'Z'

    def ends_with_a(self):
        return self.name[-1] == 'A'

def find_cycle(name, instructions):
    current = Tree.reference[name]
    seen = {}
    i = 0

    ends_with_z = []
    while (key := (current, wrap_index := i%len(instructions))) not in seen:
        seen[key] = i
        if current.ends_with_z():
            ends_with_z = i
        inst = instructions[wrap_index]
        current = getattr(current, inst)()
        i += 1

    return i-seen[key], ends_with_z, seen[key]

with open('input', 'r') as f:
    instructions, nodes = f.read().split('\n\n')
    

starts = []
for node in nodes.splitlines():
    find  = re.fullmatch('(\w+) = \((\w+), (\w+)\)', node)
    if len(find.groups()) != 3:
        raise ValueError
    me, left, right = find.groups()
    if Tree(me, left, right).ends_with_a():
        starts.append(me)
        

cycles = [find_cycle(start, instructions) for start in starts]

i = max(cycles)[1]
print(cycles)
while not all(expr:=[((i-offset) % cycle)+offset == true for cycle, true, offset in cycles]):
    i += lcm(*[x[0] for x in compress(cycles, expr)])
print(i)