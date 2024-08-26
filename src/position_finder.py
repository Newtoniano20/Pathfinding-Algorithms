"""
Copyright (©) Joel Garcia.  All rights reserved.
Licensed under the MIT License. See License.md in the project root for license information.

This project contain files and code which are propiety of 
Harvard University's CS50AI Course and are used according to the license.
"""
import numpy as np

class Position:
    def __init__(self, Xo=(0,0), waypoints={"A": (0,0)}, *args, **kwargs) -> None:
        self.references = kwargs
        self.waypoints = waypoints
        self.Xo = Xo
    
    def update_position(self, pos):
        self.Xo = pos
        
    def update_distances(self, **kwargs):
        self.references = kwargs

    def distance(self, initial, final):
        return np.sqrt(((final[0]-initial[0])**2 + (final[1]-initial[1])**2))

    def theoretical_positions(self, W1 = "W1", W2 = "W2", W3 = "W3"):
        x1 = self.waypoints[W1][0]
        y1 = self.waypoints[W1][1]
        x2 = self.waypoints[W2][0]
        y2 = self.waypoints[W2][1]
        x3 = self.waypoints[W3][0]
        y3 = self.waypoints[W3][1]
        d1 = self.references[W1]
        d2 = self.references[W2]
        d3 = self.references[W3]

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
        return np.around(-x, 2), np.around(-y, 2)

if __name__ == "__main__":
    pos = Position(waypoints={"A": (1.1, 1.1), "B": (3, 4), "C": (4, 3)}, A=1.4, B=5, C=5)
    print(pos.theoretical_positions(W1="A", W2="B", W3="C"))