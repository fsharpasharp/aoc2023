import re

with open('input', 'r') as f:
    lines = f.read().split('\n\n')


seeds = list(map(int, re.findall('\d+', lines[0])))
for line in lines[1:]:
    matches = re.findall('\d+ \d+ \d+', line)
    for i, seed in enumerate(seeds):
        for match in matches:
            y, x, width = map(int, match.split())
            if x <= seed < x+width:
                seeds[i] = seed - x + y
                break
print(min(seeds))

