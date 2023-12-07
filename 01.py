import re
from itertools import chain

with open('input', 'r') as f:
    lines = f.read().splitlines()

def digits(line, part_one=False):
    value = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    if part_one:
        value = {}

    matches = []
    matches = chain(matches, re.finditer(r'\d', line))
    for key in value:
        matches = chain(matches, re.finditer(key, line))

    return [(match.start(), value.get(match.group(), match.group())) for match in matches]

for part in [True, False]:
    s = 0
    for line in lines:
        ds = digits(line, part)
        s += int(min(ds)[1] + max(ds)[1])
    print(s)