import random
from models.card import RANKS, SUITS, Cards


class Deck:
    """Define 52 cards deck"""

    def __init__(self):
        self.cardlists = []
        for rank in RANKS:
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
