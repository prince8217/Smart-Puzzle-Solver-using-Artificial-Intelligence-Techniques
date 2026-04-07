from utils.helpers import get_neighbors, goal_state

def dfs(start, depth_limit=20):
    stack = [(start, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()

        if state in visited or depth > depth_limit:
            continue

        visited.add(state)

        if state == goal_state:
            return path + [state]

        for neighbor in get_neighbors(state):
            stack.append((neighbor, path + [state], depth + 1))

    return None
