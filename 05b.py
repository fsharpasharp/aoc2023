import re

with open('input', 'r') as f:
    lines = f.read().split('\n\n')


def DFS(a, b, intervals, index=0, depth=0):
    if a >= b:
        return []
        
    if depth == len(intervals):
        return [a]

    if index == len(intervals[depth]):
        return DFS(a,b, intervals, 0, depth+1)


    results = []

    y, x1, width = intervals[depth][index]
    x2 = x1+width
    if a < x2 and x1 < b:
        left = max(x1, a)
        right = min(b, x2)
        # Inside
        results.extend(DFS(left-x1+y, right-x1+y, intervals, 0, depth+1))

        # Part overlapping right
        results.extend(DFS(x2, b, intervals, index+1, depth))
        # Part overlapping left
        results.extend(DFS(a, x1, intervals, index+1, depth))
    else:
        results.extend(DFS(a, b, intervals, index+1, depth))
    return results



seeds = re.findall('\d+ \d+', lines[0])
intervals_outer = []
for line in lines[1:]:
    matches = re.findall('\d+ \d+ \d+', line)
    intervals = []
    for match in matches:
        y, x, width = map(int, match.split())
        intervals.append((y,x,width))
    intervals_outer.append(intervals)

minimal = float('inf')
for seed_interval in seeds:
    a, width = map(int, seed_interval.split())
    minimal = min(minimal, min(DFS(a, a+width, intervals_outer)))
    
print(minimal)

