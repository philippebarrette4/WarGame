import random
import config
from src.Card import Card

class Deck:

    # Class constructor
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in config.suits:
            for rank in config.ranks:
                # Assumes the Card class has already been defined
                self.all_cards.append(Card(suit,rank))

    # This function shuffles the deck randomly
    def shuffle(self):
        # Doesn't return anything
        random.shuffle(self.all_cards)

    # This function returns a card of the deck
    def deal_one(self):
        return self.all_cards.pop()