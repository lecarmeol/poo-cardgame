import random
from models.card import RANK, SUITS, Cards


class Deck:
    """Allows all cards to be shuffled and drawn at random"""

    def __init__(self):
        self.cardlists = []
        for rank in RANK:
            for suit in SUITS:
                card = Cards(suit, rank)
                self.cardlists.append(card)
        self.shuffle()

    def shuffle(self):
        """Shuffle all cards"""
        random.shuffle(self.cardlists)


    def draw_card(self):
        """Take the first card and remove it from the list"""
        return self.cardlists.pop()
