from math import sqrt

from Heuristics.Heuristic import get_heuristic


# euclidean distance
def euclidean_distance(x1, x2, y1, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def euclidean_heuristic(state, goal_state):
    return get_heuristic(state, goal_state, euclidean_distance)
