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

    def __str__(self):
        return self.name

with open('input', 'r') as f:
    instructions, nodes = f.read().split('\n\n')

for node in nodes.splitlines():
    find  = re.fullmatch('(\w+) = \((\w+), (\w+)\)', node)
    if len(find.groups()) != 3:
        raise ValueError
    me, left, right = find.groups()
    Tree(me, left, right)

current = Tree.reference['AAA']
i = 0
while str(current) != 'ZZZ':
    inst = instructions[i%len(instructions)]
    current = getattr(current, inst)()
    i += 1
print(current, i)

