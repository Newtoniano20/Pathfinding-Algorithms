import time
from src import Maze, AStar, Greedy, QueueFrontier, StackFrontier

PATH_TO_MAZE = "./maze1.txt"

A = (18, 0)
B = (8, 4)
C = (18, 6)
D = (0, 1)

# print("Maze:")
# m.print()
print("Solving...")

to = time.time()
m = Maze(filename=PATH_TO_MAZE, origin=A, goal=B, diagonals=True, resolution=1)
m.solve(Algorithm=AStar)
print(f"Solved. Time spent: {time.time() - to}")

print("States Explored:", m.num_explored) # number of states explored (lower the better)
print("Number of steps of the solution:", len(m.solution[0]))
# print("Solution: \n {m.print()}") # prints maze to terminal
m.output_image("maze.png", show_explored=True)  # saves image of maze

# print(m.solution) #prints solution of the maze in a step by step structure