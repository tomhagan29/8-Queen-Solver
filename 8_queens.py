import enum
import random

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        if self.parent == None:
            self.g = 0
        else:
            self.g = parent.g + 1
        
        @property
        def f(self):
            return self.g + self.h
        
        @property
        def h(self):
            return self.board.manhattan
        
            

class Solver:
    pass


"""
The N-Queens problem involves placing N queens on a NxN chess board so that no queen is able to take another.
Therefore, a Queen cannot be in the same column, row or diagonal to another.
Params: N (number of queens), k (last digit of student number), l (second last digit of student number)
Note: in the board, 0 represents blank space and 1 represents a queen
"""
class Board:
    def __init__(self, N, k, l):
        self.board = [[0]*N for _ in range(N)]
        self.k = (k % 8) + 1
        self.l = (l % 8) + 1
        # subtracting 1 if the index is out of bounds
        if self.k == 8:
            self.k = self.k -1
        elif self.l == 8:
            self.l = self.l - 1
    # returns True if the board is solved
    @property
    def solved(self):
        pass
    
    # returns the number of queens that can attack another queen
    @property
    def manhattan(self):
        pass
    
    # get list of all queens coordinates on the board
    @property
    def queens(self):
        queens = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    queens.append((i, j))
        return queens
    
    # place the fixed queen
    def fixed_queen(self):
        self.board[self.k][self.l] = 1

    # returns the positions of queens that are in the same column, row or diag
    def unsafe_queens(self):
        for queen in self.queens:
            pass
    
    # returns a list of tiles that aren't attackable by queens
    def safe_tiles(self):
        pass
    # populates board with queens in random positions
    def shuffle(self):
        for i in range(7):
            j = random.randint(0,7)
            self.board[i][j] = 1
    
    def pprint(self):
        for row in self.board:
            print(row)



board = Board(8, 8, 7)
board.shuffle()
board.fixed_queen()
board.pprint()

print(board.queens)
print(board.k)
print(board.l)
        

