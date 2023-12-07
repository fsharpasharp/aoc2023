import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

def safe(y, x, lines):
    if not (0 <= y < len(lines)):
        return True
    if not (0 <= x < len(lines[0])):
        return True
    return lines[y][x] in '.0123456789'

s = 0
for y, line in enumerate(lines): 
    matches = re.finditer('\d+', line)
    for match in matches:
        width = len(match.group())
        if all([safe(y + y_delta, match.start()+x_delta, lines) for y_delta in range(-1,2) for x_delta in range(-1,width+1)]):
            continue
        s += int(match.group())


print(s)
