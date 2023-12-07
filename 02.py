from math import prod
import re

with open('input', 'r') as f:
    lines = f.read().splitlines()



def game_possible(line):
    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    matches = re.findall('\d+ \w+', line)
    for match in matches:
        n, color = match.split()
        if int(n) > cubes[color]:
            return False
    return True

def game_power_sum(line):
    matches = re.findall('\d+ \w+', line)
    cube = {}
    for match in matches:
        n, color = match.split()
        cube[color] = max(cube.get(color, -1), int(n))
    return prod(cube.values())
            
print(sum([int(re.findall('Game (\d+)', line)[0]) for line in lines if game_possible(line)]))
print(sum(game_power_sum(line) for line in lines))