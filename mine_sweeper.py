import numpy as np

class board():
    def __init__(self, size):
        self.size = size

    def print_board(self):
        board = np.zeros((self.size+1,self.size+1))
        for index in range(self.size+1):
            board[0][index] = index
            board[index][0] = index
            if index < 10:
                board[index+1][index+1] = None
        return print(board)
    
my_board = board(10)
my_board.print_board()