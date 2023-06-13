# Function that sorts the ranking of the FrenchDesk

import FrenchDesk

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):

    rank_values =FrenchDeck.ranks.index(card.rank)  
    return rank_values * len(suit_values) + suit_values[card.suit]


