SUITS = ['2', '3','4','5','6',
         '7','8','9','10','V','D','R','A']
RANK = ['Pique', 'Coeur', 'Carreau', 'Trefle']


class Cards:
    """Allows all cards to be shuffled and drawn at random"""
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.is_face_up = False