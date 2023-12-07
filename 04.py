import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

number = '\d+'
score = 0
extras = dict()
for i, line in enumerate(lines):
    left, right = line.split('|')
    winners = map(int, re.findall(number, left)[1:]) # skip the first number
    numbers = map(int, re.findall(number, right))
    intersection = set(winners) & set(numbers)

    number_of_scratch_cards = extras.get(i, 1)
    number_of_winners = len(intersection)
    for j in range (i+1, i+number_of_winners+1):
        extras[j] = extras.get(j, 1) + number_of_scratch_cards

    if intersection:
        score += 2 ** (number_of_winners-1)

scratch_cards = 0
for i in range(len(lines)):
    scratch_cards += extras.get(i, 1)

print(score)
print(scratch_cards)