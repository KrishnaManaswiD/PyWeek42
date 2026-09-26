# this implements the deck for the game which is a collection of cards
# we may not need a deck - just spawn cards based on the game state. 

import random

from modules.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        # TODO: add cards to the deck
        pass


    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self):
        # returns the top card and removes it from the deck
        if len(self.cards) == 0:
            return None
        return self.cards.pop() 


    def deal_multiple(self, num_cards):
        # returns a list of cards and removes them from the deck
        dealt_cards = []
        for _ in range(num_cards):
            card = self.deal()
            if card is not None:
                dealt_cards.append(card)
            else:
                break
        return dealt_cards