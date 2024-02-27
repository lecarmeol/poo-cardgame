"""Entry point."""

from models.deck import Deck
from controllers.Dealer import Dealer
from views.View import View


def main():
    deck = Deck()
    view = View()
    game = Dealer(deck, view)
    game.run()


if __name__ == "__main__":
    main()
