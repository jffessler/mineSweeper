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
        return board
    
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
        translations = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        board = np.zeros((self.size + 1, self.size + 1))
        for index in range(self.size+1):
            board[0][index] = index
            board[index][0] = index
        for mine in bomb_locations:
            row = mine[0]
            column = mine[1]
            board[row][column] = 11
        for row1 in range(self.size + 1):
            if row1 > 0:
                for column1 in range(self.size + 1):
                    if column1 > 0:
                        if board[row1][column1] == 11:
                            continue
                        else:
                            num_of_bombs = 0
                            for row,column in translations:
                                new_row = row1 + row
                                new_column = column1 + column
                                if new_row < self.size + 1 and new_column < self.size + 1:
                                    if board[new_row][new_column] == 11:
                                        num_of_bombs += 1

                            board[row1][column1] = num_of_bombs
        return board

class sweeper():

    def __init__(self,row,column,board, bomb_location, answers):
        self.row = int(row)
        self.column = int(column)
        self.board = board
        self.bomb_location = bomb_location
        self.check = (int(self.row), int(self.column))
        self.answers = answers

    def board_update(self):
        self.board[self.row][self.column] = self.answers[self.row][self.column]

    def check_bomb(self):
        print(self.check)
        
        if self.check in self.bomb_location:
            ## show revealed board
            print("You hit a mine! You Died!")
            print(self.answers)
            return False
        else:
            print("check the next square!")
            self.board_update()
            print(self.board)
            return True

def play_mineSweeper(size, bombs):  
    my_board = board(size,bombs)
    theBoard = my_board.build_board()
    print(theBoard)
    bomb_location = my_board.lay_bombs()
    # print(bomb_location)
    answers = my_board.board_answer(bomb_location)
    print(answers)
    check_move = True
    while check_move == True:
        row = input("Choose a row: ")
        column = input("Choose a column: ")
        player = sweeper(row,column,theBoard,bomb_location,answers)
        check_move = player.check_bomb()
        # break

play_mineSweeper(10,10)