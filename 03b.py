from collections import defaultdict
from math import prod
import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

def inside(y,x,lines):
    if not 0 <= y < len(lines):
        return False
    if not 0 <= x < len(lines[0]):
        return False

    return True

def find_stars(y, x, value, width, lines, star_map):
    for i in range(-1,2):
        for j in range(-1, width+1):
            new_y = y+i
            new_x = x+j
            if not inside(new_y, new_x,lines):
                continue
            if lines[new_y][new_x] == '*':
                star_map[(new_y,new_x)].append(value)

s = 0
star_map = defaultdict(list)
for y, line in enumerate(lines): 
    matches = re.finditer('\d+', line)
    for match in matches:
        width = len(match.group())
        find_stars(y, match.start(), int(match.group()), match.end()-match.start(), lines, star_map)

print(sum(map(prod,filter(lambda x: len(x) == 2, star_map.values()))))