import numpy as np
import random
"""
Board class represent the chess board
N is the number of queens and the size of the board NxN
k is the last digit of the student number - 8
l is the penultimate digit of the student number - 7
The fixed queen will be placed in the position (8mod8+1, 7mod8+1)
To adjust k and l for indexing I will remove the "+ 1"
"""
class Board:

    def __init__(self, N, k, l):
        self.grid = np.array([[0]*N]*N)
        self.k = k - 1
        self.l = l - 1
        # placing fixed queen
        self.grid[l%N][k%N] = 2

    def place_queens(self):
        for i in range(8):
            if i == self.k:
                continue
            else:
                temp = random.randint(0,7)
                self.grid[temp][i] = 1


board = Board(8, 8, 7)
board.place_queens()
print(board.grid)