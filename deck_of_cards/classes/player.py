from .deck import Deck

deck = Deck()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def playerCard(self):
        pass
    # Find a way to pop a card out of their self.hand list and put onto the table