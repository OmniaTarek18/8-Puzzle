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