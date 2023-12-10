import re
from itertools import pairwise,accumulate
from functools import reduce

numbers = '-?\d+'

with open('input', 'r') as f:
    lines = f.read().splitlines()

s_end = 0
s_beg = 0
for line in lines:
    progression = list(map(int, re.findall(numbers, line)))
    ps = [progression]
    while(not all([x == 0 for x in progression])):
        progression = [b - a for (a,b) in pairwise(progression)]
        ps.append(progression)
    s_end += sum([x[-1] for x in ps])
    s_beg += reduce(lambda a,b: b-a, reversed([x[0] for x in ps]))
        
print(s_end)
print(s_beg)
