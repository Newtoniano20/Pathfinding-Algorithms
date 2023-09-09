import numpy as np

x1 = 20
y1 = 10
x2 = -15
y2 = 0
x3 = 0
y3 = -80
d1 = 19
d2 = 17.52
d3 = 86.28

# Define the known points and their distances
point1 = (x1, y1)
point2 = (x2, y2)
point3 = (x3, y3)

distance1 = d1  # Distance from the unknown point to point1
distance2 = d2  # Distance from the unknown point to point2
distance3 = d3  # Distance from the unknown point to point3

# Define the equations for trilateration
A = 2 * (x2 - x1)
B = 2 * (y2 - y1)
C = 2 * (x3 - x1)
D = 2 * (y3 - y1)

E = (distance2 ** 2 - distance1 ** 2 - x2 ** 2 + x1 ** 2 - y2 ** 2 + y1 ** 2)
F = (distance3 ** 2 - distance1 ** 2 - x3 ** 2 + x1 ** 2 - y3 ** 2 + y1 ** 2)

# Calculate the coordinates of the unknown point
x = (E * D - B * F) / (A * D - B * C)
y = (E * C - A * F) / (B * C - A * D)

# Print the approximate position of the unknown point
print(f"Approximate position: ({-x}, {-y})")