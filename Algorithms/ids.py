from collections import deque
import time
from algorithm import Algorithm


class IDS(Algorithm):
    def __init__(self, init_state, goal_test = 12345678):
        super().__init__(init_state)
        self.goal = goal_test

    def dls(self, depth):
        self.frontier = deque()
        self.explored = []
        self.parent = {}
        self.depth = 0
        max_depth = 0  # Track depth for this iteration only

        # Initialize frontier with (state, depth)
        self.frontier.append((self.init_state, 0))
        self.parent[self.init_state] = None

        # check if it is the goal
        if self.init_state == self.goal:
            self.path = self.get_path()
            self.nodes_explored += 1
            return True
        
        # Initialize depth
        max_depth = 0

        while self.frontier:
            current_state, current_depth = self.frontier.pop()
            self.explored.add(current_state)
            
            # Update maximum depth reached
            self.depth = max(max_depth, current_depth, self.depth)

            if current_state == self.goal:
                self.cost = current_depth
                self.nodes_explored += len(self.explored)
                self.path = self.get_path()  # Retrieve path to goal
                return True
            
            if current_depth < depth:

                # Get the location of the empty tile
                empty_tile = self.get_empty_tile_location(current_state)

                # Try all four possible moves
                # based on this, the order of pushing into the stack is right, down, left, up
                moves = [1, 3, -1, -3]

                # pushing the neighbors in the stack
                for move in moves:
                    # check the validity of possible moves (up, down, left, right)
                    if not self.is_valid_move(empty_tile, move):
                        continue

                    # Apply the move to generate a new state
                    new_state = self.apply_move(current_state, empty_tile, move)

                    # Check if the new state is in the explored states or not
                    if new_state not in self.explored:
                        # Add new state and depth to frontier
                        self.frontier.append((new_state, current_depth + 1))
                        self.parent[new_state] = current_state
        
        self.nodes_explored += len(self.explored)
        self.depth = max(self.depth, max_depth)
        self.cost = current_depth
        self.path = self.get_path()
        return False

    def solve(self):
        start_time = time.perf_counter()

        depth = 0
        is_goal_found = False

        while not is_goal_found:
            is_goal_found = self.dls(depth)
            depth += 1

        end_time = time.perf_counter()
        self.running_time = end_time - start_time


    def get_path(self):
        path = deque()
        current_state = self.goal
        
        while current_state is not None:
            path.appendleft(current_state)  # Add each state to the front of the path
            current_state = self.parent.get(current_state)  # Move to the parent of the current state

        return path


# ids = IDS(125340678)
# ids.dls(3)
# print('Cost: {}\nSearch Depth: {}\nNodes Explored: {}\nPath: {}'.format(ids.cost, ids.depth, ids.nodes_explored, ids.path))
# print(ids.explored)