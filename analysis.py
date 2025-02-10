import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from solution import MazeSolver, manhattan_distance, octile_distance

# Load maze files
maze_files = {
    "30x30": "maze_30x30.txt",
    "35x35": "maze_35x35.txt",
    "40x40": "maze_40x40.txt",
}

# Store results
results = []

for size, filepath in maze_files.items():
    maze = MazeSolver(filepath)

    for algo_name, algo_func in [
        ("A* (Manhattan)", lambda: maze.solve_a_star(manhattan_distance)),
        ("A* (Octile)", lambda: maze.solve_a_star(octile_distance)),
        ("GBFS (Manhattan)", lambda: maze.solve_greedy_bfs(manhattan_distance)),
        ("GBFS (Octile)", lambda: maze.solve_greedy_bfs(octile_distance)),
    ]:
        # Reset solution and explored set
        maze.solution = None
        maze.explored = set()

        # Measure execution time
        start_time = time.time()
        algo_func()
        execution_time = time.time() - start_time

        # Store results
        results.append({
            "Maze Size": size,
            "Algorithm": algo_name,
            "Nodes Explored": maze.num_explored,
            "Execution Time (s)": execution_time,
            "Path Cost": len(maze.solution[0])
        })

# Convert results to DataFrame for visualization
df = pd.DataFrame(results)

# Plot performance comparisons
sns.set(style="whitegrid")

# Nodes Explored
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Maze Size", y="Nodes Explored", hue="Algorithm")
plt.title("Nodes Explored by Algorithm")
plt.ylabel("Nodes Explored")
plt.xlabel("Maze Size")
plt.legend(title="Algorithm")
plt.xticks(rotation=45)
plt.show()

# Execution Time
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Maze Size", y="Execution Time (s)", hue="Algorithm")
plt.title("Execution Time by Algorithm")
plt.ylabel("Execution Time (s)")
plt.xlabel("Maze Size")
plt.legend(title="Algorithm")
plt.xticks(rotation=45)
plt.show()

# Path Cost
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Maze Size", y="Path Cost", hue="Algorithm")
plt.title("Path Cost by Algorithm")
plt.ylabel("Path Cost (s)")
plt.xlabel("Maze Size")
plt.legend(title="Algorithm")
plt.xticks(rotation=45)
plt.show()

