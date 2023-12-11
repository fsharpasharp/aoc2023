from math import ceil
import sys
from itertools import starmap


with open('input', 'r') as f:
    lines = f.read().splitlines()


class Grid:
    def __init__(self, grid):
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    self.start = (i,j)
                    return
    
    def value(self, y, x):
        return self.grid[y][x]

    def walk(self, coord, prev=None):
        y, x = coord
        if self.value(y,x) =='S':
            return self.find_start(y,x)
        a, b = self.walk_internal(y, x)
        if a == prev:
            return b
        else:
            return a

    def walk_internal(self, y, x):
        value = self.value(y,x)
        match value:
            case '|':
                return (y-1,x), (y+1,x)
            case '-':
                return (y,x-1), (y,x+1)
            case 'L':
                return (y-1,x), (y,x+1)
            case 'J':
                return (y-1,x), (y,x-1)
            case '7':
                return (y,x-1), (y+1,x)
            case 'F':
                return (y+1,x), (y,x+1)

    def find_start(self, y, x):
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i)+abs(j) != 1:
                    continue
                if (y,x) not in self.walk_internal(y+i, x+j):
                    continue
                return y+i, x+j



g = Grid(lines)
print(g.start)
prev, cur = g.start, g.walk(g.start)
i = 0 
boundary = set(prev)
while(cur != g.start):
    boundary.add(cur)
    prev, cur = cur, g.walk(cur, prev)
    i += 1
print(ceil(i/2))