def get_directions(path):
    directions = []
    length = len(path)
    for i in range(1, length):
        prev_state = str(path[i-1])
        curr_state = str(path[i])
        
        prev_index = 0 if len(prev_state) == 8 else prev_state.index('0')
        new_index = 0 if len(curr_state) == 8 else curr_state.index('0')
        
        if prev_index + 3 == new_index:
            directions.append("Down")
        elif prev_index - 3 == new_index:
            directions.append("Up")
        elif prev_index + 1 == new_index:
            directions.append("Right")
        elif prev_index - 1 == new_index:
            directions.append("Left")
    print(directions)
    return directions