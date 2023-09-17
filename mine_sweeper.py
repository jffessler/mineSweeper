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
        laid_bombs = set()
        count = 0
        while count < bombs:
            row = rand.randint(1,self.size)
            col = rand.randint(1,self.size)
            if (row, col) not in laid_bombs:
                    laid_bombs.add((row, col))
                    count += 1
            else:
                continue
        return laid_bombs

    def board_answer(self, bomb_locations):
        count = 1
        board = np.zeros((self.size+1,self.size+1))
        # print('board: ', board)
        for index in range(self.size+1):
            board[0][index] = index
            board[index][0] = index
        for mine in bomb_locations:
            # print('mine: ', mine)
            row = mine[0]
            column = mine[1]
            board[row][column]=9
        for row1 in range(self.size+1):
            if row1 > 0:
                for column1 in range(self.size+1):
                    if column1 > 0:
                        if board[row1][column1] == 9:
                            board[row1][column1] = None
                        else:
                            num_of_bombs = 0
                            if board[row1-1][column1-1] == None:
                                num_of_bombs += 1
                            ### the other 7 cases for counting an adjacent bomb, maybe use a recursive function call to reduce number of cases and clutter
                            board[row1][column1] = 0
        return print(board)

class sweeper():

    def __init__(self,row,column,board, bomb_location):
        self.row = row
        self.column = column
        self.board = board
        self.bomb_location = bomb_location
        self.check = [int(self.row), int(self.column)]

    def check_bomb(self):
        print(self.check)
        if self.check in self.bomb_location:
            ## show revealed board
            return print("You hit a mine! You Died!")
        else:
            return print("check the next square!")


def play_mineSweeper(size, bombs):  
    my_board = board(size,bombs)
    my_board.build_board()
    bomb_location = my_board.lay_bombs()
    # print(bomb_location)
    my_board.board_answer(bomb_location)
    while True:
        row = input("Choose a row: ")
        column = input("Choose a column: ")
        player = sweeper(row,column,my_board,bomb_location)
        player.check_bomb()
        break

play_mineSweeper(10,10)