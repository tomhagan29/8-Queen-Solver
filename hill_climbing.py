import numpy as np

class Board:
    def __init__(self, N, k, l):
        self.grid = np.array([[0]*N]*N)
        self.fixed_queen = (k-1, l-1)
    
    @property
    def solved(self):
        return self.heuristic == 0
    
    @property
    def heuristic(self):
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
                self.grid[0][i] = 1
    
    
        
    
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
# print(board.grid)
# print(board.fixed_queen)


temp = np.array([[1,2],[3,4]])
print(temp)
