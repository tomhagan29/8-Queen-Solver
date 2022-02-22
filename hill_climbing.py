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
    
    

# k is the last digit of my student number - 8
# l is the penultimate digit of my student number - 7
k = (8 % 8) + 1
l = (7 % 8) + 1



