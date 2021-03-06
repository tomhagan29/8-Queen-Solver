from copy import deepcopy
import numpy as np
import random
from collections import deque

class Node:
    
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        
        if self.parent == None:
            self.g = 0
        else:
            self.g = parent.g + 1
        
    """
    Function that returns the objective function
    """        
    @property
    def f(self):
        return self.g + self.h
    
    """
    Function returns the manhattan distance
    """
    @property
    def h(self):
        return self.board.manhattan
    
    """
    Returns true if solved
    """
    @property
    def solved(self):
        return self.board.solved
    
    """
    Returns the actions of the board
    """
    @property
    def actions(self):
        return self.board.actions
    
    """
    Returns hashable representation
    """
    @property
    def state(self):
        return str(self)
    
    

class Board:
    
    def __init__(self, N, k, l):
        self.board = np.array([[0]*8]*8)
        self.N = N
        self.k = k%N
        self.l = l%N
    
    """
    Function that checks if the board is solved
    """
    @property
    def solved(self):
        return self.manhattan == 0
    
    """
    Function that returns the number of attacks
    """
    @property
    def manhattan(self):
        attacks = 0
        
        # Checking horrizontal attacks
        for i in range(self.N):
            temp = list(self.board[i]).count(1) + list(self.board[i]).count(2)
            if temp > 1:
                attacks += temp - 1
        
        # Checking for vertical attacks
        for i in range(self.N):
            temp = []
            
            for j in range(self.N):
                temp.append(self.board[j][i])

            queens = temp.count(1) + temp.count(2) 
            
            if queens > 1:
                attacks += queens - 1
         
        # Checking for diagonal attacks
        for i in range(-self.N,self.N):
            temp = list(np.diagonal(self.board, i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
        
        for i in range(-self.N,self.N):
            temp = list(np.diagonal(np.fliplr(self.board),i))
            queens = temp.count(1) + temp.count(2)

            if queens > 1:
                attacks += queens - 1
         
        return attacks
    
    """
    Function that returns the coordinates of each queen
    """
    @property
    def queens(self):
        queens = []
        
        for i in range(self.N):
            for j in range(self.N):
                if self.board[j][i] == 1:
                    queens.append((i,j))
        
        return queens
    
    """
    Returns all the possible actions on the board
    """
    @property
    def actions(self):
        actions = dict()
        
        for queen in self.queens:
            actions[queen] = self.get_moves(queen)

        return actions
    
    """
    Returns all the moves a specified queen can make
    """
    def get_moves(self, queen):
        moves = []
        for i in range(self.N):
            if i == queen[1]:
                continue
            moves.append((queen[0], i))
            
        return moves
        
    """
    Function that moves the queen to the lowest heuristic tile
    """
    def move(self, queen, coords):
        self.board[queen[1]][queen[0]] = 0
        self.board[coords[1]][coords[0]] = 1
    
    """
    Function to populate board with fixed queen and random queens
    """
    def populate_board(self):
        
        self.board = np.array([[0]*8]*8)
        
        for i in range(self.N):
            
            temp = random.randint(0, self.N - 1)
            if i == self.k:
                continue
            else:
                self.board[temp][i] = 1
        
        self.board[self.l][self.k] = 1
    
    """
    Returns the board as a string
    """
    @property
    def hashable(self):
        return np.array2string(self.board)
                
    
    """
    Prints board in representable state
    """
    def pprint(self):
        for row in self.board:
            print(row)


class Solver:
    
    def __init__(self, start):
        self.start = start
    
    """
    A* search algorithm
    """
    def solve(self):
        
        # Got number of solutions online at https://www.datagenetics.com/blog/august42012/
        number_of_solutions = 4
        solutions = set()
        steps = 0
        queue = deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        # while the queue has elements
        while queue:
            # sorting the queue by the node's objective function in ascending order
            queue = deque(sorted(list(queue), key=lambda node: node.f))
            # taking the lowest heuristic node
            node = queue.popleft()
            # checking if the node is solved
            if node.solved:
                solutions.add(node.board.hashable)
            
            # checking if all solutions are found
            if len(solutions) == number_of_solutions:
                break
            
            steps += 1
            
            # restarting the search
            if steps == 20:
                new_board = Board(self.start.N, self.start.k, self.start.l)
                new_board.populate_board()
                queue = deque([Node(new_board)])
                seen = set()
                seen.add(queue[0].state)
                node = queue.popleft()
                steps = 0

            # for all the queens on the board
            for queen in node.board.queens:
                # skipping the fixed queen
                if queen == (node.board.k, node.board.l):
                    continue
                # creating child nodes for each possible move
                for action in node.actions[queen]:
                    new_board = deepcopy(node.board)
                    new_board.move(queen, action)
                    child = Node(new_board, node)
                    
                    # adding the child to queue
                    if child.state not in seen:
                        queue.appendleft(child)
                        seen.add(child.state)
        
        return solutions
                 
            
if __name__ == '__main__':
    board = Board(8, 8, 7)
    board.populate_board()

    s = Solver(board)
    solutions = list(s.solve())
    f = open("output.txt", "w")
    for i in range(4):
        f.write(f"\nSolution {i+1}")
        f.write("\n--------------\n")
        f.write(solutions[i])
        f.write("\n--------------\n")
        
        
        
        
        
