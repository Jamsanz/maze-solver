# Maze Solver - README

## Introduction
This project implements and compares A* and Greedy Best-First Search (GBFS) algorithms using Manhattan and Octile Distance heuristics to solve maze problems.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install matplotlib seaborn pandas pillow
```
or 
```sh
pip install -r requirements.txt
```

## Running the Code

1. **Prepare the Environment:** Ensure Python is installed (Python 3.x recommended).
2. **Execute the Solver:** Run the script with a maze file as an argument:

```sh
python solution.py maze_30x30.txt
```

Replace `maze_30x30.txt` with `maze_35x35.txt` or `maze_40x40.txt` and adjust the algorthim and heuristic as needed in line 11.

Expected Output
- The script will solve the maze using the algorithm and heuristic provided in line 11.
- It will path from A to B in the console
- it will generate`solution.png`: Visual representation of the solved maze

3. **Execute for analysis:** Run the script below:
```sh
python analysis.py
```

Expected Output
- The script will solve the maze using A* and GBFS algorithms with both heuristics.
- It will generate comparison figures for:
  - Nodes explored
  - Execution time
  - Path cost

