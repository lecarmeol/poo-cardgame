
class Players:

    def __init__(self):

        self.name_players = []
        self.nombre_of_player = 0

    def playernomber(self):
        nomber = 0
        while(nomber > 5):
            nomber = float(input("Enter the number of players : "))
            self.nombre_of_player = nomber

    def nameplayers(self):
        n = 0
        for i in range(self.nombre_of_player):
            new_players = input("Name of players ",n, " : ")
            self.name_players.append(new_players)
            n += 1
