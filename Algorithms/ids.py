from collections import deque
import time
from Algorithms.algorithm import Algorithm


class IDS(Algorithm):
    def __init__(self, init_state, goal_test = 12345678):
        super().__init__(init_state)
        self.goal = goal_test

    def dls(self, limit):
        self.explored = set()  # Reset explored for each depth limit
        self.parent = {}

        # Initialize frontier with (state, depth)
        self.frontier.append((self.init_state, 0))
        self.parent[self.init_state] = None

        goal_found = False
        self.cost = -1

        while self.frontier:
            current_state, current_depth = self.frontier.pop()
            self.nodes_explored += 1
            # Update the maximum depth reached
            self.depth = max(self.depth, current_depth)

            # Check if the current state is the goal
            if current_state == self.goal:
                goal_found = True
                if (self.cost == -1):
                    self.cost = current_depth
                    self.path = self.get_path()

                elif (self.cost > current_depth):
                    self.cost = current_depth  # Cost is depth when the goal is found
                    self.path = self.get_path()  # Get path to the goal
                continue

            # If the current depth is less than the limit, explore further
            if current_depth < limit:
                # Get the location of the empty tile in the current state
                empty_tile = self.get_empty_tile_location(current_state)

                # Define possible moves: right, down, left, up
                moves = [1, 3, -1, -3]

                for move in moves:
                    # Check the validity of the move
                    if not self.is_valid_move(empty_tile, move):
                        continue

                    # Apply the move to get the new state
                    new_state = self.apply_move(current_state, empty_tile, move)

                    if not self.check_loop(current_state, new_state):
                        # Push new state with increased depth
                        self.frontier.append((new_state, current_depth + 1))
                        self.parent[new_state] = current_state

        return goal_found  # Goal not found within the depth limit
    
    def check_loop (self,current_state, new_state):
        while (current_state != None):
            if (current_state == new_state):
                return True
            current_state = self.parent.get(current_state)
        return False

    def iddfs(self):
        depth = 0
        while True:
            found = self.dls(depth)  # Perform depth-limited search
            if found:  # If the goal is found, return
                return
            depth += 1 

    def solve(self):
        start_time = time.perf_counter()
        self.iddfs()  # Start IDDFS
        end_time = time.perf_counter()
        self.running_time = end_time - start_time

    def get_path(self):
        path = deque()
        current_state = self.goal
        
        while current_state is not None:
            path.appendleft(current_state)  # Add each state to the front of the path
            current_state = self.parent.get(current_state)  # Move to the parent of the current state

        return path


# ids = IDS(867254301)
# ids.solve()
# print('Cost: {}\nSearch Depth: {}\nNodes Explored: {}\nPath: {}'.format(ids.cost, ids.depth, ids.nodes_explored, ids.path))

# ids = IDS(125340678)
# ids.dls(3)
# print('Cost: {}\nSearch Depth: {}\nNodes Explored: {}\nPath: {}'.format(ids.cost, ids.depth, ids.nodes_explored, ids.path))
# print(ids.explored)