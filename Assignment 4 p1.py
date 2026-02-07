'''
Assignment 4
Challenge: Implement error handling to ensure that the user enters
numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a
2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the
distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''
import math

#This is the input section below

import math

# This is the input section below
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))


#The processing section below
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# The output is below

print("The distance between the 2 points are: ", distance)


