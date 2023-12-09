from operator import itemgetter
from collections import Counter

with open('input', 'r') as f:
    lines = f.read().splitlines()

class Hand:
    card_strength = {k: v for v, k in enumerate('J23456789TQKA')}

    def reg_strength(self):
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

    def strength(self):
        '''
        0-6 strength values
        0: HIGH CARD 1 card used
        1: PAIR 2 cards used
        2: TWO PAIRS 4 four cards used
        3: THREE OF A KIND 3 cards used
        4: FULL HOUSE 5 cards used
        5: FOUR OF A KIND 4 cards used
        6: FIVE OF A KIND 5 cards used
        '''
        if self.js == 5:
            return 6
        match (self.reg_strength(), self.js):
            case (x, 0):
                return x
            case (6, _):
                return 6
            case (5, 1):
                return 6
            case (3, 2):
                return 6
            case (1, 3):
                return 6
            case (0, 4):
                return 6

            case (0, 3):
                return 5
            

            case (0, 2):
                return 3
            case (1, 2):
                return 5

            case (0, 1):
                return 1
            case (1, 1):
                return 3
            case (2, 1):
                return 4
            case (3, 1):
                return 5

            case x:
                print(x)
                raise ValueError

    def __init__(self, hand, value):
        self.hand = hand
        filtered_hand = filter(lambda x: x != 'J', hand)
        self.hand_type = list(map(itemgetter(1), Counter(filtered_hand).most_common(2)))
        self.js = self.hand.count('J')
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