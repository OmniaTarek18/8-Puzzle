from Algorithms.AStar import AStar
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS
from Algorithms.ids import IDS

class SearchTechnique:
    def __new__(self, type, init_state, heuristic = None, goal_test = 12345678):
        if type == "BFS":
            return BFS(init_state)
        elif type == "DFS":
            return DFS(init_state)
        elif type == "Iterative DFS":
            return IDS(init_state)
        elif type == "A*":
            return AStar(init_state, heuristic, goal_test)
