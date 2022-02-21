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
        self.k = k
        self.l = l
    
    @property
    def solved(self):
        pass
    
    @property
    def manhattan(self):
        pass
    
    @property
    def attack(self):
        # Checking each row for multiple queens returns the row with multiple queens

        for row in self.board:
            if row.count(1) > 1:
                return row.index(1)
    
    def shuffle(self):
        for row in self.board:
            i = random.randint(0,7)
            row[i] = 1
    
    def pprint(self):
        for row in self.board:
            print(row)



board = Board(8, 8, 7)
board.shuffle()
board.pprint()
    
        

