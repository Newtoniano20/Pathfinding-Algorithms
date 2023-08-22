import time

from PathFindingAPI_A_Star import *

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

to = time.time()

m = Maze(sys.argv[1])
# print("Maze:")
# m.print()
print("Solving...")
m.solve()
# print("States Explored:", m.num_explored)
# print("Solution:")
# m.print()
m.output_image("maze.png", show_explored=True)

# print(m.solution)
print(time.time() - to)