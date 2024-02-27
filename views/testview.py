from views.View import View

class TestView(View):
    def __init__(self, nb_of_play=1):
        super().__init__()
        self.player_base_name = "player "
        self._player_count = 0
        self.nb_of_play = nb_of_play
        self._current_play = 0

    def prompt_number_of_player(self, max_nb_player):
        self.player_count = 0
        return max_nb_player
    
    def prompt_for_player(self):
        self._player_count +=1
        return self.player_base_name + str(self._player_count)
    
    def prompt_for_flip(self):
        return True
    
    def prompt_for_new_game(self):
        self._current_play += 1
        return self._current_play <= self.nb_of_play