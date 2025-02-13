import heapq
import sys
import math
import time
from django.utils.timezone import now

from maze import Maze, Node

class PriorityQueueFrontier():
    def __init__(self):
        self.frontier = []
        self.entry_count = 0  # To maintain order of insertion
    
    def add(self, node, priority):
        heapq.heappush(self.frontier, (priority, self.entry_count, node))
        self.entry_count += 1
    
    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        return heapq.heappop(self.frontier)[2]  # Return the node itself
    
def manhattan_distance(state, goal):
    """Heuristic function: Manhattan Distance."""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def octile_distance(state, goal):
    """Heuristic function: Octile Distance."""
    dx = abs(state[0] - goal[0])
    dy = abs(state[1] - goal[1])
    return dx + dy + (math.sqrt(2) - 2) * min(dx, dy)

class MazeSolver(Maze):
    
    def solve_a_star(self, heuristic):
        """Solve the maze using A* search."""
        self.num_explored = 0
        self.explored = set()
        
        start_node = Node(state=self.start, parent=None, action=None)
        frontier = PriorityQueueFrontier()
        frontier.add(start_node, priority=0)
        
        cost_so_far = {self.start: 0}
        
        while not frontier.empty():
            node = frontier.remove()
            self.num_explored += 1
            
            if node.state == self.goal:
                actions, cells = self.reconstruct_path(node)
                self.solution = (actions, cells)
                return
            
            self.explored.add(node.state)
            
            for action, state in self.neighbors(node.state):
                new_cost = cost_so_far[node.state] + 1
                if state not in cost_so_far or new_cost < cost_so_far[state]:
                    cost_so_far[state] = new_cost
                    priority = new_cost + heuristic(state, self.goal)
                    frontier.add(Node(state, node, action), priority)
    
    
    def solve_greedy_bfs(self, heuristic):
        """Solve the maze using Greedy Best-First Search."""
        self.num_explored = 0
        self.explored = set()
        
        start_node = Node(state=self.start, parent=None, action=None)
        frontier = PriorityQueueFrontier()
        frontier.add(start_node, priority=heuristic(self.start, self.goal))
        
        while not frontier.empty():
            node = frontier.remove()
            self.num_explored += 1
            
            if node.state == self.goal:
                actions, cells = self.reconstruct_path(node)
                self.solution = (actions, cells)
                return
            
            self.explored.add(node.state)
            
            for action, state in self.neighbors(node.state):
                if state not in self.explored and not frontier.contains_state(state):
                    frontier.add(Node(state, node, action), heuristic(state, self.goal))
    
    
    def reconstruct_path(self, node):
        """Reconstructs the path from the goal back to start."""
        actions = []
        cells = []
        while node.parent is not None:
            actions.append(node.action)
            cells.append(node.state)
            node = node.parent
        actions.reverse()
        cells.reverse()
        return actions, cells

    def print_execution_time(self):
        """Prints the execution time for solving the maze."""
        if hasattr(self, 'execution_time'):
            print(f"Execution Time: {self.execution_time:.4f} seconds")
        else:
            print("The maze has not been solved yet.")

# if len(sys.argv) != 2:
#     sys.exit("Usage: python maze.py maze.txt")

# s = MazeSolver(sys.argv[1])

# print("Maze:")
# s.print()
# print("Solving...")
# start_time = time.time()
# s.solve_a_star(heuristic=manhattan_distance)
# print("Nodes explored:", s.num_explored)
# print("Path cost:", len(s.solution[0]) )
# print("Execution time:", round(time.time() - start_time, 4))
# print("Solution:")
# s.print()
# s.output_image("solution.png", show_explored=True)

