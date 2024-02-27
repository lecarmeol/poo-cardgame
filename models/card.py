SUITS = ['2', '3','4','5','6',
         '7','8','9','10','V','D','R','A']
RANK = ['Pique', 'Coeur', 'Carreau', 'Trefle']


class Cards:
    """A standard card, defined by a suit and rank"""
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.is_face_up = False