import numpy as np

class board():
    def __init__(self, size):
        self.size = size

    def print_board(self):
        board = np.zeros((self.size,self.size))
        return print(board)
    
my_board = board(10)
my_board.print_board()