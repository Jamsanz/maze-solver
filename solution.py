import sys
import time
from maze_solver import MazeSolver, manhattan_distance, octile_distance

s = MazeSolver(sys.argv[1])

print("Maze:")
s.print()
print("Solving...")
start_time = time.time()
s.solve_a_star(heuristic=manhattan_distance)
print("Nodes explored:", s.num_explored)
print("Path cost:", len(s.solution[0]) )
print("Execution time:", round(time.time() - start_time, 4))
print("Solution:")
s.print()
s.output_image("solution.png", show_explored=True)

