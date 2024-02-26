REPLY = ["Y", "y", "Yes", "YES", "N", "n", "No", "NO"]
class View:
        """Interface for a Cardgame"""
        def prompt_number_of_player(self):

        def prompt_for_player(self):
                """Name of player"""
                name = None
                while name is None :
                        name = input("Enter you name :")
                return name

        def prompt_for_flip(self):
                """Flip or not"""
                flip = None
                while flip is not REPLY :
                        flip = input("Flip ? [Y/N]")
                return flip

        def prompt_for_new_game(self):
                """New game or not"""
                new_game = None
                while new_game is not REPLY :
                        new_game = input("New Game ? [Y/N]")
                return new_game

        def show_player_hand(self, result):
                """result = Player hand"""
                print("Hand :" + result)

        def show_winner(self, winner_name):
                """winner_name = Winner name"""
                print("Winner is :" + winner_name)