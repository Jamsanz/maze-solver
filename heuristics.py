import math

def manhattan_distance(state, goal):
    """Heuristic function: Manhattan Distance."""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def octile_distance(state, goal):
    """Heuristic function: Octile Distance."""
    dx = abs(state[0] - goal[0])
    dy = abs(state[1] - goal[1])
    return dx + dy + (math.sqrt(2) - 2) * min(dx, dy)

def dijkstra_heuristic(state, goal):
    """Dijkstra's heuristic: Always returns 0 (no heuristic)."""
    return 0

def weighted_manhattan_distance(state, goal, weight=1.2):
    """Heuristic function: Weighted Manhattan Distance."""
    dx = abs(state[0] - goal[0])
    dy = abs(state[1] - goal[1])
    return weight * (dx + dy)


def breaking_ties_heuristic(state, goal, epsilon=0.01):
    """Heuristic function: Breaking Ties Heuristic."""
    dx = abs(state[0] - goal[0])
    dy = abs(state[1] - goal[1])
    return dx + dy + epsilon * (dx + dy)
