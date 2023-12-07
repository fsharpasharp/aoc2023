from collections import Counter

with open('input', 'r') as f:
    lines = f.read().splitlines()

class Hand:
    card_strength = {k: v for v, k in enumerate('23456789TJQKA')}

    def strength(self):
        '''
        0-6 strength values
        '''
        if len(self.hand_type) == 1:
            return 6

        a, b = self.hand_type
        if a == 3 and b != 2:
            return 3
        if a == 2 and b == 2:
            return 2
        if a == 2:
            return 1
        if a == 1:
            return 0

        return a+1

    def __init__(self, hand, value):
        self.hand = hand
        self.hand_type = list(map(lambda x: x[1], Counter(hand).most_common(2)))
        self.value = value

    def __lt__(self, other):
        our_strength = self.strength()
        their_strength = other.strength()
        if our_strength < their_strength:
            return True
        if our_strength > their_strength:
            return False
        for our, their in zip(self.hand, other.hand):
            our_strength = Hand.card_strength[our]
            their_strength = Hand.card_strength[their]
            if our_strength < their_strength:
                return True
            if our_strength > their_strength:
                return False
        return False

    def __str__(self):
        return f'{self.hand} - {self.hand_type} - {self.strength()}'



hands = []
for line in lines:
    hand, value = line.split()
    hands.append(Hand(hand, int(value)))

s = 0
for i, h in enumerate(sorted(hands)):
    s += h.value*(i+1)

print(s)