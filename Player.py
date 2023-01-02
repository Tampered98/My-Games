import random
import math

class player:
    def __init__(self,letter):
        # letter is x or o
        self.letter=letter

        # we want all the players to get their next move given a game
        def get_move(self,game):
            pass

class randomcomp(player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square

class human(player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+'\'s turn.input move(0-9):')
#here we are going to check that this is a correct value by trying to cast
#it is an integer, and if it is not, then we say its valid
#if that spot is not available on the board, we also say its invalid
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True #if these are successful, then yayy!
            except ValueError:
                print('Invalid square.Try agian.')

        return val


