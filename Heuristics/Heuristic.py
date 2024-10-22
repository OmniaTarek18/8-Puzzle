def get_heuristic(state, goal_state, distance):
    # get position of each tile in the goal state
    goal_positions = dict()
    for i in range(9):
        goal_positions[goal_state % 10] = 8-i
        goal_state //= 10

    # calculate the heuristic sum
    heuristic_sum = 0
    for i in range(9):
        val = state % 10

        # if the value is not 0 (not an empty cell)
        if val:
            x1 = (8 - i) // 3
            y1 = (8 - i) % 3
            x2 = goal_positions[val] // 3
            y2 = goal_positions[val] % 3
            heuristic_sum += distance(x1, x2, y1, y2)
        state //= 10

    return heuristic_sum



