from models.card import *
from models.player import Player
from time import sleep


class Dealer:
    """Input: Deck,View"""
    def __init__(self, deck, view):
        self.deck = deck
        self.view = view
        self.players = []
        """Define the list of player"""

    def get_players(self, players):
        """Define the list of players
        input : players is a list of object player"""
        self.players = players

    def evaluate_game(self):
        """evaluate the winner and its best card
        return : the name of the winner (string),objet card"""

        best_card = Card(SUITS[0], RANKS[0])

        best_player_name = ''
        for player in self.players:

            for card in player.cards:

                if RANKS.index(card.rank) > RANKS.index(best_card.rank):
                    best_card = card
                    best_player_name = player.name

                if RANKS.index(card.rank) == RANKS.index(best_card.rank):
                    if SUITS.index(card.suit) > SUITS.index(best_card.suit):
                        best_card = card
                        best_player_name = player.name

        return best_player_name, best_card

    def rebuild_deck(self):
        for player in self.players:
            for card in player.cards:
                self.deck.cardlists.append(card)
        self.deck.shuffle()

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.cards.append(self.deck.draw_card())

    def run(self):
        while self.view.prompt_for_new_game():
            nb_of_player = self.view.prompt_number_of_player(5)
            for i in range(nb_of_player):
                player = Player(self.view.prompt_for_player())
                self.players.append(player)

            self.start_game()
            while not self.view.prompt_for_flip():
                sleep(1)

            for player in self.players:
                hand = []
                for card in player.cards:
                    card.is_face_up = True
                    hand.append(str(card))
                self.view.show_player_hand(str(hand))

            winner_name, best_card = self.evaluate_game()

            self.view.show_winner(winner_name)
            self.rebuild_deck()
