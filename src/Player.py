class Player:

    def __init__(self, name):
        self.name = name
        # New player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # If it's a list (multiple cards) we extend
        # Because if not, append will append the list and
        # not each values
        # Would be like all_card = [1,2,3, [1,2,3]]
        # We want all_cards = [1,2,3,1,2,3]
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # If it's a single card
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."