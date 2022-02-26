import numpy as np
import random

"""
Board class represent the chess board
N is the number of queens and the size of the board NxN
k is the last digit of the student number - 8
l is the penultimate digit of the student number - 7
The fixed queen will be placed in the position (8mod8+1, 7mod8+1)
To adjust k and l for indexing I will remove the "+ 1"
To highlight the queen I wil assign it the value 2
"""
class Board:

    def __init__(self, N, k, l):
        self.grid = np.array([[0]*N]*N)
        self.N = N
        self.k = k % N
        self.l = l % N
        # placing fixed queen
        self.grid[self.l][self.k] = 2

    def place_queens(self):
        for i in range(8):
            if i == self.k:
                continue
            else:
                temp = random.randint(0,7)
                self.grid[temp][i] = 1

    """
    Heuristic function that I will be using to score the board
    """
    @property
    def heuristic(self):
        pass
    
    """
    Returns the tile of the lowest heuristic tile on the board aka the best move
    """
    @property
    def tile(self):
        pass
    
    """
    Function to move a specified "queen" to a specified coordinate (coords)
    """
    def move(self):
        pass

    """
    Function used to check the rows in the grid for possible attacks
    """
    def check_rows(self):
        attacks = 0
        # loop through rows
        for i in range(8):
            temp = list(self.grid[i]).count(1) + list(self.grid[i]).count(2)
            if temp > 1:
                attacks += temp - 1
         
        return attacks

    """
    Function used to check the colums in the grid for possible attacks
    """
    def check_cols(self):
        attacks = 0
        for i in range(8):
            temp = []
            # adding all the elements in a column to a list
            for j in range(8):
                temp.append(self.grid[j][i])

            queens = temp.count(1) + temp.count(2) 
            if queens > 1:
                attacks += queens - 1

        return attacks 

    
    """
    Function used to check the diagonals in the grid for possible attacks
    """
    def check_diags(self):
        attacks = 0
        # checking the diagonal according to this slash \
        for i in range(-8,8):
            temp = list(np.diagonal(self.grid, i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
        
        # checking the diagonal according to this slah /
        for i in range(-8,8):
            temp = list(np.diagonal(np.fliplr(self.grid),i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
                
        return attacks
    
    
    #All functions below this comment are for testing purposes :)
    """
    Function to count the number of queens on the board
    """
    def count_queens(self):
        queens = 0
        for i in range(8):
            for j in range(8):
                if self.grid[j][i] != 0:
                    queens += 1
        return queens

    """
    Function to fill the first row with queens and the rest blank
    """
    def populate_board(self):
        for i in range(8):
            for j in range(8):
                self.grid[j][i] = 0

        self.grid[0] = [1]*8

    def move_queen(self, queen, coords):
        self.grid[queen[1]][queen[0]] = 0
        self.grid[coords[1]][coords[0]] = 1

    @property
    def pprint(self):
        for i in self.grid:
            print(i)

board = Board(8, 8, 7)
board.populate_board()
board.move_queen((1,0),(6,1))
board.move_queen((2,0),(5,2))
board.pprint

print(board.check_diags())