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
                    board[count][all+1] = 11
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
    
    # def zero_sets(self, answers):
    #     translations = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    #     zeros = []
    #     zero_check =[]
    #     zeros_subset = set()
    #     for row in range(self.size+1):
    #         if row > 0:
    #             for column in range(self.size + 1):
    #                 column > 0
    #                 if answers[row][column] == 0:
    #                     zeros_subset.add((row,column))
    #                     zero_check.append((row,column))
    #                     count = 1
    #                     run = True
    #                     while run:
    #                         for row1, column1 in translations:
    #                             row2 = row + row1 * count
    #                             column2 = column + column1 * count
    #                             print(count)
    #                             if 0 <= row2 < self.size + 1 and 0 <= column2 < self.size + 1:
    #                                 print('---------------')
    #                                 if answers[row2][column2] == 0 and (row2,column2) not in zero_check:
    #                                     zeros_subset.add((row2,column2))
    #                                     zero_check.append((row2,column2))
    #                             else:
    #                                 print("break out")
    #                                 run = False
    #                             print("end of line")
    #                             count += 1
    #                 else:
    #                     continue
    #         zeros.append(zeros_subset)
    #     return zeros


class sweeper():

    def __init__(self,row,column,board, bomb_location, answers):
        self.row = int(row)
        self.column = int(column)
        self.board = board
        self.bomb_location = bomb_location
        self.check = (self.row, self.column)
        self.answers = answers

    def board_update(self):
        self.board[self.row][self.column] = self.answers[self.row][self.column]

    def open_empty_space(self, zero_row, zero_column):
        translations = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        #reveal all zeros around a selected zero
        self.board_update()
        for x, y in translations:
            new_row = zero_row + x
            new_column = zero_column + y
            self.row = new_row
            self.column = new_column
            if self.answers[new_row][new_column] != 11:
                self.board_update()

    def zero_reveal(self, zero_row, zero_column):
        tag = 0 
        # row = None 
        # column = None
        frame = (zero_row,zero_column,tag)
        reference = [frame]
        translations = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        #reveal all zeros around a selected zero
        # self.board_update()
        for x, y in translations:
            new_row = zero_row + x
            new_column = zero_column + y
            self.row = new_row
            self.column = new_column
            if self.answers[new_row][new_column] == 0:
                # self.board_update()
                frame = (new_row,new_column,tag)
                reference.append(frame)
            elif 0 < self.answers[new_row][new_column] < 11:
                frame = (new_row,new_column,1)
                reference.append(frame)
        ### now iterate through all the points that are now stored in the reference array 


    def check_bomb(self):
        if self.check in self.bomb_location:
            ## show revealed board
            print("You hit a mine! You Died!")
            print(self.answers)
            return False
        elif self.answers[self.row][self.column] == 0:
            print("check the next square!")
            self.open_empty_space(self.row,self.column)
            print(self.board)
            return True
        else:
            print("check the next square!")
            self.board_update()
            print(self.board)
            print(self.answers)
            return True

    def check_win(self):
        if np.all(self.board == self.answers):
            print("You Win!")
            print(self.answers)
            return False
        return True

def play_mineSweeper(size, bombs):  
    my_board = board(size,bombs)
    theBoard = my_board.build_board()
    print(theBoard)
    bomb_location = my_board.lay_bombs()
    answers = my_board.board_answer(bomb_location)
    print(answers)
    # zero_set = my_board.zero_sets(answers)
    # print(zero_set)
    check_move = True
    while check_move == True:
        row = input("Choose a row: ")
        column = input("Choose a column: ")
        player = sweeper(row,column,theBoard,bomb_location,answers)
        check_move = player.check_bomb()
        check_move = player.check_win()


play_mineSweeper(2,1)