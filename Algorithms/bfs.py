from Algorithms.algorithm import Algorithm
from collections import deque
from datetime import timedelta
import time


class BFS(Algorithm):
    def __init__(self, init_state):
        super().__init__(init_state)     
        
    def solve(self):
        begin_time = time.perf_counter()
        self.frontier.append(self.init_state)
        self.parent[self.init_state] = None
        
        # check if it is the goal 
        if self.init_state == self.goal:
            return
        
        while self.frontier:
            current_state = self.frontier.popleft()
            self.explored.add(current_state)
                        
            # get index of the empty tile
            empty_tile = self.get_empty_tile_location(current_state) 
            
            # add the possible movements
            moves = [-3, 1, 3, -1]
            
            for move in moves:
                # check the validity of possible moves (up, down, left, right)
                if not self.is_valid_move(empty_tile, move):
                    continue
                              
                new_state = self.apply_move(current_state, empty_tile, move)
                   
                # check if the possible state is explored before or in frontier dequeue to prevent duplicates
                if new_state not in self.explored and new_state not in self.frontier:
                    self.parent[new_state] = current_state
                    
                    # check if it is the goal 
                    if new_state == self.goal:
                        return
                    
                    self.frontier.append(new_state)
                    
            self.running_time = time.perf_counter() - begin_time

                               

    def get_path(self):
        self.path = deque()  
        state = self.goal
        while state is not None:
            self.path.appendleft(state)
            state = self.parent[state]
        self.cost = len(self.path) - 1
        self.depth = self.cost
        return self.path


    

