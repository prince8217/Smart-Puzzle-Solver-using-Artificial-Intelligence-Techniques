from collections import deque
from utils.helpers import get_neighbors, goal_state

def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal_state:
            return path + [state]

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

    return None
