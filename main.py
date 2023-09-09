import time
from src import Maze, AStar, Greedy, QueueFrontier, StackFrontier, Position

PATH_TO_MAZE = "./maze1.txt"


Zero = (144, 259)
# 98, 259
# 144, 163
# x, y
S1 = (0, 0)
# B = (0, 13.31)
# B = (-6.3, 0)
W1 = (3.83, 9.1)
W2 = (-9.9, 13.49)
W3 = (-0.2, 19.57)
pos = Position(Xo=S1, waypoints={"W1": W1, "W2": W2, "W3":W3}, W1=9.87, W2=16.8, W3=19.6)
pos.update_distances(W1=8.95, W2=15.94, W3=18.57)
theoretical_pos = pos.theoretical_positions()
print(theoretical_pos)
A = theoretical_pos
B = W1
Scale_x = 7.3
Scale_y = -7.2


# DO NOT TOUCH
#####
A = (Zero[1]+A[1]*Scale_y, Zero[0]+A[0]*Scale_x)
B = (Zero[1]+B[1]*Scale_y, Zero[0]+B[0]*Scale_x)
#####
# print("Maze:")
# m.print()
print("Solving...")

to = time.time()
m = Maze(filename=PATH_TO_MAZE, origin=A, goal=B, diagonals=True, resolution=1)
m.solve(Algorithm=QueueFrontier)
print(f"Solved. Time spent: {time.time() - to}")

print("States Explored:", m.num_explored) # number of states explored (lower the better)
print("Number of steps of the solution:", len(m.solution[0]))
# print("Solution: \n {m.print()}") # prints maze to terminal
m.output_image("maze.png", show_explored=True)  # saves image of maze

# print(m.solution) #prints solution of the maze in a step by step structure