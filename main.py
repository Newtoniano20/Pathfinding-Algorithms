import time
import sys

from src import Maze, AStar, Greedy, QueueFrontier, StackFrontier

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

to = time.time()

A = (18, 0)
B = (8, 4)
C = (18, 6)
D = (0, 1)

m = Maze(filename=sys.argv[1], origin=A, goal=B)
# print("Maze:")
# m.print()
print("Solving...")
m.solve(Algorithm=AStar)

print("States Explored:", m.num_explored)
# print("Solution:")
# m.print()
m.output_image("maze.png", show_explored=True)

print(m.solution)
print(f"Time spent: {time.time() - to}")