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
        self.k = k % N
        self.l = l % N
        # placing fixed queen
        self.grid[self.l][self.k] = 2

    def place_queens(self):
        for i in range(7):
            temp = random.randint(0,7)
            self.grid[temp][i] = 1

    """
    Attacks is the heuristic function that I will be using to score the board
    """
    @property
    def attacks(self):
        pass
    
    """
    Returns the tile of the lowest heuristic tile on the board aka the best move
    """
    @property
    def tile(self):
        pass
    
    """
    Uses the tile function to get the best tile to lower heuristic and moves the queen in that column to the tile
    """
    def move(self):
        pass

    """
    Function used to check the rows in the grid for possible attacks
    """
    def check_row(self):
        pass

    """
    Function used to check the colums in the grid for possible attacks
    """
    def check_cols(self):
        pass
    
    """
    Function used to checkt the diagonals in teh grid for possible attacks
    """
    def check_diags(self):
        pass
    
    @property
    def pprint(self):
        for i in self.grid:
            print(i)

board = Board(8, 8, 7)
board.place_queens()
board.pprint
print(board.check_row())
