import csv
import random
import numpy as np

# Define the range for random point coordinates
x_min, x_max = -50, 50
y_min, y_max = -40, 40

# Create and open a CSV file for writing
with open('trilateration_training_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Point1_X', 'Point1_Y', 'Point2_X', 'Point2_Y', 'Point3_X', 'Point3_Y', 'Distance1', 'Distance2', 'Distance3', 'Unknownx', 'Unknowny']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(1000000):
        # Generate random coordinates for three known points
        point1 = (random.uniform(x_min, x_max), random.uniform(y_min, y_max))
        point2 = (random.uniform(x_min, x_max), random.uniform(y_min, y_max))
        point3 = (random.uniform(x_min, x_max), random.uniform(y_min, y_max))

        # Calculate distances from these points to a random unknown point
        unknown_point = (random.uniform(x_min, x_max), random.uniform(y_min, y_max))
        distance1 = ((unknown_point[0] - point1[0])**2 + (unknown_point[1] - point1[1])**2)**0.5
        distance2 = ((unknown_point[0] - point2[0])**2 + (unknown_point[1] - point2[1])**2)**0.5
        distance3 = ((unknown_point[0] - point3[0])**2 + (unknown_point[1] - point3[1])**2)**0.5

        # Write the data to the CSV file
        writer.writerow({
            'Point1_X': np.around(point1[0], 3),
            'Point1_Y': np.around(point1[1], 3),
            'Point2_X': np.around(point2[0], 3),
            'Point2_Y': np.around(point2[1], 3),
            'Point3_X': np.around(point3[0], 3),
            'Point3_Y': np.around(point3[1], 3),
            'Distance1': np.around(distance1, 3),
            'Distance2': np.around(distance2, 3),
            'Distance3': np.around(distance3, 3),
            'Unknownx': np.around(unknown_point[0], 3),
            'Unknowny': np.around(unknown_point[1], 3),
        })