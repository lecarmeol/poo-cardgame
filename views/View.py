REPLY_T = ["Y", "y", "Yes", "YES"]
REPLY_F =["N", "n", "No", "NO"]
class View:
        """Interface for a Cardgame"""
        def prompt_number_of_player(self, max_nb_player):
                """Choose number of player"""
                number_of_player = -1
                while number_of_player == -1 or number_of_player > max_nb_player :
                        number_of_player = int(input("Choose number of player (" + str(max_nb_player) + "max) :"))
                return number_of_player

        def prompt_for_player(self):
                """Name of player"""
                name = None
                while name is None :
                        name = input("Enter you name :")
                return name

        def prompt_for_flip(self):
                """Flip or not"""
                flip = None
                while True:
                        try:
                                flip = input("Flip ? [Y/N]")
                                REPLY_T.index(flip)
                                return True
                        except ValueError:
                                try:
                                        REPLY_F.index(flip)
                                        return False
                                except ValueError:
                                        pass

        def prompt_for_new_game(self):
                """New game or not"""
                new_game = None
                while True:
                        try:
                                new_game = input("New Game ? [Y/N]")
                                REPLY_T.index(new_game)
                                return True
                        except ValueError:
                                try:
                                        REPLY_F.index(new_game)
                                        return False
                                except ValueError:
                                        pass

        def show_player_hand(self, result):
                """result = Player hand"""
                print("Hand :" + result)

        def show_winner(self, winner_name):
                """winner_name = Winner name"""
                print("Winner is :" + winner_name)