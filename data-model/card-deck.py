# Example : The __len__ and __getitem__  special methods


import collections 

Card = collections.namedtuple('Card', ['rank', 'suit'])
 
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11 )] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                          for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position] 


beer_card = Card("7", "diamond")
print(beer_card)

    # checking the lenght of FrenchDeck class

deck = FrenchDeck()    
len(deck)

    # Example 2 : Making a random choice of cards 

from random import choice 

choice(deck)

    # Example 3 : Sort the ranking cards 

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value + len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)



# More uses of special methods 

# 1. emulating numeric types
# 2. String representation of objects
# 3. Boolean value of an object
# 4. Implementing collections
