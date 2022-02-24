import numpy as np

class Board:
    def __init__(self, N, k, l):
        self.grid = np.array([[0]*N]*N)
        self.fixed_queen = (l-1, k-1)
    
    @property
    def solved(self):
        return self.heuristic == 0
    
    """
    This function calculates the amount of attacks that are possible on the board
    """
    @property
    def manhattan(self):
        pass
    
    # places fixed queen on grid
    def place_fixed_queen(self):
        self.grid[self.fixed_queen[0]][self.fixed_queen[1]] = 1
    
    # populates each column with a queen except the fixed queen column
    def place_queens(self):
        for i in range(8):
            if i == self.fixed_queen[1]:
                continue
            else:
                self.grid[i][i] = 1
    
    # returns a list of tuples containing the coordinates of each queen
    @property
    def queens(self):
        queens = []
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == 1:
                    queens.append((i,j))
        return queens
    
    """
    Function to move a queen around the board
    queen is current location (x,y)
    pos is new position (x,y)
    """
    def move(self, queen, pos):
        self.grid[pos[0]][pos[1]] = 1
        self.grid[queen[0]][queen[1]] = 0
                
    def check_row(self, x):
        row = list(self.grid[x])
        out = row.count(1) - 1
        return out
    
    def check_col(self, y):
        col = []
        for i in range(8):
            col.append(self.grid[i][y])
        
        out = col.count(1) - 1
        
        if out < 1:
            return 0
        else:
            return out
    
    def check_diagonal(self, x, y):
        temp = list(np.diagonal(self.grid, (x-y)))
        return temp.count(1) - 1

"""
k is the last digit of my student number - 8
l is the penultimate digit of my student number - 7
The fixed queen needs to placed on the tile ((k mod 8) + 1, (l mod 8) + 1) = (1,8)
To match indexing of array I will subtract 1 - (0,7)
Therefore the fixed queen would be placed where the 1 is:
   0 1 2 3 4 5 6 7
0 [0 0 0 0 0 0 0 1]
1 [0 0 0 0 0 0 0 0]
2 [0 0 0 0 0 0 0 0]
3 [0 0 0 0 0 0 0 0]
4 [0 0 0 0 0 0 0 0]
5 [0 0 0 0 0 0 0 0]
6 [0 0 0 0 0 0 0 0]
7 [0 0 0 0 0 0 0 0]
 
"""
k = (8 % 8) + 1
l = (7 % 8) + 1

board = Board(8, k, l)
board.place_fixed_queen()
board.place_queens()
print(board.grid)
print(board.manhattan)