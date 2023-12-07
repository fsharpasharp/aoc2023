from math import prod
from collections import defaultdict
import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

wins = defaultdict(int)
times, distances = [list(map(int, re.findall('\d+', line))) for line in lines]
for i, (available_time, target_distance) in enumerate(zip(times, distances)):
    for j in range(available_time):
        if j*(available_time-j) > target_distance:
            wins[i] += 1
print(prod(wins.values()))

# Solving b is finding the interval between the roots of target_distance=x*(available_time-x)