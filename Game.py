import time
from Player import human,randomcomp

class TTT:
    def __init__(self):
        # now lets create a board
         self.board=[' ' for _ in range(9)] #single list ot rep 3x3 board
         self.current_winner= None

    def print_board(self):
        # assiging numbers to each chance
        for row in[self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # specifying which number correspond to which spot
        #0| 1| 2 etc
        # in essence give me indeces of the rows of each of the rows
        number_board=[[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]
        # concatnate the stings
        for row in number_board:
            print('| '+' | '.join(row)+' |')
# Create the logic for the game
#     enumerate function essentially creates a list and assings a number --help in indexing=index,value (1,x)
    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot ==' ']
        # moves=[]
        # for (i,spot) in enumerate(self.board):
        #     ['x','x','z']---> [(0,'x'),(1,'x'),(2,'z')]
        #     if spot== ' ':
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board


    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        #if valid move, then make the move(assign square to letter)
        #then return true. if invalid, return false
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner= letter
            return True
        return False

# Create a function to check for the winner
    def winner(self,square,letter):
        #winner if 3 in a row anywhere
# row index
        row_ind = square//3
        row=self.board[row_ind*3 : (row_ind+1) *3]
        if all([spot==letter for spot in row]):
            return True

        #check the column next
        col_ind=square % 3
        col=[self.board[col_ind+i*3]for i in range(3)]
        if all([spot ==letter for spot in col]):
            return True

        # check in diagonal lastly
        #but only if the square is an even number(0,2,4,6,8)
        #there are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1=[self.board[i]for i in [0,4,8]] # left  to right
            if all([spot==letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in [2,4,6]] #right to left
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all these checks fails then we don't have a winner
        return False
def play(game,x_player,o_player,print_game=True):
    #retruns the winner of the game ! or none for a tie

    if print_game:
        game.print_board_nums()

    letter='x'
    #starting letter
    # iterate while thegame still has empty squares
    #we dont have to worry about winner beacuse we ll just retrn that
    #which breaks the loop
    while game.empty_squares():
        #get the move from the appropriate player
        if letter =='o':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)
        #define a function to make a move !

        if game.make_move(square,letter):
            if print_game:
                print(letter + f'makes a move to square{square}')
                game.print_board()
                print('') #just an empty line
            if game.current_winner:
                if print_game:
                    print(letter+' wins')
                return letter
            #after we made our move , we need to alternate letters
            letter='o' if letter == 'x' else 'x'
            # if letter=='x':
            #     letter='o'
            # else:
            #     letter='x'
        time.sleep(0.8)
        if print_game:
            print ('It\'s a tie!')


if __name__=='__main__':
    x_player=human('x')
    o_player=randomcomp('o')
    t=TTT()
    play(t,x_player,o_player,print_game=True)