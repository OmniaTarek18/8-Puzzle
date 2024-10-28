
from Algorithms.algorithm import Algorithm
from Heuristics.Manhattan import manhattan_heuristic
from Heuristics.Euclidean import euclidean_heuristic
import queue
import time


class AStar(Algorithm):
    def __init__(self, initial_state, heuristic,goal_test=12345678):
        super().__init__(initial_state)
        self.goal = goal_test
        match heuristic:
            case "Manhattan":
                self.heuristic = manhattan_heuristic
            case "Euclidean":
                self.heuristic = euclidean_heuristic
            case _:
                pass
        
    def solve(self):
        start_time = time.perf_counter()
        self.frontier = queue.PriorityQueue()
        self.explored = set()
        self.parent = dict()
        # self.goal = 12345678
        self.depth = 0

        # Add the initial state to the frontier with a cost of 0 and no parent.
        self.frontier.put((0, self.init_state))
        self.parent[self.init_state] = (0, None)


        while not self.frontier.empty():
            current_state = self.frontier.get()[1]

            # Check if the current state has already been explored
            if current_state in self.explored:
                continue

            # Mark the current state as explored
            self.explored.add(current_state)

            # If the goal state is found, exit the loop
            if current_state == self.goal:
                break

            # Get the cost of the current state and increment it
            self.cost = self.parent.get(current_state)[0]
            self.cost += 1

            # Get the location of the empty tile
            empty_tile = self.get_empty_tile_location(current_state)

            # Try all four possible moves
            # based on this, the order of pushing into the stack is up, down, left, right
            for move in self.moves:
                # check the validity of possible moves (up, down, left, right)
                if not self.is_valid_move(empty_tile, move):
                    continue

                # Apply the move to generate a new state
                new_state = self.apply_move(current_state, empty_tile, move)

                # Calculate the priority of the new state
                # priority = cost + heuristic
                if new_state not in self.parent and new_state not in self.explored:
                    self.frontier.put((self.cost + self.heuristic(new_state, self.goal), new_state))
                    self.parent[new_state] = (self.cost, current_state)
                    self.depth = max(self.depth, self.cost)
                elif self.cost < self.parent[new_state][0]:
                    self.frontier.put((self.cost + self.heuristic(new_state, self.goal), new_state))
                    self.parent[new_state] = (self.cost, current_state)

        end_time = time.perf_counter()
        # Calculate the path, cost, number of nodes expanded, search depth, and running time.
        self.cost = self.parent[self.goal][0]
        self.nodes_explored = len(self.explored)
        self.running_time = end_time - start_time
        self.path = self.get_path()



    def get_path(self):
        path = []
        current_state = self.goal
        while current_state is not None:
            path.append(current_state)
            current_state = self.parent[current_state][1]
        return path[::-1]






