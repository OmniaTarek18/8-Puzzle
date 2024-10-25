from abc import abstractmethod
from collections import deque

class Algorithm:
    def __init__(self, init_state):
        self.init_state = init_state
        self.frontier = deque()
        self.explored = []
        self.parent = {}
        self.goal = [0,1,2,3,4,5,6,7,8]
        # results
        self.cost = 0
        self.running_time = 0
        self.depth = 0
        self.nodes_explored = 0
        self.path = deque()
        
    # return in this form :
    # return {
    #     'Cost' : self.cost,
    #     'Running Time' : self.running_time,
    #     'Depth':  self.cost,
    #     'Nodes Explored': len(self.explored),
    #     'Path' : path
    #     }
    @abstractmethod   
    def solve(self):
        pass
    
    @abstractmethod   
    def get_path(self):
        pass



    # Count the number of inversions in any state
    @staticmethod
    def count_inversions(state):
        inversions = 0
        s = str(state)
        if len(s) == 8:
            s = '0' + s

        for i in range(9):
            if int(s[i]) != 0:
                for j in range(i):
                    if int(s[j]) != 0 and int(s[i]) < int(s[j]):
                        inversions += 1
        return inversions

    # Check if the initial state is solvable by comparing inversions
    def is_solvable(self):
        initial_state_inversions = self.count_inversions(self.init_state)
        goal_test_inversions = self.count_inversions(12345678)
        return initial_state_inversions%2 == goal_test_inversions%2

    # Check if the move is valid
    # assume board start index is 0
    @staticmethod
    def is_valid_move(empty_tile, move):
        if move == -3: # up
            return empty_tile > 2
        if move == 1: # right
            return empty_tile % 3 != 2
        if move == 3: # down
            return empty_tile < 6
        if move == -1: # left
            return empty_tile % 3 != 0

    # Apply the move to the current state
    @staticmethod
    def apply_move(current_state, empty_tile, move):
        # get the new location of the empty tile
        new_emtpy_tile = empty_tile + move
        # get the value of the tile to be moved
        tile_value = current_state // 10 ** (8 - new_emtpy_tile) % 10
        # move the tile
        new_state = (current_state - tile_value * 10 ** (8 - new_emtpy_tile) + tile_value * 10 ** (8 - empty_tile))
        return new_state

    # Get the location of the empty tile in the state
    @staticmethod
    def get_empty_tile_location(state):
        state_str = str(state)
        # add leading zero if the state is 8 digits
        if len(state_str) == 8:
            state_str = '0' + state_str
        return state_str.index('0')


