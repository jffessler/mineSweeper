import numpy as np
import random as rand


class board():
    def __init__(self, size,num_bombs):
        self.size = size
        self.num_bombs = num_bombs

    def build_board(self):
        count = 1
        board = np.zeros((self.size+1,self.size+1))
        for index in range(self.size+1):
            board[0][index] = index
            board[index][0] = index
            for all in range(self.size):
                if count < self.size+1:
                    board[count][all+1]=None
            count += 1
        return print(board)
    
    def lay_bombs(self):
        bombs = self.num_bombs
        laid_bombs = []
        for x in range(bombs):
            location = [None, None]
            while location not in laid_bombs:
                location = [rand.randint(1,self.size+1),rand.randint(1,self.size+1)]
                laid_bombs.append(location)
        return laid_bombs



def play_mineSweeper(size, bombs):  
    my_board = board(size,bombs)
    my_board.build_board()
    print(my_board.lay_bombs())
    while True:
        row = input("Choose a row: ")
        column = input("Choose a column: ")
        print(row)
        print(column)
        break

play_mineSweeper(10,10)