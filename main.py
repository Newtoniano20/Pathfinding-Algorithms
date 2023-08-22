import time
from src import Maze, AStar, Greedy, QueueFrontier, StackFrontier

PATH_TO_MAZE = "./maze1.txt"

to = time.time()

A = (18, 0)
B = (8, 4)
C = (18, 6)
D = (0, 1)

m = Maze(filename=PATH_TO_MAZE, origin=C, goal=D, diagonals=False)
# print("Maze:")
# m.print()
print("Solving...")
m.solve(Algorithm=AStar)

print("States Explored:", m.num_explored) # number of states explored (lower the better)
print("Number of steps of the solution:", len(m.solution[0]))
# print("Solution: \n {m.print()}") # prints maze to terminal
m.output_image("maze.png", show_explored=True)  # saves image of maze

# print(m.solution) #prints solution of the maze in a step by step structure
print(f"Time spent: {time.time() - to}")