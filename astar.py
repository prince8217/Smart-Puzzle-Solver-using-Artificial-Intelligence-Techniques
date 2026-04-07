import heapq
from utils.helpers import get_neighbors, goal_state

def heuristic(state):
    distance = 0
    for i, value in enumerate(state):
        if value == 0:
            continue
        goal_index = goal_state.index(value)
        x1, y1 = i // 3, i % 3
        x2, y2 = goal_index // 3, goal_index % 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def astar(start):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal_state:
            return path + [state]

        for neighbor in get_neighbors(state):
            new_cost = len(path) + heuristic(neighbor)
            heapq.heappush(pq, (new_cost, neighbor, path + [state]))

    return None
