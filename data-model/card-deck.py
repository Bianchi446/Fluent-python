

import collections
from random import choice

Card =  collections.namedtuple('Card', ['rank', 'suit'])   # Rank and suit are counted as attributes

class FrenchDeck :
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('6', 'Diamond')
print(beer_card)

deck = FrenchDeck()

print(len(deck))

print(choice(deck))

# Our FrenchDesk class support data slicing

print(deck[:3])
print(deck[:5])

# It's also iterable 

#for card in deck:
    #print(card)


# We can use the spades_high method to sort the cards

suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_value) + suit_value[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)


