#
# from bfs import BFS
# from dfs import DFS
# from ids import IDS
from Algorithms.AStar import AStar
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS
from Algorithms.ids import IDS

class SearchTechnique:
    def __new__(self, type, init_state,heuristic = None):
        if type == "BFS":
            return BFS(init_state)
        elif type == "DFS":
            return DFS(init_state)
        elif type == "Iterative DFS":
            return IDS(init_state)
        elif type == "AStar":
            return AStar(init_state, heuristic)
        # else if type == "A*":
        #     return A*(init_state)
