import config

class Card:

    # Class constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = config.values[rank]

    # This function enable the possibility to print a Card object
    def __str__(self):
        return self.rank + " of " + self.suit