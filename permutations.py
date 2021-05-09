# Permutations - part of project
import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


def new_deck():
    return [
        '{:>2}{}'.format(*c)
        for c in itertools.product(itertools.chain(range(2, 11), FACE_CARDS), SUITS,)
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()


# Make a new deck, with the cards in order
deck = new_deck()
print('Initial deck:')
show_deck(deck)

# Deal 4 hands of 5 cards each.
hands = [[], [], [], []]
for i in range(5):
    for h in hands:
        h.append(deck.pop())


# Show the hands.
print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()


# Show the remaining deck.
print('\nRemaining deck:')
show_deck(deck)

# Example of OUTPUT:
# Initial deck:
#  2H  2D  2C  2S  3H  3D  3C  3S  4H  4D  4C  4S  5H
#  5D  5C  5S  6H  6D  6C  6S  7H  7D  7C  7S  8H  8D
#  8C  8S  9H  9D  9C  9S 10H 10D 10C 10S  JH  JD  JC
#  JS  QH  QD  QC  QS  KH  KD  KC  KS  AH  AD  AC  AS
#
# Hands:
# 1:  AS  KS  QS  JS 10S
# 2:  AC  KC  QC  JC 10C
# 3:  AD  KD  QD  JD 10D
# 4:  AH  KH  QH  JH 10H
#
# Remaining deck:
#  2H  2D  2C  2S  3H  3D  3C  3S  4H  4D  4C  4S  5H
#  5D  5C  5S  6H  6D  6C  6S  7H  7D  7C  7S  8H  8D
#  8C  8S  9H  9D  9C  9S
