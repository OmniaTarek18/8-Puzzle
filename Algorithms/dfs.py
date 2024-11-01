from collections import deque
import time
from Algorithms.algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, init_state, goal_test = 12345678):
        super().__init__(init_state)
        self.goal = goal_test

    def solve(self):
        start_time = time.perf_counter()

        # Initialize frontier with (state, depth)
        self.frontier.append((self.init_state, 0))
        self.parent[self.init_state] = None

        # check if it is the goal 
        if self.init_state == self.goal:
            self.path = self.get_path()
            self.nodes_explored += 1
            return
        
        while self.frontier:
            current_state, current_depth = self.frontier.pop()
            self.explored.add(current_state)
            
            # Update maximum depth reached
            self.depth = max(self.depth, current_depth)

            # Get the location of the empty tile
            empty_tile = self.get_empty_tile_location(current_state)

            # Try all four possible moves
            # based on this, the order of pushing into the stack is right, down, left, up
            # pushing the neighbors in the stack
            for move in self.moves[::-1]:
                # check the validity of possible moves (up, down, left, right)
                if not self.is_valid_move(empty_tile, move):
                    continue

                # Apply the move to generate a new state
                new_state = self.apply_move(current_state, empty_tile, move)

                # Check if the new state is in the explored states or not
                if new_state not in self.explored and new_state not in self.parent:
                    # Add new state and depth to frontier
                    self.frontier.append((new_state, current_depth + 1))
                    self.parent[new_state] = current_state

                    # check if it is the goal 
                    if new_state == self.goal:
                        end_time = time.perf_counter()
                        self.running_time = end_time - start_time
                        self.nodes_explored = len(self.explored) + 1
                        self.depth = max(self.depth, current_depth+1)
                        self.cost = current_depth + 1
                        self.path = self.get_path()
                        return
        

    def get_path(self):
        path = deque()
        current_state = self.goal
        
        while current_state is not None:
            path.appendleft(current_state)  # Add each state to the front of the path
            current_state = self.parent.get(current_state)  # Move to the parent of the current state

        return list(path)


# dfs = DFS(125340678)
# dfs.solve()
# print('Cost: {}\nSearch Depth: {}\nNodes Explored: {}\nPath: {}'.format(dfs.cost, dfs.depth, dfs.nodes_explored, dfs.path))