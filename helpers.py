goal_state = (1,2,3,4,5,6,7,8,0)

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for r, c in moves:
        new_r, new_c = row + r, col + c
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_index = new_r * 3 + new_c
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))

    return neighbors
