import numpy as np
import random
from copy import deepcopy

"""
To Do
    - Implement tile heuristics and optimise moves to the best tile
"""


class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    @property
    def h(self):
        return self.board.heuristic
    
    @property
    def solved(self):
        return self.board.solved


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
        self.fixed_queen = (self.k,self.l)


    """
    Randomly populate the board with queens
    """
    def random_queens(self):
        for i in range(self.N):
            if i == self.k:
                continue
            else:
                temp = random.randint(0,self.N - 1)
                self.grid[temp][i] = 1


    """
    Heuristic function that I will be using to score the board
    """
    @property
    def heuristic(self):
        h = 0
        h += self.cols()
        h += self.rows()
        h += self.diags()
        return h


    """
    Returns true if there are no possible attacks on the board
    """
    @property
    def solved(self):
        return self.heuristic == 0


    """
    Function used to check the rows in the grid for possible attacks
    """
    def rows(self):
        attacks = 0
        # loop through rows
        for i in range(self.N):
            temp = list(self.grid[i]).count(1) + list(self.grid[i]).count(2)
            if temp > 1:
                attacks += temp - 1
         
        return attacks


    """
    Function used to check the colums in the grid for possible attacks
    """
    def cols(self):
        attacks = 0
        for i in range(self.N):
            temp = []
            # adding all the elements in a column to a list
            for j in range(self.N):
                temp.append(self.grid[j][i])

            queens = temp.count(1) + temp.count(2) 
            if queens > 1:
                attacks += queens - 1

        return attacks 

    
    """
    Function used to check the diagonals in the grid for possible attacks
    """
    def diags(self):
        attacks = 0
        # checking the diagonal according to this slash \
        for i in range(-self.N,self.N):
            temp = list(np.diagonal(self.grid, i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
        
        # checking the diagonal according to this slah /
        for i in range(-self.N,self.N):
            temp = list(np.diagonal(np.fliplr(self.grid),i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
                
        return attacks
    
    """
    Function to move "queen" to "coords" both are tuples (x,y)
    """
    def move(self, queen, coords):
        self.grid[queen[1]][queen[0]] = 0
        self.grid[coords[1]][coords[0]] = 1

    """
    Function that returns a list of all the possible moves that each queen can make within it's column
    Input coordinates of queen (x,y)
    """
    def actions(self, queen):
        tiles = []
        for i in range(self.N):
            if i == queen[1]:
                continue
            else:
                tiles.append((queen[0], i))
        return tiles

    @property
    def queens(self):
        queens = []
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[j][i] != 0:
                    queens.append((i,j))

        return queens
    
    @property
    def pprint(self):
        for i in self.grid:
            print(i)

    """
    Function to count the number of queens on the board
    """
    def count_queens(self):
        queens = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[j][i] != 0:
                    queens += 1
        return queens

    """
    Function to fill the first row with queens and the rest blank
    """
    def populate_board(self):
        self.grid = np.array([[0]*self.N]*self.N)
        for i in range(self.N):
            if i == self.k:
                continue
            else:
                temp = random.randint(0, self.N -1)
                self.grid[temp][i] = 1
        
        self.grid[self.l][self.k] = 1
        

class Solver:
    def __init__(self, start):
        self.start = start
    
        
    """
    Function that solves the puzzle and returns solution
    """
 
    def solve(self):
        
        queue = []
        visited_nodes = []
        # Adding starting board to queue
        queue.append(Node(self.start))
        counter = 0
        # while elements are in the queue
        while queue:
        
            # getting first node in queue
            current_node = queue[0]
            
                
            # checking if solved
            if current_node.solved:
                print(f"Restart Count: {counter}")
                return current_node.board
            
            if current_node.h == 1:
                counter += 1
            
            # implementing backtracking to avoid local minimum
            if counter == 10:
                current_node = random.choice(visited_nodes)
            
            # getting list of queen coordinates
            queens = current_node.board.queens
            
            # looping through the queens in current board
            for queen in queens:
                if queen == current_node.board.fixed_queen:
                    continue
                else:
                    # getting a list of tiles where the queen can move
                    actions = current_node.board.actions(queen)
                    # looping through all the actions a queen can make
                    for action in actions:
                        # copying board
                        new_board = deepcopy(current_node.board)
                        # moving queen
                        new_board.move(queen, action)
                        # creating new node
                        child_node = Node(new_board, current_node)
                        # adding node to queue
                        queue.append(child_node)
            
            visited_nodes.append(current_node)
            
            if current_node in queue:
                queue.remove(current_node)
            
            queue = sorted(queue, key=lambda x: x.h)
            


                    

board = Board(8, 8, 7)
board.populate_board()

s = Solver(board)
solution = s.solve()

solution.pprint
print(solution.heuristic)