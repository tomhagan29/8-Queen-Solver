import numpy as np

class Board:
    def __init__(self, N, k, l):
        self.grid = np.matrix([[0]*N]*N)
        
    @property
    def solved(self):
        pass
    
    @property
    def heuristic(self):
        pass
    
    
"""
k is the last digit of my student number - 8
l is the penultimate digit of my student number - 7
The fixed queen needs to placed on the tile ((k mod 8) + 1, (l mod 8) + 1) 
Therefore the fixed queen would be placed where the 1 is:
   0 1 2 3 4 5 6 7
0 [0 0 0 0 0 0 0 0]
1 [0 0 0 0 0 0 0 0]
2 [0 0 0 0 0 0 0 0]
3 [0 0 0 0 0 0 0 0]
4 [0 0 0 0 0 0 0 0]
5 [0 0 0 0 0 0 0 0]
6 [0 0 0 0 0 0 0 1]
7 [0 0 0 0 0 0 0 0]
 
"""
k = (8 % 8) + 1
l = (7 % 8) + 1

board = Board(8, k, l)
print(board.grid)


