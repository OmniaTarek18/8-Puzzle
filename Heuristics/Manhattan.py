from Heuristics.Heuristic import get_heuristic

# manhattan distance
def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def manhattan_heuristic(state, goal_state):
    return get_heuristic(state, goal_state, manhattan_distance)





