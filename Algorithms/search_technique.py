
from bfs import BFS
from dfs import DFS
from ids import IDS


class SearchTechnique:
    def __new__(self, type, init_state):
        if type == "BFS":
            return BFS(init_state)
        elif type == "DFS":
            return DFS(init_state)
        elif type == "Iterative DFS":
            return IDS(init_state)
        # else if type == "A*":
        #     return A*(init_state)
