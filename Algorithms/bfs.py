from algorithm import Algorithm 
from collections import deque
from datetime import timedelta
import time


class BFS(Algorithm):
    def __init__(self, init_state):
        super().__init__(init_state)

 
    def solve(self):
        self.run_algorithm()
        return {
            'Cost' : self.cost,
            'Running Time' : self.running_time,
            'Depth':  self.cost,
            'Nodes Explored': len(self.explored),
            'Path' : self.path
            }
        
    def run_algorithm(self):
        begin_time = time.perf_counter() 
        self.bfs()                   
        self.running_time = time.perf_counter() - begin_time
        self.path = self.get_path()
        
        
    def bfs(self):
        self.frontier = deque([self.init_state])
        # check if it is the goal 
        if self.init_state == self.goal:
            return
        
        while self.frontier:
            current_state = self.frontier.popleft()
            self.explored.append(current_state)
            
            # get index of the free place 
            free_index = current_state.index(0)
            
            # add the possible movements
            step = [-3, 1, 3, -1]
            
            for i in range(4):
               # check corners 
               if (free_index in [2,5] and step[i] == 1) or (free_index in [3,6] and step[i] == -1):
                   continue
               
               new_index = free_index + step[i]
               
               if  9 > new_index > -1:
                   possible_state = current_state.copy()
                   possible_state[free_index] = possible_state[new_index]
                   possible_state[new_index] = 0
                   
                   # check if the possible state is explored before or in frontier dequeue to prevent duplicates
                   if possible_state not in self.explored: 
                        if possible_state not in self.frontier:
                            self.parent[str(possible_state)] = current_state
                            # check if it is the goal 
                            if possible_state == self.goal:
                                    return
                            self.frontier.append(possible_state)
                               

    def get_path(self):  
        
        child = str(self.goal)
        parent = self.parent[child]
        path = deque([parent, self.goal])   
               
        while parent != self.init_state:
            parent = self.parent[str(parent)]
            path.appendleft(parent)
            
        self.cost = len(path) - 1
        return path
            
    # def get_running_time(self):
    #     time_elapsed = self.end_time - self.begin_time 
    #     duration = timedelta(seconds=time_elapsed)
    #     return duration
        
                        
                        
                   
                



        


# bfs = BFS([1,0,2,7,5,4,8,6,3])
# bfs.solve()
# bfs.get_path()
# print(len(bfs.explored))